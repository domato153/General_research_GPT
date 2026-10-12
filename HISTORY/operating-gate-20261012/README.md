# 2026-10-12 운영 제안·단계 전환 관문 개선 보존

**역사 기록, 운영 규칙 정본 아님.** 현행 운영은 `main`의 AGENTS / 06_COLLABORATION_WORKFLOW / 02_RESEARCH_PIPELINE / 04_STATE_MANAGEMENT에서 조회한다. 이 브랜치 루트의 구판 규칙을 재사용·복사하지 않는다.

## 배경과 승인
- 실전 연구 `research/20261012-throgg-903`의 W01~W08 수집/초안 작성 중 **계획 밖 확장 관문이 자발적으로 발동하지 않았음**. 사용자가 이를 지적해 W10_PLAN_EXPANSION_REVIEW.md에서 최초 사후 후보 D1~D4를 제시. 앞서 최초 트리거가 수행된 것으로 소급 기록하지 않는다.
- 사용자는 2026-10-12 `domato153/translation` 운영 `main`의 반복 배치별 `운영 파일 제안` 및 종료 라우팅을 참고한 전 단계 운영 제안 영수증 + 단계 전환 검사 방식에 동의했고, 범용 `main` 개선 및 트로그 연구 브랜치 롤아웃을 명시 승인.
- `translation` 실제 근거: 10_batch_translation_workflow.md의 각 배치 상태 (이번 승인 반영 권장 / 보류 제안 / 없음), 99_batch_request_prompt.md 출력 계약, 제안은 write authority도 QA HOLD도 아님. 그 저장소는 읽기만 하고 수정하지 않음.

## 적용된 정확한 변경
- 사용자 승인 전 운영 HEAD `d3cf57fb70c426ddcedc9631b45767678ed7c8bc`.
- 범용 운영 커밋 `ce1bc9d9cd2a422dc18e783ba5991b6b50b1948c` (4파일, 단일 원자 커밋, 기존 규칙 삭제 0줄).
- AGENTS: 활성 조사 최종 응답 하단 운영 제안 영수증.
- 06: 다섯 상태 `권장 / 보류 / 없음 / 해당 없음 / 미검토`, 단계별 관문·사용자 승인/자동진행 경계.
- 02: 단계 전환 전 실질 관문 검사, 연구 계획 밖 능동 스캔과 기존 작업 누락 확인 분리, 종합 전환과 종료/보고서 검수 라우팅.
- 04: 기존 RESEARCH_PLAN 진행 기록에 중요 변화만 보존, 매 응답 파일 mirror 금지.
- 트로그 롤아웃 커밋 `3d6be6e4191b5124dfbe3a2d48e43214c075c6fe`: RESEARCH_PLAN.md 진행 관문 상태 및 W11_OPERATING_GATE_ROLLOUT.md 신규 파일. 연구 FINAL_REPORT.md·W10 및 본문 연구 자료 무변경. D1+D2 추천은 아직 미승인, D 본조사·최종완성 별도 승인 유지.
- PROJECT_BOOTSTRAP.md 및 `translation` 저장소 무수정.

## 회귀 시험과 보존
- `REGRESSION_RESULTS.md`: 기존 v2 격리/아카이브 회귀계획과 정적 검사 재사용 범위, 최초 잘못된 테스트 정의·정정, 결과/불확실성.
- `test_operating_gate_contract.cjs`: **실제 이번 턴의 현재 main 내용을 주입해 평가한 동일 JS 테스트 원문**. 독립 재현: `node test_operating_gate_contract.cjs /경로/현행-main-체크아웃` (Node 실행 자체는 여기서 별도로 시험하지 못함).
- 기록한 결과는 STATIC PASS이지 **새 ChatGPT 프로젝트에 정확한 SHA가 주입된 모델 동작 E2E PASS가 아님**.

## 역사 앵커
이 문서를 추가하는 역사 브랜치의 커밋은 첫 부모가 기존 archive HEAD `1e877b2ea1cf617fad6c8f483386489cc3098b5b`, 추가 부모가 위 운영 `main` 커밋 및 트로그 연구 적용 커밋. 루트의 구판 운영 문서는 유지하고, 추가 부모의 Git 조상에서 당시 적용 실제 원본과 근거를 복원한다. `main`에 아카이브 기록이나 개별 연구 자료를 복사하지 않는다.
