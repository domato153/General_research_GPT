# v2 결정·대안 처분 대장 (다음 스레드 재개용, 2026-10-10)

> **정본 상태:** 본 파일은 **현재 적용된 결정과 명시적으로 채택하지 않은 대안, 단순 미검증·보류를 분리**한 *새 인덱스*다. 역사 원문을 덮어쓰거나 사용자가 거부했다고 근거 없는 귀속을 하지 않는다. **상태별 이유와 출처가 없는 판단은 잠정이며, 새로운 대화에서 추정으로 '사용자 승인'으로 승격하지 않는다.**
>
> **정책 출처와 유래:** 외부 ADR(Nygard) `status/context/decision/consequences` 및 NASA 양방향 요구→설계→시험→실행 증거 추적 방법론을 **서식과 검증 경계에만 차용**. 외부 문서는 이 저장소의 작동 여부 증거가 아니다.
>
> 규칙 동결 BASE `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0` / CANDIDATE `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`; 개발 브랜치 `design/research-v2`. **1·2·3차 감사 원문 파일을 별도 보존**: [01](V2_EXTERNAL_AUDIT_01_ORIGINAL.md), [02](V2_EXTERNAL_AUDIT_02_ORIGINAL.md), [03](V2_EXTERNAL_AUDIT_03_ORIGINAL.md). 조치기록은 [감사1](V2_EXTERNAL_AUDIT_RECONCILIATION.md), [감사2](V2_REAUDIT_02_REMEDIATION.md), [감사3](V2_REAUDIT_03_REMEDIATION.md).

## 상태 용어와 승인 증거

- **ACCEPTED_IMPLEMENTED / 채택·적용**: 실제 규칙 파일에 반영. 모델이 실제 실행 성공했다는 뜻은 아님.
- **ACCEPTED_POLICY / 채택·범위 계약**: 사용자 지시 또는 설계 상위 목표. 별도 실사용 동작 검증 필요.
- **REJECTED_DESIGN / 설계에서 반려**: 특정 대안을 채택하지 않은 이유가 규칙/감사에 확인됨. **사용자가 직접 반려했다고 단정하지 않음**.
- **REJECTED_CURRENT_SCOPE / 이번 범위 반려**: 이번 과제 목적지에서 제외. 영구 폐기 아님.
- **SUPERSEDED / 이전 버전 대체**: 옛 SHA는 역사 감사 증거로 보존, 현재 시험 후보가 아님.
- **NOT_ADOPTED_AS_GATE / 관문으로 채택하지 않음**: 추가 작업을 필수 선행조건으로 만들지 않음; 절대 금지와 다름.
- **NOT_TESTED, UNVERIFIED / 실증 미실행·증거 미확인**: 불합격·반려도 아니고 합격도 아님.
- **USER_EXPLICIT vs AUDITOR_PROPOSED vs DEVELOPER_IMPLEMENTED**: 출처 열을 구분. *제안만 있고 적용되지 않은 것을 사용자 확정이라고 하지 않는다.*

## A. 채택·적용 및 보호하는 결정 (33건)

