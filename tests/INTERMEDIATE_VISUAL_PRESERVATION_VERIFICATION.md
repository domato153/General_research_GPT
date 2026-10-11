# 중간 조사·시각자료 보존 패치 — 실제 검증 기록 (2026-10-11)

## 기준·대상
- 정본 운영 `main` 시작 HEAD: `868f0df6a0acf1c53f91cb25ca4572b785761324`.
- 역사 개발 증거: `archive/research-v2-development-20261011` (읽기 전용; 과거 감사·최초 실패와 회복·실제 E2E 구분 방식 참고).
- 후보 브랜치: `design/intermediate-visual-preservation-20261011` / 1차 규칙 커밋 `f44ef4f933a47e3777306858db381afd7b227370` / 실물 그림 fixture 커밋 `4635f05ee25eabd4c345e7f1e4b1f44f644a446d`.
- 기존 조사 브랜치 `research/20261011-trump-midterms-opinion`는 근거를 **읽기만** 했고 수정하지 않았다.

## 구현 및 단위 검증
1. `PROJECT_BOOTSTRAP.md`, `02_RESEARCH_PIPELINE.md`, `04_STATE_MANAGEMENT.md`, `04B_VALIDATION_RULES.md`의 앵커를 단회 교체하여 기존 내용을 보존했다. 기존 W-ID·Stage/편집 관문·비저장·CAS·UNKNOWN 경계 유지.
2. 정적 필수 조건 10개: 중요 보고 내용·차트 메타·원본 미확보 구분·Stage6/7 연결·복원·반대조건·E2E 과장 금지·12개 시나리오 존재 → **10/10 PASS (정적 계약만)**.
3. GitHub 실제 쓰기: 운영 `main` 고정 HEAD에서 새 브랜치, base_tree 보존한 트리→커밋→기대 SHA 조건부 비강제 ref 이동 성공. 4개 규칙 파일 + 1개 테스트 계획 문서를 GitHub에서 재조회하여 blob/핵심 문구 확인 → **PASS**.
4. 실물 시각자료: 트럼프 연구 `W1_SURVEY_TIMELINE.md` W1-01의 2025 Gallup 12개 행을 출처로 SVG(표시 점 12개)·CSV(행 12개)·README(그림ID·기간·모집단·축·한계)를 동일 브랜치에 보존 후, **실제 3개 파일 blob 재조회 PASS**.
5. 읽어온 CSV·SVG·연구 W1 행 대조: **정상 12/12 PASS**. 반대시험 ① 7월 승인율 37→39 변조 검출(`w1_mismatch`), ② 7월 SVG 데이터점 삭제 검출(`svg_mismatch`), ③ Y축 설명 제거 검출(`axis_missing`) → **3/3 의도된 FAIL 검출 PASS**.

## 중요한 한계와 실전 후속 검증
- **정적 계약 및 GitHub 자산 왕복은 실제로 PASS**이나, 실제 새 ChatGPT 스레드에서 지시 없이 중간 출력을 자동 저장하는지는 **LIVE MODEL E2E NOT RUN**. 현재 프로젝트에 어떤 첨부 규칙이 실제 주입됐는지도 **UNKNOWN**.
- 원래 ChatGPT UI의 그래프 내부 옵션·픽셀·툴팁을 그대로 회수한 것이 아니라, **확인한 수치로 별도의 SVG를 재생성**한 시험이다. 원래 UI 그림과의 외형 일치는 **UNKNOWN**. GitHub 보존=사용자에게 표시됐음도 아니다.
- no-write 철회, 동시 변경 충돌, 저장 도구 실패, 이전 대화 원문 누락은 **시나리오/규칙 설계만 점검**, 각 실전 오류주입 E2E는 **NOT RUN**. 실제 실패/회복을 소급 합격으로 주장하지 않는다.
- 범위 밖 기존 연구 내용 및 `main`의 일반 조사 모듈에 대한 모든 실제 모델 워크플로 무회귀 검증은 **미수행**. 변경 관련 정상 경로는 정적·실물 파일 시험에서 검증했다.

## 결론
- **STATIC CONTRACT PASS + GITHUB FIXTURE INTEGRATION PASS / LIVE MODEL E2E UNKNOWN/NOT RUN.**
- 새 스레드 실사용 평가 시 `tests/INTERMEDIATE_VISUAL_PRESERVATION_CASES.md`의 IP01~IP12를 사용하고, 특히 최초 사용자 표시 보고서의 고유 내용·그래프와 실제 GitHub blob의 양방향 비교, no-write 및 HEAD 변경 반대시험, 최종 편집 변환을 별도 채점한다.
