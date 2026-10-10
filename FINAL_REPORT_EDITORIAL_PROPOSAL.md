# FINAL_REPORT_EDITORIAL_PROPOSAL — CVE-2024-6387

- proposal_id: CVE6387-EDITORIAL-01
- revision: 1
- research_head (proposal source snapshot): fd096bf51b8e4a1adc5f0548a2117f0acd672f28
- rules_commit: 44bd894cb464229a6d8b926f152113dd0f1bbbae
- date: 2026-10-11 (Asia/Seoul)
- status: SELECTED (2026-10-11 user-approved integrated option; full report completion delegated)
- scope: Stage 5 technical readiness audit and final editorial selection proposal; no final draft/FINAL_REPORT.md yet.
- supporting research: RESEARCH_PLAN.md, ROUND1_FINDINGS.md, ROUND2_PATCH_VALIDATION.md, ROUND3_A_C_FINDINGS.md, W5_SYNTHESIS.md

## Actual Stage 5 research audit
- W1: direct Qualys source, upstream original 2020 regression and source comparison; conditional completion. Write technical cause and 2025 developer explanation, not unproven intent.
- W2: Qualys 32-bit lab successful RCE, Unit42 external PoC failure, 2025 developer 64-bit not known to be exploited; actual 2024–2026 reported successful compromises unverified, global incident number unidentifiable. Conditional completion.
- W3: 9.8p1 upstream signal/parent logging split and Debian/Ubuntu/CentOS9 minimal backports read; Red Hat RHEL 9 published advisories, separate CVE-2024-6409. No compiler/exploit/functional all-distro tests. Conditional completion.
- W4: Official vendor fixed-package release confirmed, 2024 publicly scanned SSH banners/customer sampling cannot infer actually unpatched worldwide servers in 2026. Conditional completion.
- W5: competing claims evaluated; crucial distinctions test vs field, CVSS vs exploit frequency, deployed fix vs installed fix, later separate CVE vs 6387 regression. Conditional completion.
- Freshness spot-check 2026-10-11: reviewed official 2024 Qualys/OpenSSH source and 2025 developer statement, searched for fresh exploitation / patch failure counterevidence. No high-confidence new evidence overturned overall conclusions. Do not present absence of evidence as definitive nonexistence.
- Specific caution: 2026 CISA KEV status was cited from secondary trackers, not independently verified from complete current official dataset; avoid definitive official-absence claim or use explicit methodological qualifier in final.
- Readiness: CONDITIONALLY READY for Stage 6. No blocking unresolved W-ID; Stage 7 manuscript audit and explicit user finalize permission not yet done.

## User-facing important editorial proposals (exact key language)

### Recommended P1 (core)
**추천: 통합 기술·보안 분석 보고서(Full Report, 표준~상세).**
**본문 심화:** (1) 취약점의 기원과 신호 처리 경쟁 상태, (2) 32비트 실험 성공·공격 난이도와 실제 침해 증거의 한계, (3) OpenSSH 9.8p1과 Debian·Ubuntu·RHEL 백포트의 수정 원리, (4) CVE-2024-6409와 주요 반론, (5) 수정 패키지 배포와 실제 설치·잔존 위험의 차이, (6) 실무 대응과 조건부 결론.
**표·부록으로 압축:** 긴 소스 코드 diff, 배포판별 세부 패키지 번호, 초기 노출 통계의 측정 기준, 출처·검증 추적 자료.
**제외:** 검증되지 않은 전 세계 침해 건수·패치 적용률의 추정, 근거가 불충분한 노출 추세 그래프, 주변적인 반복 설명.
**필수 유지:** 독립 PoC 재현 실패, 64비트 성공의 시점별 미확인, CVE-2024-6409의 독립성, 노출 스캔의 표본·정의 차이, 직접 동적 검증 미실시를 본문에서 명확히 설명.

### Alternative P2
**대안: 패치 감사 중심 보고서.** 업스트림 변경과 배포판 패치 diff·테스트 근거를 본문에 더 깊게 배치하고, 공격 사례·시장 노출은 요약합니다. 코드 검토 독자에게 적합하지만 원래 A+C 질문의 비중이 줄어듭니다.

### Alternative P3
**대안: 운영 위험 중심 보고서.** 침해 관측의 불확실성과 패치 적용·서버 점검을 본문에 집중하고, 상세 코드 비교는 부록으로 보냅니다. 실무 책임자에게 편하지만 기술적 원인과 패치 완전성 분석이 압축됩니다.

## Decision boundary
- This is a stored proposal, not user approval, not a draft, not Stage 7 review, not Stage 8 completion.
- Next: show exactly the key P1/P2/P3 language to user and ask only the significant choice; if user delegates authoring and completion, Stage 6/6.5/7/8 separately verify and execute.
- External publication/sharing is not authorized.

## User selection and delegation (2026-10-11)
- User exact instruction: "좋아. 추천한 통합 기술·보안 분석 편집안으로 최종보고서를 완성해줘. 중요한 근거와 반론이 빠지지 않도록 최종 검수하고, GitHub 연구 브랜치에 저장한 뒤 여기에도 보고서 전문을 보여줘."
- Selection: P1 integrated technical-security Full Report, Standard~Expanded. Existing appendix/exclusion rules retained, all required counterevidence retained.
- Authority: complete manuscript, perform final evidence review, save on current research branch, then display full manuscript in chat; no external publication, no main/legacy branch write.
- Plan revision: original proposal_id CVE6387-EDITORIAL-01 rev1 was displayed previously and user selected it. This section records approval; it does not rewrite the original recommendation wording.
