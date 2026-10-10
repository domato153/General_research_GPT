# 범용 리서치 v2 — 운영 승격 마감 기록 (2026-10-11)

## 확정 운영 GitHub 상태
- 이전 `main` HEAD: `3bc7ea1e2241b718b23d70c26d2e5840f5810c92`.
- 선별 승격: `267c4915f6f30dea5a1f62c14afa857e79ef5b5f` (16개 운영 파일).
- PDF 범용 서식 머리말 회귀 수정 후 **운영 최종 `main` HEAD `6eef107c6b080b30fa54ecb16eda3ebbcb6daba0`**.
- 운영 파일 총 17개, 원본 대비 변경 16개; `05_DOMAIN_MODULES.md`는 기존/개발본 동일해 보존. `V2_*` 개발 기록, OpenSSH 전용 원고, `HISTORY/*`는 `main`에 넣지 않았다.
- 최종 부트스트랩 `PROJECT_BOOTSTRAP.md` blob `83bf726eed94c07c17be734626c26ab01f9e571c`.
- 사용자 승인 PDF 공통 서식 `final_pdf_html_formatting_instruction_final.md`와 `final_pdf_report_style.css` blob `749bee7420e36277daa1465dbcad539c84761c6e`. WeasyPrint 68.0으로 표적 예시 A4 14페이지 재출력, 빈 페이지·용지 밖 텍스트 블록 미검출(이 예시와 해당 렌더러에 한정).
- 실사용 설치·교체 안내: `INSTALL_CHATGPT_PROJECT.md`.

## 역사 보존과 미검증 상태
- 개발 평가 기준 스냅샷 `90290ee93b907069dd9b48ee4ed1103c59a22485`와 감사·결정/반려/보류 기록은 `archive/research-v2-development-20261011`에서 추적 가능.
- 초기 반려 PDF 시안: `HISTORY/pdf-style-smoke/`. 사용자 승인 디자인 CSS 원본·참고 HTML 및 검증 해시: `HISTORY/pdf-style-approved/`.
- D01 축약 E2E와 LONG-LITE-01~04는 각각 **검증된 관찰 범위 PASS**. LL03 내부 호출 전수 로그 미확인. /handoff → 목적어 없는 '검토해줘' 최초 P1 FAIL은 그대로 FAIL(후속 규칙 수정으로 소급 회복 금지).
- R5/CAS/API/UI, 100~200쪽 신규 작성, 실측 토큰 절감, 실제 ChatGPT 프로젝트 규칙 주입 SHA는 이전 기록대로 미시험/UNKNOWN.
- **GitHub 운영 승격 완료 ≠ ChatGPT 프로젝트 설치·실사용 검증 완료.** 프로젝트 지침과 첨부 파일은 사용자가 직접 교체하고 일반 조사 및 `research/*` 신규 채팅에서 검증할 계획. 새 채팅 A/B 런타임 테스트는 아직 실시하지 않았다.
- 기존 연구·개발·시험 브랜치는 **삭제하지 않았다**. 실제 삭제 직전 고유 자료 및 보존 ref 검증 필요.
