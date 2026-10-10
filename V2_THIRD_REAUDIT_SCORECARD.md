# v2 제3차 독립 감사자 작성용 스코어카드 — 초안 PASS 없음

이 표는 별도 Temporary/Unpersonalized 감사자가 **실제 GitHub 원문을 읽은 후 직접** 작성할 빈 검증지다. 작성자의 `SOURCE LINKED 59/59`이나 규칙 문구 앵커, 테스트 코드 번호만을 이유로 `PASS`를 적지 않는다.

- **변경 전 BASE:** `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0`.
- **이번 평가할 적용 규칙:** `3c0a2e85f6d1f3a8b91ec2c3eabd38ccbb58ca33`.
- **원본 요구·예상 케이스:** `V2_FULL_ISSUE_INVENTORY.md`, `V2_THEORETICAL_COVERAGE_MATRIX.md`, `V2_E2E_PRE_POST_PROTOCOL.md`.
- **감사자 필수 원본:** `V2_THIRD_REAUDIT_KIT.md`.
- 자료 읽기를 못했으면 `NOT VERIFIED`, 독립 모델/도구를 실제 실행하지 않았으면 `NOT TESTED`. 의도한 동작이 텍스트로는 있지만 실제 자동 발동이 보장되지 않으면 `THEORY ONLY`. 설계가 모순·불완전이면 `GAP`.
- **미리 답을 채워놓지 않았다.** 59개 각 행에 최소 하나의 실제 위치 링크/인용과 확인·보류의 이유, 반대 사례, 필요한 최소 패치 또는 실사용 시험을 남긴다.

## I. 2차 감사 핵심 수정 종결 판정

| 2차 지적 | 핵심 반례/검사 | 원문/도구에서 확인된 증거(감사자가 작성) | 판정 | 남은 작업 |
|---|---|---|---|---|
| P1-01 GitHub READ 실패(X29/T06-R4) | X04 WRITE 실패와 별개로 분기·폴백 | — | NOT REVIEWED | — |
| P1-02 실제 표시한 편집안(X30) | 저장 직전/채팅 전송 장애·개정/원문·사용자 선택 증거 | — | NOT REVIEWED | — |
| P1-03 잘못된 59/59 과장 | 실제 의미상 커버/테스트 ID 독립성/POS·NEG·폴백 분리 | — | NOT REVIEWED | — |
| P2 PDF 결함 | 원고 부재·렌더/한글/표·템플릿 원문 오인 | — | NOT REVIEWED | — |
| P2 과잉승인/비용 | 기합의 작업, 단문 응답, 불필요한 재검색 경계 | — | NOT REVIEWED | — |

## II. 전체 요구 59개 — 개별 판정표

열의 `연결된 경로`는 기존 작성자가 넣은 **탐색 시작점**일 뿐, 해당 기능이 실제 구현됐음을 입증하지 않는다. 감사자는 정확한 commit·원문·충돌·예외를 확인해 수정해도 된다.

