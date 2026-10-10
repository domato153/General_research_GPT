# W02_CAUSAL_EVIDENCE.md — AI와 실제 고용 감소의 인과관계 검증
2026-10-10 / research/20261010-ai-employment-kr-us-1538-fb22 / 시작 기준 fb22fe86834893e607072b41885277d29cfc57fc

## 사용자 확정 및 경계
- 한국·미국 중심, 2019~2026-10 공개 원자료. W02(인과효과)를 우선; W01 인구·고용률 보정을 참조한다.
- W03 개별 기업 사례, W04 세부 연령/직종, W05 새 일자리/순고용, W06 최종보고서는 미착수. 2026-10-10 W02 실행 위임은 W03~06까지 완료 위임이 아님.
- '고노출업종에서 청년고용 감소 비중', 'AI 고노출 청년 직군 19% 상대 격차', 'AI 도입 기업 고용 증가율 11% 상대 감소', 'AI 채용 대체 인원'은 서로 다른 지표; 전부를 AI가 없앤 고용인원으로 바꾸면 오류.
- 실증 분석과 실제 AI 도입 조사, 산업·직종 수준 노출 추정치를 구분한다. 대부분 인과 식별의 한계가 있는 연구설계.

## 기준 결과와 가설
- W01 한국 15~29세 최근 2025.8→2026.8 취업자 -14.3만, 그중 인구크기 효과 -6.4만, 고용률 하락효과 -7.9만(근사), 2022→2025 장기 -41.9만 중 인구 효과 67%. 이는 거시적 **회계적 분해이며 AI 인과효과와 무관**. W01_A_POPULATION_ADJUSTMENT.md 참조.
- W01 미국 22~25 연령과 비일치하는 CPS 넓은 연령집단 수치, 통계 단절(2025·26 population control)을 W02 자료와 절대치로 통합하지 않음.

## 미국: 고용 감소 관련 주요 연구
### [US1] Stanford DEL / Brynjolfsson, Chandar, Chen, 2026-08-12 수정: "Canaries in the Coal Mine"
- 원문 (2026): https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/ ; 저자 해설 https://digitaleconomy.stanford.edu/news/canariesaug26/
- ADP 급여 자료, 수백만 근로자, 2026-06까지. 22~25세 AI 고노출 직업군 고용 추세가 저노출 또래 추세 대비 19% 낮다. 경력자에서 동일 격차 미발견. 자동화적 용도에 감소 집중, 증강적 용도에 고용 안정/증가. 넓은 전체 고용 손실 신호는 없음.
- **2026년 개정판 주의**: 교육 통제 시 격차 축소; 일부 차이는 AI 이전 시점부터 나타남; ADP 표본의 격차는 전국 조사보다 큼; 데이터 파이프라인 개정 시 기업 채용 추세를 통제한 추정치가 특정 사양에 민감. 저자 스스로 인과 확정 불가 언급. 실제 기업 AI 도입 측정이 아니라 직무 노출 기반.
- 직업 간 상대적 19% 격차=AI가 그 직군 일자리 19%를 직접 없앴다는 판정 불허. 2025년 논문의 16%를 최신 숫자로 사용하지 않음.

### [US2] U.S. Census CES WP 26-27 Tucker (2026-04) "You're (not) Hired"
- 원문: https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html ; PDF https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-27.pdf
- QWI 근로자-사업체 행정자료의 산업-주별 세부 그룹. AI 고노출 상위 20% industry-state 청년 22~24세, 2022말 ChatGPT 직후 약 10분기 회귀조정 고용 -12% (저노출 비교). 즉각적 채용 수준 약 -9% 상대 변화, 이후 취업자 수준 감소의 주 동력. 논문 본문 기초계열의 -15%, 상대 추정 15만개 이상은 조정 12%와 같은 지표가 아니며 미국 전체 AI 직접 대체 규모가 아님.
- 연구 자체가 COVID 전후 고노출 산업의 청년/고령 트렌드 구조적 변화(원격근무, 학업 변화)를 인정. 삼중차분에서 이전 추세가 달라질 수 있음. 통화긴축충격의 역사적 분해는 relative gap 최대 ~1/4 설명 가능하되 급격한 고노출 분야 채용 중단의 주원인이라는 증거 부족. **AI 노출은 업종 노출 지수이며 실제 채택 관측이 아님**.
- Census Working Paper는 근거가 상세한 연구이지 정부 공식 인과효과 확정 통계가 아님.

