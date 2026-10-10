# W04 — AI의 직종·연령·경력별 영향: 신입 입직 vs 기존 근로자 이탈
기준일: 2026-10-10 / 기준 커밋 `fb22fe86834893e607072b41885277d29cfc57fc`
브랜치: `research/20261010-ai-employment-kr-us-1538-fb22`
상태: **W04 조건부 완료**, 한국·미국 1차 자료/행정·공고/기업설문/반례 확인. AI 고유 인과량 미식별. W05~06 미착수.

## 경계/방법
- 취업자(stock), 공고(postings), 실제 신규 입직(hires/starts), 총 이직(separations), 자발적 퇴사(quits), 해고(layoffs and discharges), 퇴직 후 미충원(backfill reduction), 회사의 AI로 인한 감원·채용 자체보고는 모두 다른 지표.
- 연령(한국 15~29/20대, 미국 22~25/22~24) ≠ 경력(한국 소프트웨어 '3년 미만/이상') ≠ 신규졸업자 vs 전체 구직자. 모집단 다른 퍼센트 합산·직접 비교 금지.
- QWI separations는 자발퇴사/비자발 퇴직을 나눌 수 없다. 이직 총건수 감소=해고율 감소로 단정 금지.
- QWI hires 초기 9%는 고노출 산업 상대 변화, Stanford -19%는 비교군 고용수준 상대격차, Census 대졸 -5%p는 취업 확률의 회귀조정 차이, KLI -16.1%p는 채용공고 중 신입 비중 변화, NY Fed 설문 15%,4%는 AI 도입 기업 중 업체응답 비율. 모두 서로 더하거나 평균하면 오류.
- 미국 Census QWI는 민간 산업×주 그룹에 AI **노출도** 매핑이며 산업 안 직무 실제 사용/도입 정도를 직접 관측하지 않는다.
- 한국 지역별고용조사→취업자, ICT실태조사→경력구간별 개발 인력, 민간 채용공고→수요 추정, 기업 AI 사용 실태조사→경영응답. 서로 구분.

## U1 미국 Stanford Digital Economy Lab 2026-08-12 개정, 2026-09-23 dashboard 재검토
원문: https://digitaleconomy.stanford.edu/news/canariesaug26/
최신 대시보드: https://digitaleconomy.stanford.edu/project/indicators/canaries-dashboard/
- ADP 급여자료 기반. AI 노출 직종 22~25 고용 비교군 추세 대비 -19% (2026-06 기준), 해당 연령 AI 노출 상위 2 quintile 2022-11~2026-06 절대 고용 -11%, 낮은 3 quintile 같은 나이 +10%. 2025 중간판 -15%와 구분.
- 메커니즘은 **신규채용 감소가 주된 경로**, 증가한 separations 아님. experienced workers 같은 노출 수준에서 비슷한 고용 격차가 없음.
- 자동화 용도 쏠린 직업에서 청년 고용 감소 집중; 증강 용도에서 유지/증가. 2026-09 대시보드: early career software developers, customer service reps 크게 감소; low-exposure home health aides는 증가; 26~34세까지 일부 완화된 차이가 있음.
- 단, 노출 직군의 교육 통제 격차 축소, 사전추세 존재, 표본대표성/기업 내 추세 통제 시 사양 민감성. 국경제/모든 신입 고용이 19% 감소나 AI 단독 해고 19% 주장 금지.

## U2 Census Tucker CES-WP-26-27 (2026-04)
HTML: https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html
PDF: https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-27.pdf
- QWI 행정자료 22~24세, 산업-주 AI노출 최상 quintile, 고노출 내 청년 신규 입직 **ChatGPT 직후 비교그룹 대비 약 -9%**, 10분기 후 regression adjusted 고용 -12%; 미보정 indexed series의 -15%/15만 초과 잃었다는 서술과 혼합 금지.
- 원문 p15(Fig8 주변): early career **총 separations 건수** 2025Q1 기준 4분기 reference보다 -11.5%; separation rate 감소는 그보다 약하며 전체 고용 stock 감소 영향을 받음. *자발적/비자발적 이직 구분 불가능*.
- 기업 확장에 따른 job gains (=확장고용에서 새 직원 유입)은 post-2022 초기 4개 분기 -9.1% (비교기간 기준), 기존 직원 대체 채용(backfill hires) 즉각 약 -9%, 후반 최근 4개 분기는 약 -15%. 반면 job losses는 점진적 감소, 구조적 job destruction 급증 증거 아님. Job gains/job losses는 회사 규모 순변화와 채용/이직의 분해이지 실제 각 근로자 해고/순입직의 1:1 인과기여량 아니다.
- 채용 rate는 고용 모수가 감소함에 따라 2025초 이전 비율에 가까워졌지만 채용 **절대 건수**는 회복되지 않았다는 저자 해설.
- 2020년 팬데믹 이후 업종·연령별 사전추세 차이, 재택근무/교육 수요 변화·금리 영향 일부. 생성형 AI 단독 인과효과 미식별.

