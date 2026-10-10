# 새 스레드 인수인계 누락·정합성 점검 (2026-10-10)

**판정: GitHub 기반 기록·결정 인계 준비 가능. 실제 새 ChatGPT 스레드에서 GitHub 읽기·자동 복원 성공은 NOT TESTED.** 인계 자료가 존재하는 것과 다음 스레드가 처음부터 올바르게 복원하는 것은 별개의 주장이다.

## 외부 방법론은 절차에만 참고

- ADR: 결정 상태/맥락/결정/영향 및 거부·대체 이력을 보존. https://architecture-decision-record.github.io/templates/decision-record-template-by-michael-nygard/
- NASA 양방향 요구/검증 추적: 요구 원천→설계→시험→결과, 변경 영향·중복·빠진 상위 요구 탐지. https://www.nasa.gov/reference/6-2-requirements-management/ , https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix/
- GitHub: 이동하는 branch HEAD 대신 고정 SHA와 변경 파일 비교. https://docs.github.com/en/pull-requests/committing-changes-to-your-project/viewing-and-comparing-commits/comparing-commits
- **외부 자료는 기록 방법론일 뿐 이 프로젝트의 모델 실사용 PASS 근거가 아니다.**

**BASE:** `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0`. **현행 후보:** `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`. **개발:** `design/research-v2`. 운영 `main`·역사 `research/20261010-ai-employment-kr-us-1538-fb22` 보호.

## 빠진 항목 유무 — 소스별 체크

