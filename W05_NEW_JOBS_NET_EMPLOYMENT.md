# W05_NEW_JOBS_NET_EMPLOYMENT.md — 새 일자리와 AI 순고용 효과 검증
기준일: 2026-10-10. 고정 규칙 commit: fb22fe86834893e607072b41885277d29cfc57fc. 기존 연구 브랜치: research/20261010-ai-employment-kr-us-1538-fb22.
사용자 승인 W05 범위: 실제 새로 생긴 채용 vs 기존 직원 직무 재배치; AI에 의한 손실 상쇄 여부. W06 최종 종합검증·보고 미위임.

## 0. 판정용 개념 및 이중계상 금지
- E(t)=고용인원/일자리 수 stock. ΔE=E(t1)-E(t0)는 관측 순고용 변화. **AI 순고용 효과**=E(t1 with AI)-E(t1 had AI not been adopted), 관측 안 되는 반사실적 추정량.
- **실제 외부 신규입직(gross external hires)**: 회사 바깥에서 채용된 근로자 수. 새 역할이라도 기존 근로자 재배치/직함변경은 고용 추가 0명.
- **확장 채용(net-added positions)**=외부채용과 이직·퇴사/내부구성 변화 모두 반영한 실제 자리 증가; 기존 퇴직자 충원 1명은 채용 1건이지만 순 고용 0명.
- **채용공고 postings**는 제안/수요 표명; 중복, 미충원, 기존 자리 대체 가능. 1건=고용 1명 불가.
- **직무·산업 AI 노출**과 **실제 회사의 업무 AI 도입·활용**을 분리. '데이터과학자 고용 증가=생성형 AI가 유발한 신규 인력' 불가; 데이터과학 등은 2022 이전 존재, 기존 직책으로부터 코드 전환 가능.
- 동일 모집단/기간/집계단위에 대한 인과식별된 AI 신규고용 / AI 감소 고용 양쪽이 필요하므로 서로 다른 산업/직종/연령 통계의 숫자 빼기 금지. 원부서에서 신규 AI전담팀으로 옮긴 직원은 신규 순고용 아님.
- 산업연관표의 고용 **유발**은 모델링된 간접 계수/추정. 실제 입직 기록과 별개.

## 1. 한국 — 한국은행 '고노출 직업' 증가(실제 취업자 수, AI 창출 직접증거 아님)
한국은행 [제2026-25호] 2026-09-15:
https://www.bok.or.kr/portal/bbs/P0002353/view.do?depth=200433&menuNo=200433&nttId=11064752&oldMenuNo=201150&programType=newsData&relate=Y
- '생성형AI 고노출 직업' 2023년 이후 3년 동안 취업자 +247,000, 그중 수도권 +199,000 (80.8%). 에이전틱AI 고노출 직업 2025년 +105,000, 수도권 +93,000 (88.3%). 통계는 지역별고용조사 기반 AI 직업 *노출* 분류.
- 같은 은행 제2026-19호 2026-08-18: 2022-06~2026-06 청년(15~29세) 취업자 -285,000 중 -268,000 AI 고노출 **업종**; 이 둘을 +247k -268k = -21k 'AI 순고용' 계산 **금지**. 다르다: 시점, 청년/전체 연령, 업종/직업, 인과 vs 단순 구조, 중복 가능성.
- BOK 원문은 AI 때문에 증가했다고 인과단정 경고. 수도권 집중+기업 시장 확대 가설은 가능한 해석, AI 창출 확정 아님. 청년 신규진입 장벽과 총 AI고노출 직업 종사자 성장 공존 가능.

## 2. 한국 — AI 바우처 지원사업 엄격한 처치군·비수혜 신청군 비교
한국노동연구원 고용영향평가 결과(평가연도 2025, 보도/원문 페이지):
https://www.kli.re.kr/eia/asmntRsltView.es?mid=a30301000000&nPage=1&rslt_no=336&sch_asmnt_yr=&sch_keyword=&sch_rel_mnstr=&sch_rschr=&sch_ttl=
- 2015~2024 고용보험DB+KODATA 기업-연도 패널. 이원고정효과(TWFE) 및 CSDID, 엄격 대조집단은 지원사업 **신청했으나 탈락한 기업**(선정 이전 성향 차이 축소).
- 수요기업 단순 전체 비교 시 고용 증가 +10.8%, **신청 탈락군 비교에서는 유의한 전체 고용효과 미검출**. 비수도권 수요기업 -5.52% 유의 음의 추정치(하위집단, 다중검정/선정 잔차·표본 및 임의 외삽 주의).
- 공급기업 겉보기 고용 +29.5% 역시 비교집단을 엄격히 잡으면 도입사업 직접 효과 **소거**. 공급기업은 AI 산업 일반 성장으로 고용 증가했을 가능성.
- 고용 유발 경로(정부투자 지출+운영 효과)는 산업연관 분석의 모델/추정으로 실제 사람 수 신규 입직으로 계산 금지. '운영효과의 투자대비 배율 2020~2024 약 2.3배'는 실제 순 고용 증가율 아님.
- FGI/FGD 10개 기업 방문·인터뷰: 문서/반복업무 자동화 후 기획·전략 집중, 근로자 숙련변화/재교육. 질적 재배치는 인원 증가 아님.
- 다른 Suh/Park 2026 SSRN 보조금 고용긍정 초록은 표본·시점·설계/지원 유형이 다르고 원문 미검증: 위 엄격 대조의 무효과를 일괄 반박하는 명시적 인과증거로 취급하지 않는다.
- 위 연구의 '유의한 효과 발견 못함'을 '정확히 0명 AI 영향'으로 단정하지 않는다(검정력, 상하방향 이질성).

