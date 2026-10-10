# 새 스레드 시작점 — 범용 딥 리서치 v2 개발 평가자 (2026-10-10)

**처음 3분 안에 읽을 이력·결정·문제·실험 계획의 인덱스. 새 스레드에서 다른 프로필·이전 채팅 없이 GitHub 읽기만으로 목적·권한·버전·미시험을 복원하도록 작성.**

## 0. 지금 당장 유효한 판정

> **개발 규칙 개선과 외부 3차 감사 B의 P1-A/P1-B/P2 국소 수정 완료. 59개 요구와 33개 채택 결정(기능 직접 25·관리/평가 8)의 양방향 추적 보완, 반려 결정 REJ-01~18와 시험 N01~12 ID 충돌 분리, 시험 N05/N11/X08까지 역추적 연결. 감사 1~3차 원문 보존. 이는 기록·정적 검증이며 실제 독립 GPT E2E/T06-R/실물 실패주입·비용 무회귀는 NOT TESTED. 다음 작업은 BASE↔CANDIDATE 자연어 독립 실사용 시험.**

### 네 가지 재현 좌표
- 저장소: `domato153/General_research_GPT`
- **평가/개발 브랜치:** `design/research-v2` — GitHub 최신 HEAD는 읽어서 확인하되 **후보 규칙으로 사용하지 않음**.
- **BASE:** `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0`
- **현행 후보 규칙 frozen SHA:** `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`
- **보호:** `main`, `research/20261010-ai-employment-kr-us-1538-fb22`는 수정하지 말 것. `0e572...`·`3c0a...`·`c9f8...`는 과거 감사/수정 기록.
- **역할:** 이 스레드는 **엔진 개발 평가자**로, 실제 조사 모델이 작성한 보고서·도구 로그·GitHub 결과를 독립 평가한다. 과거 AI 고용 연구를 대신 재시작하지 않음. 새 모델 자연어 E2E는 **별도 비개인화/격리 시험 프로젝트**에서 진행.

## 1. 권장 읽기 순서 (신규 스레드에서도 도구로 검증)

| 순서 | 파일 | 읽어야 할 이유 |
|---|---|---|
| 1 | [V2_NEXT_THREAD_START_HERE.md](V2_NEXT_THREAD_START_HERE.md) | 지금 역할·기준 좌표·다음 단계 |
| 2 | [V2_DECISION_REGISTER.md](V2_DECISION_REGISTER.md) | 채택 A01~A33 **33건** / 비채택 REJ-01~REJ-18 **18건** / 보류 P01~P12 **12건**, 출처별 판단 |
| 3 | [V2_HANDOFF_GAP_AUDIT.md](V2_HANDOFF_GAP_AUDIT.md) | 20개 인계 안전 점검 및 아직 검증 못한 위험 |
| 4 | [V2_REQUIREMENT_DISPOSITION_CROSSWALK.md](V2_REQUIREMENT_DISPOSITION_CROSSWALK.md) | 59개 요구 ↔ 기능관련 채택 25건 + 관리/범위·평가 채택 8건, 후속/회복 N05·N11·X08까지 역추적 |
| 5 | [V2_HANDOFF_TRACEABILITY_RECHECK.md](V2_HANDOFF_TRACEABILITY_RECHECK.md) | **이전 검토의 3가지 결함 보완 후 자동 재검사 결과**·원문 파일/링크/규칙 SHA 불변 |
| 6 | [V2_REAUDIT_03_FINAL_GATE.md](V2_REAUDIT_03_FINAL_GATE.md) | 마지막 규칙 동결·3차 감사 조치 정적 검증 결과 | 
| 7 | [V2_E2E_READY_HANDOFF.md](V2_E2E_READY_HANDOFF.md) | 실제 BASE↔후보 설치, 필수 자연어 최초 테스트·도구실패 |
| 7 | [V2_E2E_PRE_POST_PROTOCOL.md](V2_E2E_PRE_POST_PROTOCOL.md) | N01~N12 일반 사용자 입력·X01~X48 부정/경합/권한 테스트 |
| 필요시 | [V2_TEST_RESULTS.md](V2_TEST_RESULTS.md) §§1~48, [V2_FULL_ISSUE_INVENTORY.md](V2_FULL_ISSUE_INVENTORY.md) | 역사적 E2E·초기부터 모든 문제 |
| 필요시 | [외부 1차 원본](V2_EXTERNAL_AUDIT_01_ORIGINAL.md), [2차 원본](V2_EXTERNAL_AUDIT_02_ORIGINAL.md), [3차 원본](V2_EXTERNAL_AUDIT_03_ORIGINAL.md) | 제3자의 실제 판단을 개발자 조치·요약과 구별 |
| 필요시 | [V2_PROGRESS_CHECKPOINT.md](V2_PROGRESS_CHECKPOINT.md) §22, [V2_EXECUTION_PLAN.md](V2_EXECUTION_PLAN.md) §33 | 누적 상태·고정 기준·새 인계 작업의 근거 |