| 점검 | 내용 | 증거/인계 상태 | 근거 | 주의·잔여 |
|---|---|---|---|---|
| H01 | 최상위 목표: 짧은 한국어 의향 → 사용자 실질 선택 → 자율 근거·반례·최종 보고서 | RECORDED | V2_EXECUTION_PLAN.md 시작/§26 | 향후 시험에 내부 Stage/W-ID 사용자 프롬프트 제공 금지 |
| H02 | 평가자 채팅과 실제 모델 E2E 채팅 역할 분리 | RECORDED | V2_PROGRESS_CHECKPOINT.md §0 | 평가자가 과거 AI 고용 조사 브랜치 수정 금지 |
| H03 | 작업 브랜치·main·역사 연구 쓰기 권한 | RECORDED | V2_EXECUTION_PLAN.md §28 | 개발만 design/research-v2; main/과거 연구 보존 |
| H04 | 규칙 SHA/문서 HEAD/과거후보/실제 주입 SHA 분리 | RECORDED | V2_E2E_READY_HANDOFF.md | BASE cd64… / CANDIDATE ac4675… |
| H05 | 3차 P1-A/P1-B·P2 국소 수정과 8개 규칙 보존 | STATIC VERIFIED | V2_REAUDIT_03_FINAL_GATE.md | 실제 모델 반응과 무퇴행은 별개 |
| H06 | 외부 1·2·3차 감사 원문 보존 | ARCHIVED/EXACT TEXT MATCH | V2_EXTERNAL_AUDIT_01_ORIGINAL.md; 02_ORIGINAL.md; 03_ORIGINAL.md | Files 도구가 반환한 텍스트와 GitHub 파일 3/3 글자 동일; 원본 bytes 해시는 별도 미검산 |
| H07 | E01~E22 최초·중간·후반 실측 및 회복 | 22/22 TRACEABLE | V2_FULL_ISSUE_INVENTORY.md; V2_TEST_RESULTS.md §§1~48 | 최초 FAIL을 회복 PASS로 덮지 않음 |
| H08 | H/M/L 8 + R 12 + 기존 G 12 + T06R 4 + PDF 1 | 37/37 TRACEABLE | V2_REQUIREMENT_DISPOSITION_CROSSWALK.md | 기존 E22 더해 총 59 |
| H09 | 채택·반려/범위 비채택·대체·미시험 구분 | INDEXED | V2_DECISION_REGISTER.md | 33 A / 18 REJ / 12 P; 사용자 명시 판단과 개발 해석 분리 |
| H10 | 과거 C10/C13 첫 FAIL, C14 Stage7 PARTIAL과 회복 PASS | PRESERVED | V2_TEST_RESULTS.md §§42~48 | 최초 자발성 실패 소급 수정 금지 |
| H11 | 59개 소스·시험 참조와 독립성 불확실성 | STATIC LINK ONLY | V2_THEORETICAL_COVERAGE_MATRIX.md | 56 모델 행동 요구와 3 평가 규약; 7 SHARED/4 SAME-DIRECTION; 실제 PASS 아님 |
| H12 | N01~N12 / X01~X48 계획과 경고 | PLANNED | V2_E2E_PRE_POST_PROTOCOL.md | 실제 E2E 미실행 |
| H13 | 새 스레드의 실제 GitHub 연결·권한·T06-R 복원 | NOT TESTED | V2_EXECUTION_PLAN.md §25; X29 | 이번 채팅의 읽기 성공은 새 채팅의 읽기 성공 증명 아님 |
| H14 | 실제 피시험 프로젝트에 frozen rules가 주입됐는지 | UNKNOWN | V2_E2E_READY_HANDOFF.md | GitHub SHA만으로 실제 활성 규칙 증명 불가 |
| H15 | 현재 Project 첨부 Bootstrap과 검증 후보 Bootstrap의 차이 | POTENTIAL STARTUP CONFLICT | 현재 Project 자료 PROJECT_BOOTSTRAP.md vs 고정 ac4675…/PROJECT_BOOTSTRAP.md | 첨부 Project 파일은 기본 main 참조; 후보는 설계모드 SHA. Project 소스가 자동갱신됐다고 주장 금지. 새 스레드 시작 문구에서 개발 브랜치 명시 |
| H16 | READ 실패 X29, 실제 화면/저장 X30, 비저장 X44/45, 전달/개정 X46/47 | NOT TESTED | V2_E2E_PRE_POST_PROTOCOL.md | 실제 도구/UI 실패 주입 없이 PASS 불가 |
| H17 | PDF 실물·7종 출력·단문 UX·검색/승인/지연/비용 | NOT TESTED | V2_E2E_READY_HANDOFF.md | 실제 렌더와 BASE 대비 실측 필요 |
| H18 | 옛 완료 보고서·이전 감사 키트의 과거 SHA 링크 | MITIGATED | V2_DEVELOPMENT_PHASE_CLOSEOUT.md; V2_AUDIT_README.md | 이번 재개 문서가 최신 우선. 역사 기록 삭제 금지 |
| H19 | 과거 사용자에게 실제 표시된 편집안의 전체 원문 | UNKNOWN WHEN INACCESSIBLE | 04_STATE_MANAGEMENT.md; V2_TEST_RESULTS.md | 원문을 읽을 수 없다면 출력↔저장 일치 자체는 UNKNOWN, W-ID↔원고 별도 감사 |
| H20 | 완료 의미: 개발 패치/정적 준비 vs 실사용 | DESIGN COMPLETE / LIVE NOT TESTED | V2_REAUDIT_03_FINAL_GATE.md | '이론 전체 커버'를 실사용 무회귀 PASS로 승격 금지 |

## 채택·반려·보류 재점검

