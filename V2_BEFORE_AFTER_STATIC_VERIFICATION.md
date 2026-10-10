# 동일 문구 기준 변경 전·후 소스 계약 재실행

- 변경 전 고정 SHA: `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0`; 변경 후 별도 격리 브랜치: `audit/v2-e2e-hardening-20261010` (이 파일 생성 **직전** 규칙 버전).
- 수행: GitHub 8개 관련 규칙 파일을 **양쪽에서 독립 조회**해, 변경 전 `V2_BEFORE_BASELINE_REPLAY.md`와 **동일한 26개 정규식 앵커**를 재실행. 두 버전의 기존 문장을 순서대로 보존하는지 전체 줄 단위 부분수열 검사도 수행. 실제 독립 LLM E2E 아님.
- 앵커 정규식은 신규 규칙 표현을 위해 수정하지 않음. 따라서 NOT_FOUND는 불합격이나 기능 부재 단정이 아니라 소스 검색어의 거짓 음성일 수 있음. 새 규칙의 **의미론적 실제 충족**은 별도 시나리오 및 외부 감사로 검증.

| ID | 계약 | 변경 전 | 변경 후 |
|---|---|---|---|
| A01 | 초기 의향/본조사 | FOUND | FOUND |
| A02 | 지역 부분선택 | FOUND | FOUND |
| A03 | 첫 W-ID 리뷰 | FOUND | FOUND |
| A04 | W-ID 조건부 추적 | FOUND | FOUND |
| A05 | 계속=안내 작업 | FOUND | FOUND |
| A06 | 무단 최종화 | FOUND | FOUND |
| A07 | 종료신호 즉시 검사 | NOT_FOUND | NOT_FOUND |
| A08 | 감사 계획 vs 실행 | NOT_FOUND | NOT_FOUND |
| A09 | Stage5 편집선택 | FOUND | FOUND |
| A10 | 실제 표시 편집안 | NOT_FOUND | NOT_FOUND |
| A11 | Stage7 W-ID↔원고 | FOUND | FOUND |
| A12 | Stage7 반론반영 | FOUND | FOUND |
| A13 | 근거별 반례 대조 | NOT_FOUND | FOUND |
| A14 | PASS의 증거 | NOT_FOUND | NOT_FOUND |
| A15 | 측정단위 | NOT_FOUND | FOUND |
| A16 | 판본표본수치 | NOT_FOUND | FOUND |
| A17 | 최신보정우선 | NOT_FOUND | FOUND |
| A18 | 새 스레드 복원 | NOT_FOUND | FOUND |
| A19 | 다수 후보 확인 | NOT_FOUND | NOT_FOUND |
| A20 | 규칙버전삼분리 | NOT_FOUND | FOUND |
| A21 | 전달과보존 분리 | NOT_FOUND | NOT_FOUND |
| A22 | 비신뢰 명령 | FOUND | FOUND |
| A23 | GitHub SHA 동시성 | FOUND | FOUND |
| A24 | 짧은 자연어 E2E | NOT_FOUND | NOT_FOUND |
| A25 | 불필요 승인 금지 | FOUND | FOUND |
| A26 | 읽지않고 읽었다고 주장 금지 | FOUND | FOUND |

**문구 탐지:** 변경 전 13/26 → 변경 후 19/26, **신규 탐지 6개**. 정확도/성능 향상 점수가 아니며 텍스트 표현 일치 비율임.

## 기존 줄 보존 여부
| 규칙 파일 | 기존 줄 수 | 변경 후 줄 수 | 기존 줄 순서보존 |
|---|---:|---:|---|
| PROJECT_BOOTSTRAP.md | 45 | 55 | PASS |
| 00_INDEX.md | 273 | 277 | PASS |
| 01_CORE_RULES.md | 194 | 194 | PASS |
| 02_RESEARCH_PIPELINE.md | 602 | 622 | PASS |
| 03_REVIEW_MODULES.md | 451 | 456 | PASS |
| 04_STATE_MANAGEMENT.md | 234 | 241 | PASS |
| 04B_VALIDATION_RULES.md | 667 | 673 | PASS |
| 13_FINAL_REPORT.md | 772 | 777 | PASS |

- 미탐지 조건: A07, A08, A10, A14, A19, A21, A24. 외부 감사에서는 **각 조건의 실제 규칙 의미**를 읽어 검증할 것.
- 원래 8개 규칙의 문장 삭제·변경 없는 보강인지 검증: ALL PASS.
- GitHub 도구 실제 저장, SHA 확인·역사 보존과 실사용 모델 동작은 별개의 검증 차원.
