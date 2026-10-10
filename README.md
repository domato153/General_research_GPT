# General_research_GPT — 범용 딥 리서치 워크스페이스 v2

## 정본
- `main`: 범용 조사 엔진·최종보고서 양식·선택형 상태 관리 초기 템플릿·승인된 PDF 스타일 **운영 정본**. 개별 연구 데이터나 개발 실험 기록은 넣지 않는다.
- `PROJECT_BOOTSTRAP.md`: 실사용 프로젝트에 배포할 전체 부트스트랩. GitHub `main` 파일 변경만으로 ChatGPT 프로젝트 지침/첨부가 자동 갱신되지는 않는다.
- `00_INDEX.md`, `01_CORE_RULES.md`, `02_RESEARCH_PIPELINE.md`, `03_REVIEW_MODULES.md`, `04*`, `05_DOMAIN_MODULES.md`, `13_FINAL_REPORT.md`: 사용 목적에 따라 필요한 규칙만 읽는다.
- `final_pdf_html_formatting_instruction_final.md` + `final_pdf_report_style.css`: 사용자 승인 PDF 레이아웃. PDF 생성 요청이 있을 때만 참조한다.
- `10_CURRENT_SUMMARY.md`~`12_ARCHIVE_LOG.md`: 필요할 때 조사별로 쓰는 **초기 템플릿**. 단계마다 반드시 업데이트하거나 Closeout할 필요는 없다.

## 브랜치
- 장기 조사는 `main`에서 고유 `research/YYYYMMDD-주제` 브랜치를 만들어 저장한다. 짧은 질문과 명시적 GitHub 비저장 요청은 별도 처리한다.
- 조사 종료 시 해당 연구 브랜치를 `main`에 병합하지 않는다. 고유 연구 결과를 보존하지 않고 브랜치를 삭제하면 자료가 사라질 수 있다.
- v2 개발 과정의 결정·감사·최초 FAIL/후속 회복 기록: `archive/research-v2-development-20261011` (운영 규칙이 아닌 **역사 자료**).
- 과거 최초 공통 규칙 원본 커밋: `bf7b315a2b3316fc96c763d3ba82c4234a849bfc`.
- 브랜치 정리/삭제는 각 브랜치의 고유 자료를 보존·검수하고 사용자가 삭제 범위를 최종 승인한 경우에만 실시한다.

## 실사용 설치
`INSTALL_CHATGPT_PROJECT.md`를 따라 ChatGPT 프로젝트 지침과 `PROJECT_BOOTSTRAP.md` 첨부를 **별도로** 갱신한다. `/handoff` 직후 목적어 없는 `검토해줘`와 명시된 다른 검토 대상을 각각 새 채팅에서 확인한다.
