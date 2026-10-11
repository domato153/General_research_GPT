# W6-B — 2026 중간선거 여론조사의 방법·역사 편향·해석 민감도
기준 2026-10-12 KST. 사용자 승인 2안(B). W1·W5·W6 원자료에 **방법론 검증 오버레이**. 단순한 역사 오차의 2026 기계적 보정 금지.

## 공식·조사기관 방법론 근거
- [Pew Research Center 2026-09-16 연구](https://www.pewresearch.org/methods/2026/09/16/weighting-polls-on-party-affiliation-and-past-vote/): 2024 미 전국 여론조사 약 **70%**에서 정당/이전투표 선택을 가중치에 사용. Pew 내부 2020·2024 사후 표본에 정치 가중치 적용 시 후보별 평균오차 **약 1~2%p 감소**, 후보간 차이는 **약 2~3%p 개선**. 이 값은 **2026년 민주당 지지율에 +/− 보정할 수 있는 공식 오차 수치가 아님**.
- [Pew 가중치 한계 FAQ](https://www.pewresearch.org/methods/2026/09/16/faqs-about-political-weighting-in-polling-and-its-limitations/): 정당 가중치는 비응답 편향을 줄이는 데 유용하지만 동일 정당 내 응답자 편향을 완전히 보정하지 못함. 시대에 뒤처진 정당 분포로 강제 가중하면 새로운 오차 발생. 정치 관련 질문과 개인 경제상황 질문은 가중 효과가 다를 수 있음.
- [Pew 2026 3가지 방법 비교](https://www.pewresearch.org/methods/2026/09/16/3-ways-to-correct-a-polls-political-balance-party-affiliation-past-vote-and-voter-file-information/): 정당 자가식별, 과거 투표 회상, 유권자명부에 의한 정당 식별/투표 이력. 각 방법의 장단점·측정누락 집단이 달라 표본을 '모두 정치 가중치 사용'으로 동질화할 수 없음.
- [Pew 2026-10 전국 조사](https://www.pewresearch.org/politics/2026/10/08/midterm-vote-preferences-by-race-and-ethnicity-age-and-other-demographics/): Sept28–Oct04 미국성인 전체 n=5,062·하원 지지 등록유권자 n=3,917. 전국 민주44/공화36은 등록유권자 **현 지역구 후보(대부분 실제 이름 표기)** 선호. 성인 전체 대통령 승인율30과 분모 다름.
- [Cook 2026-09-17 경합지](https://www.cookpolitical.com/analysis/survey-research/battleground-district-project/new-battleground-district-poll-shows): 37개 경쟁지역의 **LV n=1,052**(9/8~11) 민주49/공화47, ±3.02%p는 묶음 표본 수준. 단일 1곳의 격차를 ±3.02로 검증할 수 없음; 선택된 경합지 평균을 435석 대표 표본으로 취급하지 않음. SMS-to-web/온라인 패널, D/R 양측 조사업체 공동 참여.
- [Pew 2026 2024·2022 검증된 투표 이력](https://www.pewresearch.org/chart/voters-who-are-highly-engaged-in-midterms-are-particularly-supportive-of-democratic-candidates/): 전체 RV 민주44/공화36, 극도 투표의욕 RV 민주59/공화35, **2022·2024 양쪽 실제 투표 이력 RV** 민주47/공화41. 의욕과 검증된 실제 과거 참여는 서로 다른 selection filters. 높은 의욕 응답층이 실제 유권자 구성을 확정하지 않음.

## 종합 차이와 검사 체크리스트
| 결과 | 조사 집단 | 조사 시기 | 비교 오류 |
|---|---|---|---|
| Pew 전국 민주44/공화36 | RV, 전국 | 2026 09/28~10/04 | 전국 RV를 경합 LV 의석으로 환산 |
| Cook 경쟁지 민주49/공화47 | 37곳 LV | 2026 09/08~11 | 37곳을 435구 전수 대표라 오인 |
| Pew 의욕 극도 민주59/공화35 | 등록유권자 중 높은 자가 응답 의욕층 | 2026 09/28~10/04 | 실현된 투표율 또는 정확한 실제 LV라고 간주 |
| Pew 2022+2024 검증투표자 민주47/공화41 | 등록유권자 중 검증된 두 선거 투표자 | 2026 09/28~10/04 | 반드시 2026 투표할 사람으로 간주 |
- **실증하지 않은 민감도 계산을 실측 데이터로 표현 금지**: 민주당 우세에 임의 2~3%p/과거 Trump 오차를 빼서 '보정된 2026 승률' 창작 금지. 민감도는 별도 가상 시나리오로만 명시해야 하고 오차의 상관관계까지 필요.
- **B 가치**: 현재 W6 표본 설계의 비교 불가·예전 편향을 분리할 수 있음. **미완료**: 각 Sena NYT/Siena 주별 top-line PDF/MOE, 2026 실제 사후 오차, 하원 개별지구별 이질 표본. 특정 후보 '95% 승리' 같은 정량확률 추가 금지.
