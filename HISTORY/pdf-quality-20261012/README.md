# 2026-10-12 PDF 시각화·페이지 조판 개선 역사 보존

> **역사 기록, 현재 실행 지시 아님.** 운영 규칙의 정본은 `main`, 트럼프 W8 연구·보고서 정본은 `research/20261011-trump-midterms-opinion`이다. 이 보관본은 두 운영 대상과 혼동해서 사용하지 않는다.

## 사용자 요청과 보존 정책
- 사용자 피드백 1: 경제정책 막대그래프 출처 주석과 0/25/50/75/100% 축 레이블의 겹침, Cook 37개 선별 경합선거구 '한 묶음' 그래프의 불필요하게 큰 세로 여백 등.
- 사용자 피드백 2: 14개 대장이 페이지 중간에서 시작하고, 다음 그래프+캡션이 통째로 밀려 이전 페이지에 큰 공백이 발생하는 문제. 대장을 새 페이지 상단에 배치하고 밀도·읽기 편함·무축약을 함께 보장하도록 요청.
- 최종 요청: 이 일련의 체계 개선·실제 실험/실패/수정/검증 기록을 기존 **역사 보존 브랜치에 보존**할 것.
- 이력 보존은 기존 archive 문서·파일을 덮어쓰지 않고, **아카이브의 기존 HEAD를 첫 부모**로 유지한 새 커밋과 `main`·연구 판본의 실제 Git 조상 연결, 그리고 읽기 쉬운 감사문 사본을 통해 수행한다. 운영 `main`이나 연구 브랜치 작업트리를 이 보존 커밋에서 수정하지 않는다. 연구 원고, PDF, 그래프 자산을 archive **루트에 병합하지 않는다**. 이력용 커밋 부모 그래프는 연구 파일까지 도달 가능하게 하므로 사용 시 현재 운영 정본으로 오해하지 말 것.

## 보존 당시 정확한 브랜치 스냅샷
- 기록 직전 역사 `archive/research-v2-development-20261011`: `462c6c05f883e6669db008eb4a0e0878bf40ac48`. 첫 부모로 보존.
- 최종 운영 `main`: `297535465be5819323c012d3dd7f3ea33ac8de9b`. 추가 부모로 보존.
- W8 연구 `research/20261011-trump-midterms-opinion`: `e84adae6e7131cfc33105f39d229268fdf696443`. 추가 부모로 보존(당시 42쪽 PDF·두 종류 감사 문서를 포함한 트리). 연구 브랜치는 유지·변경·삭제하지 않음.
- 이전 Full Report 충실도 개선 `main` 정본 `75b8c3e44f664aa4db8dcc0dc291bd6da4436568`부터 해당 시점 `main`까지의 새 엔진 변경 커밋은 3개이며, 변경 대상은 범용 지침, CSS, 검증 지침, 검증기 2개, 회귀 시험 2개다.

## 변경 1 — 차트 자체의 SVG 텍스트·밀도 교정
- **운영 엔진 커밋:** `1045ef57672a93637b628e21227ede7be327e381`
- 새 `tools/visual_layout_audit.py`: SVG의 텍스트 근사 바운딩 충돌, 한 그룹에서의 과도한 플롯 공백, 캔버스 밖 텍스트를 JSON 검토 대상으로 표시. `--strict`에서 선정된 표적 SVG 경고를 실패로 취급. 근사 알고리즘에 오탐/미탐이 있으므로 시각 E2E의 단독 판정 근거가 아님.
- 새 `tests/test_visual_layout_audit.py`: 출처↔눈금 충돌, 촘촘한 날짜눈금, 한 범주 과대 높이, 정상 다중 범주, 정상 간결한 한 범주 총 **5개 회귀**.
- `final_pdf_html_formatting_instruction_final.md` 및 `04B_VALIDATION_RULES.md`: 범례/출처 예약 영역, 단일 범주 높이 적응, 밀집 X축 눈금 조정, SVG 정적 경고 + 실제 PDF 렌더 수동 검수의 분리.
- **W8 자료별 실제 보정**: `W7-VIS-F02`/`F03` 경제정책 평가지표 주석을 눈금에서 분리하기 위해 높이 540→580, 출처 y=513→552; `W2-VIS-F02` 휘발유 날짜 축 밀집 눈금 4개 생략(원자료 13개 값/실제 날짜 그대로); `W6-VIS-F02` Cook 조사 1개 범주의 과대 높이 600→350, 플롯/범례/주석 재배치(D49%, R47% 그대로). 모든 독립 소스 CSV와 `FINAL_REPORT.md` 본문 보존.
- 연구 병합/수정 커밋: `3c5119c36682646a5fd4360610e37bc6d0fe37ab`; GitHub Actions **38190081005 성공**. 수정 당시 보고서 **36쪽·26개 SVG·6개 표**, 시각 검수 기록은 이 디렉터리의 `W8_VISUAL_LAYOUT_REMEDIATION_20261012.md`에 원문 그대로 복사.
- **허용/비허용 경계:** 한 번의 자동 이미지 존재 검사나 CI PASS를 SVG 내부 기하 완전/픽셀 시각 PASS로 과장하지 않음. 실제 렌더 확대 검수와 수치 대조는 별개.