## 2. 결정에 관한 절대적 오해 방지

- **사용자가 직접 결정:** 개선안은 **개발 브랜치에 적용**하고 `main` 승격은 이번 작업 목적이 아님. 다음 스레드 인계·독립 실증 준비. 사용자의 자연어만으로 엔진이 중요한 선택을 제안해야 한다.
- **외부 감사자의 판단:** 첫째/둘째는 '수정 후 재감사', 셋째는 **B — P1 최소 수정 후 E2E 진입**. 3차 B는 개발자 사후 코드 수정으로 **A로 소급 변경되지 않음**.
- **개발자 채택·적용:** Stage 5 최초 편집안 선저장(허용 시), 명시적 GitHub 비저장 우선, 읽기실패 별도 X29, 화면↔저장 X30, revision X47, 반론·원고 국소 검수, 편집 선택 3분기, 중복 검색/승인 억제.
- **반려/비채택(REJ-01~REJ-18; 시험 N01~N12와 다른 ID):** `main` 즉시 패치, 자동 W06 수행·보고서 최종화, 가짜 2~3개 선택지, 원고 단순 누락 때 전면 재조사, SHA=원자적 CAS 주장, 59/59=실제 E2E 성공 주장, 오래된 후보 SHA 사용 등.
- **미실행·보류는 반려가 아님:** 실제 신규 모델 E2E/냉시작/READ·WRITE 실패/UI↔blob/PDF/비용/활성 주입 SHA. 대기 중인 사항은 [결정 대장 P01~P12](V2_DECISION_REGISTER.md) 참조.
- **과거 최초 모델 실패 유지:** C10 자발 감사 FAIL, C13 내용 편집 공동 선택 FAIL, C14 핵심 반론 누락 Stage7 PARTIAL. C11/C13-R/C14-R의 별도 회복 PASS가 최초 실패를 지우지 않는다.

## 3. Project 소스/부트스트랩 주의

현재 프로젝트에 첨부되어 읽힌 기존 `PROJECT_BOOTSTRAP.md`는 일반 운영 `main`을 기준으로 안내하지만, **별도 설계 검증 모드는 frozen 후보 SHA `ac4675...`를 실제로 사용해야 한다.** GitHub 개발 브랜치의 규칙 개정으로 Project 첨부/설정이 자동 변경되지는 않는다. 평가자 스레드는 이 파일에서 dev 역할을 명시 확인한다. **피시험용 새 ChatGPT 프로젝트**는 규칙 실제 주입/버전과 GitHub 도구 권한을 시험 운영자가 확인해야 한다.

## 4. 다음 스레드 첫 번째 행동

1. **Read-only**로 `design/research-v2` HEAD 확인 후 위 문서 1~6을 읽고, 어떤 버전을 평가해야 하는지·채택/반려/미검증 수·실제 신규 E2E 미실행을 복원해 짧게 사용자에게 보고한다.
2. 새 스레드가 정확한 파일이나 GitHub 브랜치를 읽을 수 없으면 **읽기 실패와 복원 미완료**를 명시하고, 임의로 `main` 기준이나 과거 후보로 변경하지 않는다.
3. 실제 BASE↔후보 두 시험 프로젝트를 운영자가 준비했다는 근거가 오면 `V2_E2E_PRE_POST_PROTOCOL.md`를 **평가자용**으로 활용한다. 피시험 모델의 실제 사용자 문구에는 평가 정답/내부 Stage/W-ID/59행 목록을 넣지 않는다.
4. 사용자에게 새 E2E 실행 허가가 없으면 **실제 연구 브랜치 생성·원고 작성·시험 가동을 독단적으로 시작하지 않는다**. 단순 복원 질문에는 역할/계획만 정확히 보고한다.
5. 이후 P0/P1이 발견되면 `design/research-v2` 규칙만 영향범위 최소 패치, 새 frozen SHA 생성, 59행 재검증, 실패/회복을 분리 기록한다.

## 5. 새 스레드에서 붙여 넣을 최단 메시지

> GitHub `domato153/General_research_GPT`의 `design/research-v2` 개발 평가를 이어가자. **먼저 read-only로 `V2_NEXT_THREAD_START_HERE.md`와 그 안의 결정 대장·누락 점검·E2E 인계 문서를 실제 읽고**, 현재 고정 규칙 SHA/채택·반려·미검증 상태/마지막 완료 지점과 다음 작업만 확인해줘. **운영 `main`과 과거 연구 브랜치는 건드리지 말고, 실제 E2E는 내 다음 지시 전 시작하지 마.**

**인계 검증 결과:** 파일·외부 원문·채택·비채택/보류 목록은 GitHub에서 재조회 가능. **진짜 '다른 새 채팅에서 독자적으로 재개되는가'의 T06-R 실제 시험은 아직 하지 않았으므로 PASS라고 쓰지 않는다.**
