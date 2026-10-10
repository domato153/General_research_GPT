# 요구사항 ↔ 결정 처분 ↔ 시험의 양방향 추적 (2026-10-10)

**목적:** 다음 스레드에서 '이전에 무슨 근거로 채택/반려/보류했는지'와 E01~E22/외부감사/기존 기능/T06/PDF 가운데 **어느 요구가 추적되지 않는지**를 별개로 점검한다. NASA 요구→설계→시험→결과의 양방향 추적 방법을 서식으로 참고했다.

- 변경 전 BASE `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0` / 현 규칙 동결 `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`, 개발 브랜치 `design/research-v2`.
- 기준 소스: [V2_THEORETICAL_COVERAGE_MATRIX.md](V2_THEORETICAL_COVERAGE_MATRIX.md)와 [V2_DECISION_REGISTER.md](V2_DECISION_REGISTER.md). **59/59 ID 모두 실존하는 A-결정과 연결, 시험 번호 참조 존재 검사.** 이는 소스 문자열·계획 간의 **매핑 검사**이며 의미상 충분성·실제 모델 동작 합격이 아니다.
- A-결정은 **채택·설계 문서상 구현의 추적점**, **REJ-결정은 반려·이번 범위 비채택·대체**, P-결정은 미실행·미확인의 추적점이다. 비채택 대안은 [V2_DECISION_REGISTER.md](V2_DECISION_REGISTER.md)의 **REJ-01~REJ-18**을 조회한다. 시험 프로토콜의 **N01~N12는 자연어 주시험이며 반려 결정 ID가 아니다.** **'시험 실패' = '사용자가 기능을 반려했다'가 아니다.**
- 평가 전용 E14/R11/R12는 모델 행동 테스트로 채점하지 않는다. 모든 실제 모델 E2E는 **NOT TESTED**.

## 59개 항목 실제 교차표

