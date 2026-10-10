# W06_PRE_REPORT_AUDIT.md — W01~W05 사전 근거 교차검증 및 종료 가능성
검증일 2026-10-10 (Asia/Seoul). 대상 브랜치 `research/20261010-ai-employment-kr-us-1538-fb22`, 원규칙 `fb22fe86834893e607072b41885277d29cfc57fc`.
사용자 지시: **실제 근거 점검/누락·충돌 발견/추가조사 필요성 판단만**. 사용자 선택 전 `FINAL_REPORT.md` 작성·확정·전달/Closeout 금지.
이번 파일은 독립 **audit**, 원래 W01~W05 결과를 덮어쓰지 않으며 수정·추가조사 판단을 남긴다.

## 1. 검증 범위와 실행 (계획이 아닌 수행)
- 승인 `RESEARCH_PLAN.md`와 W01~W05( W01_A 포함) GitHub 실제 파일을 읽어 앞의 주요 주장/표본/원인을 추출·대조.
- 공적 원출처 실제 재조회: BLS 2026-10-02 Sep payroll/실업률; JOLTS 2026-09-29 Aug 채용/해고; OEWS 2022/2025 data scientist 실제 고용; BOK 2026-08 청년 high exposure **산업**, 2026-09 전체연령 high exposure **직업**; KLI AI 바우처 2025 고용영향평가; Census 2026 QWI PDF의 채용·이직·사전추세 및 서술(p15 화면 검증); Stanford 2026-08 19%와 비인과 선언; U.S. Census 2026-09 졸업생 원문; LinkedIn '1.3m' methodology; Block 2026 Q2 SEC 10-Q 실제 >40% 감소.
- 독립 반례 소스로 2024 peer-reviewed freelance 실증, 2025/26 한국 디지털기술 관련 실증, 2025 미국 firm task substitution+offset 연구, 2026 AI노출 직군 악화 시작이 ChatGPT 이전이라는 preprint, 2026-01 BOK 한국 AI 숙련근로자 규모 탐색.
- W01 청년 인구요인 분해 입력값을 기록에서 가져와 별도로 계산 재실행. 국가 원자료를 100% 내려받아 전체 미시 재구축한 작업은 **하지 않음**. 재계산과 원자료 확인을 분리.
- 사용자 최종 보고서 완성 위임 없음. 최종 파일 미작성.

