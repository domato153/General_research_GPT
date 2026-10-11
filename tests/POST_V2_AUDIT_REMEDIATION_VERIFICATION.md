# Post-v2 independent audit remediation verification — 2026-10-12

## Baseline and scope
- Repository: `domato153/General_research_GPT`.
- Frozen previous operating main: `dc1f2a46970db8e6fb1317f56dded12dd2224216`.
- Independent audit source: `General_research_GPT_post_v2_independent_audit_20261012.md` (user-supplied; original is not replicated into the repository).
- Implemented only targeted findings in `tools/research_validator.py`, its tests, `02_RESEARCH_PIPELINE.md`, `04B_VALIDATION_RULES.md`, and `final_pdf_html_formatting_instruction_final.md`.
- Previously approved CSS, PROJECT_BOOTSTRAP, full research workflow and historical evidence kept unchanged.

## Verified actual local execution (isolated Windows temporary clone)
- Local real Python version: 3.13.14, pytest 9.1.1.
- Initial patched parser run FAILED: unfiltered None entries in marker/heading lookup. Corrected the discovery dictionaries and reran.
- Final `python -m pytest -q tools/test_research_validator.py`: **12 passed, 1 skipped** (optional PyMuPDF/fitz not installed; this is NOT a PDF renderer PASS).
- `git diff --check`: no whitespace errors (only checkout LF/CRLF warnings).
- Existing evidence preservation, deletion, broken links, short body, snapshot Part equality and normalized delivery tests retained.
- New tests: explicit missing file/invalid UTF-8 → `HOLD` + exit 2; marker→heading and nested heading recognized; fenced fake W-ID ignored; repeated source/map IDs → HOLD; heading-only mapping remains scope `syntax_and_heading_only` and semantic adequacy UNKNOWN; unverified exclusion does not become PASS.
- No live ChatGPT UI, no new-thread self-initiated `/handoff`, no real GitHub write-conflict/no-write E2E, no PDF generation/render verification here. These remain **NOT RUN/UNKNOWN**, separately owned by the user.
- The optional validator is never authoritative for semantic adequacy, actual chat UI display or provenance truth.

## Scoped regression and safety limits
- Main and `research/*` must not be modified before final tested fast-forward. No topic-specific research changed.
- `coverage_map_structure` field is retained for backwards consumers, with explicit `scope: syntax_and_heading_only` and extra negative metadata. The only intentional default exit-code behavior change is unreadable *explicit* input file → 2; other UNKNOWN remains nonblocking absent `--fail-on-unknown`.
- PDF guide change is only a publishing rule **if PDF is requested**, not a PDF-creation request or CSS theme modification.
- First FAIL and final local pytest PASS remain distinct; Python local test does not substitute for new-project E2E.

## Integration gates
- Tested contents must be committed to isolated branch with expected parent SHA and allowed paths only.
- Candidate files and audit record must be re-fetched by blob SHA.
- After verified fast-forward to `main`, confirm main HEAD and unchanged non-target files. If the expected HEAD changes or permissions reject the update, stop and do not force-push.
