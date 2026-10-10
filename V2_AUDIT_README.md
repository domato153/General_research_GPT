# 범용 조사 엔진 v2 — 외부 독립 감사 패키지 INDEX (2026-10-10)

> **최신 새 스레드 재개·역추적 보완(2026-10-10):** [V2_NEXT_THREAD_START_HERE.md](V2_NEXT_THREAD_START_HERE.md) → [V2_DECISION_REGISTER.md](V2_DECISION_REGISTER.md) → [V2_HANDOFF_GAP_AUDIT.md](V2_HANDOFF_GAP_AUDIT.md) → [V2_REQUIREMENT_DISPOSITION_CROSSWALK.md](V2_REQUIREMENT_DISPOSITION_CROSSWALK.md). **외부 감사 원본 1·2·3차도 독립 보존 완료**. 실제 규칙 frozen `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`, BASE `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0`. **규칙 개발·정적 검증과 실제 모델 E2E 미실행을 구별**. 아래 초기 감사 문서·옛 후보 SHA는 이력이며, 새 평가 채팅은 이 최신 시작 파일을 우선한다.

> **3차 감사 보완 및 정적 검증 종료 — 신규 평가 시작점:** [V2_REAUDIT_03_FINAL_GATE.md](V2_REAUDIT_03_FINAL_GATE.md) → [V2_E2E_READY_HANDOFF.md](V2_E2E_READY_HANDOFF.md) → [V2_E2E_PRE_POST_PROTOCOL.md](V2_E2E_PRE_POST_PROTOCOL.md). 규칙 고정 `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`, BASE `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0`, N01~12/X01~48. **3차 외부 감사의 B 판정과 P1-A/B 국소 대응은 완료했으나 실제 모델 E2E/무회귀는 NOT TESTED**. 아래의 과거 3차 감사 요청서와 이전 SHA는 역사 참조이며, 동일 감사 요청을 새 E2E 모델에 주입하지 않는다. 

> **최신 작업 상태 — 3차 재감사 B, 국소 P1/P2 패치 완료 (2026-10-10):** [V2_REAUDIT_03_REMEDIATION.md](V2_REAUDIT_03_REMEDIATION.md)에서 사용자 첨부 3차 감사의 P1-A/P1-B와 추적표/모드/비용 P2 지적에 대한 **실제 수정·검증·한계**를 확인한다. **최신 규칙 고정 SHA `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`**, 변경 전 BASE `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0`. E2E는 [V2_E2E_PRE_POST_PROTOCOL.md](V2_E2E_PRE_POST_PROTOCOL.md) **N01~N12 / X01~X48**로 시행한다. [V2_THEORETICAL_COVERAGE_MATRIX.md](V2_THEORETICAL_COVERAGE_MATRIX.md)의 59행 소스 위치·시험 ID는 실제 동결 파일에서 확인했고, 공유·비대칭 시험의 **독립성은 미입증**이라고 기록했다. **실제 독립 모델 E2E·장애 주입·PDF/비용은 NOT TESTED**. `main` 승격은 범위 밖.

> **역사: 세 번째 외부 감사 직전의 요청 자료:** [V2_THIRD_REAUDIT_KIT.md](V2_THIRD_REAUDIT_KIT.md) + [V2_THIRD_REAUDIT_PROMPT.md](V2_THIRD_REAUDIT_PROMPT.md) + [V2_THIRD_REAUDIT_SCORECARD.md](V2_THIRD_REAUDIT_SCORECARD.md). 현재 감사 규칙 SHA는 `3c0a2e85f6d1f3a8b91ec2c3eabd38ccbb58ca33`; 그 아래 기록된 `c9f8...` 및 `0e572...`와 기존 감사 요청서는 **이전 회차 역사본**. 3차 평가는 두 번째 감사 지적을 수정한 최신 규칙에 대해 read-only로 실시. **새 독립 모델 실제 E2E는 NOT TESTED**.