### [US3] Yale Budget Lab synthetic DiD, 2026-05 → tracker updated 2026-09-15
- https://budgetlab.yale.edu/research/what-we-do-and-dont-know-about-how-ai-affecting-labor-market
- https://interactives.budgetlab.yale.edu/tools/ai-labor-market-tracker/?tab=current-update
- CPS 직업별 고용/실질시급, 사전추세가 비슷하게 가중된 노출 상하위 집단 비교, 2020년 제외. AI 노출직업의 평균 고용·임금/실업 차이를 유의하게 확인 못 함(2026-08 CPS 업데이트도 광범위한 AI 교란 미검출). 'AI 영향 0 확정' 아님: 좁은 22~25세 특정 초임군은 CPS 표본·직업 코드 측정이 충분하지 않고, 노출 직군의 자동화/증강 상쇄, 실제 도입 미측정.
- AI 고노출 직업은 교육비중, 성별, 경기 민감도가 비노출과 달라 단순 노출 비교는 편의 가능.

### [US4] NY Fed Audoly/Guerin/Topa 2026-05
- https://libertystreeteconomics.newyorkfed.org/2026/05/do-job-postings-show-early-labor-market-effects-of-ai/
- Lightcast 구인공고, 직업별 Anthropic AI 실제용도 포함 노출 지수. 2018~25 고노출 공고 상대감소는 ChatGPT 등장 **이전부터** 시작; 출시 후 별도 변화 단절 뚜렷하지 않고 AI 고노출 직업내 junior/senior 공고의 별도 격차 미검출. 전체 채용 둔화가 곧 AI 기여라는 설명 반박. 공고는 실제 입직/고용과 별개의 측정대상; 중복·게시 전략 등 영향 가능.

### [US5] 미국 Census 기업 AI 실제 사용
- https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html
- 2025-11~2026-01 BTOS AI 보충조사: 업체의 18% AI를 업무기능에 활용(고용 가중 32%), 도입사 57% 최대 3개 업무기능. AI를 오직 증강 용도로 쓴 사업체 66%; AI로 인한 고용 감소 보고 사업체 2%. 기업 자가보고와 사용범위에 대한 실측 설명이지 인과실험 결과가 아님. 플랫폼/업무 노출이 실제 보편 도입 아님.
- AI 노출도→실제 도입 상관관계는 유의하나 설명력은 작음: https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-61.html

### [US6] 다국 기업 CEO 설문 NBER WP34836 2026-02/03
- https://www.nber.org/papers/w34836
- 약 6000명 미국/영국/독일/호주 기업 경영진 설문, 3년간 AI 영향 미국 업체 89%는 고용 영향 없음, 미국 응답 평균 -0.09% 영향(저자 코딩). 스스로 추산/회상 응답이지 행정 고용 실제 검증·인과 식별이 아님. 예측과 혼동 금지.

## 한국 실증
### [KR1] 한국은행 이슈노트 제2026-19호 2026-08
- https://www.bok.or.kr/portal/bbs/P0002353/view.do?menuNo=200433&nttId=11063845
- 국민연금·경활 조사. 2022-06~2026-06 청년 취업자 -28.5만 중 -26.8만이 AI 고노출 업종에 해당(94%는 고용 감소의 **구성비**, 원인기여율 아님). 같은 업종 50대 고용 증가. 자동화 중심 업종에서 더 큰 감소, 증강 중심 업종에서는 그 패턴 제한; 대졸 청년 실업률 상승, 청년 기존 근로자 유출과 신규 채용 감소 함께 관찰.
- **원문 스스로 제시한 대안 설명**: 팬데믹 이후 과잉채용 정상화, 경력직 채용 선호, 사내 교육 감소, 재택근무 확대. AI가 그러한 변화 가속화 가능성 수준; 직접 AI 도입 기업과 비도입 기업의 엄격한 가상 반사실을 만들지 않아 국가별 AI 순고용 수치 식별 불가.

