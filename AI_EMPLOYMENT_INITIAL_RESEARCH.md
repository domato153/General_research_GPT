# AI와 일자리: 2026-10-10 1차 실증조사 및 검증 메모

> 조사 상태: **1차 조사·반례 검토 완료, 최종보고서 미확정**. 사용자 조사축·산출물 형식은 미합의. 고정 규칙 기준: 0632ca0356e5d5d43773ba9e262d7ae85a234c12. 기존 브랜치·main 변경 없음.

## 조사 목적 및 기본 범위(제안, 사용자 승인 아님)
- 질문: 생성형 AI가 이미 일자리를 감소시켰는가? 규모·영향집단·인과 여부는?
- 기본 지역: 미국·한국, 비교 근거 덴마크. 2022년 11월 이후 ~ 2026-10-10.
- 조사축: (1) 발표된 해고와 실제 고용 감소 (2) 신규채용 위축 (3) 집단별/직종별 차이 (4) 대안 설명 (5) 기존 일자리 변화와 신규 일자리 (6) 중기 전망과 관측치 분리.
- 보고서 기본 설계: 개념·지표 설명 → 국내외 통계 → 인과 및 경쟁 가설 → 직종·세대별 영향 → 전망·시나리오 → 결론·근거 수준. 최종 작성은 별도 사용자 위임 확인.

## 현재 잠정 결론
1. 경제 전체 대규모 AI 유발 실업은 아직 통계적으로 확인되지 않았다(Yale Budget Lab 2026-09-15, Stanford 2026-08).
2. AI 노출이 높은 **청년 신입 고용 감소**는 미국 행정데이터·한국 행정데이터·덴마크 기업자료에서 반복 발견된다. 그러나 관찰된 감소분이 전부 AI 인과효과는 아니다.
3. 감원 사유의 'AI' 표기는 실제 AI 대체를 증명하지 않는다. 계획 감원은 실제 실직자와 다르고 미충원은 별도다.
4. 사회 전체의 AI 순고용 증감 규모는 현재 신뢰 가능한 단일 추정치가 없다.

## 확인된 근거

### 미국 해고 공표(원자료)
- Challenger, Gray & Christmas, 2026-10-01: 2026 1~9월 총 발표 감원 573,195명; AI 사유 언급 120,136명(약 21%), 9월 3,961명. 2025 AI 사유 감원 계획 54,836명. 회사 발표의 reason coding, 실제 원인 검증/퇴직 완료 아니며 일반 인구 총량도 아님.
- https://www.challengergray.com/blog/job-cuts-fall-in-september-hiring-plans-up-3-over-2025-on-weak-early-seasonal-hiring/
- https://www.challengergray.com/wp-content/uploads/2026/04/Challenger-Report-March-2026-1.pdf

### 미국 노동시장 연구
- Stanford Digital Economy Lab, revised 2026-08-12: ADP 급여 데이터. 22~25세 AI 고노출 직업군 상대 고용 격차 −19%(2026-06; 2025-07 관측에서는 −15%), 주로 신규 고용 감소. 경제전체 대규모 대체 관찰 못함. 연구팀 명시: **서술적 차이이지 인과효과 추정 아님**. 교육 통제 시 격차 축소; ADP표본과 국가 표본간 크기 차이.
- https://digitaleconomy.stanford.edu/news/canariesaug26/
- US Census Bureau Lee Tucker 2026-04 working paper, 산업·주 셀 기준 AI 최상위 노출 집단 청년 22~24세 회귀조정 고용 −12% (챗GPT 출시 후 10분기), 채용 감소가 주된 경로.
- https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-27.html
- US Census Bureau Orr, Tucker, Warren, 2026-09 working paper, AI 최고노출 전공 상위 10%의 졸업 직후 취업 확률 −5%p, 초기 분기 소득 −13%. 관찰 분석; 자료·저자 중복으로 미국 두 논문을 완전 독립 근거로 중복 계산 금지.
- https://cdn.www.census.gov/library/working-papers/2026/adrm/CES-WP-26-56.html
- Yale Budget Lab, tracking updated 2026-09-15: 직업 구성·AI 사용 노출과 미국 고용/실업 변화 상관 및 synthetic DID에서 AI 영향 명확히 탐지 못함. macro/직업단위에서 영향 미검출은 세부 집단 효과 부정을 뜻하지 않음.
- https://budgetlab.yale.edu/research/tracking-impact-ai-labor-market
- Anthropic, 2026-03-05: 관찰된 AI 사용 기반 노출도와 실업의 유의미한 전반적 연관 없음, 청년 채용둔화 암시. Claude 이용 데이터 편향 고려.
- https://www.anthropic.com/research/labor-market-impacts

