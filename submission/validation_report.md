# FlipRate Submission Validation Report

**Validation date:** 2026-11-16 WAT  
**Scope:** local deterministic checks only  
**External calls:** none  
**Overall result:** **PASS WITH LIMITATIONS**

## Checks passed

| Check | Result |
|---|---|
| Final-report abstract length | **PASS** — 198 words, within the required 150-250 words. |
| PDF page count | **PASS** — 8 pages total; main report pages 1-5, references page 6, appendices pages 7-8. |
| PDF upload size | **PASS** — 263,699 bytes, below 25 MB. |
| PDF rendering | **PASS** — all eight rendered pages visually inspected. |
| Official template | **PASS** — report built from the supplied official DOCX template; retained package styles and structure were audited. |
| Python compilation | **PASS** — current and preserved pre-revision simulation scripts compile under Python 3.12.3. |
| JSON parsing | **PASS** — 25 local JSON files parsed. |
| Governance JSONL parsing | **PASS** — 1 JSONL file / 9 nonblank event rows parsed. |
| CSV parsing | **PASS** — 8 local CSV files parsed. |
| XML parsing | **PASS** — 8 preserved raw arXiv XML files parsed. |
| Source register | **PASS** — 21 rows, 21 unique source IDs, required bibliographic fields present, stable URLs use HTTPS. |
| Raw-source checksums | **PASS** — all 24 files listed in `research/raw/README.md` match their recorded SHA-256 digests. |
| Simulation provenance | **PASS** — current simulator digest plus four recorded output digests match `simulation_summary.json`. |
| Stored statistical disposition | **PASS** — `single_active_80pct_power_pass` is `false`; affected-model CR1/Holm power is 0.7224 (72.24%). |
| Submission navigation | **PASS** — submission-facing local Markdown links resolve after excluding preserved raw-review line locators from file-link interpretation. |
| Contradiction scan | **PASS** — no active document states that the 80% target passed, execution is authorized, experiments ran, adjudication completed or empirical model results exist. |

## Citation and source-register integrity boundary

There is no completed paper or bibliography to subject to a full paper-level citation audit. The performed check therefore validates local source-register structure, stable-URL syntax, raw-record presence and recorded checksums. It does not re-query external indexes, independently re-read every source, reproduce cited papers' numerical results or certify global literature completeness. Existing source-specific limitations remain in `research/source_register.csv`, `research/related_work.md` and the audits.

## Markdown note

The preserved raw ARS methodological challenge uses Markdown links whose targets are absolute file paths suffixed with source line locators such as `file.md:131`. A generic filesystem link parser reports those locator strings as missing paths. They are preserved audit locators, not broken submission navigation. Active submission and current project-document links resolve.

## Remaining blocked checks or actions

- Author affiliation: not confirmed and not invented.
- Portal upload and acceptance receipt: not performed or claimed.
- Empirical reproducibility: not applicable because no model experiment or confirmatory dataset exists.

## Final interpretation

The scientific report artifact is complete and locally validated. Submission remains limited by unconfirmed affiliation and the unperformed portal upload. These checks do not authorize experiment execution.
