# 중요 그래프 실물보존 — 실제 적용·검증 결과 (2026-10-11)

## 기준
- 패치 기준 운영 main: `1433cc780101967087abb5d0e093058a3aa2cef2`.
- 후보 브랜치: `design/core-visual-materialization-20261011`.
- 기존 역사 개발 아카이브를 읽고 과거 FAIL/회복 분리, GitHub blob 실물 확인, 서로 다른 판정 종류와 no-write 경계 원칙을 사용.

## 실제 트럼프 연구 복구
- 연구 브랜치의 W1 승인율 2026 대표 관측 10개 → SVG/CSV 저장 → W1 본문 이미지 임베드 → GitHub 실제 재조회. **10/10 값 일치**.
- 연구 브랜치의 W7 해외분쟁 최대문제 관측 2026-02 1%, 03 14%, 04 8% → SVG/CSV 저장 → W7 본문 이미지 임베드 → 실제 재조회. **3/3 값 일치**.
- 실물 파일: `assets/W1-VIS-F03_reuters_ipsos_approval_2026.{svg,csv}`, `assets/W7-VIS-F01_war_issue_salience_2026.{svg,csv}`.
- 이전 ChatGPT UI 픽셀/툴팁 회수는 불가능했으므로 실제 데이터 재생성 그래프다. 연구 파일 자체에서 이 한계를 명시함.

## 후보 규칙 검증
- 원격 파일 재조회: `PROJECT_BOOTSTRAP.md`, `02_RESEARCH_PIPELINE.md`, `04B_VALIDATION_RULES.md`, `04_STATE_MANAGEMENT.md`, `13_FINAL_REPORT.md`, `tests/CORE_VISUAL_MATERIALIZATION_CASES.md`. 실물 자산 요구·재조회·부정 판정·최종 선택된 그림 수록·비저장 예외 유지 확인.
- 정상 조사 그래프 2건: **2/2 PASS**.
- 데이터/그래프 불일치 또는 누락을 주입한 대조: SVG 파일 없음 / 본문 이미지 링크 없음 / CSV 한 값 변조 / W7 3월 막대 누락 → **4/4 의도한 결함 탐지**.
- 첫 번째 테스트 하네스는 Markdown 내 첫 동일 URL 링크만 바꿔 실제 이미지 링크를 제거하지 못했는데도 제거했다고 가정한 **시험 입력 자체 오류**가 있었다. 이를 이미지 문법 `![...](...)` 연결을 정확히 제거하는 입력으로 수정해 재실행했으며 그 결과 4/4를 검출했다. 초기 실패를 규칙 결함이나 성공 기록으로 오인하지 않는다.
- 기존 연구 브랜치 외 자료 삭제/병합 없음. 메인 규칙은 비강제 업데이트와 버전 확인으로만 배포.

## 판정 경계
- **정적 규칙 적용 PASS / GitHub 실물 파일·링크·CSV↔SVG 내용 대조 PASS**.
- 신규 ChatGPT 프로젝트에 수정 부트스트랩이 실제 주입되어 추가 지시 없이 매번 그림을 자동 생성하는지 **LIVE MODEL E2E NOT RUN**.
- 사용자 화면 원형과 재생성 SVG의 시각적 완전 동일성 **UNKNOWN**.
- no-write, 원격 저장 장애, 경쟁 HEAD 변경, 이후 조사 값 수정, 선택형 최종보고서 제작은 **설계 검사만**, 별도 실전 E2E NOT RUN.