## U3 2026-09 신작: Orr, Tucker, Warren, Census CES-WP-26-56
https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-56.html
- 대학졸업자 행정자료, **AI 노출 상위 10% 전공**의 회귀조정 *졸업 후 최초 고용 확률* -5%p, *완전분기 첫 소득* -13%. 이는 AI 노출 전공 취업자의 상대 변동으로 미국 전체 신규졸업자 고용 -5%p/전국 평균 임금 -13%가 아님.
- 소득 감소 약 절반은 동일 산업 내 소득 하락, 나머지는 음식점/소매 등 저임금 산업으로 이동한 구성효과. 졸업 후 시간이 흐를수록 약해지나 노출 상위 전공은 차이 남음.
- 신규채용 진입경로 직접 증거 강화. 전공별 AI노출은 실제 도입 아니며 노동공급/다른 전공별 쇼크를 완전히 배제 못 함.

## U4 뉴욕 연준 AI 사용 기업 지역 표본, 2026-09-01
https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/
- 2026.08 New York & northern NJ 지역 사업체 설문: 61% 서비스, 51% 제조업 AI 사용.
- **AI 사용하는 서비스 업체 응답 기업의 비율**: 지난 6개월 AI 때문에 채용을 덜함 약 15%, 직원 해고 4% (2025년 1%), AI 활용 위해 채용 늘림 13%; 1/3 초과 서비스 업체 기존 직원 재훈련. 제조업 AI 해고 응답 0. 직원 중 실제 AI 사용 중위 비율은 서비스17%, 제조7%.
- AI 사용자 업체 응답 비율, 직원 수 비율·국내 전체 업체 비율·AI 효과 취업자 순수 변화량이 아님. 설문에 보고한 AI 원인이 기업 자기인식. 표본은 뉴욕·뉴저지 북부 지역, 미국 전국 대표 불가.
- 질문의 "fewer hires than without AI"는 기업 자체 counterfactual로서 **실제 채용의 역추정치**, 감원/해고와 다름. "13% hired more"와 "15% hired fewer"는 업체비율로 합산하여 순고용 -2% 계산 불가.
- BLS JOLTS https://www.bls.gov/news.release/jolts.t05.htm Aug 2026 layoffs+discharges ~1.641 million, 1.0%, Aug 2025 1.832million/1.2%. **JOLTS는 AI 노출과 직종/연령별 감원분을 식별하지 못함**. 시계열 변동을 AI 단독 효과로 단정 금지.

## K1 한국은행 BOK 이슈노트 제2026-19호
https://www.bok.or.kr/portal/bbs/P0002353/view.do?menuNo=200433&nttId=11063845
- 국민연금+경활 2022.06~2026.06 청년 15~29세 전체 -28.5만, AI 고노출 업종 -26.8만(94% **해당 업종 구성비**, AI causal share 아님). 소프트웨어 출판·프로그래밍·정보 서비스 및 전문서비스와 관련. 같은 업종 50대 고용은 증가/유지.
- 청년고용 감소는 **신규채용 축소 + 기존 청년근로자 이탈 증가** 둘 다 기여, AI 고노출 업종 실업자로의 유출 증가도 관측. 그러나 이탈에는 자발퇴사/해고/기간만료/다른 사업장 이직 등 복수 경로가 있으므로 해고 증가 인과로 단정 금지. W01 인구구조 감소까지 'AI 해고'에 합산 금지.
- 자동화 이용이 높은 업종 청년 약화 vs 증강 업종 제한. 학력/경기/팬데믹/remote work/경력직 채용 선호와 혼재. 거시 현상 인과미식별.

