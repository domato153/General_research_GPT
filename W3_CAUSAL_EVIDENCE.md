# W3_CAUSAL_EVIDENCE — 한국·미국 충전 인프라 → 전기차 보급 인과효과 1차 검증

- 기준일: 2026-10-11 (Asia/Seoul).
- 기존 조사 `research/20261011-kr-us-ev-charging-adoption`, 고정 출발 `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`.
- 사용자 요청: 이전 A안 W1 자료 보완 다음 인과관계 부분도 조사. W3 실증 원문/초록 비교를 **선행 진행**. W1 부분완료, W2 미착수 그대로. W4 원래 계획의 독립적인 반례 전수검토는 미완료.
- 본 파일은 **기존 논문 추정결과 검증**, 직접 신규 패널 구성·회귀추정·계수 재현을 수행하지 않음.
- 선정: 각국 직접 충전 접근성/설치/규제 → EV/BEV 신규등록·판매의 관측적 또는 준실험적 연구 우선. 결론의 반대 방향, null, 대상 EV 유형 및 정책/설치 효과 구분.

## K-01 한국 Kim·Woo·Choi, 2026 [working paper]
- `Charging Ahead or Catching Up? Causal Evidence on EV Adoption and Charger Expansion in South Korea`, KDI School Paper DS26-01, SSRN 6138466, last revised 2026-01-28. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6138466
- 2023–2025 월별 한국 EV 등록·충전기 설치; IV 회귀로 동시성과 역인과 처리 시도.
- 저자 보고 결과: **완속 충전기 양(+)의 유의한 효과, 급속 음(-)의 유의한 계수**. 완속 양의 효과는 도시·고소득 시군구에 집중.
- 근거 범위: SSRN **원저자 초록** 대조. 전체 본문 PDF/첫단계 F통계/IV 배제제약 및 실제 수치 계수·표준오차 **미열람**. 약한 IV, 정책/지역교란, 계수 시간선행 해석 검증 전. 급속이 BEV 수요를 '감소시킨다'고 확정 금지.
- 중요: 저자들은 급속의 음의 부호를 수요 대응/기존 설치의 변화와 연결하지만 이는 경쟁 설명으로 보존.

## K-02 한국 노수현·김경아, 2026 [학술지, KCI 후보]
- `아파트 내 충전 인프라 의무화가 전기차 보급에 미치는 효과: 연속 처치 이중차분법을 중심으로`; 글로벌융합연구학회지 5(1), 334–348, DOI 10.57199/jgcr.2026.5.1.334. https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003318538
- 2022-01 100세대 이상 기축 공동주택 주차면의 2% 충전시설 의무화 조치, 지역의 과거 기축 아파트 수에 기초한 **처치 강도**; 시·군 패널, continuous-treatment DID.
- 저자 초록: 고노출 지역에서 정책 이후 **전기차 신규 등록이 통계적으로 유의하게 증가**; 제주 제외/처치강도 정의 변경에 강건. 구매 보조금 양의 상호작용. 고령화율·인구밀도 이질성.
- 핵심 한계: 정책 노출의 intent-to-treat 효과 ≠ 실제 충전기 포트 한 개의 증분 효과. 정책 시행일과 실제 의무 설치·집행 시차, 아파트 비중과 지역의 다른 추세/보조금/건설 변동의 상관, 평행추세 및 이벤트스터디 결과 **초록만으로 미확인**. KCI 후보 학술지/독립 검증 부족. 초록에 추정계수 및 신뢰구간 미제시.

## U-01 미국 Lou·Niemeier, 2026 [Nature Communications, 전체 HTML 원문 확인]
- `EV-ready building codes and electric vehicle adoption`, 2026-05-07, Nature Communications 17, 6150. https://www.nature.com/articles/s41467-026-72664-6
- 2019-01-11 Maryland Howard County EV-ready building code, other counties as controls; 1999–2024 MD EV records covering 75,097 vehicles; census block SDID.
- 발표: 정책 도입 뒤 연평균 census block당 EV +0.25대 (저자 해석 pre-policy 대비 +28%; **census block당**이지 미국 전국 신규차 점유율 아님), BEV별 +0.253대/블록/연; PHEV +0.047대/블록/연. 효과 고소득·단독주택 지역 집중.
- 중요한 방법 한계 **본문 명시**: 표준 DID의 **평행추세 검정 통과 실패**, 따라서 SDID 주분석; 정확한 최초 EV 등록일 부재로 차량 출시일/연식 및 사회관계망 최초 영상 리뷰일 등으로 등록시점 대체. 2019–2023 31%라는 숫자는 저자 해석이며 국가 일반화 금지; 교란/집행 차이 존재 가능.
- 시사: 정책 효과 (EV-ready wiring/construction readiness) ≠ 공공 충전소/포트 추가 효과. BEV/PHEV 분리 및 실제 효과 크기 정의 유지.