| ID | 결정 근거 주체 | 채택한 규칙·범위·이유 | 정본 근거 | 미완료 확인 |
|---|---|---|---|---|
| A01 | 사용자 확정 | 일상어 한두 문장으로 조사·협업·반론·보고서의 관문을 모델이 자율 처리 | V2_EXECUTION_PLAN.md 최상위 목적/§26; 01_CORE_RULES.md | N01~N12 |
| A02 | 사용자 정정 | 개선안의 실제 작업 대상은 `design/research-v2`; `main`이 아님 | V2_EXECUTION_PLAN.md §28; V2_PROGRESS_CHECKPOINT.md §15 | 개발 HEAD/권한 |
| A03 | 사용자 요청·개발 수용 | 초반 E01~22와 외부 H/M/L/R 및 기존 G01~12·T06-R/T09 전체를 한 검증 집합에서 추적 | V2_FULL_ISSUE_INVENTORY.md; V2_THEORETICAL_COVERAGE_MATRIX.md | 59개 추적 |
| A04 | 개발 채택 | 평가자 채팅은 소스·실제 모델 결과를 독립 판정; 연구 모델 대신 과거 연구를 재실행·수정하지 않음 | V2_PROGRESS_CHECKPOINT.md §0 | 연구 HEAD 보호 |
| A05 | 개발 채택 | 변경 전/후 규칙 ref는 `cd64...`와 `ac4675...`; 파일 blob, 개발 HEAD, 실제 주입 SHA 분리 | V2_E2E_READY_HANDOFF.md; V2_E2E_PRE_POST_PROTOCOL.md §A | 활성 주입 확인 |
| A06 | 설계 채택 | 열린 의향·부분 승인·실질 계획 공개·명시적 착수의 권한을 단계별로 구분 | 02_RESEARCH_PIPELINE.md; 00_INDEX.md; E01/E02/E05 | N01~N03/X38 |
| A07 | 설계 채택 | 최초 실질 결과·새 검증 경로를 사용자가 선택할 필요가 있을 때 선제 추천 | 02_RESEARCH_PIPELINE.md; E04/E06 | N04~N07/X27~28/X39 |
| A08 | 설계 채택 | 기준 W-ID의 선행 수행·잔여 필수조건을 추적하고 과거 Summary와 최신 보정 충돌 구별 | 02_RESEARCH_PIPELINE.md; 04_STATE_MANAGEMENT.md; E03/E13 | X09/X14/X22 |
| A09 | 설계 채택 | 대표모집단·사례·판본·효과 단위·[체감]과 실제 관측치·인과 반례를 구분 | 03_REVIEW_MODULES.md; E07~12 | X23~25/X31~33/X40~41 |
| A10 | 1차 감사 권고 수용·개발 적용 | '보고서로 넘어가도 돼?'는 현재 자료 실제 종료 준비 감사이지 W06 전부/최종 저장 자동 위임이 아님 | V2_EXTERNAL_AUDIT_01_ORIGINAL.md; V2_EXTERNAL_AUDIT_RECONCILIATION.md; 02_RESEARCH_PIPELINE.md | N08/X17 |
| A11 | 1차 감사 권고 수용·개발 적용 | 편집 일반 준비/초안만/전체 완성을 구별하고 필요할 때만 내용 선택권 제시 | V2_EXTERNAL_AUDIT_01_ORIGINAL.md; 02_RESEARCH_PIPELINE.md | N09/X15~16 |
| A12 | 1차 감사 권고 수용·개발 적용 | W-ID 원자료 자체의 결함만 표적 재조사; 이미 확보된 연구의 원고 편집 누락은 국소 수정 | V2_EXTERNAL_AUDIT_RECONCILIATION.md; 02_RESEARCH_PIPELINE.md | X18/X19 |
| A13 | 1~3차 감사 권고 수용·개발 적용 | 최초 Stage5부터 중요 편집안 원문·proposal_id/revision/근거·반론 저장 후 재조회(허용시); 실제 출력과 저장의 차이 검증 | V2_EXTERNAL_AUDIT_03_ORIGINAL.md P1-A; V2_REAUDIT_03_REMEDIATION.md | N09/X30/X46 |
| A14 | 3차 감사 권고 수용·개발 적용 | revision 변경이 중요 선택을 바꾸면 이전 선택 자동 승계 금지, 변하지 않으면 재승인 남발 금지 | 02_RESEARCH_PIPELINE.md; 04_STATE_MANAGEMENT.md | X47 |
| A15 | 2차 감사 권고 수용·개발 적용 | 실제 표시 채팅 원문에 접근 불가능하면 출력↔저장 동일성 `UNKNOWN`; W-ID↔원고 반론 감사는 별도 | V2_EXTERNAL_AUDIT_02_ORIGINAL.md; 04_STATE_MANAGEMENT.md | X20/X30 |
| A16 | 3차 감사 권고 수용·개발 적용 | 명시적 GitHub 비저장/브랜치 금지는 기본 연구 브랜치 생성보다 우선 | V2_EXTERNAL_AUDIT_03_ORIGINAL.md P1-B; PROJECT_BOOTSTRAP.md | X44 |
| A17 | 3차 감사 권고 수용·개발 적용 | 기승인 연구의 '채팅에도 보여줘'는 기존 GitHub 저장 의무 자동 취소가 아님 | PROJECT_BOOTSTRAP.md; V2_REAUDIT_03_REMEDIATION.md | X45 |
| A18 | 개발 채택 | 완성/자체감사 PASS는 실제 파일·원문·반론 ID·원고 위치 등 확인한 범위로만 보고 | 04B_VALIDATION_RULES.md; 02_RESEARCH_PIPELINE.md | N10/X06/X07/X30 |
| A19 | 2차 감사 권고 수용·개발 적용 | 브랜치 목록/자료 읽기 실패와 GitHub 쓰기 실패 별도 취급, 읽지 않은 복원을 성공 주장 금지 | V2_EXTERNAL_AUDIT_02_ORIGINAL.md; 04_STATE_MANAGEMENT.md | X29≠X04 |
| A20 | 설계 채택 | T06-R 유일/여러 후보·없음·원문 불가에서 최신 HEAD와 알려진 범위만 복원 | 04_STATE_MANAGEMENT.md; V2_EXECUTION_PLAN.md §25 | T06-R R1~R4 |
| A21 | 1차 감사 권고 수용·개발 적용 | Contents 파일 blob SHA와 브랜치 HEAD 서버측 atomic CAS를 구분; 경합·부분저장 중단/재조회 | PROJECT_BOOTSTRAP.md; V2_EXTERNAL_AUDIT_01_ORIGINAL.md | X05/X21 |
| A22 | 개발 채택 | 외부 비신뢰 문서의 지시는 내용으로만 취급, 사용자 권한·`main` 보호 | PROJECT_BOOTSTRAP.md; 01_CORE_RULES.md | X03 |
| A23 | 개발 채택 | GitHub 저장장애 시 사용자 보관용 인계와 미저장 고지, 채팅 전달과 영구 저장 상태 구별 | PROJECT_BOOTSTRAP.md; H1/M1/G06/G07 | X04/X37 |
| A24 | 2차 감사 권고 수용·개발 적용 | 59 SOURCE-LINKED는 성공률이 아니며 POS/NEG/FAIL 할당·실측을 분리 | V2_EXTERNAL_AUDIT_02_ORIGINAL.md; V2_THEORETICAL_COVERAGE_MATRIX.md | 59행/NOT RUN |
| A25 | 3차 감사 P2 일부 수용 | 59개 실제 source :line 재검증; 중복 시나리오 7행과 SAME-DIRECTION 의심 4행 표시 | V2_EXTERNAL_AUDIT_03_ORIGINAL.md; V2_REAUDIT_03_REMEDIATION.md | 행별 테스트 독립성 |
| A26 | 3차 감사 P2 일부 수용 | Source Dossier 포함 7가지 결과 모드 보존, 중요 대안 없으면 가짜 2~3개 선택지 금지 | 02_RESEARCH_PIPELINE.md; 13_FINAL_REPORT.md | X36/X48 |
| A27 | 3차 감사 P2 일부 수용 | 실질 변화 없는 이전 검사 재사용; 모든 W-ID 재조회·추가 승인 과잉 금지 | 02_RESEARCH_PIPELINE.md; V2_REAUDIT_03_REMEDIATION.md | X48/호출량 |
| A28 | 2차 감사 권고 수용·개발 적용 | PDF 요청 시에만 실제 원고+PDF 서식 파일·렌더 결과/표/한글 검사 | 13_FINAL_REPORT.md; final_pdf_html_formatting_instruction_final.md | X26/X34/X35 |
| A29 | 개발 채택 | 실제 E2E에는 상세 감사 키트를 피시험 모델 사용자 프롬프트로 주입하지 않음 | V2_E2E_PRE_POST_PROTOCOL.md §E/F; V2_EXECUTION_PLAN.md §26 | N01~N12 |
| A30 | 사용자 요청 수용·개발 수행 | 외부 독립 감사를 3회 실시하고 지적사항을 개발 브랜치에서 국소 보완, 감사를 실제 모델 PASS로 소급하지 않음 | V2_EXTERNAL_AUDIT_0{1,2,3}_ORIGINAL.md; V2_REAUDIT_03_FINAL_GATE.md | 원본 3건 보존 |
| A31 | 개발 채택 | 최초 실패와 명시 요청 뒤 회복 PASS를 항상 별도 채점 | V2_TEST_RESULTS.md §§42~48; V2_E2E_PRE_POST_PROTOCOL.md | C10/C13/C14 |
| A32 | 개발 채택 | 운영 `main`/과거 연구 브랜치 원형 보존, 개발에서만 수정 | V2_PROGRESS_CHECKPOINT.md §§15,20,21; PROJECT_BOOTSTRAP.md | HEAD 재조회 |
| A33 | 사용자 현재 요청 수용 | 다음 스레드 재개를 위한 고정 버전·결정 대장·감사 원문·실행/미실행 분리 인계 작성 | V2_NEXT_THREAD_START_HERE.md; V2_DECISION_REGISTER.md | 새 대화 읽기 검증 |