### [KR2] 한국노동연구원 WPS 사업체패널
- https://www.kli.re.kr/kli_eng/panelBriefView.es?mid=a10104030000&pblct_sn=10287 (2026-06-24): 2023 사업체 AI 도입 5%(2022 1.5%); 도입/비도입 업체 채용/고용증가율 '비슷한 추이', 단기 고용 감소로 연결되는 명확한 증거 없음. 도입 업체 숙련직 비율 +5.3%p, 저숙련직 -4.4%p(2019~2023); 직원구성 변화는 채용/이직/분모 효과 분리해야 함.
- https://www.kli.re.kr/kli_eng/rschRptpView.es?mid=a20101000000&nPage=1&pblct_sn=10276&sch_keyword=&sch_rsch_fld_no=&sch_type=&sch_yr= (2025-12-31): 도입 직후 단기 일자리 증가 관계 이후 약화/유의성 불확실, 전문/사무 증가·관리직 감소, 업종·규모 편차. 업체 선택 및 도입 정도 차이로 보편적 인과효과 불가.
- 서로 다른 기간/표본/방법이므로 2026 브리프가 2025 보고서를 반드시 뒤집는다고 볼 수 없음.

### [KR3] 한국 AI 맞춤형 소프트웨어 보조금 수혜 연구 Suh/Park 2026-07(8월 등록)
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7158038
- 보조금 수혜기업 선정 시차를 사건연구로 이용, 수혜 기업에서 고용 증가 및 기존 업무 축소/AI 관련 컴퓨터·관리 직무 증가; 젊은/기존 역할별 차이. 기술의 **고용창출과 구조조정** 가능성을 보여주는 이질적 반례. 단, 현재 초록만 직접 확인했고 원문 원인 식별(당첨선정의 외생성/공통추세/대조군)을 독립 검증하지 못했으므로 확정적 causal proof 아님. 정부 보조금 수혜의 정책묶음 영향=순수 AI 기술 효과가 아닐 가능성.

## 제3국 독립 교차확인 (한국·미국 결론에 직접 외삽 금지)
### [DK1] Bonin/Darougheh/Kuchler Danish Nationalbank WP223 2026-09
- https://www.nationalbanken.dk/en/news-and-knowledge/publications-and-speeches/working-paper/2026/ai-adoption-and-firm-size-employment-effects-in-monthly-administrative-data
- **실제 도입 업체** 2023 채택 vs 미도입, 월별 행정근로자료와 연계. 2025 말까지 고용 증가율/사전 추세 대비 약 11% 뒤처짐 (실제 직원 11% 해고가 아님), 중소규모 기업에서 낮은 신규채용에 집중. 경제 전체 효과 미미. 도입 결정 외생 아님: 성장추세/선택 편의 잔존, observational 비교로 확정적 causal 인과 추론 금지.

### [DK2] Humlum/Vestergaard NBER WP33777 2025, 2026-03 revision
- https://www.nber.org/papers/w33777
- 노동자 실제 AI 챗봇 채택조사 + 임금·기록 근로시간과 workplace, diff-in-diff. ChatGPT 등장 약 2년 뒤 평균 임금·근로시간 효과 유의하지 않음; 관측 평균효과 2% 초과 배제할 정밀도. AI 관련 신업무/직무 이동 증가. 총고용 감소 연구라기보다 **노동시간/소득의 평균 무효과** 측정이므로 [DK1] 고용성장 비교와 엄밀한 동일 종속변수 모순 아님.

### [GLOBAL1] Chandar/Klein Teeselink "How Does AI Change Labor Demand?" 2026-09-21
- https://digitaleconomy.stanford.edu/publication/how-does-ai-change-labor-demand/
- 41개국 12.5억 구인공고·1.54억 고용기록; 생성형 AI 요구 공고로 업체 채택 간접 추정, 도입 다국적기업 국외 자회사/비도입 비교의 도구변수 사건연구. 신입(junior) 비중 감소는 신입 절대고용 감소보다 **경력자 고용 증가**로 주로 설명, 총고용은 소폭 증가 시사. AI 채택 공고가 실도입과 완전 동일하지 않고 국외자회사 표본 일반화 한계.
- '신입 비중 감소=신입 일자리 감원' 계산 금지.