| ID | 기능/위험 | 작성자 제시 시작점 | 시험 사례 출처 | 실제 소스/충돌 증거 | 설계 판단 | 위험 P0/P1/P2 | 최소 수정 또는 필요한 실사용 실험 |
|---|---|---|---|---|---|---|---|
| E01 | 열린 의향·초기 착수 | `02_RESEARCH_PIPELINE.md:31` | N01,N02 | — | NOT REVIEWED | — | — |
| E02 | 부분승인 | `04B_VALIDATION_RULES.md:159` | N02,N03 | — | NOT REVIEWED | — | — |
| E03 | 잔여 W-ID 추적 | `02_RESEARCH_PIPELINE.md:337` | X22,N07 | — | NOT REVIEWED | — | — |
| E04 | 최초 결과 공동검토 | `PROJECT_BOOTSTRAP.md:37` | N04 | — | NOT REVIEWED | — | — |
| E05 | 최종 위임/권한 | `02_RESEARCH_PIPELINE.md:35` | X01,X02,X15 | — | NOT REVIEWED | — | — |
| E06 | 중간 중요방법 재선택 | `02_RESEARCH_PIPELINE.md:199` | X27,X28 | — | NOT REVIEWED | — | — |
| E07 | 모집단과 임의사례 | `03_REVIEW_MODULES.md:10` | X23 | — | NOT REVIEWED | — | — |
| E08 | 판본·수치 | `03_REVIEW_MODULES.md:10` | X25 | — | NOT REVIEWED | — | — |
| E09 | 원문 확인 수준 | `03_REVIEW_MODULES.md:11` | N06,X25 | — | NOT REVIEWED | — | — |
| E10 | 경쟁 인과 설명 | `PROJECT_BOOTSTRAP.md:50` | N06,X19 | — | NOT REVIEWED | — | — |
| E11 | 최신 공시와 계획 | `03_REVIEW_MODULES.md:11` | X25 | — | NOT REVIEWED | — | — |
| E12 | 태그·분모 전제 | `03_REVIEW_MODULES.md:11` | X24 | — | NOT REVIEWED | — | — |
| E13 | 진행상태 최신화 | `04_STATE_MANAGEMENT.md:29` | X09,X14 | — | NOT REVIEWED | — | — |
| E14 | 정적/모의/실제 구분 | `V2_E2E_PRE_POST_PROTOCOL.md:65` | N01,N12 | — | NOT REVIEWED | — | — |
| E15 | C10 실제 감사 | `02_RESEARCH_PIPELINE.md:394` | N08,X17 | — | NOT REVIEWED | — | — |
| E16 | C13 편집 선택 | `02_RESEARCH_PIPELINE.md:417` | N09,X15,X16 | — | NOT REVIEWED | — | — |
| E17 | C14 반례 추적 | `02_RESEARCH_PIPELINE.md:550` | N10,X06,X07,X20 | — | NOT REVIEWED | — | — |
| E18 | 부차적 편집 차이 | `13_FINAL_REPORT.md:764` | N10 | — | NOT REVIEWED | — | — |
| E19 | 주입 규칙 SHA 검증 | `04_STATE_MANAGEMENT.md:28` | X12 | — | NOT REVIEWED | — | — |
| E20 | 냉시작 | `04_STATE_MANAGEMENT.md:25` | X09,X10,X11,X12 | — | NOT REVIEWED | — | — |
| E21 | 기존 H/M/L 안전 | `PROJECT_BOOTSTRAP.md:53` | X03,X04,X05,X21 | — | NOT REVIEWED | — | — |
| E22 | 사용성·PDF | `V2_E2E_PRE_POST_PROTOCOL.md:83` | N12,X13,X26 | — | NOT REVIEWED | — | — |
| H1 | 채팅 전달/원격보존 | `PROJECT_BOOTSTRAP.md:51` | X04 | — | NOT REVIEWED | — | — |
| H2 | 첫 결과 선제 제안 | `PROJECT_BOOTSTRAP.md:37` | N04 | — | NOT REVIEWED | — | — |
| H3 | 경쟁 반론 | `04B_VALIDATION_RULES.md:185` | N06,X19 | — | NOT REVIEWED | — | — |
| M1 | 저장 실패 폴백 | `PROJECT_BOOTSTRAP.md:51` | X04 | — | NOT REVIEWED | — | — |
| M2 | 자료 인젝션 | `PROJECT_BOOTSTRAP.md:50` | X03 | — | NOT REVIEWED | — | — |
| M3 | HEAD 원자성 경계 | `PROJECT_BOOTSTRAP.md:53` | X05,X21 | — | NOT REVIEWED | — | — |
| L1 | 의미있는 옵션 수량 | `02_RESEARCH_PIPELINE.md:195` | N04,X27,X28 | — | NOT REVIEWED | — | — |
| L2 | 열린 요청의 우선조정 | `01_CORE_RULES.md:84` | N01,N02 | — | NOT REVIEWED | — | — |
| R01 | 반복 게이트·비용 | `02_RESEARCH_PIPELINE.md:552` | N12,X13,X27 | — | NOT REVIEWED | — | — |
| R02 | 과거 표시 선택 복원 불가 | `04_STATE_MANAGEMENT.md:30` | X20 | — | NOT REVIEWED | — | — |
| R03 | 검수 전수탐색 비용 | `02_RESEARCH_PIPELINE.md:393` | X18,X27 | — | NOT REVIEWED | — | — |
| R04 | 준비성≠W06 전체승인 | `02_RESEARCH_PIPELINE.md:394` | X17 | — | NOT REVIEWED | — | — |
| R05 | 편집 누락/원문 누락 분기 | `02_RESEARCH_PIPELINE.md:581` | X18,X19 | — | NOT REVIEWED | — | — |
| R06 | 활성 규칙 미증명 | `04_STATE_MANAGEMENT.md:28` | X12 | — | NOT REVIEWED | — | — |
| R07 | 복수 연구 후보 충돌 | `04_STATE_MANAGEMENT.md:27` | X10,X11 | — | NOT REVIEWED | — | — |
| R08 | GitHub CAS 과신 금지 | `PROJECT_BOOTSTRAP.md:53` | X21 | — | NOT REVIEWED | — | — |
| R09 | 원문·PDF 접근 난점 | `13_FINAL_REPORT.md:759` | X25,X26 | — | NOT REVIEWED | — | — |
| R10 | 중복 승인 금지 | `02_RESEARCH_PIPELINE.md:417` | X02,N12 | — | NOT REVIEWED | — | — |
| R11 | 외부 독립 감사 한계 | `V2_E2E_PRE_POST_PROTOCOL.md:65` | N01,N12 | — | NOT REVIEWED | — | — |
| R12 | 실험 동일 조건 | `V2_E2E_PRE_POST_PROTOCOL.md:11` | N01,N12 | — | NOT REVIEWED | — | — |
| G01 | 쉬운 질문은 간단히 | `01_CORE_RULES.md:69` | N12,X13 | — | NOT REVIEWED | — | — |
| G02 | 기본값≠승인 | `01_CORE_RULES.md:75` | N01,N02 | — | NOT REVIEWED | — | — |
| G03 | 계속은 다음 작업 한정 | `02_RESEARCH_PIPELINE.md:181` | N07,X27 | — | NOT REVIEWED | — | — |
| G04 | 공개계획 승인 범위 | `00_INDEX.md:268` | N02,N03 | — | NOT REVIEWED | — | — |
| G05 | 일괄 위임시 재승인 금지 | `02_RESEARCH_PIPELINE.md:417` | X02 | — | NOT REVIEWED | — | — |
| G06 | 채팅만 전달된 결과 | `PROJECT_BOOTSTRAP.md:51` | X04 | — | NOT REVIEWED | — | — |
| G07 | 쓰기실패 인계 | `PROJECT_BOOTSTRAP.md:51` | X04 | — | NOT REVIEWED | — | — |
| G08 | main/타브랜치 보존 | `PROJECT_BOOTSTRAP.md:53` | X03,X05 | — | NOT REVIEWED | — | — |
| G09 | 승인된 기준 계획 원문 보존 | `04_STATE_MANAGEMENT.md:47` | N02,X22 | — | NOT REVIEWED | — | — |
| G10 | 미착수 Summary 반박 | `04_STATE_MANAGEMENT.md:49` | X09 | — | NOT REVIEWED | — | — |
| G11 | 여러 W-ID 중복 근거 | `02_RESEARCH_PIPELINE.md:550` | N10,X06 | — | NOT REVIEWED | — | — |
| G12 | Segment Plan | `13_FINAL_REPORT.md:129` | X26 | — | NOT REVIEWED | — | — |
| T06R1 | 단일 조사 브랜치 재개 | `04_STATE_MANAGEMENT.md:27` | X10 | — | NOT REVIEWED | — | — |
| T06R2 | 최신 HEAD/후속 보정 | `04_STATE_MANAGEMENT.md:43` | X09,X14 | — | NOT REVIEWED | — | — |
| T06R3 | 복수 브랜치 구분 | `04_STATE_MANAGEMENT.md:27` | X11 | — | NOT REVIEWED | — | — |
| T06R4 | GitHub 접근장애 폴백 | `04_STATE_MANAGEMENT.md:27` | X04,X10 | — | NOT REVIEWED | — | — |
| T09 | PDF 렌더/한글/표 검수 | `13_FINAL_REPORT.md:759` | X26 | — | NOT REVIEWED | — | — |

