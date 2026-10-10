# v2 개발 역사 보존 · 2026-10-11

- 동결 전 개발 HEAD: `90290ee93b907069dd9b48ee4ed1103c59a22485` (`design/handoff-fidelity-review-20261011`).
- GitHub `V2_*` 진행·감사·채택/비채택·보류·미시험, 최초 P1 FAIL와 회복 근거 및 과거 설계 규칙 전체가 이 archive 브랜치의 원본 트리에 보존됨.
- PDF-STYLE 최초 피시험 HEAD: `0b34dcfa02a88d687ef25a474a84c9a924396dd5`; 원본 `report.html` blob `11d00ce36fa3af2ab8beb3f49f622ce89baf0b29`, `report_style.css` blob `2f18e0c528c92ba8c538f33ab678a1c8d8644d1e`를 `HISTORY/pdf-style-smoke/`에 정확히 복사 (사용자 반려 구서식).
- 이후 사용자가 승인한 신규 디자인은 이 구서식과 별개이며, 일반 운영 지침·범용 CSS로만 본선 적용하고 실제 OpenSSH 결과물은 연구 기록으로 보존한다.
- `main`은 조사 템플릿 전용. 실험 로그·고유 주제 원고·실행 fixture는 `main`으로 병합하지 않는다.
- 기존 `research/*`의 개별 연구 자료는 이 archive에 자동 포함되지 않음. 향후 삭제 전 각 브랜치 최종 HEAD와 고유 내용의 불변 보존 경로를 별도 검증해야 한다. 현재 어떤 연구 브랜치도 삭제하지 않는다.
- 초기 운영 main 기준 SHA: `3bc7ea1e2241b718b23d70c26d2e5840f5810c92`. 최초 13개 원본 기준 SHA: `bf7b315a2b3316fc96c763d3ba82c4234a849bfc`.
