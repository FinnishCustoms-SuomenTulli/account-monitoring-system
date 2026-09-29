#!/usr/bin/env python3
"""Validate every XML under examples/ against the XSD schemas in schemas/.

Each schema declares exactly one global root element (Document or AppHdr) in its
own targetNamespace, and the schemas do not import each other. Most examples are
SOAP envelopes that carry the ISO 20022 messages (AppHdr + Document) nested
inside soap:Body, so validating a whole file against a single schema is not
possible.

Instead, we build a catalog {(namespace, localname): schema} from the schemas,
then walk each example and validate every element whose (namespace, localname)
matches a catalog entry. That transparently covers SOAP-wrapped messages,
standalone AppHdr/Document files, and any schema/example added later -- no
per-file mapping to maintain.

Value checks (VALUE_CHECKS): some leaf fields have a well-known format the XSD
type does not fully pin down -- free-form text (e.g. head.001 EmailAdr is
Max2048Text with no pattern) or timestamps that are valid xs:dateTime but not
required to be UTC (the camt.052 ISODateTime fields, unlike head.001, do not
require a "Z"). VALUE_CHECKS adds a regex per (namespace, localname) so the
example *values* stay realistic and consistent, not just structurally valid.

External code checks (external_codes.json): ISO types many <Cd> fields as
External*Code, which the XSD treats as an unconstrained string -- so a wrong code
(DIVI for DIVD, Y for COID, or a code where only Prtry is valid) passes XSD
untouched. resolve_codeset() derives the applicable ISO code set from each <Cd>'s
context, and we check membership against external_codes.json, extracted from the
ISO External Code Sets workbook. Regenerate that file when the workbook updates;
see the comment above EXTERNAL_CODES.

Exit code is non-zero if any matched element fails validation or any file is not
well-formed. Files with no matching schema are reported as UNMATCHED (a visible
gap, e.g. register.003 which has no schema here) but do not fail the run.

Usage:
    python examples/validate.py                  # validate the repo
    python examples/validate.py --generate-codes # (re)build assets/iso20022.org/external_codes.json
    python examples/validate.py --selftest       # run the built-in self-check
"""
import json
import re
import sys
from pathlib import Path
from re import Pattern

try:
    from lxml import etree  # XSD validation needs libxml2; stdlib xml cannot do it
except ImportError:
    sys.exit("lxml is required: pip install lxml")

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "schemas"
EXAMPLES_DIR = ROOT / "examples"
XSD_ELEMENT = "{http://www.w3.org/2001/XMLSchema}element"
HEAD_NS = "urn:iso:std:iso:20022:tech:xsd:head.001.001.01"
CAMT_NS = "urn:iso:std:iso:20022:tech:xsd:camt.052.001.08"
AUTH1_NS = "urn:iso:std:iso:20022:tech:xsd:auth.001.001.01"

# Value-format checks: (namespace, localname) -> (regex, message). The value must
# fully match the regex. These catch wrong-looking values the XSD type accepts.
#
# Timestamps/dates are typed xs:dateTime / xs:date, so the XSD already rejects
# impossible dates -- but only head.001 requires UTC ("Z" suffix); the camt.052
# ISODateTime fields do not, while every example (and the head.001 convention)
# uses "...Z". The checks below enforce that UTC convention and a plain date form.
# (A parse-based check is deliberately avoided: xs:dateTime allows "24:00:00",
# which Python's strptime rejects, so a regex on the lexical shape is safer.)
_UTC_DATETIME = (re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z"),
                 "not an ISO-8601 UTC timestamp (YYYY-MM-DDThh:mm:ss[.ffffff]Z)")