| ID | 보호할 요구/문제 | 소스 위치(고정 규칙) | 채택된 결정 ID | POS 참조 | NEG 참조 | FAIL/FALLBACK | 기존 추적표의 독립성 주의 | 실제 신규 E2E |
|---|---|---|---|---|---|---|---|---|
| E01 | 열린 의향·초기 착수 | `02_RESEARCH_PIPELINE.md:31` | A06 | N01 | N02 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E02 | 부분승인 | `04B_VALIDATION_RULES.md:159` | A06 | N02 | X38 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E03 | 잔여 W-ID 추적 | `02_RESEARCH_PIPELINE.md:337` | A08 | N07 | X22 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E04 | 최초 결과 공동검토 | `PROJECT_BOOTSTRAP.md:38` | A07 | N04 | X39 | — | SAME-DIRECTION/비대칭 의심; 실제 반대 상태 판정 필요 | NOT RUN |
| E05 | 최종 위임/권한 | `02_RESEARCH_PIPELINE.md:35` | A06,A10 | X02 | X01,X15 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E06 | 중간 중요방법 재선택 | `02_RESEARCH_PIPELINE.md:199` | A07 | X28 | X27 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E07 | 모집단과 임의사례 | `03_REVIEW_MODULES.md:10` | A09 | X23 | X31 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E08 | 판본·수치 | `03_REVIEW_MODULES.md:10` | A09 | X25 | X40 | X32 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E09 | 원문 확인 수준 | `03_REVIEW_MODULES.md:11` | A09 | N06 | X25 | X32 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E10 | 경쟁 인과 설명 | `PROJECT_BOOTSTRAP.md:51` | A09 | N06 | X19 | X32 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E11 | 최신 공시와 계획 | `03_REVIEW_MODULES.md:11` | A09 | X25 | X33 | X33 | SHARED SCENARIO: X33 | NOT RUN |
| E12 | 태그·분모 전제 | `03_REVIEW_MODULES.md:11` | A09 | X24 | X41 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E13 | 진행상태 최신화 | `04_STATE_MANAGEMENT.md:29` | A08 | X09 | X14 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E14 | 정적/모의/실제 구분 | `V2_E2E_PRE_POST_PROTOCOL.md:65` | A24,A29 | — | — | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E15 | C10 실제 감사 | `02_RESEARCH_PIPELINE.md:394` | A10 | N08 | X17 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E16 | C13 편집 선택 | `02_RESEARCH_PIPELINE.md:417` | A11,A13 | N09 | X15,X16,X46 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E17 | C14 반례 추적 | `02_RESEARCH_PIPELINE.md:551` | A13,A18,A14 | N10 | X06,X07,X30,X47 | X20,X46 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E18 | 부차적 편집 차이 | `13_FINAL_REPORT.md:764` | A11,A18 | N10 | X18 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E19 | 주입 규칙 SHA 검증 | `04_STATE_MANAGEMENT.md:28` | A05 | X12 | X42 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E20 | 냉시작 | `04_STATE_MANAGEMENT.md:25` | A20 | X10 | X11 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E21 | 기존 H/M/L 안전 | `PROJECT_BOOTSTRAP.md:54` | A21,A22,A23 | X05 | X03 | X04,X21 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| E22 | 사용성·PDF | `V2_E2E_PRE_POST_PROTOCOL.md:83` | A26,A28,A29 | N12 | X13 | X34,X35 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| H1 | 채팅 전달/원격보존 | `PROJECT_BOOTSTRAP.md:52` | A23,A16 | X45 | X44 | X04 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| H2 | 첫 결과 선제 제안 | `PROJECT_BOOTSTRAP.md:38` | A07 | N04 | X27 | — | SAME-DIRECTION/비대칭 의심; 실제 반대 상태 판정 필요 | NOT RUN |
| H3 | 경쟁 반론 | `04B_VALIDATION_RULES.md:185` | A09 | N06 | X19 | X32 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| M1 | 저장 실패 폴백 | `PROJECT_BOOTSTRAP.md:52` | A23 | X37 | X04 | X04 | SHARED SCENARIO: X04 | NOT RUN |
| M2 | 자료 인젝션 | `PROJECT_BOOTSTRAP.md:51` | A22 | N04 | X03 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| M3 | HEAD 원자성 경계 | `PROJECT_BOOTSTRAP.md:54` | A21 | X05 | X21 | X21 | SHARED SCENARIO: X21 | NOT RUN |
| L1 | 의미있는 옵션 수량 | `02_RESEARCH_PIPELINE.md:195` | A07 | X28 | X27,X48 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| L2 | 열린 요청의 우선조정 | `01_CORE_RULES.md:84` | A06 | N01 | N02 | — | SAME-DIRECTION/비대칭 의심; 실제 반대 상태 판정 필요 | NOT RUN |
| R01 | 반복 게이트·비용 | `02_RESEARCH_PIPELINE.md:554` | A27 | N12 | X13,X27,X48 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R02 | 과거 표시 선택 복원 불가 | `04_STATE_MANAGEMENT.md:30` | A15,A14 | X20 | X30,X47 | X20,X46 | SHARED SCENARIO: X20 | NOT RUN |
| R03 | 검수 전수탐색 비용 | `02_RESEARCH_PIPELINE.md:393` | A27 | X18 | X19 | X32 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R04 | 준비성≠W06 전체승인 | `02_RESEARCH_PIPELINE.md:394` | A10 | N08 | X17 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R05 | 편집 누락/원문 누락 분기 | `02_RESEARCH_PIPELINE.md:583` | A12 | X18 | X19 | X32 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R06 | 활성 규칙 미증명 | `04_STATE_MANAGEMENT.md:28` | A05 | X12 | X42 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R07 | 복수 연구 후보 충돌 | `04_STATE_MANAGEMENT.md:27` | A20 | X10 | X11 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R08 | GitHub CAS 과신 금지 | `PROJECT_BOOTSTRAP.md:54` | A21 | X05 | X21 | X21 | SHARED SCENARIO: X21 | NOT RUN |
| R09 | 원문·PDF 접근 난점 | `13_FINAL_REPORT.md:759` | A28 | X26 | X34 | X35 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R10 | 중복 승인 금지 | `02_RESEARCH_PIPELINE.md:417` | A17 | X02 | X15,X16,X48 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R11 | 외부 독립 감사 한계 | `V2_E2E_PRE_POST_PROTOCOL.md:65` | A29 | — | — | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| R12 | 실험 동일 조건 | `V2_E2E_PRE_POST_PROTOCOL.md:11` | A05 | — | — | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G01 | 쉬운 질문은 간단히 | `01_CORE_RULES.md:69` | A01 | N12 | X13 | — | SAME-DIRECTION/비대칭 의심; 실제 반대 상태 판정 필요 | NOT RUN |
| G02 | 기본값≠승인 | `01_CORE_RULES.md:75` | A06 | N01 | N02 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G03 | 계속은 다음 작업 한정 | `02_RESEARCH_PIPELINE.md:181` | A07 | N07 | X27 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G04 | 공개계획 승인 범위 | `00_INDEX.md:268` | A06 | N03 | N02 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G05 | 일괄 위임시 재승인 금지 | `02_RESEARCH_PIPELINE.md:417` | A11,A16 | X02,X45 | X44 | — | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G06 | 채팅만 전달된 결과 | `PROJECT_BOOTSTRAP.md:52` | A23,A16 | X45 | X44 | X04 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G07 | 쓰기실패 인계 | `PROJECT_BOOTSTRAP.md:52` | A23 | X37 | X04 | X04 | SHARED SCENARIO: X04 | NOT RUN |
| G08 | main/타브랜치 보존 | `PROJECT_BOOTSTRAP.md:54` | A22 | X05 | X03 | X21 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G09 | 승인된 기준 계획 원문 보존 | `04_STATE_MANAGEMENT.md:47` | A08 | N03 | X22 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G10 | 미착수 Summary 반박 | `04_STATE_MANAGEMENT.md:49` | A08 | X09 | X14 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G11 | 여러 W-ID 중복 근거 | `02_RESEARCH_PIPELINE.md:551` | A18 | N10 | X06 | X20 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| G12 | Segment Plan | `13_FINAL_REPORT.md:129` | A26 | X36 | X43 | X35 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| T06R1 | 단일 조사 브랜치 재개 | `04_STATE_MANAGEMENT.md:27` | A20 | X10 | X11 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| T06R2 | 최신 HEAD/후속 보정 | `04_STATE_MANAGEMENT.md:43` | A20 | X09 | X14 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| T06R3 | 복수 브랜치 구분 | `04_STATE_MANAGEMENT.md:27` | A20 | X11 | X10 | X29 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |
| T06R4 | GitHub 접근장애 폴백 | `04_STATE_MANAGEMENT.md:27` | A19 | X10 | X29 | X29 | SHARED SCENARIO: X29 | NOT RUN |
| T09 | PDF 렌더/한글/표 검수 | `13_FINAL_REPORT.md:759` | A28 | X26 | X34 | X35 | 독립성 미검증(서로 다른 ID만으로 입증 불가) | NOT RUN |