## 2. 재검증 통과 (A: 핵심 그대로 보존)
1. 미국 Sep2026 CES +29k; 실업률 4.2%, BLS published 2026-10-02. https://www.bls.gov/news.release/archives/empsit_10022026.htm ; Sep2026 total 159,044k https://fred.stlouisfed.org/series/PAYEMS/ ; JOLTS Aug2026 7.1m openings, 5.2m hires, 5.1m separations; quits3.1m, layoffs/discharges1.6m. https://www.bls.gov/news.release/archives/jolts_09292026.htm. 매크로 미국 감원 급증이 전체노동시장에 걸쳐 뚜렷하다는 근거는 아님.
2. 스탠퍼드 ADP 2026-08 revision 22–25 고노출 직군 19% 상대격차, 채용 중심; 저자 'descriptive patterns not causal estimates'. https://digitaleconomy.stanford.edu/news/canariesaug26/ . Stanford 2026-09 dashboard는 **균형 패널 약 25천 회사**, 탈락·신생기업/표본 대표성 제한; 전국 전체노동시장 대표 추정치로 사용 불가. https://digitaleconomy.stanford.edu/project/indicators/canaries-dashboard/
3. Census 2026-04 QWI 원문 PDF 직접 검증: 22–24 신규입직 즉각 -9% 비교기간, 10분기 회귀조정 고용 -12%; **총 separations 건수** 2025Q1까지 기준 4분기 대비 -11.5%, 이직률은 해당 절대건수만큼 크게 하락하지 않음; 총 separations는 자발/비자발 해고 분리 불가능. p15 'replacement hires' 즉각 -9%, 마지막 4분기 -15%. https://www2.census.gov/library/working-papers/2026/adrm/ces/CES-WP-26-27.pdf . 중요 추가 확인: 채용 경로 단독을 과대일반화하지 말 것. 감소된 separations는 청년 고용 stock 손실을 **완충**; 연구 내부 flow counterfactual에서 hires 감소가 전체 관측 고용 감소를 설명하지만 AI 원인 추정 100% 아님.
4. 2026-09 Census 대졸 연구 고노출 전공 취업 -5%p / 최초 완전분기 소득 -13% 비교집단 회귀조정 확인: https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-56.html . Census working paper 저자의 주장이지 센서스의 공식 인과효과 확정 수치 아님.
5. 한국 BOK 2026-08 청년 -28.5만, -26.8만 AI 고노출 **업종** 구성 (94%) 확인: https://www.bok.or.kr/eng/bbs/B0000354/view.do?depth=400409&menuNo=400409&nttId=11064434&oldMenuNo=400007&programType=newsDataEng&relate=Y . BOK 2026-09 전체연령 생성형AI 고노출 **직업** +24.7만, 수도권+19.9만, 20대 고노출 직업은 수도권·비수도권 **모두 감소**라는 추가 조건 확인: https://www.bok.or.kr/portal/bbs/P0002353/view.do?menuNo=200433&nttId=11064752&pageIndex=1
6. W01-A 요인분해 **산술 재계산**: 2025.8→2026.8 청년 -14.3만 = 인구 -6.4204만 + 고용률 -7.8796만; 2022→2025 연평균 -41.9만 = 인구 -28.1316만 + 고용률 -13.7684만. 입력 수치는 W01-A에 이미 있는 BOK/고용부/KOSIS 기록값(공표 반올림)을 사용했으며 원자료 개별 항목 전체를 새로 받지 않음. 수치 45%, 67%는 **AI 인과기여 비중이 아니다**.
7. Block SEC 2026-Q2 10-Q Note 19 실제 workforce >40% 감소+계획 Q2 완료 확인, H1 구조조정 $495m. AI 자동화 외 우선순위·성과관리·조직중앙화 복합 요인 공식 명시, '4k all replaced by AI' 불가: https://www.sec.gov/Archives/edgar/data/1512673/000162828026053368/xyz-20260630.htm
8. 미국 BLS OEWS Data Scientists 2022 May159,630 → 2025 May262,440 실제 **고용규모 추정** +102,810 확인, 채용입직+102,810이라는 뜻 아님. https://www.bls.gov/oes/2022/may/oes152051.htm ; https://www.bls.gov/news.release/ocwage.t01.htm ; OEWS 3-year rolling panels/모델 기반 추정 설명: https://www.bls.gov/oes/2025/may/oes_tec.htm
9. LinkedIn 2026 1.3m 'AI related jobs' original methodology = 2023–2025 **job postings** that mention role titles; NOT verified new people hired or net new jobs. https://news.linkedin.com/2026/2026-Davos-Press-Release
10. KLI AI Voucher employment study 2025 actual result: +10.8% demand / +29.5% supply naive comparison vanish when application-rejected controls used; non-capital demand -5.52% subgroup, null != proof of zero; causal effect applies program/voucher package, not all firm AI. https://www.kli.re.kr/eia/asmntRsltView.es?mid=a30301000000&nPage=1&rslt_no=336&sch_asmnt_yr=&sch_keyword=&sch_rel_mnstr=&sch_rschr=&sch_ttl=

## 3. 연구간 충돌 해소 (조건 차이이므로 모순으로 분류하지 않음)
- **BOK -26.8만 vs +24.7만**: 전자는 2022.6–2026.6 청년(15~29)·고노출 산업(industry), 후자는 2023~2026 전체연령·고노출 직업(occupation). 합산/차감 금지; BOK 2026-09는 전체연령 증가 중 20대는 **감소**라고 명시. 서술하면 양립.
- **Stanford/Census young-entrant negative vs Yale full-occupation aggregate null**: 다른 모집단, 종속변수, 표본과 통계력; narrow segment effect와 aggregate null 병존. 나쁜 연구를 다수결로 골라 결정하지 않음.
- **Census QWI -12% vs Stanford -19%**: 산업-주 22–24 회귀조정 고용 *상대 수준* vs ADP 22–25 직업 노출 *상대 추세*; 분모와 기간 다름, 보편 AI 해고율로 사용 금지.
- **미국 채용↓ vs 기업 감원 실증**: W04 QWI cohort/industry에서 job starts↓ and separations↓; W03 Block 특정 회사 직접 감원. 양립 가능; 'AI 해고 없음' 일반화 불가.
- **AI 도입기업 고용증가 vs AI 노출직 고용감소**: 선택편의(도입기업은 성장기업일 가능성)와 직업/기업 단위 다름. KLI 신청탈락기업 대조에서 apparent +10.8/+29.5 사라진 사례가 해당 문제의 직접 실증.
- **한국 NBER Aum/Shin 2025/2026 버전의 표현 변화**: StLouis Fed 2025 published summary는 특히 비IT 서비스 여성과 기술별 교육효과를 강조, NBER 2025 abstract/SSRN 2026 update는 고숙련·여성 부정효과 강조; 같은 저자/연구계열의 **판본 차이** 및 디지털 기술(AI·big data·IoT/클라우드) 묶음. 독립적인 한국 GenAI 연구 2개로 계수하지 않음. 아래 누락 항목으로 연구설계 본문 비교 필요.