## 3. 한국 인공지능 산업 고용자료의 계정 범위 확인
과학기술정보통신부·SPRi 2025 인공지능산업 실태조사 2026-09-14 공개:
https://spri.kr/posts/view/24026?code=stat_sw_ai_reports
SWSTAT https://stat.spri.kr/uportal/search/searchPage.do
- 인공지능 산업 인력/직무/경력별 통계 존재. **PDF의 채용 실제/계획/현재 숫자 본문과 조사항목을 직접 검증한 표 없음**, 따라서 근거 없는 AI 신규 채용 인원 수 발명/인용 금지.
- portal 메타 주석: 2025 조사 때 일부 주요 기업 주 사업유형 AI SW→AI HW 변동으로 과거 AI 인력 숫자 직접 시계열 비교 주의. 업종/사업분류 변경에 의한 직무 재분류는 새 인원 순창출 아님.

## 4. 미국 — BLS OEWS 실제 직업 stock (2022.5 vs 2025.5)
직업 및 고용 수준 자료:
https://www.bls.gov/oes/2022/may/oes152051.htm
https://www.bls.gov/oes/2022/may/oes151252.htm
https://www.bls.gov/oes/2022/may/oes151212.htm
https://www.bls.gov/news.release/ocwage.t01.htm
- data scientists(SOC 15-2051): 2022 May 159,630 → 2025 May 262,440, **+102,810(+64.4%)**.
- software developers(SOC 15-1252): 2022 May 1,534,790 → 2025 May 1,687,890, **+153,100(+10.0%)**.
- information security analysts(SOC 15-1212): 2022 May 163,690 → 2025 May 190,650, **+26,960(+16.5%)**.
- 직업 자체는 AI/GenAI의 실질 수혜 비율이 불분명하고 이전부터 있던 직업이며, 자료는 고용 **stock**, hiring flows 아니다. 동일 직업 안 신규 채용/재분류/폐업/퇴직 분리 불가. self-employed 제외. 특히 소프트웨어 개발은 AI 기술 때문이 아닌 수요/경기 영향이 다양.
- 세 직업의 변동을 합쳐 'AI로 만든 채용 282,870명' 주장은 금지; 다만 (AI와 관련될 수 있는) 실제 고용이 증가한 직업이 있다는 **반례**.

## 5. 미국 — 실제 AI사용 기업의 신규 채용(+), 채용회피(-), 재훈련 및 감원
NY Fed 2026-09-01 (2026 Aug NY/northern NJ business surveys):
https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/
- AI 사용 서비스 기업 중 13% 'AI 활용 위해 직원 추가 채용', 약 15% 'AI 때문에 채용을 덜함', 4% 'AI 때문 직원 해고', >33% '기존 직원 재훈련'. 제조업 AI사용 업체 중 직원 추가채용 0%, 해고 0%, 재훈련 20%+.
- 채용 '13%'는 **업체 비중**이고 추가로 채용된 직원 수 / 미국 전국 회사 비중이 아니며 AI 사용에 따른 회사의 자기보고. 해당 회사의 총 고용 순증가 자료와 연결되지 않음.
- 13%-15%-4%=net job change처럼 업체비율을 가감하는 수식 금지. 재훈련은 외부 신규 채용 아님. AI 미도입 업체도 비교 필요.
- U.S. Census BTOS 2026 18% firms use AI, 66% augment only, 2% reported AI employment decrease; actual firm adoption and worker use not identical:
https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html