### E2E 착수 전 시험 독립성·소스 앵커 판정 보완 (2026-10-10)

- 이 표의 `file:line`은 **현재 이동하는 개발 HEAD가 아니라 frozen `ac4675d50bc0355b0939f7eb32b6fd72605acfb4` 규칙/프로토콜 원문**의 줄을 뜻한다. 외부 종합감사가 지적한 줄번호 초과 사례를 실제 원문으로 다시 읽은 결과 **59개 행 모두 존재하는 실제 줄**이었으며, E15/Pipeline:394·R05/Pipeline:583·G04/Index:268·T09/Final:759도 관련 계약을 가리켰다. 소스 위치 존재는 모델 행동 PASS나 시험 검출 능력 PASS가 아니다.
- SHARED 7행 / SAME-DIRECTION 4행의 **요구별 반증 상태·관찰 지표·동일 사건 중복 집계 방지** 규약은 [`V2_E2E_PRE_POST_PROTOCOL.md` F.3](V2_E2E_PRE_POST_PROTOCOL.md)에서 채점한다. 본 표의 POS·NEG 표시는 독립 반대 시험 수의 보증이 아니다.
- X37은 기존 GitHub 보존 승인 없는 독립 단발 채팅 전용 요청으로 한정하고, 기승인 조사에 대한 단순 채팅 추가 요청은 X45, 기존 승인 후 **명시적 쓰기 철회**는 X44 변형으로 구별한다. 기존 59개 요구·60개 N/X ID를 증설하거나 소급 PASS로 바꾸지 않는다.