## B. 반려·비채택·대체된 대안 (18건)

| ID | 처분 분류 | 채택하지 않은 대안 | 이유·남기는 예외 | 근거 |
|---|---|---|---|---|
| N01 | REJECTED_CURRENT_SCOPE | '개선안은 `main`에 바로 적용' | 사용자가 개발 브랜치 적용 대상이라고 직접 정정; `main` 자체를 영구 사용 금지한 것은 아님 | V2_EXECUTION_PLAN.md §28 |
| N02 | SUPERSEDED | 외부 최초 후보 `c9f8...` / 개발 최초 `0e572...` / 2차 수정 `3c0a...`를 현재 최신 후보로 취급 | 최신 후보는 `ac4675...`; 이전 SHA는 과거 감사 재현에만 사용 | V2_E2E_READY_HANDOFF.md |
| N03 | REJECTED_AS_PROOF | 규칙 문자열 59/59, 26개 정규식 또는 30개 자가 시나리오 통과를 모델 E2E PASS로 사용 | 정적 계약/증거 레벨만 채택하고 실제 모델 PASS 주장은 배척 | V2_THEORETICAL_COVERAGE_MATRIX.md |
| N04 | REJECTED_AS_PROOF | 명시 요청 뒤 C11/C13-R/C14-R 성공으로 최초 C10/C13/C14 실패 소급 삭제 | 최초 FAIL/PARTIAL과 회복 PASS 분리 | V2_TEST_RESULTS.md §§42~48 |
| N05 | REJECTED_DESIGN | 종료 가능 질문만으로 W06 전체 재조사·보고서 최종 확정 자동 착수 | 질문은 준비 감사의 권한만 | 02_RESEARCH_PIPELINE.md |
| N06 | REJECTED_DESIGN | 중요 선택이 남은 '준비'에서 원고 먼저 확정하고 내용 선택 나중 | 먼저 추천/차이 제시, 명시적 초안/완성 위임 예외는 허용 | 02_RESEARCH_PIPELINE.md |
| N07 | REJECTED_DESIGN | 이미 W-ID에 있는 반론이 원고에 누락됐을 때 매번 전체 Stage1~3 재시작 | 국소 수정/검수, 원자료 자체 결함이면 표적 재조사 | 02_RESEARCH_PIPELINE.md |
| N08 | REJECTED_DESIGN | 의미 없는 옵션을 2~3개 강제하고 기승인 작업마다 승인 재요구 | 실질 선택이 있는 상황만 사용자 협의 | 02_RESEARCH_PIPELINE.md |
| N09 | REJECTED_DESIGN | 사용자가 GitHub 비저장을 지시해도 기본값으로 `research/*` 생성/쓰기 | 명시적 no-write 우선, 읽기/채팅은 가능 | PROJECT_BOOTSTRAP.md |
| N10 | REJECTED_DESIGN | 과거 채팅 내용을 열람 못해도 표시↔저장 일치를 PASS 처리 | `UNKNOWN`; W-ID↔원고는 별도 검수 | 04_STATE_MANAGEMENT.md |
| N11 | REJECTED_DESIGN | 파일 blob SHA 확인만으로 브랜치 전체 HEAD CAS 원자성 완전 보장 주장 | 서버 지원 수준 별도 확인, race/부분저장 정직 | PROJECT_BOOTSTRAP.md |
| N12 | REJECTED_DESIGN | GitHub READ 장애를 WRITE 장애 X04 하나로 대체해 합격 주장 | 독립 X29 필요 | V2_EXTERNAL_AUDIT_02_ORIGINAL.md |
| N13 | REJECTED_AS_PROOF | 동일 X-ID를 POS/NEG/FAIL에 재사용한 횟수를 독립 반대 실험 건수로 주장 | 공유/같은 방향 표시와 항목별 평가를 우선 | V2_THEORETICAL_COVERAGE_MATRIX.md |
| N14 | PARTIALLY_REJECTED | 3차 감사의 Bootstrap 48줄·Pipeline 567줄 주장을 그대로 수용 | 지적 목적(실제 line 검증)은 채택, 당시 파일 전체 줄수 주장은 실제 fetch 55/623과 달라 반려; 이동한 행만 검증·갱신 | V2_REAUDIT_03_REMEDIATION.md |
| N15 | NOT_ADOPTED_AS_GATE | 추가 4차 정적 감사만 반복해 실제 신규 모델 E2E를 대체 | 제3차 B의 두 P1 국소 수정 뒤 우선 다음 독립 E2E로 이동; 추가 감사 자체가 영구 금지 아님 | V2_REAUDIT_03_FINAL_GATE.md |
| N16 | NOT_ADOPTED_AS_GATE | 과거 AI 고용 연구 브랜치에서 같은 조사 C1~C14 전부 다시 하고 기존 연구 결과 덮어쓰기 | 새 독립 프로젝트/브랜치와 E2E로 수행 | V2_PROGRESS_CHECKPOINT.md §0·§21 |
| N17 | REJECTED_EVIDENCE | 외부 감사자 개발 요약을 원본 보고서 자체로 간주 | 원문 1/2/3차 별도 보존, 조치 기록과 구분 | V2_EXTERNAL_AUDIT_01/02/03_ORIGINAL.md |
| N18 | NOT_ADOPTED_AS_RULE | 모든 조사에 PDF 생성·전수 인용 검사·보고서/절차 로그 강제 | 요청·조건에 따른 필요 경로만 적용 | 13_FINAL_REPORT.md; 01_CORE_RULES.md |

