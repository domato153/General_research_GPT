# Post-v2 운영 개선 · 개발 브랜치 정리 보존 — 2026-10-12

> **역사 기록 / 현재 실행 지시 아님.** 기존 v2 역사 정본은 이 아카이브의 `V2_*`, `HISTORY_*` 파일과 과거 커밋을 그대로 유지한다. 이 기록은 2026-10-11~12 후속 운영 개선과 5개 `design/*` 정리 스냅샷이다.

## 원격 스냅샷 (보존 커밋 작성 직전)
- 운영 정본 `main`: `7fd46d9fb738fcb74f63f0f6e23aec00c27b945f` (후속 코드·규칙·테스트가 이미 병합됨).
- 이전 역사 HEAD: `2bdfadb260beae8b506b79ac54cab7640e507006`. 이 역사 커밋의 **첫 부모**로 유지한다.
- 별개 현행 조사 `research/20261011-trump-midterms-opinion`: `068e13063e5d88ead9e96a8568b6ed14cb96e3f3` (이 정리에서 **변경·삭제하지 않음**).

| 정리 대상 임시 브랜치 | 정리 직전 보존할 HEAD | `main`에 대한 관계 |
|---|---|---|
| `design/biography-visual-quality-20261011` | `dc1f2a46970db8e6fb1317f56dded12dd2224216` | 현 운영 `main`의 조상·포함 이력 |
| `design/core-visual-materialization-20261011` | `911aaa93b24e82568b75176461085743f09b99e2` | 현 운영 `main`의 조상·포함 이력 |
| `design/intermediate-visual-preservation-20261011` | `1433cc780101967087abb5d0e093058a3aa2cef2` | 현 운영 `main`의 조상·포함 이력 |
| `design/post-v2-audit-remediation-20261012` | `9d80a40a3dd5e2b58d2afa9b767a947d685f4f63` | 현 운영 `main`의 조상·포함 이력 |
| `design/scope-trigger-strength-20261012` | `7fd46d9fb738fcb74f63f0f6e23aec00c27b945f` | 현 운영 `main`의 조상·포함 이력 |

각 임시 HEAD를 기준으로 `main`과 GitHub 비교했으며, 현 `main`에 비해 **ahead 0** (해당 개발 이력의 새 커밋 없음)을 확인했다. 임시 개발 브랜치에는 이 시점의 별도 미병합 고유 원고가 없다. **이름과 SHA의 기록만으로 보존을 보장하지 않기 때문에**, 이 문서가 포함되는 역사 **커밋의 추가 부모로 운영 `main` HEAD와 5개 임시 브랜치 HEAD를 실제 연결**한다. 아카이브 작업 트리는 기존 v2 역사본에 새 역사 문서만 더하고 현행 엔진 파일·연구 원고를 복사/병합하지 않는다.

## 남길 핵심 판단과 근거
1. **중간 조사 원문·시각자료 보존:** W-ID 중간 보고의 유일한 논증·반례·관측·출처 및 의미 있는 그래프 원자료뿐 아니라 실제 SVG/PNG 자산과 Markdown 연결을 보존. 표·명세만 있는 상태와 실제 시각 파일의 보존 PASS를 구별. 인물·사건 도판은 주체·시기·권리·원출처를 구별하고 실제 렌더·UI 미확인은 UNKNOWN으로 남김. 관련 커밋: `f44ef4f`, `1433cc7`, `cc8ff40`, `911aaa9`, `dc1f2a4`. 당시 근거는 현재 운영 `main`의 `tests/INTERMEDIATE_VISUAL_PRESERVATION_*`, `CORE_VISUAL_MATERIALIZATION_*`, `BIOGRAPHY_VISUAL_DESIGN_CASES.md`와 커밋에서 복구 가능.
2. **검증기·의미 충실도 국소 보완:** 누락/손상된 명시적 파일은 `file_access=HOLD` / exit 2; 마커 뒤 제목과 코드 펜스 가짜 W-ID를 구별; 수록 매핑 중복·제외와 단순 heading 검사의 의미 범위 분리. 선택적 Python 검사로 실제 의미·채팅 UI·PDF 렌더 PASS를 주장하지 않음. 관련 커밋: `a6c213f`, `9d80a40`. `tests/POST_V2_AUDIT_REMEDIATION_VERIFICATION.md`가 테스트 기록.
3. **선택 시각화의 범위 정확성:** 전체 의제 중 선택한 7개처럼 일부 범위를 그릴 때 전체 분포·전체 순위로 오인되지 않도록 문서별 범위를 명시. 공통 규칙은 `356893e`, 실제 주제별 차트/연구 보정은 별개 연구 브랜치에 있으며 이 아카이브에 복사하지 않음.
4. **발동 강도·사용자 선택형 확장:** 복합 조사 첫 결론의 그럴듯함으로 Stage 2~3 실질 근거 검증 생략 금지. 주요 조사 묶음→종합분석 전환 때 계획 내부 W-ID 점검과 별도로 고가치 미요청 누락축 선제 발굴. 결정적 근거 오류(A)는 자율 검증·정정, 선택적 새 조사축(D)은 후보 개수 상한 없이 투명하게 공개하고 2~3개 권장 실행 조합 및 현 근거로 진행 선택권 제공. 무단 자동 착수·무한 라운드·단발 질문 과잉 관문 방지. 관련 커밋: `9adabf2`, `208a6c1`, `7fd46d9`.
5. **실제 시험과 한계 분리:** 최종 규칙 후보 `7fd46d9`을 Windows 임시 clone에서 실행해 새 **정적 배치 테스트 11/11 PASS**, 기존 Python validator **12 PASS, 1 SKIP**(선택적 PDF 라이브러리), `git diff --check PASS`. 이전 실행에서는 테스트 파일의 trailing whitespace 1건으로 diff check FAIL 후 `7fd46d9`에서 수정·재시험. 20개 강도/트리거 시나리오는 **시험 문서만 추가**, 실제 새 프로젝트 모델의 자발적 발동·도구 동작/E2E는 **NOT RUN / UNKNOWN**. PDF 실 렌더와 과거 채팅 UI 픽셀 일치도 PASS가 아니다.