## 변경 2 — Full Report 대장 페이지 시작·큰 여백·빈 페이지 회귀
- **운영 엔진 첫 커밋:** `3f60f9376237496cc30c09a835c14ea5bbbdca8a`
- `final_pdf_report_style.css`의 `.report-section.major-break`를 `break-before:auto`에서 `break-before:page`로 변경. 단, 보고서의 최상위 번호 장에만 HTML 변환기에서 `major-break`를 **opt-in**으로 부여하며 홀짝 강제는 하지 않음. 짧은 보고서·소절에는 일률적 새 페이지를 강제하지 않음.
- 새 `tools/pdf_pagination_audit.py`: PDF 추출 텍스트의 최상위 장 시퀀스·상단 Y 좌표를 hard issue로 검사하고, **본문 30% 이상 미사용**은 원인별 검토 후보로 분류. 정상 장 마지막 공백을 자동 실패로 오판하지 않음.
- 새 `tests/test_pdf_pagination_audit.py`: 장이 페이지 중간에서 시작/정상 새 페이지/누락/정상 장 끝 공백/중간의 그림 밀림 경고에 대한 기본 5개와 이후 무본문 페이지를 찾는 **추가 1개**, 합계 **6개 회귀**.
- `final_pdf_html_formatting_instruction_final.md`·`04B_VALIDATION_RULES.md`: 대장 새 페이지, 제목-첫 문단 묶음, 도표·캡션 분리 방지, 30% 경고에 따른 원인 분석과 실제 재조판을 도입. 36쪽 고정 등을 위해 연구 내용을 임의 축약하거나 축/범례를 읽기 어렵게 만들지 않음.
- **실제 발견/수정의 연쇄:**
  1. GitHub Actions **38191681426 실패**: 연구 브랜치에 예전 CSS가 남아 있던 상태에서 검사기가 대장 시작 위치 10건 오류를 실제 검출. CSS/지침을 최신 `main`으로 동기화.
  2. GitHub Actions **38191718285 성공**: 대장 14개 상단 시작 조건을 충족했지만 43쪽 PDF의 4쪽에 장식용 HR 때문에 사실상 빈 본문 페이지가 생김. 기존 검사에는 이 결함이 빠져 있었음.
  3. **운영 엔진 후속 보완** `297535465be5819323c012d3dd7f3ea33ac8de9b`: 장식용 HR이 대장 강제 페이지 전환과 맞물리면 PDF에서만 생략 허용; 검사기에서 무본문 페이지를 **hard fail**, 회귀 6개로 보완. 원본 Markdown의 HR은 유지.
  4. 연구 PDF 생성기 `tools/export_w8_pdf.py`에서 번호장 `major-break` 지정, 최종 PDF용 장식 HR 제한적 생략, 생성 후 검사 JSON 기록; 운영 업데이트와의 연구 병합 `aeec239729e88841dfd083b146ad6d0732c52b5c`. GitHub Actions **38192002982 성공**으로 최종 **42쪽** PDF 저장.