> **오해 방지:** N01의 `main` 개발 적용 반려는 사용자가 **명시적으로 정정**한 결정이지만, N14 줄번호 일부 반려는 **개발자 원문 검증 판단**이다. N15 같은 후속 정적 감사 미채택은 **이번 순서의 운영 판단**이지 외부 감사 자체를 전부 거부한 것이 아니다. N02는 '거절된 설계'가 아니라 **대체된 역사 후보**다. N17은 이번에 원본 파일을 보존하면서 인계 결함을 복구한 것이다.

## C. 보류·미검증·불확실 (반려가 아님, 12건)

| ID | 상태 | 미실행 작업/불확실 | 다음 스레드 처리 기준 |
|---|---|---|---|
| P01 | NOT_TESTED | 동등조건 BASE↔CANDIDATE 신규 ChatGPT 실제 E2E | N01~N12, X01~X48; actual_active_rules 주입 확인 필수 |
| P02 | NOT_TESTED | T06-R R1~4 새 대화에서 GitHub 직접 복구 | X09~X12/X29; 단일·복수·자료누락·READ 장애 |
| P03 | NOT_TESTED | C10/C13/C14 최초 자발 발동과 반론·원고 실물 내용 | N08~N10; 복구와 구별 |
| P04 | NOT_TESTED | 실제 표시한 편집안/선저장 revision/UI↔blob 검증 | X30/X46/X47; UI 불가시 UNKNOWN |
| P05 | NOT_TESTED | no-write 실제 원격 쓰기 호출 0회와 기존 저장권한 보존 | X44/X45 |
| P06 | NOT TESTED | GitHub HEAD 경쟁, 부분저장, 외부 지시 인젝션 | X03~X05/X21 |
| P07 | NOT_TESTED | PDF 실제 원고 입력·한글/표 렌더 실패 | X26/X34/X35 |
| P08 | NOT_TESTED | 일곱 보고서 형식·장문 Part·단발질문 정상 동작 | X36/X43/N12 |
| P09 | NOT_TESTED | 검색량/승인턴/시간·토큰·비용 비교 | X27/X48; 결과 실측 전 무회귀 확정 금지 |
| P10 | UNVERIFIED | 실제 프로젝트의 active rules SHA | GitHub 고정 커밋은 증거 아님; 설치/설정 운영자 확인 |
| P11 | UNVERIFIED | 테스트 번호 참조와 시나리오 의미론 독립성 | 59행의 7 SHARED + 4 SAME-DIRECTION 검토가 별도로 남음 |
| P12 | DEFERRED_OUT_OF_SCOPE | 운영 `main` 승격 또는 실제 연구 브랜치 변경 | 사용자 별도 요청 전 시행 금지 |

