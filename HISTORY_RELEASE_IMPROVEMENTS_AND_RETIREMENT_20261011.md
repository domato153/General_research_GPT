# 운영 승격 후 개선·브랜치 정리 전 이력 보존 — 2026-10-11

> **역사 기록, 운영 지침 아님.** 현행 범용 조사 규칙의 정본은 `main`; 이 역사 브랜치의 루트 규칙 파일은 구판이며 이 문서의 보존 부모 그래프 또는 고정 커밋을 통해 후속 버전을 조회한다. 과거 `HISTORY_*` 파일의 당시 '현재 상태'를 오늘의 브랜치 상태라고 해석하지 않는다.

## 보존 목적 및 검증 경계

- 2026-10-11 후속 운영 개선(PR #2~#5)과 그때의 실제 원본 파일·변경 코드·개발 브랜치·연구 시험 브랜치의 **전체 Git 커밋/트리 이력**을 이 역사 브랜치의 조상 그래프에서 계속 도달 가능하도록 남긴다.
- 역사 보존 커밋의 **첫 번째 부모**는 수정 전 역사 브랜치 HEAD `30746a5971177bc77ea01d013399166fcf8c9c73`이며, **추가 부모 7개**는 운영 main `868f0df6a0acf1c53f91cb25ca4572b785761324`과 아래 6개 브랜치 최종 HEAD이다. 기존 역사 이력의 원본 커밋을 개정·덮어쓰지 않는다.
- 각 SHA가 기록된 문서만으로 영구 보존되는 것이 아니다. **보존 커밋의 실제 부모 연결·업데이트된 archive ref·원본 자료 재조회 성공을 확인한 뒤에만** 브랜치 삭제를 진행할 것.
- 연구 자료는 공통 `main` 트리에 병합하지 않는다. 보존된 연구 커밋은 역사 브랜치의 *조상*에서만 확인하며 일반 역사 브랜치 루트 디렉터리에는 연구 전문이 자동 나타나지 않는다.

## 후속 운영 개선 PR·고정 원본

| 운영 커밋 (전체 SHA) | 릴리스 | 내용 |
|---|---|---|
| `03e91ff0789d0f008929258aecb841d5c165ba35` | PR #2 | 조사 자료·개별 W-ID 정보 보존, 반복 보완 및 사용자 선택, 최종 기준본과 채팅·시각자료 신뢰 경계 |
| `a0e97337ec0fb6157a060db283f3548c3d12f85b` | PR #3 | PDF 내용 완전성→의미 충실도→실제 렌더 품질. 채팅 UI 이미지 복제 강제 대신 정보·비교 관계 보존 |
| `7b348d427733ad5be795fa91b822fb03164a962f` | PR #4 | 읽기 전용 선택형 research_validator.py: evidence/final/pdf, 별도 pytest 회귀시험. 기계적 PASS와 의미/실제 UI/시각 UNKNOWN 분리 |
| `868f0df6a0acf1c53f91cb25ca4572b785761324` | PR #5 | /handoff 직전 미저장 내용 W-ID 보존, 인계 뒤 목적어 없는 검토의 양방향 자료 보존 감사, 중간 채팅 보고서 새 논증·반론을 W-ID에 누적 |

- 규칙 원본 재조회: `git show 868f0df6a0acf1c53f91cb25ca4572b785761324:PROJECT_BOOTSTRAP.md`, `...:02_RESEARCH_PIPELINE.md`, `...:04_STATE_MANAGEMENT.md`, `...:04B_VALIDATION_RULES.md`, `...:13_FINAL_REPORT.md`.
- 코드 원본: `git show 868f0df6a0acf1c53f91cb25ca4572b785761324:tools/research_validator.py`, `git show 868f0df6a0acf1c53f91cb25ca4572b785761324:tools/test_research_validator.py`.
- 승인 PDF 스타일 원본: `git show 868f0df6a0acf1c53f91cb25ca4572b785761324:final_pdf_report_style.css`, `git show 868f0df6a0acf1c53f91cb25ca4572b785761324:final_pdf_html_formatting_instruction_final.md`.
- 운영 `main`의 규칙과 역사 브랜치의 구판 규칙을 동일 판본으로 주장하지 않는다.

## 삭제 전 브랜치명 → 커밋 HEAD (각 전체 이력 보존 대상)

| 브랜치 | 최신 HEAD |
|---|---|
| `design/20261011-handoff-report-preservation` | `eb8da96d1389f11925a2fd07c56e1a2c26e4336e` |
| `design/20261011-optional-research-validator` | `f0ba91ce5cb7d0c0d6789791af068b01553eb148` |
| `design/20261011-pdf-semantic-fidelity` | `43fc182277dabc54210d295778ea2a71648d3f94` |
| `design/20261011-research-fidelity-continuity` | `04575de84175998e89cd2fa38b2edbac2acca813` |
| `research/20261011-rapid-trigger-mice` | `6483136f429795b2c42447f06d348285d8e8feef` |
| `research/20261011-trump-midterms-polling` | `9d6684f6f4d47e8524e74325c68448eddb37571e` |

- 위 6개 중 `research/20261011-trump-midterms-polling`은 진행 중이던 조사까지 포함하며 사용자가 **이전 조사·진행 중 트럼프 조사도 삭제하여 새로 시험**할 것을 명시했다.
- 삭제 전 각 브랜치 HEAD가 기록된 SHA와 여전히 동일한지 검사한다. 동시 스레드가 작업을 추가했다면 **그 브랜치는 삭제하지 말고 변경분을 다시 보존 후 재검증**한다.
- 삭제 기록은 실제 GitHub refs 삭제 성공 및 잔여 브랜치 목록을 조회한 경우에만 **완료**로 남긴다. 이 기록의 존재만으로 삭제를 선언하지 않는다.
- 과거 26개 브랜치 정리 이력은 별도 `HISTORY_RETIRED_BRANCH_HEADS_20261011.md`, `HISTORY_BRANCH_CLEANUP_COMPLETED_20261011.md`에 보존하고 이 기록과 혼동하지 않는다.

## 검증 수준과 미해결 과제

- PR #2/#3: 관련 규칙 정적 검사 및 9개 합성 상황 검사. 실제 ChatGPT 장문·PDF 전체 렌더 E2E는 미수행.
- PR #4: 코드·문서 정적 검사 및 시제품 시험을 확인했지만 **GitHub 업로드된 정확한 Python 판본의 실행시험은 미확인**. 이 검사기는 중요한 사실의 의미/실제 UI/시각 디자인 합격을 증명하지 않는다.
- PR #5: 정적 조건·24개 시나리오 및 규칙 보존 검사를 통과했으나 실제 다른 ChatGPT 스레드의 `/handoff`·후속 `검토` E2E는 수행하지 않았다.
- 채팅 프로젝트 첨부 부트스트랩의 실제 판본·실주입 여부는 GitHub 저장 사실만으로 검증할 수 없다. 사용자가 최신 부트스트랩 교체를 보고했지만 연결된 실제 런타임 설정 SHA는 **UNKNOWN**.
- 삭제한 연구 브랜치 자료는 고정 SHA로 재구성·브랜치 생성할 수 있으나, **기존 조사 자체의 후속 수행·검증이 완료되었다는 뜻은 아니다**.

## 복구 지침

```sh
# clone/fetch 후 역사 브랜치의 조상에 기록된 각 SHA를 확인
git fetch origin archive/research-v2-development-20261011
git cat-file -t 9d6684f6f4d47e8524e74325c68448eddb37571e
git show 9d6684f6f4d47e8524e74325c68448eddb37571e:RESEARCH_PLAN.md
# 필요한 경우 선택된 고정 SHA에서만 별도 새 연구 브랜치 복원
git branch recovered-trump-9d6684f6 9d6684f6f4d47e8524e74325c68448eddb37571e
```

보존 부모와 GitHub 실제 브랜치 삭제 결과를 확인하기 전 이 문서를 삭제 완료 증빙으로 사용하지 않는다.
