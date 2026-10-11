# W7 전체 종합검증 출처·반례·통합·시각자료 확인 (2026-10-12)

## 목적·범위·판정
- 2026-10-12 사용자 명시 W7 조사 지시와 실행 중 연결 단절 후 복구를 기준으로 작성. 신규 최종보고서/Stage5 편집안 승인/선거 결과 또는 승률 예측 아님.
- 기준 근거: 연구 `W1_*`, `W2_*`, `W3_*`, `W4_*`, `W5_*`, `W6_*`, 앞선 `W7_*` 및 승인된 A~E·F(실제 경합지역에 한정)의 실물 자료; 새 통합 정본 `W7_FULL_INTEGRATED_CAUSAL_AND_ELECTORAL_REVIEW_20261012.md`.
- **조건부 완료:** 2025~2026 국정승인 추세, 2026 경제·전쟁·이민·외교·의료/재정·사법·2024 투표층/투표의욕·하원/상원 경합·지도/여론 방법의 경쟁설명과 불리한 반례를 직접 연결. 선거일 이전 실제 득표·기권·선거구 당선·정책별 국정지지 변화의 정밀 인과효과 **미관측/미식별**.
- 이전 W-ID의 정량값·기존 그래프를 업데이트 없이 재활용하는 부분은 **W-ID 기저 검증 상속**이며, 이번 실행에서 2025~2026 모든 기관의 원문을 전수 재검색했다는 뜻이 아니다. 새 수치로 도입한 Pew 경제 정책 책임 인식/이란 평가 관측은 아래 원출처에서 독립 확인.

## 새 독립 근거 3개 SVG/CSV와 출처 대조
| 신규 그림/CSV | 원문 자료 | 값 (자료 내 관측) | 비교단위/주의 |
|---|---|---|---|
| `W7-VIS-F02_pew_economic_policy_attribution_all_adults_2025_2026` | Pew 2026-10-08 cost concerns | 2025-09 better24/worse53, 2026-01 28/52, 2026-07 20/60, 2026-10 19/65 | 미국 성인 전체 정책 결과 인식, 국정승인/객관 경제 효과 아님 |
| `W7-VIS-F03_pew_economic_policy_attribution_republicans_2025_2026` | 동일 Pew | 공화+lean better47/57/42/39 vs worse19/18/28/35 | 공화/lean 성향집단 단면; 같은 사람의 고정패널 개인 변화 주장은 불가 |
| `W7-VIS-F04_pew_iran_war_handling_approval_mar_oct_2026` | Pew 2026-10-08 Iran conflict | 미국 전체 2026-03 37, 10월33; 공화+lean 69→63; 민주+lean9→9 | 정책/전쟁별 대응 승인이지 전체 국정승인이 아님. 두 시점 집단은 별도 표본 |
- 직접 확인한 Pew 문서:
  - https://www.pewresearch.org/politics/2026/10/08/cost-concerns-dominate-as-publics-economic-ratings-turn-more-negative/
  - https://www.pewresearch.org/short-reads/2026/10/08/iran-conflict-remains-deeply-unpopular-as-many-americans-expect-it-to-go-on-for-months/
  - https://www.pewresearch.org/politics/2026/10/08/with-americans-in-a-sour-mood-democratic-voters-are-more-engaged-in-midterms/
  - https://www.pewresearch.org/chart/republican-and-democratic-voters-rate-economy-as-top-voting-issue-in-midterms/
- SVG 자체에 `<title>`, `<desc>`, `data-date/data-series/data-value` 숫자 표기. CSV 4×2 + 4×2 + 6×1 = **22개 수치**를 CSV 순서·키와 SVG 표시 속성으로 비교하고 22/22 일치 확인. W7 Markdown 세 그림 실제 `![](...svg)` 경로로 연결. 웹브라우저별 픽셀 렌더/예전 채팅 UI 원형 **검증 불가(UNKNOWN)**.

## 필수 보고서 동등반영 후보 범위 검사
| 기저 정본 | W7 연결절 | 사용자 선택 Stage5 이후 Full Report 상세형에 반영할 고유 정보 |
|---|---|---|
| W1 세 기관 여론 | §1 | 기관별 전기간 추세·변곡점, 국정 승인과 정책신뢰 구별 |
| W2 경제·관세 | §2~3 | 유가/CPI 결측/실질소득·소비·제조업 반례, 정책 결과 인식 |
| W3 이란/중국/우크라이나/NATO | §3~4 | 사건 전후 시점, 이란·외교 신뢰의 당파 차이, NATO 실제 목표와 미확정 외교성과 분리 |
| W4 국내 이민·법원·재정·의료 | §5 | 추방 목표·ICE 집행 구별, CBO 미래 전망과 2026 실측 분리 |
| W5 2024 검증 투표연합 | §6~7 | GOP 하원77/민주5/미결정13, 전환/기권/의욕 구별 |
| W6 하원/상원 | §8 | 전국 RV vs 37경합 LV vs 실제 후보·상원 5주, 예측/실제결과 구별 |
| 승인 A 선거구 | §9 | 현재 9주 경계·미주리 예외, 2024 경계와 현재경계 동일성 검사 |
| 승인 B 방법론 | §9,11 | 과거 정치 가중 효과와 2026 일률 보정 금지 |
| 승인 C 투표율 | §7,9 | Census CVAP와 Pew House/VEP 계열 분리·2022 참여 반례 |
| 승인 D 자금/후보 | §8~9 | FEC vs PAC/광고, 후보개인 효과 |
| 승인 E 정당대안 | §9~10 | 반트럼프 동기와 민주당 자체 인기/양당 비호감 분리 |
| 승인 F 데이터센터 | §9~10 | 실제 경합지역 에너지 비용 쟁점 한정, 전국 인과효과 과장 금지 |
- 연결 표는 연구→W7 추적이며 **최종 `FINAL_REPORT.md` 실문장에 동등 반영된 증거는 아님**. Stage5 사용자 상세/통합/부록/제외 편집 선택 후 Stage7 최종원고 양방향 감사 필수.

## 잠재 결함·재검증 조건
- **A(해당 강한 주장을 쓰려 할 때):** 2026-10 미확정 외교합의를 양측 실행 완료라 쓰거나, Missouri 폐기 지도 그대로 2026 하원 결과로 계산하거나, CBO 장기 전망을 현재 실측·의석 예측으로 변환하려면 별도 근거 필수. W7에서는 이 주장들을 **보류/제한**해 범위 내 완료 가능.
- **B(후속 자료 가치):** Siena/개별 경합주 topline PDF/MoE, 개별 2026 하원 district 현 지도 2024 표 재집계, 최신 FEC 개별 캠페인 잔고, 데이터센터별 전력비 인과, 미국내 새 외교법원 사건 직접 영향. 새 W-ID 무단 발족/435구 전수 명령 불가.
- **E(현재 자료 한계):** 사건별 트럼프 승인율 감소의 독립 기여 %p, 2026년 11월 실현 turnout/하원·상원 의석. 단일 날짜들 사이 상관을 통제된 인과분석으로 부르지 않는다.
- **인계·최종화 주의:** W7 조건부 완료와 W8 미착수를 동시에 보존. 마지막으로 사용자에게 W7 가설 비교·반례·추가 한계를 설명하고 **Stage5 사용자 수록/종료 준비 관문**을 제안. 사용자 승인 없이 `FINAL_REPORT.md` 또는 PDF 작성/최종 게시 금지. 본 감사도 실제 파일/브랜치에 커밋·재조회한 경우에만 '원격 보존 완료' 표현 허용.