## U-02 미국 Gifford·Barbier, 2026 [Energy Policy]
- `The role of charging infrastructure and income on electric vehicle adoption`, Energy Policy 211 (2026) 115098. DOI 10.1016/j.enpol.2026.115098. https://www.sciencedirect.com/science/article/pii/S0301421526000327
- Washington 2019–2023 county panel, BEV/PHEV 등록밀도 및 새 공공 충전시설, 소득·설치기술 상호작용, 지역 고정효과. 저자 원문 공개 텍스트 확인.
- 결과: 공공 충전시설과 BEV 밀도의 양의 효과는 **고소득 카운티에 집중**, DCFC 효과 > Level 1/2, PHEV 유의하지 않음; reverse causality / lag / placebo 검증에서 본문이 효과 방향 지지 주장.
- 해석: 관찰 패널+고정효과의 잔여 시간가변 교란 및 충전사업자 입지 선택은 완전히 소거할 수 없음. registration density 결과는 신규 flow와 다름. 한국 K-01의 완속 우세와 부호가 다르지만 기간·지역/기술/지표·설계가 달라 명백한 모순으로 단정 금지.

## U-03 미국 Lee·Nilsson, 2025 [Journal of Transport Geography]
- `Estimating the effect of a state-level charging infrastructure funding program on plug-in electric vehicle adoption`, Journal of Transport Geography 129, 104406. DOI 10.1016/j.jtrangeo.2025.104406. https://www.sciencedirect.com/science/article/pii/S0966692325002972
- Maryland의 AFIP 충전 인프라 재정 지원 2011–2021 주 패널, synthetic control 및 공간/시점 placebo/leave-one-out.
- 저자 보고: BEV, PHEV 모두 긍정적 관측 관계이나 **공간 placebo 검증에서 PHEV 정책 효과가 더 신뢰도 높고 BEV는 제시적(suggestive) 효과**라고 분리. 합산 PEV가 전부 BEV라는 주장 금지.
- 재정 지원 프로그램 효과 ≠ 실제 충전소 1기 설치의 물리적 증분 효과. 완전한 원문 표/효과 % 및 대조군은 추가 확인 필요.

## U-04 미국 Afzal·Hawkins, 2024 [Energy Policy, 반례]
- `Electric vehicle and supply equipment adoption dynamics in the United States`, Energy Policy 193, 114275, DOI 10.1016/j.enpol.2024.114275. https://www.sciencedirect.com/science/article/pii/S0301421524002957
- 2012–2021 미국 카운티 EVSE 위치, Experian EV 등록(2년 간격 등의 stock) 자료; 비선형 Granger와 GPS+GAM dose-response.
- 저자 결과: EV 설치/보급의 **양방향 선후관계**, 높은 설치율 구간에서 PEV 보급 반응 약화; 충전시설 투자만으로 PEV 구매 증가 보장 안됨.
- Granger 유의성은 교란 없는 인과적 개입 효과의 증거가 아님. generalized propensity score는 **관측 교란에 대한 식별가정** 의존. PEV에는 BEV와 PHEV 포함.

## U-05 미국 Kaufmann·Newberry·Xin·Gopal, 2021 [Nature Energy, null]
- `Feedbacks among electric vehicle adoption, charging, and the cost and installation of rooftop solar photovoltaics`, Nature Energy 6, 143–149, DOI 10.1038/s41560-020-00746-w. https://www.nature.com/articles/s41560-020-00746-w
- Massachusetts 월별 EV 구매와 AFDC 공공 충전시설+주택 태양광 도입, Granger causality test.
- 저자 결과: 충전시설 설치 → EV 구매 및 역방향 모두 **그랜저 인과성 유의한 증거 미발견**. 원자료/코드 OpenBU 공개 https://open.bu.edu/handle/2144/41462
- '유의미한 결과 없음'은 **효과가 0인 것이 확인됐다**는 말이 아님. 그랜저 방향성 테스트가 정책 설치의 인과효과와 같지 않음; Massachusetts와 시기 특이성.

## U-06 미국 Li·Tong·Xing·Zhou, 2017 [JAERE, 구조모형]
- `The Market for Electric Vehicles: Indirect Network Effects and Policy Design`, J. Assoc. Environmental and Resource Economists 4(1), 89–133. DOI 10.1086/689702. https://www.journals.uchicago.edu/doi/10.1086/689702
- 미국 353 metropolitan statistical areas 2011–2013 분기 EV 판매와 충전시설 수, 전기차 수요↔충전시설 투자 양면 시장의 간접 네트워크 효과 구조모형.
- 저자 counterfactual: 동액 예산 충전시설 보조가 구매세액공제보다 전기차 보급 확대에서 **2배 이상 효과적일 수도** 있음. 이 숫자는 **2011–2013 조기시장 구조모형의 정책 시뮬레이션**이지 2018–2025 관측 전국 정책실험의 효과나 충전기 10% 설치 탄력성 아님.