## D. 일자/버전별 판단 연결 (원본을 새 결론으로 덮지 않음)

| 감사/실측 | 원본 증거 | 당시 판정 | 현재 처분 |
|---|---|---|---|
| 과거 C10 | `V2_TEST_RESULTS.md` §42 | 최초 FAIL | 유지; 새로운 N08에서 개선 여부를 시험 |
| 과거 C11 | §43 | 별도 회복 PASS | 최초 C10 FAIL 삭제 불가 |
| 과거 C13 | §45 | 최초 FAIL | 유지; 새로운 N09에서 개선 여부 시험 |
| 과거 C13-R | §46 | 회복 PASS | 최초 C13 FAIL 삭제 불가 |
| 과거 C14 | §47 | 최종화·저장·채팅 전달 PASS / 중요한 반론 Stage7 PARTIAL | 본문의 반론 누락과 메커니즘 실패 보존 |
| 과거 C14-R | §48 | 4종 비교 자료 회복 PASS | 최초 C14 PARTIAL 삭제 불가 |
| 외부감사 #1 | `V2_EXTERNAL_AUDIT_01_ORIGINAL.md` / `c9f8...` | 수정 후 재감사, main NO-GO | 권고 중 타당한 설계 국소 반영; main은 범위 밖 |
| 외부감사 #2 | `V2_EXTERNAL_AUDIT_02_ORIGINAL.md` / `0e572...` | 수정 후 재감사 | 읽기실패 분리, 표시안 추적, 59/59 자기확증 철회 |
| 외부감사 #3 | `V2_EXTERNAL_AUDIT_03_ORIGINAL.md` / `3c0a...` | B — P1-A/P1-B 수정 후 E2E | 수정 후 규칙 `ac4675...`; 외부감사 자체가 A로 바뀌지는 않음 |
| 새 독립 BASE↔후보 | `V2_E2E_PRE_POST_PROTOCOL.md` | NOT TESTED | **바로 다음 실증 작업** |

