# W6-A — 2026 하원 선거구 재획정·의석 구조 감사
기준 2026-10-12 KST. 사용자 승인 2안(A). W6의 전국 여론과 지역구·의석 해석에 대한 **구조적 오차 방지**. W7 전체 종합판정 전.

## 독립 원문/데이터와 실제 판정
- [미국 인구조사국 120th Congressional Districts, 확인 2026-10](https://www.census.gov/programs-surveys/decennial-census/about/rdo/congressional-districts.html): 2026년 실효적 새 경계 주는 **9개**: Alabama, California, Florida, Louisiana, North Carolina, Ohio, Tennessee, Texas, Utah. **Missouri는 2026-09-23 연방대법원 조치**로 바뀐 지도를 적용하지 않고 2022/2024 경계를 유지. 인구조사국의 일부 기존 120th 파일은 폐기된 미주리 지도로 먼저 생성되어 2026-10-07까지 block equivalency 파일은 다시 제작, TIGER/Line GIS 계열은 이후 별도 갱신 예정. 지도 '처음 제출' 10주와 '실제 적용' 9주를 구분.
- [Cook PVI 설명](https://www.cookpolitical.com/cook-pvi): 지구/주의 2020·2024년 양당 대선 득표를 전국 득표와 상대 비교하는 **구조적 당파 성향** 지표. 선거구별 새 경계에 따른 2024 대선 결과를 **2026 현행 경계로 재집계한 것**만 현재 PVI에 활용. 2024 당시 옛 경계 득표를 새 선거구 1:1로 매핑하는 오류 금지. Cook의 선거 판정 등급(Lean/Toss-Up)은 PVI와 다름.
- [Cook 2026-09-10 경계 영향 전망](https://www.cookpolitical.com/analysis/house/redistricting-analysis/2025-2026-redistricting-tracker-how-many-seats-could-flip-0?check_logged_in=1): 당시 새 경계만의 공화당 순증을 **약 4석**으로 추정. **미주리 2026-09-23 결정 이전 전망**이므로 2026-10-12 유효한 순증 확정값 또는 W7 결과로 소급 인용 금지. 법원판결/지도 확정 시점별 산출값 재계산 필요.
- [Cook 2026-09 경합 37선거구 LV 조사](https://www.cookpolitical.com/analysis/survey-research/battleground-district-project/new-battleground-district-poll-shows): 37곳 민주49·공화47, 2024년 Trump 평균 +5라는 수치는 *Cook가 선택한 37개 선거구 묶음*에 해당. 전체 하원435석이나 같은 개인의 2024→26 선택 변화 수치 아님. 지역구 경계·교체를 확인하기 전 임의 7%p 이동 추정 금지. 2026-04 36개 지구와 2026-09 37개 지구 비교는 표본 지역구가 달라 선택편향 존재.

## 결론과 결함 분류
- **A(현재 의석 전망과 지도 간 숫자 대응 시)**: Missouri 구버전 지도를 활용하거나 선거구 이전 경계의 대통령 득표를 같은 번호 현 경계 득표로 대응하면 구조적 오류. 해당 비교는 차단·정정한다.
- **B(자료 강화)**: 각 9개 주 새 경계 GIS/2024 재집계·PVI 전체표 대조 및 Cook 2026-10 최신 순의석 추정 별도 확인. *이번에는 원문 변경 주와 기준·시차 감사만 완료*; 435구 재계산이나 최신 net seat 모델은 미시행.
- **정상 한계(E)**: 전국 민주 우세가 개별 435구 의석으로 자동 환산되지 않음. 후보·현역·turnout·재획정은 다른 요인.
- **실질 종료 범위**: 경계가 바뀐 주·미주리 법적 예외, 2024 대비 새 지구 비교의 조건, Cook의 분석과 실현 결과 구분은 충족. 추가로 전체 GIS 모델을 자동 필수 연구로 확대하지 않는다.
- **시각화**: 수치보다 최신 경계 여부와 예외 문서가 중요한 항목이므로 무근거 지도·정량 순의석 차트를 생성하지 않는다.