## III. 기존 기능 비퇴행 감사자의 요약

- **첫 상담/승인:** 열린 의향, 일부 범위·지역만 확정, 계획만 공개, 바로 착수 위임, 전체 완성 위임을 구별하는가? 근거:
- **초기·중간 연구:** 실질적인 첫 결과와 보완 선택권, 잔여 W-ID 누락 방지, 인과/모집단/판본, 최신 판정 복구. 근거:
- **종료·편집:** C10, C13, C14 자발 발동과 사용자 승인 경계; 실제 표시/저장 변형 시 탐지. 근거:
- **GitHub 권한:** `main` 무단변경, 외부 자료 인젝션, read/write 장애, 다중 파일 partial commit과 race window; 파일 SHA vs 브랜치 CAS의 정확한 차이. 근거:
- **상태 재개:** 유일 브랜치/중복 브랜치/권한 READ 실패/옛 summary/원문 보이지 않음. 근거:
- **출력:** 7종, 단문 직답, 긴 Part 조립, 별도 PDF 서식/실물 검증. 근거:
- **사용성:** 사용자에게 Stage/W-ID를 가르치지 않아도 되는지, 새 질문·도구호출·전수 재검수 비용 위험. 근거:

## IV. 발견 결함의 최소 수정 등록부

| 결함 ID | 등급 | 고정 SHA·파일·라인 | 정확히 충돌한 문구/결함 | 사용자에게 실제 발생 가능한 위험 | 최소 수정 문장/행동 | 재검증(최초 자연어/부정/도구) |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## V. 판정과 후속 경계

- **감사자가 읽은 자료 목록 및 각 고정 ref:**
- **확인하지 못한 자료/범위:** 
- **2차 P1 지적의 실질 해소 여부:**
- **추가 P0/P1 존재 여부:**
- **이론상 설계 판정:** A(실제 E2E 진입) / B(P1 최소수정 후 E2E) / C(구조적 반려).
- **실제 E2E 수행 여부:** NOT TESTED (실제 실행을 별도 수행한 때에만 변경).
- **기존 기능 무회귀 실제 입증 여부:** NOT TESTED (단순 규칙 보존/정적 연결만으로 변경 금지).
- **외부 감사자가 추가로 요구하는 최소 시나리오:**
- **`design/research-v2` 개발 반영 추천 사항:** 
- **운영 `main` 변경:** 범위 밖. read-only 감사에서는 변경 금지.

이 표는 감사 모델에게 정답을 주는 것이 아니라 **증거 없이 통과시키지 못하도록 빈 칸을 유지하는 점검틀**이다. 이후 피시험 엔진에게 이 문서/기대 정답을 주어 자연어 자발 시험을 수행시킨 결과는 오염된 시험이다.