## U-07 미국 Gbeda·Takumah·Kumah, 2026 [SSRN working paper; 서로 다른 판본 주의]
- `Effects of Charging Infrastructure on Electric Vehicle Adoption and Transportation Emissions in the United States: A Panel Analysis`, SSRN paper ID 7306323 (posted 2026-08-18): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7306323
- 50개 주+DC 2013–2025, FE와 state-level ZEV 의무 정책 staggered DID. FE에서 충전시설 수가 EV adoption과 양의 **연관**; 포트보다 station location의 효과가 크고, private 시설과의 관계가 강함.
- 핵심 해석 함정: 논문의 staggered DID는 **ZEV 판매 의무 도입 정책 효과**이며 **충전기 설치의 독립 인과효과가 아님**. 이전 판본으로 ID 6146447/6223755 존재; 사양 변경에 주의. 사전공개, 인과 단정 금지.

## 방법별 실증 해석과 상충 반례
- 이론적 수요 경로: 더 가까운/신뢰할 수 있는 충전 접근성 → 충전 부담 감소 → 구매 가능성 증가. 공급 경로: EV 보급 증가/수요 예측 → 설치 사업자 진입. 이들은 동시에 존재 가능.
- 가설 H_A 충전기 설치가 BEV 구매를 유발함: K-02, U-01 준실험 정책효과; K-01 IV 완속 양; U-02 FE 긍정.
- 경쟁 가설 H_B 보급수요·소득·정책 등이 설치와 구매를 동시 유발함: U-04 양방향, U-05 그랜저 null, K-01 급속 음, U-02 고소득 이질성. U-07 ZEV mandate는 직접 정책 교란 변수.
- 정량 비교의 단위: 전기차 **신규등록 flow** vs 누적 보유 **stock**; PEV 합산 vs BEV 단독; 공공 충전소 **station locations** vs 단일 기 **chargers** vs 포트 **EVSE** vs EV-ready 사전 배선; 정책효과 **ITT** vs 실물 설치 증분 효과. 같은 표에서 공통 %로 계산 금지.
- 연구 기간 이질성: 2011–2013 초기시장, 2012–2021 카운티, 2019–2023 워싱턴, 2023–2025 한국, 2026 발행 연구의 정책 시행 2019/2022. 최신 2026 문헌 ≠ 2026 등록 효과.
- 효과 추정의 핵심 미식별: 한국/미국 공통 2018–2025 BEV 신규등록 지역 패널 + 일관된 공공 EVSE 가동/설치 지역 패널 부재. 본 조사에서 '충전기 10% → BEV 몇 %'를 직접 추정/재현하지 못함.

## 임시 판정
1. '충전시설 접근성 증진 정책이 BEV 구매·등록을 늘릴 수 있다'는 **상당한 조건부 근거**가 있음; 일반적인 전국 공공충전기 수 증가 효과는 **미확정**.
2. 단순 전체 충전기 숫자 확대의 한미 공통 인과 탄력성 수치 **추정 불가**. 양국 동일 방향/충전기 유형 최적화는 현재 근거로 불가.
3. 한국 K-01 급속 음 추정은 급속 설치가 EV 수요를 떨어뜨린다고 보장하지 않음; 미국 U-02 급속 양 추정과 설계·분모·환경이 다름. 조사 결론을 바꾸는 중요한 불일치로 추적.
4. 메릴랜드 U-01 +0.25대/블록/연과 +28%는 건축 규제 **지역 한정** 정책효과, 한국 충전기 10% 증가의 정량 계수로 사용 금지.
5. W3 = **조건부 부분 완료** (기존 연구 기반 식별 메커니즘·핵심 반례 검증; 직접 추정 미수행). W4는 일부 연구를 선행 리뷰했지만 계획의 독립적 반론/원문 전수검증 **대기**. W1 부분완료, W2 대기.

## 다음 계획 및 결정
- W2 실제 변화: 한국의 지역별 *신규* BEV 등록+전체 운영자 EVSE 설치 시계열, 미국 주별 신규 BEV 등록 flow 데이터를 직접 수집·정의 확인. W1 접근 실패는 명시하고 가능한 공식 집계로 범위를 좁힐 경우 먼저 사용자 결정.
- W3 표적 심화: K-01의 IV 도구와 1단계 F·배제제약, K-02의 사전추세/신뢰구간/집행시차, U-01의 날짜 대체·SDID 진단, U-02의 변수 시차 및 모델, U-03의 SCM placebo와 BEV/PHEV 결과를 원문 표까지 확인.
- W4 관련: 위 연구에 불리한 독립 연구/인과적 상충을 병렬 추적하되 선행 리뷰를 W4 전체 완료로 표시하지 않음.
