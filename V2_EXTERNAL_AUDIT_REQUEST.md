# 외부 Temporary/Unpersonalized ChatGPT에 그대로 보낼 감사 요청

한국어로 답하라. 범용 딥 리서치 엔진 v2의 규칙 개선 **후보안**을 독립적으로 감사해줘. 작성 모델이 제시한 검사 점수를 믿지 말고 실제 GitHub 원문과 변경 내용을 보고 결함을 적극 찾아줘.

공개 저장소: https://github.com/domato153/General_research_GPT
변경 전 BASE: cd64bef326544cacc0dc05fe6f65d9e1bd318fc0
변경 후보 CANDIDATE: c9f8b9a52eab43e24f322e19da03e3006504a206
실제 원문 비교: https://github.com/domato153/General_research_GPT/compare/cd64bef326544cacc0dc05fe6f65d9e1bd318fc0...c9f8b9a52eab43e24f322e19da03e3006504a206
자료 폴더: https://github.com/domato153/General_research_GPT/tree/audit/v2-e2e-hardening-20261010

**먼저 읽을 파일:** V2_EXTERNAL_AUDIT_HANDOFF.md. 전체 이슈는 V2_FULL_ISSUE_INVENTORY.md(E01~E22), 전체 기존 시험은 V2_TEST_RESULTS.md(§§1~48), 변경 설명은 V2_CANDIDATE_CHANGE_SPEC.md, 자기 비판은 V2_SELF_REVIEW_AND_LIMITATIONS.md, 자체 검사는 V2_BEFORE_BASELINE_REPLAY.md·V2_BEFORE_AFTER_STATIC_VERIFICATION.md·V2_SCENARIO_GATE_WALKTHROUGH.md, 이후 독립 E2E 계획은 V2_E2E_PRE_POST_PROTOCOL.md, 재현용 인위적 자료는 V2_AUDIT_FIXTURE.md야. 해당 원본 규칙 파일 7개와 수정하지 않은 공통 규칙도 직접 비교해줘.

**핵심 목적:** 사용자는 내부 Stage·W-ID·GitHub 명령·검수 체크리스트를 몰라도 **짧은 일상어로 조사 의향·방향·진행·최종보고서 준비/완성을 요청**할 수 있어야 한다. AI는 중요한 방향·검증 방식·편집 선택을 먼저 제안하고 사용자 선택을 존중하되, 실제 출처·반론·누락·한계를 자율 검수해 확정·보존/채팅 전달의 권한을 지켜야 해. 불필요한 승인과 과도한 검색·중복 검수도 실패야.

**독립 감사할 항목:** (1) 초기 C1~C3/기존 계획추적 PARTIAL, 중간 C6~C9 선제 선택 부족·질문 분모 불일치·원문 판본/상태 오류, 최종 C10 감사 FAIL·C13 편집 미제안 FAIL·C14 반론 누락 PARTIAL, 과거 외부 H1~H3/M1~M3/L1~L2를 **빠짐없이** 검토. (2) 후보의 7개 수정 규칙이 문제를 진짜 해결하도록 설계됐는지, 불필요한 중복·모순과 새 실패 경로는 무엇인지. (3) 후보 규칙의 안전/모호성/새 스레드 복원·주입 SHA·권한/데이터 보존의 가능성과 한계. (4) 문서 정적/모의 검증과 **새 모델 실사용 E2E의 차이**, 독립 변경 전/후 실제 시험을 실행할 최소 계획.

**절대 주의:** 동일 26 정규식 검사 13→19, 작성자 자신이 만든 30 소스 전이 조건 8→30은 **문서·모의 검사이지 실제 ChatGPT E2E 결과가 아님**. 과거 실제 연구 출발 SHA와 새 후보의 주입 SHA 일치는 증명되지 않았어. C10·C13 최초 FAIL과 C14 최초 PARTIAL은 뒤의 회복 PASS로 지우지 마.

**출력 요구:** 먼저 조건부 승인/수정 후 재감사/반려 판정과 이유. 이어서 E01~E22의 문제별 근거·후보 대응·미해결·P0/P1/P2, 실제 수정이 필요한 문장/위치와 최소 패치, 기존 장점의 회귀/오버헤드 위험, 추가 블라인드 정상·부정 테스트, 새 스레드 T06-R 및 실제 변경 전/후 모델 E2E 합격선, 운영 main 승격의 GO/NO-GO를 보고해줘. 실제 보지 못했거나 실행하지 않은 것은 NOT VERIFIED / NOT TESTED로 표시하고, 문서에 없는 내용을 추측으로 채우지 마.

**실행 권한:** read-only 감사다. GitHub 파일·main·실제 연구 브랜치를 수정하거나 배포하지 마. 감사자에게는 분석용 상세 자료를 보여줘도 되지만 **피시험 모델에게 장문 정답·체크리스트를 직접 주어 자율성이 좋아졌다고 판정하지 마**. 접근 제한이 있다면 정확히 어떤 파일·도구가 막혔는지 보고해줘.