> **최신 상태 — 2차 외부 재감사 완료 및 수정 반영:** 2차 Temporary 감사는 기존 개발 규칙 `0e5721...`을 검토해 **'수정 후 재감사'**를 판정했다. 지적된 P1/P2를 `design/research-v2`에 보완했으며 새 규칙 고정 SHA는 **`3c0a2e85f6d1f3a8b91ec2c3eabd38ccbb58ca33`**. **최신 정본은 [V2_REAUDIT_02_REMEDIATION.md](V2_REAUDIT_02_REMEDIATION.md), [V2_THEORETICAL_COVERAGE_MATRIX.md](V2_THEORETICAL_COVERAGE_MATRIX.md), [V2_E2E_PRE_POST_PROTOCOL.md](V2_E2E_PRE_POST_PROTOCOL.md)**. 소스/연관시험 **59/59**, 평가규약 3항목을 뺀 56개 행동 요구의 정상·부정 시험 설계, 실패·폴백 34건. 이 결과는 **실제 모델 E2E 성공이 아니다**. 아래 첫 감사 요청서와 2차 감사 요청서는 각각 **이미 수행한 외부 감사의 당시 기록**이다. 지금 단계의 다음 작업은 **동등조건 실제 자연어 E2E·T06-R·X29/X30**이며 `main` 변경이 아니다.

> **첫 감사 후·두 번째 감사 전 상태 (역사 기록):** 외부 감사 권고를 반영한 규칙이 **`design/research-v2`에 PR #1으로 적용 완료**. 정확한 고정 규칙 ref는 `0e5721bc730f6f8b67f816bf0e589b8870b43d8b`이며, 소스·시험 계획 전수 매핑 **59/59**, 보호 계약 **18/18**, 개발 적용 7개 규칙 blob 동일성을 별도 재검증했다. **독립 ChatGPT 실사용 E2E는 NOT TESTED**. `main`은 이번 작업의 적용 대상이 아니다. **이 문서의 2차 재감사는 이미 끝났다. 현 시점에 같은 요청서를 반복 제출하지 않는다.** 아래 구후보 `c9f8...` 관련 절과 초기 26/30 검사 내용은 **첫 번째 외부 감사 당시의 역사적 기록**이며, 현재 적용 규칙으로 오인하면 안 된다.

## 초기 외부 감사 당시의 결과 (역사 기록)
**첫 외부 비개인화 read-only 감사를 시작할 당시의 상태**다. 원문 규칙 개정 후보와 22개 이슈·기존 실제 E2E·동일 정적 검증·자체 모의 전이·동등조건 실제 E2E 계획 및 부정시험이 모두 준비됐다. 하지만 **변경 전/후 새 독립 ChatGPT 실제 E2E는 아직 실행하지 않았고**, 운영 main 병합/규칙 정식 배포는 **불허/승인 대기** 상태다.

## 가장 먼저 열 파일
1. **V2_EXTERNAL_AUDIT_REQUEST.md** — 별도 Temporary / Unpersonalized 감사에게 복사할 **외부 평가 요청문**.
2. **V2_EXTERNAL_AUDIT_HANDOFF.md** — 평가자 작업 지도, 전체 검증할 질문·출력 계약.
3. **V2_FULL_ISSUE_INVENTORY.md** — E01~E22, **초기 협업 실패 및 계획추적부터 마지막 감사·편집·반례 누락까지**.
4. **V2_CANDIDATE_CHANGE_SPEC.md** — 7개 규칙 파일 변경의 근거·기대 동작·범위·보호 게이트.
5. **V2_SELF_REVIEW_AND_LIMITATIONS.md** — 현재 패치의 중복 규칙/비용/정보 유실/CAS/실제 주입 SHA 등 R01~R12 비판.