## 4. 실질 누락 및 출처 충돌 (W06에서 새로 확인; 우선순위)
### A1 · 핵심 누락: 미국 AI 고노출 고용여건 악화 **ChatGPT 이전 시작**
- Frank et al. (2026-01), arXiv preprint, monthly US unemployment insurance + millions LinkedIn profiles: 고노출 실업위험 **early 2022부터**, 대졸 cohort 2021 이후 entry gap ChatGPT 공개 이전부터 벌어짐; 더 AI노출 커리큘럼 수강한 졸업자는 post-ChatGPT 첫 임금 높고 job search 짧았다는 반례. https://arxiv.org/abs/2601.02554 . **arXiv 원고/동료심사 확정 아님**, Stanford 19%와 2026 Census graduates 5%p/13%에 대한 상당한 대안설명. 서로 AI '노출 전공'과 'AI 관련 강의 수강'은 다른 개념이므로 정면 동일 지표 반증 아님. W02/04 최종 서술 시 인과확신을 낮추고 기간·비교집단 재검토 필요.
### A2 · 핵심 누락: 한국 AI 포함 디지털기술 *고용* 준실험
- Aum/Shin (2025; SSRN rev2026), `The Labor Market Impact of Digital Technologies`. 한국 지역별 기술노출 차이 활용, 고숙련·여성 및 비IT서비스 고용 수요 감소 근거, IT 서비스에서는 높은 숙련직 고용과 공고가 반대 방향. https://www.nber.org/papers/w33469 ; https://www.stlouisfed.org/publications/review/2025/apr/labor-market-impact-of-digital-technologies ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5140715 . **단점** 기술 범위 AI뿐 아니라 빅데이터·IoT/클라우드, 기간 2022 GenAI 직접 효과 측정과 다름. 한국 심층 인과조사의 지역/성별/고숙련 반례로는 반드시 반영 필요; 'AI로 한국 여성 일자리 줄었다'라고 단정 금지. 2025/2026 판본 본문 교차확인 권장.
### A3 · 핵심 누락: 미국 기업 내부 기술 노출과 **직무 대체·고용 상쇄** 함께 측정한 연구
- Hampole/Papanikolaou/Schmidt/Seegmiller, NBER W33509 (2025-09 revision), 2010–2023 기업/직업/업무 AI 노출을 측정, 과거 대학 채용 네트워크 기반 도구변수로 직무 고노출 수요↓ 및 AI 도입 기업 생산성에 따른 타 업무 채용 수요↑를 함께 식별하여 **기업 전체 고용효과는 작음**이라는 결과. https://www.nber.org/papers/w33509 ; https://people.duke.edu/~rampini/HampolePapanikolaouSchmidtSeegmiller2025.pdf . 2010~2023 역사적 폭넓은 AI/ML이라 2023~26 GenAI 효과를 직접 대변하지 않지만 W05의 '상쇄 인과근거 부재'를 **경제 전체 아닌 기업 표본 수준에서 보완**하는 중요 누락. 도구변수 제외제약·연구시점·처치부호 재평가 필요.
### A4 · 핵심 누락: 온라인 프리랜서 고용과 **경력자 피해** 실증
- Hui/Reshef/Zhou (2024) `Organization Science` 35(6), ChatGPT/DALL-E 공개 전후 플랫폼 거래 비교, 고노출 프리랜서 계약/소득 감소. Brookings 저자 요약은 월 계약 약 -2%, 월수입 약 -5%; 과거 실적 높은 숙련 프리랜서도 부정적 영향, 때로 더 큼. https://pubsonline.informs.org/doi/10.1287/orsc.2023.18441 ; https://www.brookings.edu/articles/is-generative-ai-a-job-killer-evidence-from-the-freelance-market/ . **국적 제한 없는 글로벌 플랫폼·정규 급여 근로자 아닌 프리랜서**이므로 한국/미국 전국 일자리 순고용 계수 불가. 그래도 W04 '경력자가 안전' 일반화 및 W02 직접 노동대체 경로를 재평가할 반례.
### B1 · 중요 보강: 한국 실제 AI 숙련 노동자 규모/이동
- BOK 2025-36 (2026-01-09) LinkedIn 직업 이력 1.1m 사용자, AI skill 인력 약 **57,000 (2024)**, AI 보유 근로자 국외취업 약 16% (11,000), 임금 프리미엄 ~6%. https://www.bok.or.kr/eng/bbs/B0000354/view.do?menuNo=400409&nttId=10095619 . LinkedIn 프로필 기반 모델 추정이며 AI 때문에 새로 채용된 순 고용인원 아님. W05의 한국 숙련·직무이동 통계 배경으로 넣으면 강화, 필수 보고서 gate는 아님.
### B2 · 기존 원문 세부검증
- W03 Klarna와 KT 본사 직원 연도별/단독·연결 범위와 감원·자회사 이동 구분, W04 KLI 개발직 채용공고 집계 단위/플랫폼 커버리지, W01 미국 2025/26 CPS 인구통계 기준단절, 2026-08 한국 취업인구 원자료 항목은 **선행 근거문서로 추적 가능**하나 이번 W06에서 원표 전체/모든 수치 1:1 재다운로드 검증은 수행하지 않음. 오류를 발견했다고 주장하지 않고 검증 수준을 다르게 기록.