## E. 업데이트 규칙

1. 새 시험에서 다른 결과가 나와도 **기존 결정 행을 침묵 수정하지 않는다**. 새 행과 실제 GitHub HEAD·파일/blob·사용자 발화·출처를 기록하고 이전 행을 `SUPERSEDED`로 연결한다.
2. 실제 사용자 승인/반려 기록이 없는 제안은 '사용자 확정'이라고 부르지 않는다. 감사자 제안은 개발자 채택과 별도로 표시한다.
3. P0/P1 수정이 생기면 `02_RESEARCH_PIPELINE.md` 등의 실제 규칙 diff→새 frozen SHA→59요구 매핑→기존 기능/반례 회귀→실사용 시험으로 이력을 연결한다.
4. X-ID/정적 문구/외부 감사는 모델의 실사용 PASS가 아니며, 편집·저장·GitHub HEAD 결과를 외부에서 직접 볼 수 없는 경우 `UNKNOWN/NOT VERIFIED`를 사용한다.
5. 새 대화는 [V2_NEXT_THREAD_START_HERE.md](V2_NEXT_THREAD_START_HERE.md)에서 최신 상태를 읽는다. 과거 `V2_DEVELOPMENT_PHASE_CLOSEOUT.md`의 `0e572...`는 역사 기록이다.

## 방법론 링크 (형식·원칙 참고, 이 프로젝트 실증 자료가 아님)
- ADR status/context/decision/consequences: https://architecture-decision-record.github.io/templates/decision-record-template-by-michael-nygard/
- NASA Requirements Management, traceability/change management: https://www.nasa.gov/reference/6-2-requirements-management/
- NASA verification matrix: https://www.nasa.gov/reference/appendix-d-requirements-verification-matrix/
- GitHub commit compare: https://docs.github.com/en/pull-requests/committing-changes-to-your-project/viewing-and-comparing-commits/comparing-commits