## 테스트와 재현
| 파일 | 정확한 의미 | 현재 결과 |
|---|---|---|
| V2_TEST_RESULTS.md (§§1~48) | 다른 시험 프로젝트에서 사용자가 제공한 **실제 모델 출력과 GitHub 증거** 기록 | C10/C13 최초 FAIL, C14 최초 Stage7 PARTIAL; 회복은 별도 PASS |
| V2_BEFORE_BASELINE_REPLAY.md | 변경 전 고정 규칙 8파일, **26 정규식 문구 앵커**와 과거 실제 출력의 리플레이 | **13/26 문구 FOUND** |
| V2_BEFORE_AFTER_STATIC_VERIFICATION.md | **동일 26 정규식** 변경 전후, 원래 파일 줄 보존 | **13/26→19/26 문구 FOUND; 기존 8파일 모든 줄 순서보존** |
| V2_SCENARIO_GATE_WALKTHROUGH.md | **소스앵커 기반 합성 30 전이 시나리오**, 두 버전의 요구계약 표현 확인 | **8/30→30/30 문구 충족; 독립 모델 E2E 아님** |
| V2_AUDIT_FIXTURE.md | 두 합성 도서관·사전추세/동일 사용자의 **중요 반례가 원고에서 빠진 결함 주입** | 실제 연구가 아닌 인위적 테스트 재료 |
| V2_E2E_PRE_POST_PROTOCOL.md | BASE/CANDIDATE 독립 프로젝트·자연어 N01~N12·부정 X01~X28·냉시작 T06-R (현재 파일은 적용 규칙 SHA로 보정됨) | **실제 독립 실행 NOT TESTED**, 외부 시험 운영용 |

이 수치는 **규칙 문구와 자체 시나리오가 서술된 정도**에 불과하다. 정적 19/26 또는 자가 30/30을 **실제 LLM 성공률이라고 평가하면 오류**다. 사용자에게 내부 체크리스트를 길게 넣은 대화 결과를 자율성 PASS로 인정하지 않는다.

## 초기 외부 감사 당시 읽기 기준 — 현재 비교 대상으로 사용하지 말 것
- **변경 전 BASE:** cd64bef326544cacc0dc05fe6f65d9e1bd318fc0
- **변경 후 CANDIDATE 고정 SHA:** c9f8b9a52eab43e24f322e19da03e3006504a206
- GitHub: https://github.com/domato153/General_research_GPT
- 비교: https://github.com/domato153/General_research_GPT/compare/cd64bef326544cacc0dc05fe6f65d9e1bd318fc0...c9f8b9a52eab43e24f322e19da03e3006504a206
- **7개 후보 변경 파일:** PROJECT_BOOTSTRAP.md, 00_INDEX.md, 02_RESEARCH_PIPELINE.md, 03_REVIEW_MODULES.md, 04_STATE_MANAGEMENT.md, 04B_VALIDATION_RULES.md, 13_FINAL_REPORT.md. 비변경 CORE, 상태 템플릿, 도메인 모듈 등은 회귀 대상으로 남는다.
- **문서/감사 작업 브랜치:** audit/v2-e2e-hardening-20261010. 감사 문서 추가로 HEAD가 움직여도 **후보 규칙은 위 동결 SHA를 사용**한다.

## 주의: 과거 실제 E2E와 새 후보의 버전 차이
기존 AI 고용 연구 브랜치 출발 SHA는 fb22fe86834893e607072b41885277d29cfc57fc였다. 과거 실제 프로젝트에 최신 설계 규칙 a10efe04c354bdae463c77424f7672f9615916da가 로딩됐는지 확인하지 못했다. **그 과거 실사용 C1~C14는 문제 재현 자료**로 가치가 있지만, 동결 BASE vs 동결 CANDIDATE의 동일조건 실사용 비교로 주장할 수는 없다.

## 권장 외부 감사 작업 순서
1. 먼저 E01~E22 및 역사 실측의 **관측/추론/미검증**을 따로 분류한다.
2. 실제 SHA 비교로 7파일 패치만 존재하고 운영 main·연구 브랜치가 변경되지 않았는지 독립 확인한다.
3. R01~R12의 반대 가설·비용/권한/중복·Stage5/Stage7 조건 충돌을 의도적으로 찾는다.
4. 외부 심사자는 읽기 전용 판단만 수행하고 **P0/P1/P2** 미해결과 최소 수정안을 제시한다.
5. 외부 감사 후 필요한 수정 승인 시 다른 고정 후보 SHA 생성 → 변경 전/후 실제 독립 모델 자연어 E2E → T06-R 냉시작 및 GitHub 실패/동시성 부정시험 → 최종 운영 반영 여부 사용자 결정.

이 패키지 자체에 실사용 최종 성능 PASS나 운영 배포 승인 권한은 없다.