## K2 한국노동연구원 2025-12 「최근 소프트웨어 개발자 취업자 수 및 직무 변화」 (지상훈)
논문 15p 원문: https://repository.kli.re.kr/handle/2021.oak/11907 / PDF https://repository.kli.re.kr/bitstream/2021.oak/11907/2/%eb%85%b8%eb%8f%99%eb%a6%ac%eb%b7%b0_no.249_2025.12_6.pdf ; 동일 2025-12월호 https://www.kli.re.kr/pdfPreviewDownload?fileName=E0212D120459C71749258D7100223D8C_22.pdf&fileNameOrg=%EB%85%B8%EB%8F%99%EB%A6%AC%EB%B7%B0_2025%EB%85%84+12%EC%9B%94%ED%98%B8_web.pdf&filePath1=jsphome%2FDATA%2FpblctList%2Fissue%2FE0212D120459C71749258D7100223D8C
- 자료: 지역별고용조사/ICT실태조사/민간 채용 공고 (사람인·잡코리아) 등의 별도 모집단. 실제 면접/입직자 아님.
- Software developer **신입 공고 비중 2022 53.5%→2024 37.4% (-16.1%p)**. 전체 공고 신입 비중 같은 기간 -5.6%p, 연구/공학직 관련 -11.9%p. 직종 특유 더 큰 수요 비대칭, 경기 영향도 존재.
- **신입 공고 건수** 약 62k (2022) → 22k (2024) **(-~64.5%)**; 경력 공고 약 54k→36k (-~33.3%). 두 그룹 다 감소하되 신입 더 급감. 이 건수는 반올림된 원문 분석값으로 계산했으며, 근사값임. 최초 신입 숫자 2022=62k, 경력=54k의 합으로 산출되는 비중과 원문 53.5%는 반올림 오차 있음.
- ICT실태조사: 2024년 경력 3년 미만 개발 직원 전년 -9천명, 경력 3년 이상 +4.2만명. **3년 미만 노동자의 집단 stock 감소는 기존 재직자 9천명 해고를 의미하지 않음**: 3년차 승급·자연 퇴직·채용·해고가 모두 섞임.
- 지역별고용조사 20대 개발자 2022 상반기 이후 증가 정체, 30대 2024 하반기 21.2만명; 2018 18.3만과 장기 비교 시 +2.9만이나 다른 기간 비교의 AI 인과결론 금지.
- 연구자는 생성형 AI와 경기침체/금리/팬데믹 디지털 과잉채용 조정의 기여를 분리 못 한다고 명시.
- 입직공고 2022→2024는 AI 사용의 실제 도입 대조군이 아니므로 채용공고 수치 전체를 AI 감소효과로 계산하지 않음.

## K3 한국노동연구원 2026-09 공식 세미나 발표 요약
https://www.kli.re.kr/kli/nscvrgView.es?b_list=10&keyField=&keyWord=&keyYear=&mid=a10305000000&nPage=1&nscvrg_data_sn=993
- 전산업 고용 전체에 뚜렷한 AI 전후 추세 변화는 확인되지 않고, 노동시장 진입 청년/신규채용 쪽 신호 강함. 관리자 인터뷰/직업 현장 조사에서 AI 이후 신입 채용 줄임 또는 결원충원 위주 채용 의견.
- 근로자 업무 AI 사용률 51.8% vs 기업 공식 AI 도입률 9.6% (측정단위/시점 다른 두 조사; 절대 격차를 단일 모집단의 비율차로 계산하면 오류). 기업의 AI 도입 실측을 노동자 업무 사용과 혼동 금지.
- 발표/종합 논평과 정량 인과식별된 결과를 동일한 근거수준으로 취급 금지.

## 기타 직종 및 경력 반례
- Stanford 2026-09 대시보드/2026-08 논문: software developers + customer support agents 내 청년 고용감소 vs home health aides 증가. 다른 모든 행정·번역·디자인·회계 직군을 'AI로 채용 급감 확인'으로 일반화 불가.
- 41개국 Chandar & Klein Teeselink 2026-09-21, 1.25bn postings/154m employment, 신입비중 감소 주된 원인은 senior 증가였고 junior absolute 감소가 아니라는 반례: https://digitaleconomy.stanford.edu/publication/how-does-ai-change-labor-demand/ . 도입은 GenAI job posting proxy이므로 직접 채택 완전 관측 아님.
- 한국 노동연구원 WPS 기업패널: AI 도입사업체 숙련 상위 구성 증가/낮은 숙련구성 감소, 전문·사무 증가·관리직 지연 감소. 지표가 skill composition이지 개별해고 인과. https://www.kli.re.kr/kli_eng/panelBriefView.es?mid=a10104030000&pblct_sn=10287 ; https://dl.kli.re.kr/%26/10110/contents/7738034
- 뉴욕 연준 구인공고 연구 2026-05: ChatGPT 이전부터 AI 노출 직무의 공고수 하락, junior/senior 유의한 노출별 차이 미검출: https://libertystreeteconomics.newyorkfed.org/2026/05/do-job-postings-show-early-labor-market-effects-of-ai/ ; 광범위한 일반화 억제.