## 분류 집계와 누락 검사

- E01~E22 **22/22**, 이전 감사 H1~H3/M1~M3/L1~L2 **8/8**, 신규 외부 위험 R01~R12 **12/12**, 기존 기능 보호 G01~G12 **12/12**, 냉시작 T06-R1~R4 **4/4**, PDF T09 **1/1**, 총 **59/59**을 현재 A-결정과 연결했다. **33개 A-결정의 역방향 검사**는 별도 수행: 59행이 참조하는 **25개 기능 관련 결정 + 아래의 관리·범위·평가 프로세스 결정 8개 = 33개**이며, 관리 결정을 억지로 모델 행동 요구에 배정하지 않는다.
- 원래 시험 번호 N01~N12/X01~X48의 존재만 확인했다. **같은 X-ID 여러 행/열 사용의 독립성 문제는 여전히 미해결**이며, 테스트의 시나리오별 **서로 다른 실패 조건**을 평가자가 직접 채점해야 한다.
- **외부 감사 원문 3개, 각 차수 대응 기록, 이슈 22개, 시나리오 N/X, 실제 결과 §§1~48, 사용/비사용 18개 대안**이 별도의 원문 출처로 보존되어 있으므로, 개발자가 뒤늦게 지적을 임의 '채택'으로 꾸밀 필요가 없다.
- '자료를 안 봤으면 UNKNOWN', '실제 신규 모델 시험이 없다면 NOT RUN', '대체된 후보는 SUPERSEDED', '사용자가 실제 거부하지 않은 것은 사용자 반려 아님' 원칙을 각 재개 시 보존한다.

## 59개 모델 요구 밖의 채택 결정 8건 — 역방향 거버넌스 추적

이 결정들은 중요하지만 **개별 모델 기능의 POS/NEG/FAIL 테스트로 분류하면 시험 완전성을 과장**한다. 59개 본문 행에 강제로 끼워 넣지 않고, 결정 원문·검증 증거·상태를 별도로 기록한다. 본문 행에서 제외해도 **결정 대장 33건 전체가 역방향으로 도달 가능**해야 한다.