- **실제 최종 W8 검증 결과:** 본문 장 14/14가 페이지 상단(시작 쪽 4,6,9,13,16,18,22,26,29,33,35,37,40,41), 빈 본문 페이지 0건, 그림 26개/표 6개/캡션 26개/한글 폰트·링크 존재. 전체 42쪽을 이미지 렌더해 접촉시트와 위험 페이지를 확인. 22쪽 남은 약 31.5% 공백은 다음 그래프·캡션의 가독성 보존을 위해 예외로 유지. 다른 여러 장 마지막 페이지의 큰 여백은 새 장 시작으로 인한 의도된 결과.
- 최종 PDF: `exports/Trump_2026_Midterms_Full_Report_20261012.pdf`; 당시 연구 트리 blob `03d759a5b84c15781ee6d61863ff1bff20df2254`, **1,320,566 bytes**, SHA-256 `91bcff97e69f18ca1c8e6305bf844b22e5b783a1b44989fdc58f5087b3f7b80d` (연구 감사에서 기록된 검증값).
- 연구 완성 감사 기록은 이 디렉터리의 `W8_PDF_PAGINATION_IMPROVEMENT_AUDIT_20261012.md`로 **Git blob 자체를 재사용하여 내용 변경 없이 보존**.

## 검증 수준·실패를 역사에서 지우지 않는 규칙
| 관점 | 확인된 증거 | 검증되지 않은 것 |
|---|---|---|
| 변경된 공통 규칙/도구 | 위 3개 운영 commit, 실행 가능한 도구와 테스트 파일 존재, GitHub 원격 HEAD 확인 | 모든 다른 보고서의 자동 미관측 결함까지 제거되었다는 주장 |
| SVG 적응형 배치 | 신규 5개 단위 회귀와 표적 4 SVG 검사 PASS, W8 36쪽의 실제 시각 검사 기록 | 모든 SVG의 서체·변환별 완전한 충돌 부재 |
| PDF 조판 | 신규 6개 단위 회귀와 W8 42쪽 실제 렌더, 14장 페이지 시작, 무본문 0, 자료·캡션 보존 | 저마다 다른 렌더러·인쇄 장치에서의 픽셀 동일성 |
| 조사 내용 | W8 원고/CSV를 이번 조판 개선에서 변경하지 않음 | 2026 정치·경제 사건의 새로운 원출처 전수 재조사 |
| 공백 | 빈 페이지 결함 제거, 22쪽 그림 밀림은 근거 있는 허용 | 30% 이상 공백 자동 삭제 또는 페이지 수 최소화 |

**정본 우선순위:** 이 아카이브 기록 자체는 당시 판단·결함·검증 경계를 재현하는 자료다. 새 실무 작업은 언제나 현재 `main`을 읽고, 연구 W-ID·PDF 변경은 해당 `research/*` 브랜치에서만 별도로 승인받아 실행한다.

## 복원·재검증 명령 (예시)
```bash
git fetch origin main research/20261011-trump-midterms-opinion archive/research-v2-development-20261011
git show 297535465be5819323c012d3dd7f3ea33ac8de9b:tools/visual_layout_audit.py
git show 297535465be5819323c012d3dd7f3ea33ac8de9b:tests/test_visual_layout_audit.py
git show 297535465be5819323c012d3dd7f3ea33ac8de9b:tools/pdf_pagination_audit.py
git show 297535465be5819323c012d3dd7f3ea33ac8de9b:tests/test_pdf_pagination_audit.py
git show e84adae6e7131cfc33105f39d229268fdf696443:W8_PDF_PAGINATION_IMPROVEMENT_AUDIT_20261012.md
git show e84adae6e7131cfc33105f39d229268fdf696443:exports/Trump_2026_Midterms_Full_Report_20261012.pdf > /tmp/w8_20261012.pdf
python -m unittest discover -s tests -p 'test_visual_layout_audit.py' -v
python -m unittest discover -s tests -p 'test_pdf_pagination_audit.py' -v
python tools/pdf_pagination_audit.py /tmp/w8_20261012.pdf --expect-chapters 14 --strict
```
> 원본 archive 커밋 트리에 위 도구가 최상위로 설치된 것은 아니다. 도구·PDF 명령은 각 지정 SHA의 트리에서 실행하거나 경로를 맞춰 사용한다.
