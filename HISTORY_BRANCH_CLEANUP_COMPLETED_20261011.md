# v2 브랜치 정리 완료 기록 — 2026-10-11

## GitHub 최종 상태
- 정리 직전 브랜치 총 28개: 운영 `main` 1, 역사본 `archive/research-v2-development-20261011` 1, 정리 대상 26(개발·감사 4, 연구 22).
- GitHub CLI 인증 계정 `domato153`로 GitHub API를 사용해 나머지 26개 브랜치 ref 삭제 완료. **운영 `main`과 역사 브랜치는 보존.**
- 최종 branch refs 조회: `refs/heads/main` = `6eef107c6b080b30fa54ecb16eda3ebbcb6daba0`, `refs/heads/archive/research-v2-development-20261011` = `f9da9e13281d9aab24ea61c3286c023a2166cddb`(본 완료 기록 커밋 이전).
- 삭제 실행 전 후보 26개의 각 HEAD와 `HISTORY_RETIRED_BRANCH_HEADS_20261011.md` 원본 목록 대조; 총 27부모 Git 커밋 `f9da9e13281d9aab24ea61c3286c023a2166cddb`의 추가 부모에 26개 전체 HEAD를 정확하게 연결한 후 삭제. 따라서 **각 연구/개발 브랜치의 전체 커밋 이력이 역사 브랜치 조상 그래프에 도달 가능**. 해당 자료를 `main`으로 잘못 병합하지 않음.
- 삭제된 `research/20261010-v2-smoke`의 기존 HEAD `bf54731f0340fb7b4747ab79b44b6319328a3d13`에서 `FINAL_REPORT.md` 재조회 성공. 삭제 이후에도 `research/20261011-openssh-cve-2024-6387` HEAD `d55714adb510cbdd293ae9d92a358a22e5dc9812`, `research/20261011-kr-us-ev-charging-adoption` HEAD `818c7f21bdbc4ef33a66cf343c306f6b90abb9ac`, `research/20261010-ai-employment-kr-us-1538-fb22` HEAD `cbe5b68d8a0fcfa355d320268ceb8b3c8e9d634b`에서 실제 `FINAL_REPORT.md` 읽기 성공. 구 PDF 시안 `0b34dcfa02a88d687ef25a474a84c9a924396dd5:report.html` 재조회 성공.
- 이 기록의 저장으로 archive HEAD는 다시 새 커밋으로 전진한다. `HISTORY_RETIRED_BRANCH_HEADS_20261011.md`는 **삭제 전 원래 명칭→HEAD**의 복원 정본이며, 기존 `HISTORY_BRANCH_INVENTORY.md`는 릴리스 당시 스냅샷일 뿐 최신 브랜치 목록이 아니다.

## 사용·복구
- 이전 연구 자료는 `github.com/domato153/General_research_GPT/blob/<기록된 SHA>/<파일명>` 또는 `git show <SHA>:<path>`로 접근한다.
- 필요하면 GitHub API로 원래 SHA에 새 브랜치 ref를 생성하거나 `git branch <새이름> <SHA>`로 복원한다. 원래 브랜치명은 삭제됐지만 원래 커밋 및 파일은 역사 브랜치의 조상으로 보존된다.
- 운영 `main` 승격은 완료. 실사용 ChatGPT 프로젝트 지침·첨부 교체 및 신규 대화 런타임 테스트는 별개로 미실시, 실주입 SHA UNKNOWN. 최초 인계 라우팅 P1 FAIL과 시험별 한정 PASS는 소급 변경하지 않는다.