## 복구·안전 경계
- 이 기록 및 위 테스트·개선 커밋의 Git 객체는 역사 커밋의 부모 관계를 통해 보존한다. `git show <SHA>:<경로>`, `git log <SHA>`로 당시 판본·증거를 읽거나 특정 SHA에서 새 브랜치를 생성할 수 있다.
- `main`은 **현행 범용 운영 규칙**, 역사 브랜치의 `PROJECT_BOOTSTRAP.md` 등 과거 파일은 **구판본 증거**다. 역사 HEAD를 그대로 운영본으로 교체하지 않는다.
- 브랜치 참조 삭제는 별도 단계이다. 삭제 **완료 여부**는 실제 REST DELETE와 후속 브랜치 조회 결과가 있는 추가 역사 기록에서 확인해야 하며, 이 보존 스냅샷만으로 삭제 완료라고 주장하지 않는다.
- 이 기록은 현재 `research/*` 자료/상태를 재감사한 결과가 아니다. 사용자 연구 브랜치를 삭제·병합하지 않는다.

## 실제 정리 완료 결과 (별도 후속 확인)

- 실행 도구: 사용자 인증 `gh` CLI(계정 `domato153`)에서 GitHub REST API `DELETE /repos/domato153/General_research_GPT/git/refs/heads/design/...`. 원격 파일·연구 브랜치를 변경하지 않았다.
- 삭제 직전 REST GET으로 보호 브랜치 3개와 임시 브랜치 5개의 **정확한 HEAD**를 모두 비교하고, **각 DELETE 직전** 해당 임시 ref의 SHA를 다시 확인했다. 전체 5개 DELETE가 정상 종료(프로세스 exit 0).
- 삭제된 임시 ref는 상단 표의 5개 전부다. 삭제 후 GitHub branches API 원격 결과: 정확히 **3개**: `main` = `7fd46d9fb738fcb74f63f0f6e23aec00c27b945f`; `archive/research-v2-development-20261011` = `b8cf7192d1ea09dbf47ea787a451bcd9b2d7434e` (본 완료 기록 추가 커밋 전); `research/20261011-trump-midterms-opinion` = `068e13063e5d88ead9e96a8568b6ed14cb96e3f3`.
- **역사 보존 커밋** `b8cf7192d1ea09dbf47ea787a451bcd9b2d7434e`의 부모 커밋을 GitHub Git Commit API로 재조회하여 과거 아카이브 HEAD·운영 main HEAD·개발 고유 HEAD가 연결된 사실을 확인했다. 최종 보존 상태는 이 완료 기록 추가 이후 새 archive HEAD를 기준으로 재조회한다.
- 삭제 ref의 이름은 더 이상 존재하지 않는다. 복원은 이 문서의 고정 SHA로 수행하며, 같은 이름의 브랜치가 다시 만들어졌다고 가정하지 않는다.
- 원격 브랜치 삭제는 Git 커밋 객체·실물 연구/운영 파일 삭제가 아니다. 운영/연구 본체 보존의 진짜 완료 여부는 이력에서 해당 SHA가 도달 가능한지 별도 확인한다.