## 1차 주장과 반례 적합성
1) '청년 고용은 AI 때문에 줄었다': 한국 인구 감소와 고용률 하락(최근 -14.3만 인구 -6.4만/율 -7.9만)은 W01-A의 인과요인 아닌 회계요인; AI만 추정 불가.
2) '기존 노동자 해고는 늘지 않았다': 스탠퍼드/미국 Census는 **특정 고노출 직종의 조정 주경로가 신규채용 감소**라는 사실을 보일 뿐, 국가적으로 AI 관련 기존 직원 해고가 없다는 뜻 아님. Block W03 명확한 해고 반례. 한국 BOK 이탈 증가와도 지역/자료 차이로 양립.
3) 'AI 노출직 신입 비중 감소=신입직 해고': 모집단의 성장이 경력직 중심이면 junior share 하락에도 junior count 그대로일 수 있음.
4) '나이=경력': 22~25세에도 경력직 존재, 중년 직무전환 신입도 존재; Korea 경력<3 년 구간 3년차 연령승급 누적 수 효과 포함.
5) 'AI 때문에 여성/특정 학력/전문직 전부 불리': 인구/교육/산업 통제 후 동일 방향 확증 자료 없음. Stanford 여성 상대 AI exposure 증가 보고만으로 여성 실업률 영향 결론 금지.
6) 'AI 보조 직군 고용 유지=AI가 고용 창출': 자동화 대조와 고용 상관만 관측, AI가 없었다면 몇 명이 고용됐을지 반사실 불명.

## W04 판정과 후속
- **조건부 완료:** 미국 early career 실제 입직↓ vs separations 비증가(오히려 감소하는 건수), 기업 AI 사용자 설문에서 AI로 채용↓ 업체>실제 해고 업체, 한국 소프트웨어 신입 공고↓/3년미만 stock↓/BOK 젊은 근로자 이탈↑라는 차이, 직종별 반례 및 AI 인과한계 검증.
- 관측상 영향은 경력 사다리 첫 단에 더 집중되는 증거가 강함; 한국은 기존 청년 이탈도 있으므로 해고 영향 부정 금지. 신입의 채용 기회 축소에 대한 AI 고유 인과기여분은 현재 식별 불가.
- 한계: 동일 회사·직군·개인 단위 AI 채택기록-실제 해고사유/퇴사원인 및 전국 대표 직종별 입직 패널 부족. 한국 민간 공고 coverage와 변화 주의. 미국 QWI 업종 집계, Census graduates cohort 다른 범위. 주요 새 실증(2026-09 Census graduate)이 AI 관련 **초기 경력 진입 장벽** 가설 강화.
- 사용자가 승인한 다음 W05에서는 고용 창출과 손실의 분자/분모, 신규 직무 vs 기존 직군 재배치, 실제 입직과 공고를 구분해 검증. W05 및 W06은 W04 지시로 자동 착수하지 않음.

## W06-A 연구 4편에 따른 연령·경력 비교 판정 보정 (2026-10-10)
근거 파일: `W06_A_FOUR_STUDY_VALIDATION.md`.
- 미국 일부 AI 고노출 직종 초임의 채용 감소라는 **관측 사실 유지**, 단 Frank et al.의 2022 초 선행 악화로 인한 경쟁설명 추가; ChatGPT 발표 후 악화 전부를 AI 원인으로 단정하지 않음.
- Hui/Reshef/Zhou의 2022.1~2023.4 Upwork DiD에서 과거 실적 좋은 프리랜서도 계약·수입 감소로부터 유의하게 보호되지 않음. 따라서 '경력자가 AI에서 안전'이라는 **보편적 주장 폐기**. 고성과자 피해가 반드시 더 크다고 통계적 확정도 금지.
- Aum/Shin 2025 Review의 연령 그룹 'young'은 **25~49세**, 'old'는 50세 이상이며 분석기간 2017~19. 한국 청년(15~29) 또는 2022+ 생성형 AI 충격 표본과 합칠 수 없음.
- 월별 프리랜서 **계약 수 감소** ≠ 기존 임금근로자의 해고 ≠ 청년 입직 수. 미국 QWI의 총이직 감소와 Hui 계약 감소는 서로 다른 모집단과 지표이므로 모순 아님.
