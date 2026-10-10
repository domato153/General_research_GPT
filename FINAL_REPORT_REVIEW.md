# FINAL_REPORT_REVIEW — CVE-2024-6387

- Review date: 2026-10-11 (Asia/Seoul).
- User approval and instruction: P1 integrated technical-security Full Report, source/contradiction audit, GitHub research-branch save and full in-chat delivery.
- Research source head at user selection: 6c390e71dda9ab7152368888efffd606c6cf246e.
- Report draft commit: a6a1c153ff836e4d5fea1b77b0f4277b1a2100db, path FINAL_REPORT_DRAFT.md, read back successfully, 15,944 Unicode code units.
- Main source files re-read: ROUND1_FINDINGS.md, ROUND2_PATCH_VALIDATION.md, ROUND3_A_C_FINDINGS.md, W5_SYNTHESIS.md, RESEARCH_PLAN.md and preserved editorial P1.
- Report mode: Full Report, Standard~Expanded. 7 body sections + 4 explanatory appendices + 20 traceable primary/secondary links. Written result-based, not W-ID-plan copy.

## Claim/objection-to-manuscript content review

| W-ID | Actual manuscript location | Specific grounded results verified | Essential counterevidence and bound |
|---|---|---|---|
| W1 | 2.1–2.2 / 4.1 / A | Qualys 2006 safeguard, 2020 752250c, SIGALRM unsafe logging, upstream source confirmed | Direct dynamic exploitation not performed; source links S1 S2 S3 S4 |
| W2 | 3.1–3.3 / 6 / D | Qualys Debian i386 root execution and 10k/3–4h/6–8h, NVD 8.1, Unit42 public PoC fail, 2025 developer scope, Veriti 7.4 counterexample | Do not assert large-scale compromise, 64bit infeasibility or zero real incidents |
| W3 | 4.1–4.4 / A | 9.8p1 _exit/child_reap, Debian Ubuntu #if0, CentOS caveat, CVE-6409 separate downstream cleanup_exit, 9.9 log regression, login-timeout.sh scope | Source-level comparison not binary proof; initial RHEL RPM != later CentOS source provenance |
| W4 | 5.1–5.3 / B | 2024 initial Debian Ubuntu RHEL packages and Amazon classification; Unit42 ~7m of ~23m; Qualys 14m estimate and ~700k customer ~31% | Censys/Shodan and customer sampling differ; no 2026 global installed-patch fraction inferred |
| W5 | Summary / 6 / 7 / D | Distinguishes proven lab exploit vs real intrusion, CVE-6409 independence, distribution vs deployment; operational remediation and uncertainties | CISA KEV status secondary not independently official-verified; explicit unknowns remain |

## Stage 7 textual and evidence audit
- 20 automated source-to-report checks executed against fetched draft and fetched actual stored evidence: 19 exact/semantic token checks initially passed. D-07 failed because the check expected literal string '비영향 버전', but manuscript explicitly reads 'OpenSSH 7.4처럼 이번 8.5p1~9.7p1 회귀 영향 범위 밖의 버전' in section 3.3, and section 6 distinguishes its incorrect classification. Actual explanatory passage inspected and accepted; no claim omission. 20/20 content checks accepted after manual contextual inspection.
- D-01 initial 2006 safeguard / 2020 regression: present section 2.2. D-03 unique laboratory denominators: Debian 12.5 i386, 1만회, 3–4h vs 6–8h, ASLR: present section 3.1. D-06 Unit42 independent failure described and explicitly not negating Qualys success: present section 3.3. D-09/10 minimal distro patches and separate privilege context CVE-6409: present section 4 and Appendix A.
- D-14 2024 exposure comparison: Unit42 ~7m of 23m, Qualys 14m search estimation, Qualys customer 700k/31%; distinct populations and detection methods noted in same table and interpreting prose, not conflated or used as 2026 patch trends.
- D-16 missing incident verification is NOT rewritten as zero cases. D-17 CISA KEV incompletely verified from primary full official catalog described as uncertainty. D-18 temporary LoginGraceTime=0 and MaxStartups DoS warning present.
- Direct 32-bit/64-bit exploit proof boundary preserved; upstream patch path and Debian/Ubuntu/CentOS/RHEL backport distinction preserved; actual RPM binary dynamic tests NOT claimed performed. The 9.9 audit-logging regression is distinguished from security-fix failure.
- Section headings 1–7, appendices A–D, date and source list [S1]–[S20], follow-up triggers checked. No unsupported global compromise count, 2026 patch-adoption fraction or cross-population trend calculation.
- Changes after audit: Only document metadata changed from '검토 대상 원고' to '근거·반론 검수 완료 및 최종 원고 확정(원격 보존·대화 전달 상태는 별도 검증)'. No substantive claims were changed after Stage 7.
- Verdict: Stage 7 editorial and evidence mapping PASS within existing research limits; no new research undertaken, no unverified tests claimed.
- Stage 8 user finalization authorization: YES, exact user instruction saved in FINAL_REPORT_EDITORIAL_PROPOSAL.md. Persistence is to be checked by reading FINAL_REPORT.md on target branch after commit. Chat delivery of full manuscript must happen separately; tool save alone is not delivery.