## 5. 실제 결론 변화
- **보존:** 한미 총고용의 일제 붕괴 아님, 일부 초기경력 고노출 직종 신규입직 위축, 기업 Block의 AI 연계 실제 인력감축, AI 원인에 의한 국가별 순고용 및 상쇄율 *미식별*.
- **강화/보정 필요:** 'AI 때문에 초년 근로자 취업 위축 **유력**'의 확신 정도를 산업별 기존 하락 추세·2021~22 선행 악화 연구를 비교할 때까지 **부분 설명 가설/인과 기여량 불명**으로 약화해 서술. '고용충격이 신입 위주'는 정규직 청년 표본에서는 타당해도 프리랜서 숙련자에게 일반화 금지.
- **추가 검토 시 변화 가능한 핵심:** 일부 IT/디지털 AI 노출 근로자 감소와 기업 내 다른 직무 채용으로 상쇄되는 구조를 측정한 Hampole 연구의 방법론 및 한국 Aum/Shin의 기술별 인과요인 분리; 전자적 플랫폼 프리랜서 실효과가 GenAI 직접 연결을 강화할 수 있음. *국가 전체 순고용 부호*는 이 연구로도 확정 어려움.

## 6. 종료 준비성/추천, 사용자 선택 관문
- 종료 가능성: **조건부·중간~높음**. 기존 큰 결론은 유지되지만 근거 심층성(사용자 최우선 원인 검증)을 고려하면 A1~A4 네 편을 원문 방법·표본·식별 전략 중심으로 짧은 보완조사 1회가 가장 가치 높음. 대규모 W01 재조사/새 자료가 나올 때까지 대기는 권장하지 않음.
- **추천**: 지정된 브랜치에서 A1~A4 원문/모형과 기간을 대조하고 중요한 결론 보정(W02/W04/W05 부록), 그 후 W06 Stage 5 종료 판단을 갱신해 최종보고서 작성할지 사용자 재판단. 외부 프리랜서 연구·옛 AI/ML 기술 연구는 미국/한국 2022~2026 GenAI 자료와 섞지 않는다.
- 대안: 현 근거와 이번 발견한 누락 원문 초록·조건을 한계로 설명해 곧바로 **조건부 최종보고서** 작성하기(보수적으로 확신 수준 낮춤); 아예 광범위한 신규연구(효익 대비 비용 큼).
- 사용자 동의 전 새로운 보완 연구 대규모 확장, 최종 `FINAL_REPORT.md` 작성/확정, Closeout 및 브랜치 병합 금지. 이번 W06 실제 audit 문서만 보존.

## 7. 보고서 반영 규칙 (아직 보고서 미작성)
- 노출≈잠재 업무 가능성, 채택≈기업/근로자 실제 사용, AI causal≈반사실 비교 (별개의 세 층).
- 한국 청년 인구 감소·고용률 변화와 미국 CPS benchmark break를 모든 실제 고용 변화에 연결.
- 고용 stock / 입직 flow / 자발 퇴사·비자발 해고 / 채용공고 / 공고상 AI skills / AI기반 직무명 변경 / 신입 구성비 / 실제 신규 채용 / 비용절감 **서로 다른 지표**, AI 순고용 수치의 무작위 합산 금지.
- 2026 Census working papers, arXiv preprints, 자체 회사/플랫폼 설문, peer-reviewed papers의 근거 등급 명시. 'Census 공식적으로 AI 영향 인정'처럼 과장 금지.
- 2010~23 기존 AI/ML 효과 및 디지털 기술 묶음 vs 2022~26 생성형 AI 효과를 별도 소절/표로 분류.