## 6. 채용공고로 부풀려진 'AI 일자리 130만개' 검증
LinkedIn 2026-01-14 original press & methods:
https://news.linkedin.com/2026/2026-Davos-Press-Release
- headline: 'more than 1.3 million new AI-enabled jobs globally' (2023~2025).
- **METHOD:** count of LinkedIn **job postings**, containing titles/keywords e.g. Data Annotator, AI Forensic Analyst, Head of AI, AI Engineer, Forward-Deployed Engineer/Product Manager, NOT 1.3 million new people employed or net occupational stock; may include vacancies not filled, repeated and replacement.
- LinkedIn 2026 PDF https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/linkedIn-labor-market-report-building-a-future-of-work-that-works-jan-2026.pdf gives individual job postings category: Data Annotator 774k, AI Forensic Analyst 49k, Head of AI 298k, AI Engineer 177k, Forward-Deployed Engineer/PM 9k; roughly ~1.307m postings. Claim 'AI created net 1.3m workers' is **measurement category error**. Separate report '600k data center roles added net on LinkedIn' has different methodology/broader AI enabled role attribution; don't double-count and not causal AI labor gain.
- 2026 Lightcast AI index: AI skills appear in 2.5% of US postings, +55% year-on-year; 2025 agentic AI mentions ~90k postings, again no actual employment headcounts: https://lightcast.io/resources/research/stanford-ai-index-2026
- AI skill required as feature in existing accountant, salesperson job ≠ brand-new job.

## 7. Hiring expansion mechanism and counterexample 41 countries
Chandar & Klein Teeselink 2026-09-21 "How Does AI Change Labor Demand? Evidence from 41 Countries":
https://digitaleconomy.stanford.edu/publication/how-does-ai-change-labor-demand/
- 1.25 billion ads +154 million employment records, infer AI adoption using GenAI job ads, study foreign affiliates vs controls with instrumented event-study.
- junior **share** relative decline, *mostly senior absolute employment growth*, not junior total number dropping; *suggestive modest growth in overall headcount* in treated firm. This is a direct observed **employee stock** expansion in sample, but AI adoption is proxy; event design/local affiliates and spillovers/instruments constrain validity. US/Korea national effect not measured.
- illustrating shares: junior10 and senior40 → junior10 and senior45 => junior share20%→18.2%, actual junior employment=10 unchanged, total jobs +5. Do not count fractional share decline as junior layoffs.
- firm AI adoption and positive headcount might reflect rapidly growing firms selecting AI, not AI causing growth. Global cross-country sample proxy caveat.

## 8. Alternative U.S. labor-market interpretation
LinkedIn 2026-02 Software engineer labor market study:
https://economicgraph.linkedin.com/content/dam/me/economicgraph/en-us/PDF/us-software-engineer-talent-landscape-2026.pdf
- entry SWE hiring generally followed overall SWE/tech hiring; overall decline macroeconomic cycles. Role shifting into AI-adjacent and non-tech business/analytic positions; AI 'created enough to offset' not estimated. Avoid extrapolating Stanford ADP narrow sample patterns to broad labor market.
- Yale 2026-09 tracker no broad detectable employment shock; industry-level employment aggregate and narrow young cohort can coexist.

## 9. Synthesis: two different questions
1) Observed aggregate employment after AI adoption? Korea total annual +680k 2022→2025, U.S. CES +5.462m Sep2022→Sep2026 (W01). This **does not identify** AI net effect; macro employment driven by demography/recovery/cycle and other industries, not limited to AI-linked positions.
2) Has *AI-caused* gross-new-hire created more jobs than *AI-caused* destruction? **Not identified for US/Korea.** Korean AI voucher rigorous comparison null; NY Fed self-reported hire firms and fewer-hire firms both exist, not counts; international 41-country slight positive employee growth only in sampled multinational affiliates; loss evidence early-career US cohorts and Block W03; no common quantitative counterfactual under uniform horizon/strata.
3) No basis to claim "net positive" or "net negative" for **causal AI effect** across both countries, and certainly not enough to calculate offset ratio.
4) Qualitative strongest: demand for AI skills and technical roles is rising; incumbent retraining/internal mobility substantial; losses can concentrate on new entrants; sector-specific gains and losses coexist; not guaranteed that new AI jobs accessible to displaced juniors due to skill geography and qualification mismatch.
5) Regional: Korea BOK high-exposure gains mostly capital region; new positions do not automatically offset lower-skilled youths in other sectors or places.

## W05 status / next
- **조건부 완료:** new hires vs internal deployment/retitling; job postings vs actual hiring; firm observed stock vs AI-caused increment; offset strictest inference checked. Documents recorded with source URLs; Korean 2025 AI industry survey confirmed publication but no unverified numerical claim. W01~04 relevant crosschecks done.
- Important new finding: Korean KLI voucher strict applicant control wipes out apparent +10.8% customer/+29.5% supplier effects; US LinkedIn 1.3m 'new jobs' methodology = postings; US BLS data scientists 2022→2025 +102,810 actual workforce stock. **These alter the strength of job creation claims downward**, but do not establish negative net effect.
- Next W06: reconcile all estimates and conflicts, audited summary table, finalize only with explicit user authorization; W06/FINAL_REPORT.md **not** commenced. No write to main or other branches.
