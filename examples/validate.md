# `validate.py` — example validator

Validates every XML file under `examples/` against the XSD schemas in `schemas/`
and against the ISO 20022 External Code Sets. Used as the CI gate for this repo.

## What it checks

1. **Schema (XSD).** Builds a catalog `{(namespace, root element): schema}` from
   `schemas/*.xsd`, then validates every `AppHdr` / `Document` subtree it finds —
   so SOAP-wrapped messages and standalone headers are all covered without any
   per-file configuration.
2. **Value formats.** Some fields have a format the XSD type doesn't fully pin
   down — free-form text (`head.001` `EmailAdr` is `Max2048Text` with no pattern)
   or timestamps that are valid `xs:dateTime` but not required to be UTC (the
   `camt.052` `ISODateTime` fields, unlike `head.001`, don't require a `Z`).
   `VALUE_CHECKS` adds a regex per field so example *values* stay realistic and
   consistent (e.g. emails look like emails, timestamps are `…Z`), not just
   structurally valid.
3. **External code values.** ISO types many `<Cd>` fields as `External*Code`,
   which the XSD treats as an unconstrained string — so a wrong code (e.g. `DIVI`
   for `DIVD`, `Y` for `COID`) passes XSD untouched. `resolve_codeset()` infers
   the applicable code set from each `<Cd>`'s context and checks membership
   against `external_codes.json` (see [Code sets](#code-sets)).

Exit code is non-zero if any subtree fails validation, any file is malformed, or
any `<Cd>` is not a valid member of its code set. Files whose namespace has no
schema here (e.g. `register.003`) are reported `UNMATCHED` but do not fail.

**It does not stop at the first problem.** A recovering XML parser is used, so a
single run reports *every* issue in *every* file — all well-formedness errors,
then the schema/value/code issues found on the best-effort recovered tree —
rather than aborting a file at its first error. Fix the `[well-formedness]`
issues first: some structural errors below them are cascade artifacts of a
malformed tag and disappear once the file parses cleanly. The summary line
reports files-with-issues, total issues, and unmatched counts.

## Requirements

- **Python** 3.x
- **[`lxml`](https://pypi.org/project/lxml/)** — XSD validation (libxml2); required to run the validator.
- **[`openpyxl`](https://pypi.org/project/openpyxl/)** — only for `--generate-codes` (reading the ISO workbook); *not* needed to validate.
- Standard library only otherwise: `json`, `re`, `pathlib`, `sys`.

```sh
pip install lxml            # to validate
pip install lxml openpyxl   # to also regenerate the code sets
```

## Usage

```sh
python examples/validate.py                   # validate the repo (CI entry point)
python examples/validate.py --selftest        # built-in self-check
python examples/validate.py --generate-codes  # (re)build assets/iso20022.org/external_codes.json
```

If `assets/iso20022.org/external_codes.json` is missing, validation still runs
but prints a `NOTE` and skips the external-code check (structure and value
checks still apply).

## Code sets

`assets/iso20022.org/external_codes.json` holds the ISO External Code Sets the examples use.
It is **generated and gitignored**, not committed. The tracked source is the
zip in `assets/iso20022.org/` (e.g. `ExternalCodeSets_XLSX_November_2025_v2.zip`).

To (re)generate locally:

```sh
unzip -o assets/iso20022.org/*.zip -d assets/iso20022.org/  # -> *.xlsx (gitignored)
python examples/validate.py --generate-codes                # -> assets/iso20022.org/external_codes.json
```

Update the code sets by dropping a newer ISO zip into `assets/iso20022.org/` and
re-running the two commands. To validate more `External*Code` fields, add the
field's context to `resolve_codeset()` and its code-set name to `CODE_SETS` in
`validate.py`, then regenerate.

## Continuous integration

The GitHub Action **[`.github/workflows/validate-xml.yml`](../.github/workflows/validate-xml.yml)**
runs on every push / pull request that touches `examples/`, `schemas/`, or
`assets/iso20022.org/`. It installs `lxml` + `openpyxl`, unzips the code-sets
zip, runs `--generate-codes`, then runs the validator.
