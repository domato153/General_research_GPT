# 변경 전 고정 규칙 소스 계약 재현 — 독립 모델 E2E 아님

- 실행일: 2026-10-10
- **대상 규칙 SHA: `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0`**. 대상 소스 8개 파일 전체 GitHub 원문을 이 SHA로 직접 조회.
- 시험 범주: 실제 소스에 명시적 행동 트리거/출력·근거 계약이 존재하는지 **정규식/문구 앵커 검사**. 판정은 보수적 탐지이며 문장 표현 차이로 거짓 음성이 있을 수 있음. 실패가 실제 모델 동작 실패를 뜻하지 않고, 통과도 실제 동작 보증이 아님.
- **변경 전 관측된 사람+모델 실사용 사례 리플레이:** C1~5 PASS, C6~9 조사 실행 PASS/새 선택지 PARTIAL, C10 선제 감사 FAIL→C11 회복, C13 자발 편집 선택 FAIL→C13-R 회복, C14 첫 원고 검수 PARTIAL→C14-R 회복, 구 규칙 출발 SHA와 계획 신후보 분리 미증명. 정본 `V2_TEST_RESULTS.md` §§31~48; 예전 후보의 초기 협업 순서 FAIL·일부 계획 추적 PARTIAL은 그 이전 항목 §§14,19,26에 별도 기록.
- **실제 새 독립 ChatGPT 실행:** NOT RUN / NOT CLAIMED. 모델 실행은 외부 비개인화 감사 단계에 넘김.

## 소스 계약 앵커 판정
| ID | 비교 조건 | 원문 앵커 | 해당 파일 |
|---|---|---|---|
| A01 | 초기 조사 의향/본조사 분리 | FOUND | PROJECT_BOOTSTRAP.md |
| A02 | 지역 등 부분합의 ≠ 전체 승인 | FOUND | PROJECT_BOOTSTRAP.md |
| A03 | 첫 실질 W-ID 결과에 재선택 관문 | FOUND | 02_RESEARCH_PIPELINE.md |
| A04 | W-ID 완료/부분완료/보류 추적 | FOUND | 02_RESEARCH_PIPELINE.md |
| A05 | 계속해는 이전에 안내한 작업만 | FOUND | 02_RESEARCH_PIPELINE.md |
| A06 | 자동 최종화 금지 | FOUND | 02_RESEARCH_PIPELINE.md |
| A07 | Stage 5 종료신호로 즉시 실제 출처 파일 조회 | NOT_FOUND (source-specific) | PROJECT_BOOTSTRAP.md, 02_RESEARCH_PIPELINE.md |
| A08 | Stage 5 계획만 vs 감사실행 구분 | NOT_FOUND (source-specific) | 02_RESEARCH_PIPELINE.md |
| A09 | Stage 5 편집안 추천 규칙 | FOUND | 02_RESEARCH_PIPELINE.md |
| A10 | 편집안 사용자 응답 원문 보존 | NOT_FOUND (source-specific) | 02_RESEARCH_PIPELINE.md, 04_STATE_MANAGEMENT.md |
| A11 | Stage 7 W-ID 근거↔원고 | FOUND | 02_RESEARCH_PIPELINE.md |
| A12 | Stage 7 반례 누락 실제 대조 | FOUND | 02_RESEARCH_PIPELINE.md |
| A13 | Stage 7 모든 필수 비교연구 포함/제외 근거 검사 | NOT_FOUND (source-specific) | 02_RESEARCH_PIPELINE.md, 04B_VALIDATION_RULES.md |
| A14 | PASS는 실제 대조 증거가 있어야 함 | NOT_FOUND (source-specific) | 04B_VALIDATION_RULES.md |
| A15 | 측정단위 사례vs대표 빈도 | NOT_FOUND (source-specific) | 02_RESEARCH_PIPELINE.md, 04B_VALIDATION_RULES.md |
| A16 | 판본·표본·수치 직접 연결 | NOT_FOUND (source-specific) | 03_REVIEW_MODULES.md, 04B_VALIDATION_RULES.md |
| A17 | 과거 요약보다 최신 보정 우선 | NOT_FOUND (source-specific) | 04_STATE_MANAGEMENT.md |
| A18 | 새 스레드 자연어 자동 재개 | NOT_FOUND (source-specific) | PROJECT_BOOTSTRAP.md, 04_STATE_MANAGEMENT.md |
| A19 | 동명 연구 브랜치 충돌시 확인 | NOT_FOUND (source-specific) | 04_STATE_MANAGEMENT.md |
| A20 | 규칙 실행 SHA/연구 출발 SHA/현재HEAD 3분리 | NOT_FOUND (source-specific) | PROJECT_BOOTSTRAP.md, 04_STATE_MANAGEMENT.md |
| A21 | 저장완료와 채팅 전달 분리 | NOT_FOUND (source-specific) | PROJECT_BOOTSTRAP.md |
| A22 | 비신뢰 도구·외부자료 명령 차단 | FOUND | PROJECT_BOOTSTRAP.md |
| A23 | HEAD 충돌·조건부 갱신 | FOUND | PROJECT_BOOTSTRAP.md |
| A24 | 짧은 자연어 사용자 요청이 기본 E2E | NOT_FOUND (source-specific) | PROJECT_BOOTSTRAP.md, 00_INDEX.md, 02_RESEARCH_PIPELINE.md |
| A25 | 추가 승인/장황한 검수 강제 금지 | FOUND | 02_RESEARCH_PIPELINE.md |
| A26 | 실제 브랜치/파일 없으면 조회했다고 주장 금지 | FOUND | PROJECT_BOOTSTRAP.md |

**소스 앵커 발견 13/26**. 이는 정확도·성능 점수가 아니다. 결측은 실제로 필요한 새 문장인지, 다른 표현으로 이미 충분한지를 별도 의미론 감사에서 확인한다. 새 문구의 통과율만으로 후보가 행동상 우수하다고 하지 않는다.

## 변경 전 문제의 타당한 해석
- Stage5/7/편집 규칙은 **이미 상당수 존재**한다. C10/C13/C14 실측 실패는 '규칙 완전 부재'가 아니라 발동조건·작업 완료증거·결정 내용 계보가 실행에서 충분히 강제되지 않았다는 것.
- 예전 단독 시험의 실패/지금 한 주제 PASS 혼용 금지. 초기 E2E 전체 반복실행 새 데이터는 없음.
- **이 시험의 한계:** 정규식 문구 탐지와 과거 GitHub/사용자 출력 리플레이. 실제 검색·도구·심사자 모델의 블라인드 행동 비교, 동시 저장 경쟁, 토큰비용/지연, 신규 스레드 독립 재개는 테스트하지 않았다.
