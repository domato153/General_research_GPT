# 운영 관문 변경판 국소 회귀 결과 · 2026-10-12

## 고정 테스트 대상
- repository: `domato153/General_research_GPT`.
- 검증한 운영 기준: `main` 커밋 `ce1bc9d9cd2a422dc18e783ba5991b6b50b1948c`.
- 연구 적용 판본: `research/20261012-throgg-903` 커밋 `3d6be6e4191b5124dfbe3a2d48e43214c075c6fe`.
- 참조한 구 유지보수 아카이브: `archive/research-v2-development-20261011` (쓰기 전 HEAD `1e877b2ea1cf617fad6c8f483386489cc3098b5b`).
- 기존 체계: `tests/test_trigger_scope_strength.py`와 `tests/TRIGGER_SCOPE_STRENGTH_CASES.md`, `tests/test_full_report_fidelity_rules.py`; 역사 `V2_POST_E2E_PATCH_REGRESSION_PLAN.md`의 R01~R10 분리·회귀, `HISTORY_POST_V2_DEV_CLEANUP_20261012.md`의 강도/범위 11 정적 PASS·20 E2E NOT RUN 구분 원칙.

## 이번에 실제 실행한 검사 (도구 V8 JavaScript 실행, GitHub 커넥터로 main 원문 직접 로드)
| 검사 | 수행·관측 | 결과 |
|---|---|---|
| 기존 트리거/범위 계약의 Python 원래 assertion과 동등한 JS 이식 검사 TSC01~TSC11 | 현재 main의 AGENTS/00_INDEX/02/03/04B/06/T01~20 fixture 확인; **Python unittest 자체는 실행하지 않음** | **11/11 STATIC PASS** |
| 기존 Full Report 충실도 Python assertion과 동등한 JS 이식 검사 FR01~FR09 | 08/02/13/04B 및 research_validator 문구·장 경계 확인; **원래 Python unittest 실행 아님** | **9/9 STATIC PASS** |
| 새 운영 영수증·단계관문 긍정 검사 OP01~OP20 | 출력 의무/단발 예외/5상태/사용자 승인/무단 HOLD/범위 밖 후보/Stage 0~8/기록 미러/미확정 최종화 경계 | **20/20 STATIC PASS** |
| 새 규칙 의도적 결손 5개 주입 검사 | 출력 의무, 미검토 표현, 확장검토 트리거, HOLD 경계, 상태 mirror 방지 문구를 제거한 검사 대상 | **5/5 결손 검출** |
| 보존형 CLI 테스트 `test_operating_gate_contract.cjs` | 실제 동일 main 원문을 전달해 15 긍정+1 기준+5 결손 주입 검사 (어휘 중복된 결손은 전체 제거하는 방식으로 제어) | **21/21 STATIC PASS** |
| HEAD/원격 저장 검증 | 기존 운영 main 4파일과 트로그 연구 W11/계획·초안 SHA 재조회, 역사 추가 부모·경로 범위 아래 별도 확인 | 적용본 정합성 PASS |

### 최초 실패·정정 내역 (과거 결과 삭제 금지)
1. 처음 새 20개 검사에서 OP18 1개 FAIL: 검사자가 '관문 미실시' 조건을 06 문서에서만 찾았으나 실제 책임 문서는 02였음. 검사 대상을 바로잡아 **20/20 PASS** 재확인. **운영 규칙 자체의 고장이라고 입증된 것은 아님.**
2. 재현 가능한 새 CLI 코드 시안에서 mutation 기준 X00 FAIL: 존재하지 않는 문구를 찾음. `02_RESEARCH_PIPELINE.md`에 실제 존재하는 구절 `계획 밖 새 조사축 탐색`으로 정정.
3. 다음 CLI 시안에서 N02/N04 mutation 두 개 미검출: 단일 `replace` 후 동일 문구가 다른 위치에도 남아있었음. 전체 일치 제거로 정정해 **21/21 PASS** 확인. 원본 계약 보완이 아닌 시험 fixture 작성의 오류로 분류.

## 한계·미실행
- **실제 Python 명령 미실행**. 연결 데스크톱은 테스트 시점 OFFLINE, 격리 컨테이너의 github.com DNS 연결 실패. 원본 Python 테스트 결과를 '실행했다'고 표기하지 않음. JS 이식판을 별개 실행.
- **실제 ChatGPT 새 세션에 규칙을 주입한 E2E NOT RUN / active injected SHA UNKNOWN**. 지금 대화에서 지난 응답의 운영 제안 출력 사례는 있으나 새 채팅/독립 모델의 자발적 트리거·미승인 방지 성능을 실증하지 않음.
- 이전 아카이브 T01~T20 자연어 시나리오 전부 실제 피시험 모델 재생한 것 아님. 다음 독립 시험에는 '사용자 지적 없이 종합 전환시 계획 확장 제안', '복수 후보 전수 공개', '후보 없음', 'D만 선택하면 A는 자체 수정', '단발/대량 불필요 로그 방지', '사용자 계속해의 승인 범위', '영수증만 출력하고 검색 생략' 반례 등을 실제 도구·원문과 대조할 것.
- 원격 쓰기 CAS 충돌·추가 모델/클라이언트 주입 여부, 노스카 게임 자체 데이터 재검증도 이번 시험 범위 밖.
- **회귀 시험의 정적 통과는 100% 예방을 증명하지 않는다.** 다음 실전에서 누락이 발견되면 최초 실패 로그를 보존하고 영향 받은 관문과 본문을 국소 수정·재검수할 것.

## 재현 명령
```sh
# 최신 main을 별도 체크아웃하고 본 역사본의 JS 회귀 검사
node HISTORY/operating-gate-20261012/test_operating_gate_contract.cjs /path/to/main-checkout

# 원래 Python 검사(이번 턴에는 직접 실행하지 않음)
python -m unittest discover -s tests -p test_trigger_scope_strength.py -v
python -m unittest discover -s tests -p test_full_report_fidelity_rules.py -v

# 유의: 실전 behavioral E2E는 독립 실사용 주입과 모델 도구 로그가 필요
```
