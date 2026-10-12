# v2 개발 역사 보존 · 2026-10-11

- 동결 전 개발 HEAD: `90290ee93b907069dd9b48ee4ed1103c59a22485` (`design/handoff-fidelity-review-20261011`).
- GitHub `V2_*` 진행·감사·채택/비채택·보류·미시험, 최초 P1 FAIL와 회복 근거 및 과거 설계 규칙 전체가 이 archive 브랜치의 원본 트리에 보존됨.
- PDF-STYLE 최초 피시험 HEAD: `0b34dcfa02a88d687ef25a474a84c9a924396dd5`; 원본 `report.html` blob `11d00ce36fa3af2ab8beb3f49f622ce89baf0b29`, `report_style.css` blob `2f18e0c528c92ba8c538f33ab678a1c8d8644d1e`를 `HISTORY/pdf-style-smoke/`에 정확히 복사 (사용자 반려 구서식).
- 이후 사용자가 승인한 신규 디자인은 이 구서식과 별개이며, 일반 운영 지침·범용 CSS로만 본선 적용하고 실제 OpenSSH 결과물은 연구 기록으로 보존한다.
- `main`은 조사 템플릿 전용. 실험 로그·고유 주제 원고·실행 fixture는 `main`으로 병합하지 않는다.
- 기존 `research/*`의 개별 연구 자료는 이 archive에 자동 포함되지 않음. 향후 삭제 전 각 브랜치 최종 HEAD와 고유 내용의 불변 보존 경로를 별도 검증해야 한다. 현재 어떤 연구 브랜치도 삭제하지 않는다.
- 초기 운영 main 기준 SHA: `3bc7ea1e2241b718b23d70c26d2e5840f5810c92`. 최초 13개 원본 기준 SHA: `bf7b315a2b3316fc96c763d3ba82c4234a849bfc`.

## 후속 v2 운영 개선 및 설계 브랜치 정리 (2026-10-12)
- `HISTORY_POST_V2_DEV_CLEANUP_20261012.md`: 최근 개발 브랜치별 고정 HEAD·부모 이력 보존·주요 개선·실제 시험/미검증·정리 결과와 복구 방법. 이 문서는 **2026-10-11 최초 v2 이력의 대체본이 아니다**.

## Full Report 상세형 충실도 개선 보존 (2026-10-12)
- `HISTORY_FULL_REPORT_FIDELITY_20261012.md`: 외부 감사 교차검증, 주요 설계 결론, 운영 `main` `75b8c3e` 패치·32 PASS/1 SKIP 정적 검증과 실전 E2E 미검증 구분, 역사보존 추가 부모 커밋 및 세 브랜치 상태.
## PDF 시각화·페이지 조판 실전 보완 (2026-10-12, 후속 역사기록)
- [`HISTORY/pdf-quality-20261012/README.md`](HISTORY/pdf-quality-20261012/README.md): W8 실물 PDF에서 확인된 출처↔축 겹침·단일 범주 과대 공백·밀집 날짜 눈금·대장 중간 시작·장식 HR 빈 페이지까지의 **문제→수정→실패→재시험→남는 경계**와 복원 명령을 통합 기록.
- [`HISTORY/pdf-quality-20261012/W8_VISUAL_LAYOUT_REMEDIATION_20261012.md`](HISTORY/pdf-quality-20261012/W8_VISUAL_LAYOUT_REMEDIATION_20261012.md): 연구 브랜치의 원래 SVG 교정 36쪽 판 감사 파일을 Git blob 그대로 재사용.
- [`HISTORY/pdf-quality-20261012/W8_PDF_PAGINATION_IMPROVEMENT_AUDIT_20261012.md`](HISTORY/pdf-quality-20261012/W8_PDF_PAGINATION_IMPROVEMENT_AUDIT_20261012.md): 실제 42쪽 최종 보고서의 페이지 조판·상단 장 시작·빈 페이지 검수 파일을 Git blob 그대로 재사용.
- 관련 운영 `main` 커밋: `1045ef57672a93637b628e21227ede7be327e381`, `3f60f9376237496cc30c09a835c14ea5bbbdca8a`, `297535465be5819323c012d3dd7f3ea33ac8de9b`.
- 보존 시점 운영 `main` HEAD `297535465be5819323c012d3dd7f3ea33ac8de9b`, 연구 HEAD `e84adae6e7131cfc33105f39d229268fdf696443`, 직전 역사 HEAD `462c6c05f883e6669db008eb4a0e0878bf40ac48`.
- 역사 기록용 커밋은 위 **직전 archive HEAD를 첫 부모**, 해당 main·research 고정 HEAD를 추가 부모로 하여 각 정본의 당시 원본 코드/검증기/CSV/SVG/PDF Git 객체를 실제 연결한다. 루트의 과거 `PROJECT_BOOTSTRAP.md` 등 구판 운영 파일은 변경하지 않는다. 이 기록은 원본 조사자료를 운영 `main`으로 옮긴 사실을 뜻하지 않는다.

## 운영 제안·단계별 관문 계약 개선 (2026-10-12)
- [운영 관문 이력](HISTORY/operating-gate-20261012/README.md): 기존 번역 배치별 운영 제안 영수증에서 파생된 조사 Stage별 제안·종합 전환 강제 검사, 운영 `main` `ce1bc9d9cd2a422dc18e783ba5991b6b50b1948c` 및 트로그 롤아웃 `3d6be6e4191b5124dfbe3a2d48e43214c075c6fe`의 정확한 권한 범위와 역사적 증거를 보존.
- [회귀 결과와 제한](HISTORY/operating-gate-20261012/REGRESSION_RESULTS.md): 기존 JS 동등 재시험 11+9, 신규 20, 결손 변형 5, 보존용 JS 시험 21의 **정적 PASS**, Python/독립 모델 E2E NOT RUN 명시.
- 역사 커밋은 위 시점의 운영 main·연구 커밋을 추가 부모로 연결하고, 기존 루트 파일·연구 원고는 복제/치환하지 않음.