1. [V2_DECISION_REGISTER.md](V2_DECISION_REGISTER.md)에는 **A 33건(채택·설계 적용), REJ 18건(진짜 반려/이번 범위 비채택/옛 후보 대체/잘못된 증명 반려), P 12건(미검증·불확실·운영 범위 보류)**을 분리했다. **사용자가 직접 반려하지 않은 대안을 '사용자 반려'라고 쓰지 않았다.**
2. [V2_REQUIREMENT_DISPOSITION_CROSSWALK.md](V2_REQUIREMENT_DISPOSITION_CROSSWALK.md)에서 기존 59개 요구 **E22 + 이전 외부 H/M/L8 + R12 + G12 + T06R4 + T09 = 59건**, 모두 실제 A-결정과 시험 근거 참조. 채택 A33건 중 직접 기능 연결 25건과 별도 거버넌스 8건을 구분하며, 후속/회복 N05·N11·X08도 별도 연결했다. 이는 **형식적 양방향 추적의 충족**이지 59개 기능의 실사용 성공률이 아니다.
3. 외부 원본 [1차](V2_EXTERNAL_AUDIT_01_ORIGINAL.md)·[2차](V2_EXTERNAL_AUDIT_02_ORIGINAL.md)·[3차](V2_EXTERNAL_AUDIT_03_ORIGINAL.md)를 보존했다. **외부 감사의 B/P1 권고와 개발자 '국소 수정 완료'는 서로 다른 출처·판정**이다. 이전 3차 B가 사후 A가 된 적은 없다.
4. **반려 아닌 미검증:** C10/C13/C14 새 후보 최초 자발성, GitHub 냉시작/READ, no-write, 실제 편집안 UI↔blob, CAS, PDF 렌더, 비용. 기존 첫 FAIL과 회복 PASS는 별도.
5. 외부 3차 감사의 '라인 번호 오류' 지적은 **원문 위치 재검증 취지를 채택**, 일부 전체 줄수 주장만 실제 고정 원문 조회와 달라 **부분 반려**. 이 두 사실을 함께 보존했다.
6. **다음 게이트:** 사용자 허가 없이 4차 정적 외부감사나 옛 고용 연구 재실행을 필수 관문으로 새로 만들지 않는다. 진짜 BASE↔CANDIDATE 자연어 신규 E2E를 우선 준비한다.

## 실질적 잔여 위험

- **RISK-BOOTSTRAP:** 이 프로젝트에 첨부된 기존 `PROJECT_BOOTSTRAP.md`는 운영 `main` 참조를 기본으로 안내한다. 이번 개발 후보의 **설계 검증 모드 고정 SHA 지침이 현재 Project 소스 자체에 자동 반영된 것은 아니다.** 새 평가자 스레드는 [V2_NEXT_THREAD_START_HERE.md](V2_NEXT_THREAD_START_HERE.md)를 명시 읽고 개발 브랜치를 선택해야 한다. **시험 프로젝트**에서 후보 규칙을 실제 로드했는지는 별도 확인 필요.
- **RISK-LIVE:** 신규 독립 모델 동일조건 E2E, T06-R R1~R4, X29, X30, X44~47, PDF/비용은 실행하지 않았다. 문구·추적표 수치를 기능 검증으로 바꾸지 말 것.
- **RISK-PROVENANCE:** 세 감사 원문을 지금 GitHub에 텍스트 그대로 보존했지만, 3차 외부 감사가 지적한 이전 기록의 잘못된 전체 줄수는 '외부 감사 원문'에서 수정하지 않았다. 반박·조치 기록은 `V2_REAUDIT_03_REMEDIATION.md`에 독립 보존한다.
- **RISK-MODALITY:** 새 스레드가 이전 채팅의 모든 사용자 표시 편집안과 이 채팅 UI의 상태를 볼 수 있다고 보장하지 않는다. GitHub 문서에 없는 정보는 `UNKNOWN` 처리한다.

## 재개 직후 read-only 자체 검증

1. `design/research-v2` HEAD를 실제 확인하고 `V2_NEXT_THREAD_START_HERE.md` → `V2_DECISION_REGISTER.md` → `V2_REQUIREMENT_DISPOSITION_CROSSWALK.md` → `V2_E2E_READY_HANDOFF.md` 순서로 읽는다.
2. BASE `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0` / 후보 `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`, 평가자 채팅의 역할, 역사 첫 FAIL/회복 분리, 미실행 시험, `main`/역사 연구 수정 금지를 **도구 증거로** 확인한다.
3. 이 읽기가 실패하면 복원 PASS라고 주장하지 말고 접근 제약과 필요한 최소 정보만 요청한다.
4. **피시험 모델의** 첫 사용자 발화에는 59항목·N/X 목록·내부 단계 정답을 전달하지 않는다. E2E 운영자는 [V2_E2E_PRE_POST_PROTOCOL.md](V2_E2E_PRE_POST_PROTOCOL.md)를 **별도로** 관리한다.

**업무범위:** 이번 작업에서 엔진 규칙 수정·`main` 변경·과거 연구 브랜치 갱신·새 E2E 실제 실행을 하지 않는다.
