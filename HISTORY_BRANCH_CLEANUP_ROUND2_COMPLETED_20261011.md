# 운영 개선 후 2차 브랜치 정리 완료 — 2026-10-11

## 실제 완료 상태
- 사용자 요청: 운영 `main`과 기존 개발 역사본 외 브랜치 전체 정리. 기존 조사·진행 중 트럼프 조사 포함.
- 보존 커밋: `1b8d9c1bbc39f725934dbecbed6ee668211bc4c4` (기존 역사 HEAD 첫 부모, 운영 main + 6개 정리 대상 HEAD를 추가 부모로 연결).
- 보존 문서: `HISTORY_RELEASE_IMPROVEMENTS_AND_RETIREMENT_20261011.md` (원래 브랜치 이름·전체 HEAD·PR #2~#5 개선과 검증 한계·복구 지침).
- GitHub CLI 인증 사용자 `domato153`로 REST Git ref DELETE를 실시한 뒤, GitHub 원격 브랜치 목록을 다시 조회해 **6개 모두 삭제를 확인**했다.
- 삭제 대상: 개발 4개 `design/20261011-handoff-report-preservation`, `design/20261011-optional-research-validator`, `design/20261011-pdf-semantic-fidelity`, `design/20261011-research-fidelity-continuity`; 연구 2개 `research/20261011-rapid-trigger-mice`, `research/20261011-trump-midterms-polling`.
- 삭제 직후 남은 브랜치(ref)는 **`main` = `868f0df6a0acf1c53f91cb25ca4572b785761324`** 및 **`archive/research-v2-development-20261011` = `1b8d9c1bbc39f725934dbecbed6ee668211bc4c4`** 두 개뿐이다(이 완료 기록 추가 커밋 이전).
- 삭제된 트럼프 연구의 HEAD `9d6684f6f4d47e8524e74325c68448eddb37571e`에서 GitHub를 통해 `RESEARCH_PLAN.md` 원문을 실제 재조회했다(blob `a614322e0404b727e8960e8afd009adf082bf71d`). 이는 **삭제된 연구 데이터가 별도 커밋으로 계속 접근 가능하다는 최소 복구 확인**이며 연구 내용 E2E가 아니다.
- 생성되는 이 완료 기록 커밋으로 역사본 HEAD는 한 번 더 전진하므로, 위 정리 직후 HEAD와 이후 최신 archive HEAD는 구분한다.

## 복구 및 한계
- 보존 커밋 부모 SHA가 삭제된 브랜치 HEAD를 모두 포함함을 GitHub Git Commit API에서 확인했다(8 parents: 과거 역사 HEAD 1, 최신 운영 main 1, 개발 4, 연구 2). 그러므로 대상의 전체 커밋 조상 이력은 역사 브랜치에서 도달 가능하다.
- 필요 시 `git show 9d6684f6f4d47e8524e74325c68448eddb37571e:RESEARCH_PLAN.md` 등으로 조사 파일을 열거나 기록된 HEAD에서 브랜치를 복원한다. 복원 시 현재 `main`에 고유 조사 자료를 합치지 않는다.
- 기존 1차 26개 브랜치 정리 기록(`HISTORY_BRANCH_CLEANUP_COMPLETED_20261011.md`)은 별도 역사 사실이다. 역사 파일의 과거 당시 '남은 연구 브랜치' 또는 '현재 운영 SHA' 표현은 현재 상태를 뜻하지 않는다.
- PR #2~#5의 정적/시나리오 검사와 실제 ChatGPT 프로젝트 UI 동작·새 독립 연구 검증을 혼동하지 않는다. ChatGPT 프로젝트 첨부 부트스트랩은 사용자가 교체를 보고했지만 실제 모델 주입 SHA는 도구로 검증하지 못했다.
