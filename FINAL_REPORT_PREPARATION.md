# Final Report Preparation — OpenSSH CVE-2024-6387 (regreSSHion)

- Prepared: 2026-10-11 (Asia/Seoul)
- Project rule baseline: 44bd894cb464229a6d8b926f152113dd0f1bbbae
- Research branch: research/20261011-openssh-cve-2024-6387
- Stage 5 conclusion: conditionally ready for drafting, after real evidence audit
- Editorial proposal: CVE6387-EDITORIAL-01 rev1, RECOMMENDED (not selected)
- Decision in latest user request: END FURTHER RESEARCH and PREPARE final report. Not permission to presume selected report framing or claim draft/final complete.
- No fresh external research under this instruction. Reuse recorded, traced source material only.
- Draft not written; Stage 7 review and Stage 8 confirmation not performed.

## Proposed baseline structure (pending user's editorial choice)
- Format recommendation: Full Technical Security Report, Standard~Expanded, public factual basis through 2026-10-11.
1. Executive Summary — separate technical RCE feasibility, field exploitation confidence, patch source correctness, in-field deployment certainty.
2. Scope and method — what was checked, facts vs inference, platform/time restrictions, absence of own exploit/build testing.
3. Root cause and regression — CVE-2006-5051 safeguard, 2020 regression, SIGALRM/logging/glibc race.
4. Exploitability and actual exploitation evidence — Qualys 32-bit Debian/glibc experiment, repeated attempt cost, 64-bit status as dated statement, PoC / scans vs proven incidents.
5. Patch correctness and secondary issue — OpenSSH 9.8p1 architectural fix vs Debian, Ubuntu, CentOS/RHEL minimal backports; CVE-2024-6409 separate issue; functionality regressions and test boundaries.
6. Vendor distribution and residual risk — Debian/Ubuntu/RHEL advisories with dates/versions; 2024 global SSH exposure snapshots and denominators; cannot infer 2026 installed patch fraction; practical operations checks.
7. Competing claims, caveats and final technical/security verdict — actual risk and tradeoff, strongest counterarguments, conditions under which verdict changes, recommended verification actions.
Appendix A: selected code paths / upstream-to-backport changes (with stable source URLs).
Appendix B: vendor package versions and advisories.
Appendix C: key source dossier and methodological limitations.

## W-ID → report section → source map (main assertions, not work log)
| W-ID | Report section(s) | Recorded supporting evidence | Required caveat / counterevidence |
|---|---|---|---|
| W1 root cause | 3, 5 | ROUND1_FINDINGS.md; original Qualys; upstream V_9_7_P1 and V_9_8_P1 sources; 2020 commit 752250c | Linux/glibc context; no own exploit |
| W2 attack realism | 4, 7 | ROUND1_FINDINGS.md; ROUND3_A_C_FINDINGS.md; Qualys, Unit42, 2025 Damien Miller statement | PoC not equal intrusion; Unit42 PoC reproduction failed; 64-bit lack-of-knowledge dated; zero-incident claim forbidden |
| W3 patch | 5, Appendix A | ROUND1_FINDINGS.md; ROUND2_PATCH_VALIDATION.md; OpenSSH, Debian, Ubuntu, CentOS patches; Red Hat advisories | Static code validation not dynamic binary attestation; CVE-2024-6409 separate; deployment differences |
| W4 distribution/residual | 6, Appendices B/C | ROUND3_A_C_FINDINGS.md; Debian DSA, Ubuntu USN, Red Hat RHSA, Unit42 and Qualys initial exposure | Backported versions; banner counts not actual vulnerable/installed counts; different denominators |
| W5 synthesis/contradiction | 1, 7 | W5_SYNTHESIS.md and previous evidence files | Existence of exploit vs prevalence; 6409 vs 6387; patch publication vs application; CISA KEV not independently certified from full source |

## Report editing decision still open (do not silently assume approval)
- P1 RECOMMENDED: Integrated technical-security report. Deeply include technical root cause, exploit evidence, upstream and distro patches, independent related CVE, distribution vs actual installation, operational conclusion.
- P2 ALTERNATIVE: Patch audit heavy, A/C concise.
- P3 ALTERNATIVE: Operations/incident/patch deployment heavy, technical diffs in annex.
- Canonical wording and preserved revision in FINAL_REPORT_EDITORIAL_PROPOSAL.md.
- User has decided to stop further research, not which of P1–P3 to select or to commission a full draft/final. Report preparation completed as an evidence-to-sections blueprint.

## Stage 7 target checks (future, NOT performed)
- Every relevant counterpoint actually explained in prose, not merely linked.
- Quantitative 2024 measurements name denominators, dates, source and absence of dynamic attestation.
- Initial Qualys 32-bit success not generalized to x86_64 or actual field compromise.
- 9.8p1 and downstream backport code paths distinguished; CVE-2024-6409 not conflated.
- A 'fixed' vendor tracker not generalized to 2026 actual patch installation rates.
- Recheck source URLs and all quantitative claims in assembled manuscript; no new evidence without a user-specified resumption of research.
- Keep proposal selection record and manuscript validation separate from mere GitHub save.