_DATE = (re.compile(r"\d{4}-\d{2}-\d{2}"), "not an ISO-8601 date (YYYY-MM-DD)")
VALUE_CHECKS: dict[tuple[str, str], tuple[Pattern[str], str]] = {
    (HEAD_NS, "EmailAdr"): (re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+"), "not a valid email address"),
    (HEAD_NS, "CreDt"): _UTC_DATETIME,
    (CAMT_NS, "CreDtTm"): _UTC_DATETIME,
    (CAMT_NS, "DtTm"): _UTC_DATETIME,
    (CAMT_NS, "FrDtTm"): _UTC_DATETIME,
    (CAMT_NS, "ToDtTm"): _UTC_DATETIME,
    (CAMT_NS, "AccptncDtTm"): _UTC_DATETIME,
    (CAMT_NS, "FrDt"): _DATE,
    (CAMT_NS, "ToDt"): _DATE,
    (AUTH1_NS, "FrDt"): _DATE,
    (AUTH1_NS, "ToDt"): _DATE,
}

# ISO External Code Sets used by the examples' <Cd> fields, keyed by code-set name.
# external_codes.json is generated and gitignored: unzip the tracked
# assets/iso20022.org/*.zip there, then run  python examples/validate.py --generate-codes
CODES_SRC_DIR = ROOT / "assets" / "iso20022.org"
CODES_FILE = CODES_SRC_DIR / "external_codes.json"
# Code sets resolve_codeset() maps to. ExternalFinancialInstitutionIdentification1Code
# is not published by ISO, so it is stored empty (any <Cd> there is flagged).
CODE_SETS = [
    "ExternalEntryStatus1Code",
    "ExternalPurpose1Code",
    "ExternalCashAccountType1Code",
    "ExternalBalanceType1Code",
    "ExternalOrganisationIdentification1Code",
    "ExternalAccountIdentification1Code",
]
try:
    EXTERNAL_CODES = {k: set(v) for k, v in json.loads(CODES_FILE.read_text(encoding="utf-8")).items()}
except FileNotFoundError:
    EXTERNAL_CODES = {}


def build_catalog(schemas_dir=SCHEMAS_DIR):
    """Map (targetNamespace, root element name) -> (schema filename, XMLSchema)."""
    catalog = {}
    for xsd in sorted(schemas_dir.glob("*.xsd")):
        doc = etree.parse(str(xsd))
        tns = doc.getroot().get("targetNamespace")
        schema = etree.XMLSchema(doc)
        for el in doc.getroot():
            if el.tag == XSD_ELEMENT and el.get("name"):
                catalog[(tns, el.get("name"))] = (xsd.name, schema)
    return catalog


def _qname(el):
    """QName of an element, or None if its tag is not a resolvable qualified name.

    The recovering parser can leave elements with unresolved-prefix tags (e.g.
    'head001:AppHdr' when the prefix was never declared); etree.QName raises on
    those, so callers treat them as unrecognised and skip them.
    """
    if not isinstance(el.tag, str):  # comments / processing instructions
        return None
    try:
        return etree.QName(el)
    except ValueError:
        return None


def resolve_codeset(el):
    """Return the ISO external code set a <Cd> element must belong to, or None.

    The code set is not in the XML; it is fixed by the field's position, so we
    infer it from the parent (and, for scheme codes, the nearest identifying
    ancestor). Fields we don't recognise return None and are left unchecked --
    e.g. bank-transaction Domn/Fmly codes, which live in a separate ISO list.
    """
    q = _qname(el)
    if q is None or q.localname != "Cd":
        return None
    parent = el.getparent()
    pq = _qname(parent) if parent is not None else None
    if pq is None:
        return None
    simple = {
        "Sts": "ExternalEntryStatus1Code",
        "Purp": "ExternalPurpose1Code",
        "CdOrPrtry": "ExternalBalanceType1Code",  # only under Bal/Tp in these messages
        "Tp": "ExternalCashAccountType1Code",     # only under CdtrAcct/DbtrAcct here
    }
    if pq.localname in simple:
        return simple[pq.localname]
    if pq.localname == "SchmeNm":
        ancestors = set()
        p = parent
        while p is not None:
            aq = _qname(p)
            if aq is not None:
                ancestors.add(aq.localname)
            p = p.getparent()
        if "FinInstnId" in ancestors:
            return "ExternalFinancialInstitutionIdentification1Code"
        if "OrgId" in ancestors:
            return "ExternalOrganisationIdentification1Code"
        if "Acct" in ancestors:
            return "ExternalAccountIdentification1Code"
    return None


def validate_file(xml_path, catalog):
    """Return list of (label, ok, message) for well-formedness, schema, value and
    code checks. A recovering parser is used so one run reports *all* problems in
    a file -- every well-formedness error, plus the schema/value/code issues found
    on the best-effort recovered tree -- instead of stopping at the first.

    Schema hits report ok=True/False; well-formedness/value/code entries are
    appended only on failure. message is None when ok, else a relative-safe string.
    """
    results = []
    parser = etree.XMLParser(recover=True)
    tree = etree.parse(str(xml_path), parser)
    seen_wf = set()
    for e in parser.error_log:
        detail = f"{e.line}:{e.column}: {e.message}"
        if detail not in seen_wf:
            seen_wf.add(detail)
            results.append(("well-formedness", False, detail))
    if tree.getroot() is None:  # nothing recoverable
        return results
    for el in tree.iter():
        q = _qname(el)
        if q is None:  # comment, PI, or recovery artifact with an unresolved prefix
            continue
        key = (q.namespace, q.localname)

        hit = catalog.get(key)
        if hit:
            schema_name, schema = hit
            if schema.validate(el):
                results.append((schema_name, True, None))
            else:
                # Report every error libxml2 collected for this subtree, not just
                # the last one, so a single run gives the complete picture. Each
                # error stringifies with an absolute filename, so rebuild it from
                # the fields (only the relative path, added in main, is shown).
                seen = set()
                for e in schema.error_log:  # reset per validate(); no cross-subtree bleed
                    detail = f"{e.line}:{e.column}:{e.level_name}:{e.domain_name}:{e.type_name}: {e.message}"
                    if detail not in seen:
                        seen.add(detail)
                        results.append((schema_name, False, detail))

        check = VALUE_CHECKS.get(key)
        if check:
            pattern, desc = check
            text = (el.text or "").strip()
            if not pattern.fullmatch(text):
                results.append((f"value:{q.localname}", False, f"{desc}: {text!r}"))

        codeset = resolve_codeset(el)
        if codeset in EXTERNAL_CODES:
            code = (el.text or "").strip()
            if code not in EXTERNAL_CODES[codeset]:
                hint = "" if EXTERNAL_CODES[codeset] else " (no such ISO code set -- use Prtry)"
                results.append((f"code:{codeset}", False, f"{code!r} is not a valid {codeset}{hint}"))
    return results


def main():
    catalog = build_catalog()
    if not catalog:
        sys.exit(f"No schemas found in {SCHEMAS_DIR}")
    if not EXTERNAL_CODES:
        print(f"NOTE  {CODES_FILE.name} not found -- external <Cd> values not checked.\n")

    xmls = sorted(EXAMPLES_DIR.rglob("*.xml"))
    issues = 0            # total problems across all files
    failed_files = 0      # files with at least one problem
    unmatched = 0
    for xml in xmls:
        rel = xml.relative_to(ROOT)
        results = validate_file(xml, catalog)
        if not results:
            print(f"UNMATCHED  {rel}: no schema for its namespace(s)")
            unmatched += 1
            continue
        file_issues = 0
        for label, ok, message in results:
            if ok:
                print(f"OK    {rel}  [{label}]")
            else:
                print(f"FAIL  {rel}  [{label}]: {message}")
                file_issues += 1
        issues += file_issues
        if file_issues:
            failed_files += 1

    print(f"\n{len(xmls)} file(s): {failed_files} with issues, "
          f"{issues} issue(s) total, {unmatched} unmatched.")
    return 1 if issues else 0


def selftest():
    """Self-check: catalog builds, XSD catches a broken subtree, value checks work."""
    catalog = build_catalog()
    assert catalog, "catalog is empty"
    assert (HEAD_NS, "AppHdr") in catalog
    assert ("urn:iso:std:iso:20022:tech:xsd:camt.052.001.08", "Document") in catalog

    # XSD: an empty Document (missing required children) must fail its schema.
    ns = "urn:iso:std:iso:20022:tech:xsd:camt.052.001.08"
    _, schema = catalog[(ns, "Document")]
    assert not schema.validate(etree.fromstring(f'<Document xmlns="{ns}"/>'))

    # Value check: EmailAdr must look like an email, not placeholder prose.
    email_re, _ = VALUE_CHECKS[(HEAD_NS, "EmailAdr")]
    assert email_re.fullmatch("matti.meikalainen@example.com")
    assert not email_re.fullmatch("Virkailijan sähköpostiosoite")

    # Timestamp check: UTC datetimes (incl. 24:00:00 and fractions) pass; a
    # missing "Z", an offset, or junk fails.
    dt_re, _ = VALUE_CHECKS[(CAMT_NS, "CreDtTm")]
    assert dt_re.fullmatch("2019-05-08T24:00:00Z")
    assert dt_re.fullmatch("2022-09-28T08:16:34.315328Z")
    assert not dt_re.fullmatch("2019-05-08T00:00:00")        # no Z -> not UTC
    assert not dt_re.fullmatch("2019-05-08T00:00:00+02:00")  # offset, not Z
    assert not dt_re.fullmatch("not-a-timestamp")
    date_re, _ = VALUE_CHECKS[(AUTH1_NS, "FrDt")]
    assert date_re.fullmatch("2020-09-01")
    assert not date_re.fullmatch("2020-09-01T00:00:00Z")

    # Code-set context resolution works without the generated data...
    org_cd = etree.fromstring(
        f'<AppHdr xmlns="{HEAD_NS}"><Fr><OrgId><Id><OrgId><Othr>'
        "<Id>x</Id><SchmeNm><Cd>Y</Cd></SchmeNm></Othr></OrgId></Id></OrgId></Fr></AppHdr>"
    ).find(f".//{{{HEAD_NS}}}Cd")
    assert resolve_codeset(org_cd) == "ExternalOrganisationIdentification1Code"
    # ...and membership is enforced once external_codes.json has been generated.
    if EXTERNAL_CODES:
        assert "COID" in EXTERNAL_CODES["ExternalOrganisationIdentification1Code"]
        assert "Y" not in EXTERNAL_CODES["ExternalOrganisationIdentification1Code"]
        assert "DIVD" in EXTERNAL_CODES["ExternalPurpose1Code"]
        assert "DIVI" not in EXTERNAL_CODES["ExternalPurpose1Code"]
    else:
        print("  (external_codes.json not generated -- code membership not checked)")

    # Every real example parses and its matched elements resolve.
    for xml in EXAMPLES_DIR.rglob("*.xml"):
        validate_file(xml, catalog)

    print("selftest OK")
    return 0


def generate_codes():
    """Regenerate external_codes.json from the ISO code-sets workbook in assets/.

    Reads the .xlsx extracted from the tracked assets/iso20022.org/*.zip (the
    GitHub Action unzips it first). Both the .xlsx and the generated JSON are
    gitignored; only the .zip is tracked.
    """
    try:
        import openpyxl  # only needed to regenerate, not to validate
    except ImportError:
        sys.exit("openpyxl is required for --generate-codes: pip install openpyxl")
    xlsxs = sorted(CODES_SRC_DIR.glob("*.xlsx"))
    if not xlsxs:
        sys.exit(f"no .xlsx in {CODES_SRC_DIR} -- unzip the External Code Sets .zip there first")

    wb = openpyxl.load_workbook(xlsxs[0], read_only=True, data_only=True)
    sets = {}
    for i, row in enumerate(wb["AllCodeSets"].iter_rows(values_only=True)):
        if i == 0 or not row[0]:
            continue
        code = str(row[1] or "").strip()
        if code:  # skip rows with no code value -- an empty <Cd/> must not validate
            sets.setdefault(str(row[0]).strip(), set()).add(code)

    out = {name: sorted(sets.get(name, set())) for name in CODE_SETS}
    out["ExternalFinancialInstitutionIdentification1Code"] = []  # not published by ISO
    CODES_FILE.write_text(
        json.dumps(out, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {CODES_FILE.relative_to(ROOT)}: "
          f"{len(out)} code sets, {sum(len(v) for v in out.values())} codes")
    return 0


if __name__ == "__main__":
    if "--generate-codes" in sys.argv:
        sys.exit(generate_codes())
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    sys.exit(main())