### 한국의 상충 증거
- 한국은행 2026-08-18: 2022-06~2026-06 청년고용 감소 285,000명, 그중 AI 노출 높은 산업에서 268,000명(94%); 정보서비스 −31.4%, 출판 −27.4%, 컴퓨터프로그래밍 −16.6%, 전문서비스 −11.6%; 50대 고용은 동일 산업에서 증가. 4년간 인력 감소의 원인을 AI에 전부 귀속할 수 없다고 연구진도 명시. 기업 과잉채용 정상화·경력선호·사내훈련 감소·원격근무 등 대안.
- https://www.bok.or.kr/eng/bbs/B0000354/view.do?depth=400409&menuNo=400409&nttId=11064434&oldMenuNo=400007&programType=newsDataEng&relate=Y
- 한국고용정보원 2026 여름호, 고용노동부 발표 2026-08-31: 고용보험 취득자는 AI 노출도 관계없이 감소; 청년 인구 감소와 경제활동참가 축소를 주요 요인으로 파악. 30세미만 2022=100 기준 2025 고노출 86.6 vs 저노출 92.5, 차이 5.9pt, 그러나 출범 전부터 차이 추세. 사업체 조사 2,297개 도입률 28.6%, 도입 기업 75.6% 생성 AI 사용, 감원목적 아닌 반복업무 경감·생산성 제고 응답. 한국은행 연구와 서로 연구대상/분모·측정/조정법 달라 반박 자료로 병기 필요.
- https://www.moel.go.kr/news/enews/report/enewsView.do?news_seq=19850
- 한국은행 2026-06-08 시간 절감 3.8%(주당 약 1.5시간), 실제 생산증가와 명확한 연결 없음(잠재효율 vs 실현산출 구분).
- https://www.bok.or.kr/eng/bbs/B0000354/view.do?menuNo=400409&nttId=10098400

### 덴마크
- 중앙은행 2026-09-16: 2023/24 AI 신규 도입 기업의 2025년 고용성장률이 비도입 비교 기업 대비 약 11% 낮음(상대적·추세대비). 감소는 주로 신규채용. 경제 전체 고용효과 크지 않음. **11%가 실제 직원 감원률은 아님**.
- https://www.nationalbanken.dk/en/news-and-knowledge/publications-and-speeches/analysis/2026/artificial-intelligence-and-the-labour-market-the-transition-has-begun
- NBER Humlum & Vestergaard 2025, revised 2026-03: AI 챗봇 도입에 따른 개인 근로시간·소득 평균효과 2% 이상의 변화 배제(2년 후) — 기업의 상대적 신규채용 감소와 다른 지표, 논리적 모순 아님.
- https://www.nber.org/papers/w33777

### 전망과 실측 구분
- ILO–NASK 2025: 전세계 일자리 중 25%가 생성 AI '노출' 가능. 실직률 25% 아님. https://www.ilo.org/resource/news/one-four-jobs-risk-being-transformed-genai-new-ilo%E2%80%93nask-global-index-shows
- WEF Future of Jobs 2025: 2030년까지 170m 창출/92m 대체/78m 순증 전망은 **AI만**이 아니라 인구·녹색전환·거시경제 등 여러 변화의 종합 전망(고용주 설문에 기반한 예측). AI와 정보처리 기술만을 따로 보면 창출 11m, 대체 9m의 전망(이 역시 관측이 아님).
- https://www.weforum.org/publications/the-future-of-jobs-report-2025/in-full/2-jobs-outlook/

## 비판적 검토 / 보완 과제
- 미국과 한국의 청년 상대격차는 고용률·취업확률·고용자 수 등 단위가 달라 직접 비율 비교 금지.
- 산업분류와 직업분류의 차이, 기준 기간, 표본 선택, 청년인구 감소, 고금리 및 코로나 이후 과잉채용 등을 컨트롤해야 함.
- AI 사용 여부에 따른 선택편향: AI 도입 기업과 비도입 기업의 기존 성장·직종 믹스 차이.
- 대체효과와 보완효과를 함께 보고, 채용 감소가 지속·확산되는지, 기존 직원의 이직·실업으로 전이되는지 추가 점검.
- 장기 영향 시나리오는 확정 불가. 종합 판정 전에 고용지표 원시 데이터, 정책 및 업종 분해 검토 가능.