| 채택 ID | 분류 | 이유 / 원래 결론 | 직접 확인할 원본·증거 | 실증 구분 |
|---|---|---|---|---|
| A02 | 사용자 범위 결정 | 개선안 적용은 개발 `design/research-v2`, `main`은 제외 | 사용자 정정 / GitHub `main` HEAD 보호 | SOURCE/BRANCH CHECK |
| A03 | 범위·목록 관리 | 초기부터 전체 E22 + 외부·기존 기능 = 59개 인벤토리 보존 | `V2_FULL_ISSUE_INVENTORY.md` / 본 파일의 59개 ID 목록 | DOCUMENT CHECK |
| A04 | 평가자·시험모델 역할 구분 | 개발 평가자가 과거 AI 고용 연구를 무단 재개하지 않음 | `V2_PROGRESS_CHECKPOINT.md` §0 / 역사 연구 브랜치 HEAD | WORKFLOW BOUNDARY |
| A25 | 감사 증거 수준 | 실제 소스 행 확인, 공유/동방향 테스트의 독립성 의심 표시 | `V2_THEORETICAL_COVERAGE_MATRIX.md`와 frozen 규칙 줄/시험 정의 | STATIC, SEMANTIC OPEN |
| A30 | 외부 감사 이력 | 1~3차 감사 원문·개발자 대응을 분리 저장, 3차 B를 A로 소급하지 않음 | `V2_EXTERNAL_AUDIT_0{1,2,3}_ORIGINAL.md`, `V2_REAUDIT_03_REMEDIATION.md` | ARCHIVE CHECK |
| A31 | 실험 판정 원칙 | C10/C13 최초 FAIL·C14 PARTIAL과 회복 PASS를 별도로 집계 | `V2_TEST_RESULTS.md` §§42~48 / `V2_E2E_PRE_POST_PROTOCOL.md` | EVALUATOR RULE |
| A32 | 브랜치 보호 | 운영 `main`과 역사 `research/*`에 이번 개선안 쓰지 않음 | GitHub 최신 HEAD·변경 diff | PERMISSION/HEAD CHECK |
| A33 | 인수인계 범위 | 다음 스레드 시작파일/판정 대장/감사 원문/미시험 분리를 제공 | `V2_NEXT_THREAD_START_HERE.md`, `V2_HANDOFF_GAP_AUDIT.md` | READABLE; COLD START NOT TESTED |

## E2E 시험 전체 집합 → 요구/판정의 역방향 연결

기본 POS/NEG/FAIL 열 밖에서도 다음 시험을 **빠뜨리지 않고** 보존한다. 특히 **회복 시험을 최초 정상 동작 합격에 합산하지 않는다.**

| 시험 | 연결된 59개 요구 | 시나리오 분류 | 정확한 판정 |
|---|---|---|---|
| **N05** | E06, G03 | 사용자가 추천 검증법 승인 후 실제 보완 수행 | 승인 범위대로 출처 조사·내용 보정했는지, 추천만 반복했다면 FAIL |
| **N11** | E17, G11 | 최초 원고 누락 지적 뒤 별도 **회복** | 최초 N10/C14 실패 보존, 회복은 별도 점수 |
| **X08** | E12, E07 | 채용공고·실제 입직·순고용 혼동의 부정 사례 | 방법론과 관측 단위를 구별하는지 |

**상태:** 위 3건도 `V2_E2E_PRE_POST_PROTOCOL.md`에 정의만 존재하며 **NOT RUN**. 59개 요구에 POS·NEG·FAIL을 중복 할당한 횟수는 독립 시험 수가 아니고, 모델의 실제 동작 검증은 전건 미실행이다.

## 추적 실패 때의 수정 순서

1. 새로운 요구나 결함을 발견하면 **임의로 기존 59건의 PASS를 수정하지 말고** 새 ID/기존 ID의 원인·감사 근거를 기록한다.
2. 해당 A-결정/기존 규칙 source와 N-비채택 이유·P-미검증에 연결한다. 처리 방법이 바뀌면 이전 처분을 SUPERSEDED하고 변경된 결정을 새로 등록한다.
3. 영향 받은 Stage·원문 blob·출력·사용자 권한·관련 X-ID 회귀를 실제로 확인하고, 새 고정 SHA를 지정한다.
4. 사용자에게 요구하지 않은 별도의 본조사/브랜치 쓰기/운영 main 병합은 수행하지 않는다.

**외부 방법론 참고(서식만 사용):** https://www.nasa.gov/reference/6-2-requirements-management/ 및 https://swehb.nasa.gov/spaces/SWEHBVD/pages/102695440/SWE-055%2B-%2BRequirements%2BValidation