### [GLOBAL2] 프랑스 AI 채택 2017~2020 연구 (GenAI 직접 아님)
- https://doi.org/10.1257/pandp.20251047
- DiD에서 AI 채택업체 고용·매출 증가 관련; 행정용 프로세스 AI vs 기타 목적에 따라 고용 방향 다름. 과거 일반 AI이므로 생성형 AI 2022~2026 인과효과 추정 직접 증거로 세지 않음.

## 독립 연구간 경쟁 설명 평가
1. **팬데믹/원격근무/학력**: Census 삼중차분에서 팬데믹기 이전 격차, Stanford 2026 교육통제 시 격차 축소; NY Fed 공고 감소의 출시 전 시작. AI 아닌 공통 설명 일부 지지, 하지만 Census 2022말 신규 채용 급격한 감소와 자동화 용도별 차이는 전부 설명 못 함.
2. **통화긴축/경기**: Census 모델은 고노출-저노출 청년 고용 수준 격차의 최대 약 25%까지 과거 통화정책 충격 설명 가능; 급격한 신규 채용 감소를 이 요인만으로 설명했다는 연구 근거 없음. 단일 계량 역사분해이며 전체 격차 나머지 75%가 AI의 효과라는 근거는 전혀 아님.
3. **AI 노출 ≠ AI 사용**: 미 Census 2026 노출/실사용 설명력 작음; 고노출 직업군이 기술도입 기업군이 아님. Stanford·Census·BOK 자료는 명확한 순수 도입효과로 해석 불가. Denmark/한국 보조금/미 BTOS 등의 실제 도입 측정이 필수 보완.
4. **신규채용 감소/해고**: Stanford/Census/Danish WP는 신규 채용의 둔화가 주요 메커니즘; BOK 한국은 채용과 청년 이탈이 함께 관측됨. 따라서 세계 공통으로 '해고 없다' 결론도 불가.
5. **관측 대상 차이**: Yale CPS broad occupation aggregate null; Stanford ADP very young narrow occupation decrease; NY Fed postings vacancy no junior differential; Census actual starts. 서로 다른 지표·통계력·표본의 결과라 양자택일/단순 투표 금지.
6. **도입에 따른 고용 증가**: 한국 보조금 기업, KLI 일부, 41국 senior growth, 프랑스 채택업체 고용증가: 생산성 확대/직무 재배치 경로. 순 고용에 대한 식별된 보편값 없음.

## W02 판정
- **AI가 일부 초기경력자 신규채용을 감소시킬 수 있다는 가설: 유력/인과 추정 부분 지지**. 독립 행정자료 미국 Stanford·Census 같은 방향, 그러나 노출기준·사전추세와 선택편의 탓에 순수 AI 효과 크기 미식별.
- **한국 청년 취업자 -28.5만, AI 고노출 -26.8만 중 AI 직접 기여**: 미식별. W01 인구회계효과 -7.9만(최근 월 비교)도 AI 인과량 아님.
- **전체 한국·미국 대량 해고 또는 전반 순고용 감소**: 본 자료로 확증 불가; 현재 광범위 AI 유발 고용 붕괴는 공식 총고용·반례 연구와 부합하지 않음.
- **실제 도입 기업에서 인과적 영향**: 효과의 부호/분포가 다르며 인과식별이 높은 수준으로 확정됐다고 보기 어려움. 한국 보조금연구 PDF 미검증, 덴마크 선택편의 남음.
- **W02 상태 조건부 완료:** W02 요구사항(비교집단/사전추세/대안설명/실제 도입/불확실성 검증) 수행. 잔여 과제 W03에서 업체 도입과 감원 실측 케이스 교차검증, W04 연령/경력, W05 순고용. 새로운 큰 반례가 나오면 W02 재개. 'AI로 없어진 국가별 일자리 수'는 임의 작성 금지.

## 권장 후속
원래 승인 W03(기업 AI 도입·고용 사례의 실제 전후 비교)로 이동하는 것이 타당. W02에서 확인한 AI노출 proxy 취약성을 기업 채택 실측·고용명세/신규 입직·해고로 검증하는 연결 작업. 구체적 검색/판단은 W03에서 실행. 사용자 '다음 단계 진행' 지시 없이 W03 완료로 표시하지 않음.
