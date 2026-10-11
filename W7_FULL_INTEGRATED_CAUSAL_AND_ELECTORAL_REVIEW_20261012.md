# W7 — 트럼프 2기 국정여론 악화와 2026 미국 중간선거: 전체 경쟁 설명·인과 경계 종합검증
기준일: **2026-10-12(KST)**. 관측 종료: 2026-10-12 확인 가능한 공개 자료; 2026-11-03 선거 결과는 **미발생**. 연구 브랜치: `research/20261011-trump-midterms-opinion`. **본 문서 상태: W7 핵심 종합검증 조건부 완료. W8 `FINAL_REPORT.md`가 아니며 Stage 5 편집선택·최종확정은 아직 수행 전.**
근거 기준: 기존 W1~W6 및 사용자 승인 보완 A~E + F(실제 경합지역 한정) 상세 파일, 주요 원문 선택 재조회. 기존 모든 조사 파일과 그래프 유지. 현상 관측·설문 응답·통계 전망·정치 분석가 전망·인과 추론을 구분.

## 0. 연구 질문·판정의 범위
1. **국정평가:** 2025~2026 트럼프 지지율 변화와 2024 투표층 내부의 불만은 어느 정도 실측됐는가?
2. **경쟁 원인:** 경제·관세·이란 전쟁·에너지, 중국·우크라이나·NATO, 이민·ICE, 사법·민주주의/윤리, 재정·의료·주거, 정당 자체 경쟁력과 추가 데이터센터 의제 중 어떤 경로에 시계열·집단·공식 자료가 있는가?
3. **행동 경로:** 국정불만 → 하원/상원 지지 → 실제 11월 투표 → 선거구별 의석 변화에서 어떤 연결고리가 관측되고 어떤 것은 미관측인가?
4. **예측 경계:** 선거 결과를 아직 모르는 상태에서 무엇을 강하게 말할 수 있고 무엇은 확률/승부 단언을 보류해야 하는가?

**판정 언어:** [실측/직접 설문] 자료에 같은 정의의 관측이 있음, [강한 정합] 시간·조사 설문·공식 사건/가격 자료가 여러 경로에서 양립, [그럴듯한 가설] 독립 인과분리는 없음, [반례로 제한] 주장 전체나 강한 버전이 관측과 충돌, [보류/미식별] 신뢰할 자료·실제 결과가 없음. 수치 크기의 단순 증가가 높은 인과 식별력을 뜻하지 않는다.

## 1. W1: 지지율 하락의 시작과 의미
- **2025년부터 하락**: Gallup 미국성인 국정승인 2025-01 47 → 2025-12 36. 2025-07 37, 10월 41로 단조 하락 아님. Pew 미국성인 2025-02 47 → 2026-01 37 → 2026-10 30(가운데 불규칙 조사 시점 있음). Reuters/Ipsos 2026 월별 대표 관측 1월38→7월37→10월32, **월별 동일 조사계약/완전한 월평균 보장 안 됨**.
- **같은 기관/문항의 평가 하락**: Pew 2024-11 정책판단 신뢰 경제59 → 2026-10 35(-24p), 외교53→35(-18p), 이민53→41(-12p). 이는 **국정 승인율이 아니라 해당 정책 판단에 대한 신뢰**. 경제와 외교·이민은 서로 독립 효과가 아니라 동시 불만 가능성.
- **전통 지지층 내부**: Pew 2024 Trump 검증투표층(2024 실제 투표기록, 후보 선택은 당시 사후 자가보고) 국정승인 2025-02 95 → 2026-10 67, 2026-07 75 → 10월67. 현 GOP/Lean GOP의 국정승인과 2024 Trump 투표층은 다른 분모. 직접 대선 투표자 승인 하락이 *하원 민주당으로 실제 이동했다*는 뜻 아님.
- **교차기관 확인**: 2026-10 Pew 국정승인30, Reuters/Ipsos 약32 → 방향은 일치. 절대수준 차이 2p를 기관 간 월간 변화로 측정하지 않으며 모든 조사 설계를 동일하다고 간주하지 않는다.
- **강한 반례**: 이란 전쟁이 2026-02-28 이후 시작됐다면 전쟁만으로 2025년부터의 하락을 설명할 수 없다. 2025~2026-07의 반등/정체도 단일 사건의 선형 충격 모형을 지지하지 않는다.
- 원자료: `W1_SURVEY_TIMELINE.md`, `W1_2026_IPSOS_MONTHLY_RECHECK.md`, `W3_W7_EVENT_CAUSAL_REVIEW.md`, `assets/W1-VIS-F01_gallup_2025_approval.svg`, `assets/W1-VIS-F02_pew_2025_2026_approval.svg`, `assets/W1-VIS-F03_reuters_ipsos_approval_2026.svg`.
- 직접 재확인: https://www.pewresearch.org/politics/2026/10/08/trumps-approval-rating-drops-as-fewer-americans-are-confident-in-his-handling-of-the-economy-other-issues/

## 2. W2: 경제·생활비가 최상위 설명 후보인 근거와 반례
### 2.1 관측 가격·체감·정치적 책임귀속은 서로 다른 자료
- EIA 전국 휘발유 주간 소매평균: 2026-02-23 $2.937/gal → 05-11 $4.500 → 10-05 $4.354. 2월 대비 10월 **약 +48.2% 관측 가격상승**, ***이란 전쟁 단독 기여율이 아님***. 국제 공급·정제·계절·세금·관세 등 다중 원인.
- BLS CPI-U 2025-01~2026-08 **2025년 10월 공식 결측**(연방 셧다운). 관측하지 않은 CPI를 선형보간하거나 2026년 전년동월과 직접 정확히 비교해 유효한 공식 발표치로 둔갑시키지 않는다.
- BEA 2026-08 실질 가처분소득 전월 0.0%와 실질 소비 +0.6% 동시 관측. 이는 소비 증가도 부담 부재를, 소득 정체도 거시 경제 전면 붕괴를 증명하지 않는 반례. BLS 2026-09 제조업 +9천명, 2025-12 저점대비 +7.2만명 관측은 '제조업 완전 붕괴/관세 부흥 인과 확정' 두 강한 주장을 모두 제약. 주거 CPI vs 신규 모기지 대출금리(약7.4%)는 서로 다른 비용 개념.
- **새 W7 원문 대조 — 경제정책에 대한 직접 정치적 평가 (Pew)**: 2025-09 미국성인 '트럼프 경제정책으로 경제 악화' 53%/개선24%, 2026-01 52/28, 2026-07 60/20, 2026-10 65/19. **공화당·공화 성향층** 같은 질문 '악화' 2025-09 19→2026-10 35, '개선' 47→39(2026-01 개선57에서 더 크게 후퇴). **정책 책임귀속이 기존 공화 성향층에서도 악화**하는 중요한 직접 관측. 하지만 객관적인 GDP·CPI 인과효과 자체를 측정한 설문은 아님.
- 같은 Pew 2026-10 **등록유권자** '중간선거 투표에 매우 중요' 경제84%, 의료68%, 에너지54%, 민주주의73%, 이민59%, 외교57%. 여러 쟁점 복수응답형 중요도이며 **각 쟁점의 국정승인 변화 인과율로 산술 분배할 수 없다**.
![Pew 트럼프 경제정책 평가 미국 전체 2025~26](assets/W7-VIS-F02_pew_economic_policy_attribution_all_adults_2025_2026.svg)
[원자료 CSV](assets/W7-VIS-F02_pew_economic_policy_attribution_all_adults_2025_2026.csv) · [SVG](assets/W7-VIS-F02_pew_economic_policy_attribution_all_adults_2025_2026.svg)
![Pew 공화당 성향층 트럼프 경제정책 평가 2025~26](assets/W7-VIS-F03_pew_economic_policy_attribution_republicans_2025_2026.svg)
[원자료 CSV](assets/W7-VIS-F03_pew_economic_policy_attribution_republicans_2025_2026.csv) · [SVG](assets/W7-VIS-F03_pew_economic_policy_attribution_republicans_2025_2026.svg)
- 원문: https://www.pewresearch.org/politics/2026/10/08/cost-concerns-dominate-as-publics-economic-ratings-turn-more-negative/
- 실측 근거: `W2_ECONOMIC_TIMELINE.md`, `W2_INCOME_HOUSING_MANUFACTURING_RECHECK.md`, EIA `assets/W2-VIS-F02_gasoline_2025_2026.svg`, CPI `assets/W2-VIS-F01_cpi_2025_2026.svg`.
### 2.2 관세 책임
- 2025-04 광범위 관세 정책과 NY Fed 연구의 관세 노출 소비재 가격수준 효과는 경제 체감의 경쟁 메커니즘을 뒷받침한다. **소비재 품목의 관세 노출 연구 ≠ 전체 CPI 상승분 중 관세 효과 확정 ≠ 대통령 국정승인 하락 %p 식별**. 2026-02 연방대법원 IEEPA 권한 판결은 *모든 가능한 관세 권한 자체의 폐지*가 아니다.
- 고용·제조업 일부 회복, 실질 소비 증가, 특정 조세정책 지지라는 반례는 '경제 성과 전면 악화'라는 과잉 일반화를 제한한다. 그럼에도 체감 생활비와 대통령의 경제정책 평가 악화가 *정치적 설명력 후보 중 가장 직접적*이라는 판정은 유지.

## 3. W3: 이란 전쟁·에너지 경로는 추가 압박이지만 기존 하락의 원인은 아님
- 사건 순서: 2026-02-28 전쟁 전 2025 Gallup / 2026-01 Pew에서 이미 하락 → 개전 뒤 연료비 상승·불승인 관측 → 2026-10에도 정책 반대 우세.
- Pew 같은 질문 2026-03/10 미국성인: 이란 전쟁 대응 승인 **37→33**, 반대 **61→65**; **공화당·공화 성향 승인 69→63**, 민주당·민주 성향 **9→9**. 후자의 당파별 비대칭은 기존 지지층 불만이 전쟁 평가에도 생겼음을 뒷받침한다. 표본 동일인 추적 결과 아님.
- 2026-10 조사에서 미국성인 **77%**는 이란전 관련 군사작전이 *추가 6개월 이상* 이어질 것으로 생각(6~12개월30 + 1년 넘게47). 미래 전쟁 기간에 대한 **기대**, 실제 전쟁 지속 확정 아님. 전쟁 대응 전체 반대65, 정책목표 달성 신뢰 낮음. Reuters/Ipsos 최대 문제 전쟁 비중 2026-02 1%→03 14%→04 8%, 현저성은 충격 후 하락. 전쟁 반대/이슈 중요도/경제책임의 다른 질문을 합쳐 기여율 산정 금지.
![이란 전쟁 처리 Pew 승인율 2026년 3월과 10월](assets/W7-VIS-F04_pew_iran_war_handling_approval_mar_oct_2026.svg)
[CSV](assets/W7-VIS-F04_pew_iran_war_handling_approval_mar_oct_2026.csv) · [SVG](assets/W7-VIS-F04_pew_iran_war_handling_approval_mar_oct_2026.svg)
- 직접 원문: https://www.pewresearch.org/short-reads/2026/10/08/iran-conflict-remains-deeply-unpopular-as-many-americans-expect-it-to-go-on-for-months/
- 전달경로와 경쟁원인: 전쟁/호르무즈 긴장 → 원유·해상운임·정제·보험비 → 주유소 가격 → 가계 비용 인식 → 경제정책 책임귀속 → 국정평가/선거동기, 각 화살표는 별개의 자료·모형/미식별이 필요. 에너지 가격의 계절·국제 공급 충격 반사실 부재. **이란 전쟁이 2026년의 경제·국정 불만을 추가 악화시켰을 가능성은 강한 시간 정합을 갖지만, 그 추가 효과 크기 미식별**.
- 출처: `W3_W7_EVENT_CAUSAL_REVIEW.md`, `W7_ALTERNATIVE_EXPLANATIONS_ROUND3.md`, 기존 `assets/W7-VIS-F01_war_issue_salience_2026.svg`.

## 4. W3 나머지 외교: 중국·우크라이나·NATO를 경제/전쟁으로 대체하지 않음
- Pew 외교정책 판단신뢰 2024-11 53→2026-10 35; 이는 이란전·대중관계·우크라이나·동맹·기타 사건의 혼합 가능성이 있으며 **외교 단일사건 인과량이 아니다**.
- 중국 대응 Pew 신뢰 2025-08 45→2026-03 39, 우크라이나 40→32(각각 같은 질문 연속 구간). 중국 대중(對中) 미국인 호감도 2025 21→2026 27% 증가는 '미중관계에 대한 모든 평가가 일방 악화' 설명의 반례. NATO는 2026-03 미국 전체의 가입 이익 인식59, **공화 성향38 vs 민주 성향82**로 평가 분리.
- NATO 회원국의 2035년까지 GDP 5% 수준 안보지출 목표 합의는 당시 *미래 목표*, 현재 5% 실제 지출 달성 실측이 아님. 우크라이나 전쟁의 지원 찬반·러시아 비호감·휴전 협정의 실질 이행을 구분한다. 2026-10 러시아/우크라이나 연료·휴전 제안의 공식 양측 합의·집행 및 사건 후 여론은 확보 못해 결론 근거에서 제외.
- 위 외교 평가를 직접 '중간선거 민주당 득표 몇 %p'로 전환할 교차표·동일개인 인과자료 부족. **외교 신뢰 하락은 독립적인 설명영역으로 채택, 구체 선거효과는 미확인**.
- 정본: `W3_CHINA_UKRAINE_NATO_20261012.md`, `W7_COMPETING_EXPLANATIONS_W3_W4_20261012.md`, `assets/W3_W4-VIS-F01_pew_policy_confidence_2024_2026.svg`, `assets/W3-VIS-F04_pew_nato_membership_benefit_2026.svg`. NATO 원문: https://www.pewresearch.org/short-reads/2026/04/06/republicans-have-become-less-likely-to-say-nato-membership-benefits-the-us/

## 5. W4 국내 정치: 이민 목표·집행, 사법, 건강보험/재정의 분화
### 5.1 이민
- Pew 미국성인 '불법체류자 추방 과도' 2025-02 **44→2025-10 53→2026-04 52**; 공화 성향 2026-04 **19**(반면 '너무 적다' 공화 성향28), 민주 성향84. 2026-02 ABC/WaPo/Ipsos **모든 불법체류자 추방 찬성50%, ICE 집행 전술 반대62%, ICE 폐지 반대50%**. 질문 다른 논점들을 의도적으로 분리.
- 따라서 **집행전술 반발 ≠ 모든 추방 반대 ≠ ICE 전면 폐지 지지**. Cook 경쟁하원 37곳의 '이민 문제 대응' 상대적 정당 신뢰 공화 **+5p**는 '공화당의 이민 정책 강점이 완전히 사라졌다' 주장에 반례.
- 원문: https://www.pewresearch.org/short-reads/2026/05/04/about-half-of-americans-continue-to-say-trump-administration-is-doing-too-much-on-deportations/
### 5.2 법원·제도·윤리
- 2026-02 *Learning Resources v. Trump* IEEPA 관세권한 해석 제한. 다른 법적 근거의 관세와 개별 사건의 항소/집행정지는 별도. 2026-10 Pew **69%는 트럼프가 공직 결정에서 개인사업 이해를 분리할 것으로 신뢰하지 않는다**(미국성인). 2026 중간선거 경제84 이외에 **민주주의73%** '매우 중요'(등록 유권자, 16개 주제 가운데 응답). 중요하다는 답 = 단일 방향 정치성향이나 특정 제도 위험 평가가 아님.
- 원문: https://www.pewresearch.org/politics/2026/10/08/trumps-approval-rating-drops-as-fewer-americans-are-confident-in-his-handling-of-the-economy-other-issues/
### 5.3 재정·의료
- 2025 조정법(P.L.119-21) CBO 추정: *2025~2034* 적자 증가 약 **$4.2tn(미래 전망/특정 기준선)**, *2026~2035* Medicaid 지출 약 **-$1.2tn(미래 전망)**. 2034 무보험자 추가 약 750만명도 별도 모형추정(정의·기준선 재확인 필요), **2026 실제 보험 미가입·가계 피해 숫자로 전용 금지**.
- KFF 등록유권자 의료비 문제 처리 정당 신뢰 2026-04 **민37 / 공26**, 2026-09 **민42 / 공22**. 하지만 자당의 세금정책/부정수급 대응을 지지하는 별도 표본·문항은 다른 결과를 줄 수 있으므로 의료 정책 전체의 민주당 절대 다수 지지로 단정 불가.
- 출처: `W4_IMMIGRATION_JUDICIARY_FISCAL_HEALTH_20261012.md`, `assets/W4-VIS-F02_pew_deportations_too_much_2025_2026.svg`, `assets/W4-VIS-F03_kff_healthcare_party_trust_2026.svg`, https://www.cbo.gov/publication/62105 , https://www.kff.org/public-opinion/kff-health-tracking-poll-health-care-issues-in-the-lead-up-to-the-2026-midterm-election/
- **W4 설명력 판정:** 국내 갈등은 경제 외 대안 설명으로 반드시 존치. 실제 ICE 집행 건수/피해-혜택·소송 최종 판결·메디케이드 시행지역과 하원 후보 변화의 독립효과는 미확인.

## 6. W5: 기존 2024 지지연합의 '불만→선거 의향' 연결 검증
- Pew 2026-09-28~10-04 **등록유권자**의 2024 검증 대선 투표집단:
| 2024 집단 | 2026 공화당 하원 | 2026 민주당 하원 | 기타 | 미결정 |
|---|---:|---:|---:|---:|
| Trump | 77 | 5 | 5 | 13 |
| Harris | 3 | 87 | 3 | 7 |
| 2024 비투표/당시 투표 부적격 포함 | 26 | 39 | 6 | 29 |
- Trump 2024 중 현 GOP 비호감 하위 약25%: 공화하원49, 민주하원12, 기타14, 미결정25. Harris 2024 중 민주당 비호감 하위 약25%: 민주하원73, 공화하원8, 기타5, 미결정14. Trump 코어의 불만은 *민주당 즉시 전향보다는 기존 공화 결집 약화와 미결정*이 더 두드러짐.
- **행동 정의가 다름:** Pew의 2024 투표했다는 사실만 공식 유권자 명부로 검증, 2024 누구 선택했는지는 직후 자가 응답. 2026 하원 후보는 현재 사전 선호. 이것이 2024 대선→2026 하원 **동일인 실제 투표 전환 및 기권**을 확정하지는 않음.
- Pew 2026 하원 **민주 후보 지지자 vs 공화 후보 지지자**의 '투표 의욕 매우 높음' 민주 **63 vs 46**, 선거 많이 생각함 50 vs36, 승리 정당 중요78 vs69. Reuters 별도 문항 2024 Harris 지지집단 매우 열성48 vs Trump30도 방향 유사, 설문/분모 달라 통합 지표 금지.
- 과거 투표기록 검증 2022+24 양쪽 투표 집단 현재 하원 민주47/공화41; '극도 투표 의욕' 집단 민주59/공화35. **투표의욕층과 실제 예상 투표층은 같지 않음**. 2024 비투표자 2026 등록유권자 중 미결정29로 분모/미투표자 정의 차이 큼.
- 원자료: `W5_2024_VOTER_COALITIONS_AND_TURNOUT_20261012.md`, `assets/W5-VIS-F01_2024_coalitions_2026_house.svg`, `assets/W5-VIS-F02_disaffected_2024_voters_2026_house.svg`, `assets/W5-VIS-F03_congressional_engagement_2026.svg`.
- Pew 원문: https://www.pewresearch.org/politics/2026/10/08/with-americans-in-a-sour-mood-democratic-voters-are-more-engaged-in-midterms/
- **W5 결정:** 기존 2024 공화 지지층에 취약성이 증가한 것은 직접 관측. 민주당 전향+기권/저투표 의욕의 개인별 시계열 인과 분해는 불가능.

## 7. W5 추가 C: 투표율 역사 경로는 높은 의욕을 확정 결과로 만들지 못함
- Census CPS 시민 투표연령인구(CVAP) 대상 조사 2018 중간 **53.4%**, 2022 **52.2%**. Pew 공식 하원 유효 투표표/추정 유권자격(VEP) 2018 **48.1%**, 2022 **45.1%**. **두 측정계열은 분모/분자/통계법이 달라 한 연속 그래프/수치 차이로 계산 금지**.
- Pew 2022 검증 연구에서 2020 Trump 대선 투표층이 2022 중간선거 실제 참여 **71%**, Biden 투표층 **67%**. 공화당 하원 전국표 우세의 상당 부분이 기권/참여 구성효과였고, 두 선거 모두 참여한 유권자의 직접 정당 전환은 상대적으로 적었음. **이는 2026 Harris/Trump 투표층이 같은 결과를 낸다는 예언이 아니라 역사적 경쟁 메커니즘**.
- 인구조사국 CPS 2022 투표자에서 선거일 전 투표 47.1%, 우편투표 31.8%; 두 범주는 겹친다. 2026-10 현재 전국 모든 주의 조기투표 수·정당/투표용지를 균질한 자료로 취합하거나 11월 실제 투표율을 추정하지 않았음.
- 보존: `W5_C_HISTORICAL_TURNOUT_20261012.md`, `assets/W5C-VIS-F01_census_midterm_citizen_turnout_2018_2022.svg`, `assets/W5C-VIS-F02_pew_house_vote_turnout_2018_2022.svg`. 원문 https://www.census.gov/newsroom/press-releases/2024/congressional-election-voting-report.html ; https://www.pewresearch.org/short-reads/2023/03/10/turnout-in-2022-house-midterms-declined-from-2018-high-final-official-returns-show/ ; https://www.pewresearch.org/politics/2023/07/12/republican-gains-in-2022-midterms-driven-mostly-by-turnout-advantage/

## 8. W6: 전국 등록유권자→경합 하원→개별 후보→상원, 추론 강도 감소
### 8.1 단면 및 정치 분석의 구분
- Pew 2026-09-28~10-04 전국 **등록유권자(RV)** 하원 후보 선호 **민44 / 공36**, 제3후보5·미결정15. 많은 지역구에서 실제 후보 이름을 제시하고 일부 예외 generic 선택. 같은 조사의 대통령 국정승인30은 **미국 성인** 분모. Reuters/Ipsos 2026-10 RV 민주44/공화37와 대체로 방향 일치하나 모집단/문구/시기별 절대값을 연결한 여론조사 평균을 만들지 않음.
- Cook 2026-09-08~11 **37개 선별 경합 하원 선거구 LV n=1052** 민주49/공화47, 표본오차 ±3.02%p는 전체 선별 묶음에 대한 설명; 37개 각각에 적용할 수 있는 독립 district poll은 아님. 평균 2024 Trump +5p 지역들이지만 **2024 대선 후보와 2026 하원 의석은 다른 투표**이므로 단순 '개인의 7p 민주전향' 불가. 2026-04 경합지역 36곳과 9월 37곳의 집합이 달라 50/44→49/47 격차 변화도 고정 패널 추세가 아님.
- NY-21 Siena 2026-10 실제 지역 후보 민주 Gendebien46/공화 Constantino42(LV), **같은 응답자 의회장악 선호 공화50/민주45**: *후보 개인평가와 정당 전체 선호 사이의 차이*를 보여주는 선명한 반례. 양당 전체 선호-후보 실제 선호 혼동 금지.
- Cook 2026-10-09 전문 판정상 **18개 하원 등급 민주 방향 조정**, **민주당 순증9~19석 / 추정 총224~234석**은 **전문가 판세/시나리오**, 단일 조사 투표예측 확률이나 11/03 개표 결과 아님.
### 8.2 상원: 다른 선거구와 의석 산술
- 현 상원 공화53 / 민주 및 민주계 무소속47. 민주당이 공화당 부통령의 동수 결정권을 넘어 다수당이 되려면 정적 전제 아래 **순증4석** 필요. 모든 100석이 아니라 선거 대상 일부(정규+보궐)의 후보/상황이 중요.
- NYT/Siena 2026-10-03 **서로 다른 5개 주 LV 조사**: AK 민주50/공화43, IA 민주47/공화48, KS 45/45, OH 민주49/공화46, TX 민주51/공화45. 한 설문프로젝트의 5주 선별 관측일 뿐 전체 경합주 동질 평균/승리 확률 아님. Kansas 민주 후보 명칭은 Siena 홈페이지에서 `Adam Hamiliton` 오자로 보이며 **최종 후보 공식 명단 철자 미재확인**, 후보 이름이 핵심 아닌 비교표에서 현재 비율만 사용.
- NC Cooper vs Whatley, ME Troy Jackson vs Susan Collins, GA Ossoff vs Mike Collins, MI El-Sayed vs Rogers는 각 조사자·문구/모집단·후보 효과 달라 한 시점의 합산 승률로 환산하지 않음. MI 후보 숫자 없는 것은 미검증 수치를 창작하지 않기 때문.
- 원자료: `W6_HOUSE_SENATE_BATTLEGROUND_POLLS_20261012.md`, `assets/W6-VIS-F01_siena_senate_five_states_2026.svg`, `assets/W6-VIS-F02_cook_37_battleground_house_2026.svg`.
- 직접 출처: https://www.cookpolitical.com/analysis/house/house-overview/eighteen-more-house-race-ratings-move-democrats-favor ; https://www.cookpolitical.com/survey-research/2026-battleground-district-project ; https://sri.siena.edu/2026/10/03/nytimes-siena-poll-of-likely-voters-senate-races/

## 9. 승인 보완 A~F가 전체 해석을 실제 어떻게 강화했는가
| 보완 ID | 연구 고유 관측/반례 | W7 결론에 주는 의미 | 현재 잔여 |
|---|---|---|---|
| A 선거구 경계 | Census 2026 실제 변경 9주; Missouri 9/23 미 연방대법원 결정 뒤 **2022/24 옛 지구 유지**; 10/07 BEF 재생성, 일부 GIS는 과거 미주리 신지도 | 2024 특정지구의 대선 지지와 2026 하원 전망을 비교할 때 경계 일치 필수. **Cook 9/10 지도효과 GOP 순이득 약4석은 9/23 법원결정 이전 전망**이라 현재 적용 확정값으로 인용 불가 | 전구 새 PVI/2024 경계재집계·정치분석가 최신 순의석 모델 B |
| B 조사 편향 | Pew 2024 전국 여론조사 약70%가 정치가중 사용, 2020·24 자체 사후조사 정확도 후보별1~2p, 격차2~3p 개선 | '과거 Trump 과소추정이므로 2026 전국 민주 지지율에서 3p 삭감'은 허용 불가. 가중치도 공화 응답자 내부 비대표성 해결 못함 | 상원 개별 topline/MOE 전수·가중효과 지역별 실증 B |
| C 역사/조기 | Census CPS CVAP 2018 53.4/2022 52.2; Pew House/VEP 48.1/45.1, Trump2020 2022참여71 vs Biden67 | **중간선거 실제 결과는 동기보다 구성과 참여가 중요할 수 있음**. 2026 민주당 높은 설문 의욕은 실제 승리를 확정하지 않음 | 2026 실제 turnout 사후 전까지 E |
| D 후보·자금 | FEC 2025-01~2026-06말 의회후보 수입 $2799.1m·지출 $2036.7m, 정당/PAC는 별도 계정; FL-14 광고 관측 공화$6.3m·민주$3.8m; Cook 후보 유형 가상질문 차이 | 금액·후보 기조·현역이 각 의석 경쟁에 영향을 줄 수 있지만 **돈→득표 인과 계량 미실시**. 전국 +8p 여론을 선거구에 그대로 적용 금지 | 9~10월 FEC 최신/지출효율·후보 호감자료 B |
| E 민주당 자체 경쟁력 | Pew 2026-10 미국성인 정당 호감 민주40/비호감58, 공화 호감37/비호감61. Cook 경합 LV 의회 양당 호감41/비호감56 | **반트럼프/민주후보 선호와 민주당 정책 열광은 구별**. 민주당 지지층의 의욕과 양당 비호감이 동시에 가능 | 정책공약별 직접 선호·개인 동기 분리 B |
| F 경합 지역 한정 | Pew 2026-10 지역 데이터센터 건설을 지지하는 정치인을 **싫어함 61% RV**, 민주 지지층75·공화44; Ohio Senate·PA-08 House에서 전력비/센터 입지 논쟁 | 기존 주유비/관세뿐 아니라 **전력비·AI 인프라 유치**의 지역 체감경제 경로 가능. AI '매우 중요한 투표 의제'44 < 경제84. 전국 전기료 인과효과/투표 득표 효과 입증 아님 | 주별 전력회사 실제 계약/설비 효과·후보 연계 독립 설문 B |
- 보완 상세: `W6_A_REDISTRICTING_STRUCTURE_20261012.md`, `W6_B_POLL_ERROR_AND_METHOD_20261012.md`, `W5_C_HISTORICAL_TURNOUT_20261012.md`, `W6_D_CANDIDATE_MONEY_INCUMBENCY_20261012.md`, `W5_W6_E_PARTY_APPEAL_VS_ANTI_TRUMP_20261012.md`, `W4_W6_F_DATACENTERS_ENERGY_SWINGDISTRICTS_20261012.md`, `W7_PREFLIGHT_BALANCED_SUPPLEMENT_A_F_20261012.md`.
- 중요한 보완은 **원래 W1~W6에 없는 고유 결과**이므로 단순 링크나 '기타 변수' 한줄로 뭉개면 향후 Full Report 상세형 수록 불충실. 그러나 서로 연계된 내용을 W2/W5/W6 절에 충분히 통합하는 것은 허용.
- 주요 외부 대조: https://www.census.gov/programs-surveys/decennial-census/about/rdo/congressional-districts.html ; https://www.pewresearch.org/methods/2026/09/16/weighting-polls-on-party-affiliation-and-past-vote/ ; https://www.fec.gov/updates/statistical-summary-of-18-month-campaign-activity-of-the-2025-2026-election-cycle/ ; https://www.pewresearch.org/politics/2026/10/08/midterms-2026-appendix-additional-charts/ ; https://www.pewresearch.org/politics/2026/10/08/economy-ranks-as-top-issue-in-midterms-for-all-voters-but-partisans-differ-over-the-importance-of-other-issues/

## 10. 가설별 증거·반례·최종 판정 매트릭스
| ID/경쟁가설 | 지지 관측 | 강한 반례 / 교란·대체 | W7 판정 |
|---|---|---|---|
| H1. 트럼프 국정 지지율 하락은 표본변화만의 착시다 | Gallup2025/Pew2025~26/Ipsos2026 기관별 시간 하락, 검증 Trump2024 집단 승인95→67 | 기관 설계·필드·응답자 비동질성, 2026-07 부분 반등 | **기각에 가까움**: 장기 하락 관측은 다중 자료로 강함; 정확한 동일인 변화·단기 월별 크기는 제한 |
| H2. 모든 하락은 2026 이란 전쟁 때문 | 개전 후 유가 상승, Pew 전쟁 대응불승인65, 공화 승인69→63 | 전쟁 이전 2025 승인하락, 2026 일부 반등, 유가 외 대안 | **전 기간 단독원인은 반증**; 전쟁 이후 추가 경로는 그럴듯, 효과 크기 보류 |
| H3. 생활비·관세/경제정책은 주요 불만 설명 경로 | 경제 의제중요84; Pew 경제정책 악화 평가2026-10 65, GOP악화35·개선39; EIA 실측·BEA | 제조업 최근 저점 후 증가·실질 소비 증가, 관세/전쟁 비용 귀속 교란 | **상대적으로 가장 직접적인 정합 증거**. *국정승인 -n%p*의 인과 크기 미식별 |
| H4. 이민 문제에서 공화당의 모든 경쟁 우위가 붕괴했다 | 추방 과도52, ICE 전술 반대62 | 추방 정책 목적 일부 지지, 공화 lean 추방 과도19, Cook 경합 이민신뢰 R+5 | **강한 일반화 기각**; 집행방식에 대한 갈등은 독립 유효 |
| H5. 중국·우크라이나·NATO 반발이 국정 하락의 독립 원인 | 외교정책 신뢰53→35, 당파/지역 평가의 차이 | 중국 호감 증가, NATO 2035 목표, 미확정 제안, 투표 교차자료 부재 | **대안 설명 존재**; 독립 인과 크기 미확인 |
| H6. 법원·민주주의·윤리는 경제보다 무관 | 민주주의 선거중요73, 사업이해 분리 신뢰 부족69, 법원 관세권 판결 | 중요도는 특정 법정판결이나 특정 후보 지지 직접 측정 아님 | **무관 주장 지지 어려움**; 성격·기여율은 보류 |
| H7. 재정·Medicaid 피해는 이미 2026 실측됐다 | CBO 장기 지출/적자 예상, KFF 의료비 정당신뢰 D+20 | CBO 2034/35 전망이며 실제 피해 집계가 아님, 다른 의료정책/당파 신뢰 반례 | **실현된 결과 주장 기각**; 미래 부담/정당 정책 갈등은 중요 |
| H8. 2024 Trump 투표자 불만=민주당 전향 | Trump2024 국정승인67 vs 초기95 | 현재 GOP하원77/DEM5/기타5/미결정13, 자당비호감층도 GOP49 | **직접 전향 일괄설 기각**. 결집약화·미결정 더 두드러짐 |
| H9. 민주당 투표 의욕 우세=실제 투표율·의석확정 | Pew 민주 극도의욕63 vs 공화46, 2024 Harris vs Trump 적극의욕 차 | 2022 공화 실제 turnout우세, 2024+22 검증투표층 하원 민주47/공화41, 표본조사 예측오차 | **사전 환경상 민주에 유리한 신호**, 실현/승률 미확정 |
| H10. 전국 D+8이면 모든 하원에서 D+8·상원 장악 | 전국 Pew RV D44/R36 | Cook 경쟁37 LV D49/R47, NY21 실제 후보 vs 정당 장악 선호 엇갈림, 주별 상원 5개 LV 제각각 | **불가**: 지역·투표가능집단·후보·지도/돈·상원 의석산술 분리 |
| H11. 민주당이 유리한 이유는 민주당 자체 인기가 압도적이기 때문 | 전국 하원 D선호 및 일부 상원 LV 우세 | 민주 정당 호감40/비호감58, 경쟁지 양당 비호감56, 반트럼프 투표동기44 | **불충분**: 반정부/동원/후보별 경쟁 설명이 필수 |
| H12. AI·데이터센터가 전국 선거의 최대 단일 원인 | AI 투표중요44, 데이터센터 지지 정치인 비호감61, Ohio/PA08 사례 | 경제84, 지역 사례 대표성 부족, 입지/전력 실제 효과 계산 부재 | **전국 최대 설명 기각**; 지정 지역 추가 경로로 유지 |

## 11. 인과 식별 감사: 실제 관측·가정·불가능한 숫자
### 11.1 서로 다른 수준의 종속변수
| 단계 | 측정치 | 현재 상태 | 잘못된 연결 |
|---|---|---|---|
| 국정 승인 | Pew 30% 미국성인/Reuters32% 등 | 2026-10 시점 여론 관측 | 각 이슈 반대 비율을 국정승인 전체 원인으로 산술 합산 |
| 정책 신뢰/책임 인식 | 경제판단 신뢰35, 정책 악화 평가65, 이란 전쟁 승인33, ICE 집행 반감 | 서로 다른 정책·같은 개인 여부 불명 | 정책별 35/65를 국정 승인30과 직접 차감 |
| 정당·후보 하원 선택 | Pew RV D44/R36, Trump2024 그룹 GOP77/DEM5 | 사전 선택(등록유권자) 관측 | GOP 불만23% 전부 민주당 득표로 처리 |
| 투표 의욕·가능성 | 민주 후보지지층63% 극도동기, Cook LV 사전 | 자가 동기·모형 분모; **실제 참여는 미래** | 동기63%=투표율63% 주장 |
| 실제 최종 투표 | 2026-11-03 선거 | **기준일 미발생** | 현 여론을 실제 투표 집계라 표현 |
| 하원·상원 의석 | 지구별 득표 집계, 상원 주별 승리 | 전문가 전망 외 실제 미발생 | 전국 민주+8을 의석 8%/당선확률로 바꿈 |
### 11.2 식별 장벽
- 개인별 2024→26 정책평가·국정승인·하원후보선호·투표이력/실현의 연결 다변량 패널, 주별 노출·후보/정책 실행 차이, 동시 경제/전쟁 충격의 충분한 대조군과 반사실 설계 없음.
- **공통방법 편향**: Pew 같은 시기 불만 여러 질문은 하나의 응답자 정치정체성이 공동 원인일 수 있음. 정책문제에 대한 반응과 국정승인/정당지지가 동시에 변한다고 각각이 *독립된 원인*인 것은 아님.
- **선택·모집단 편향**: 미국 전체 성인 vs RV vs LV vs 검증 2024 투표집단, Cook 선별 37구, Siena 5주. 2026 새 지구 경계와 2024 구지구 자료 매칭도 오차 가능.
- **시간/역인과**: 유권자가 대통령을 싫어하기 때문에 경제책임·정당정책을 낮게 평가할 수도 있음. 가격 실측의 정책 인과·정치적 책임귀속의 방향을 동일시하지 않음. 2025 이후 다양한 사건이 겹쳐 10개 시점의 승인지표만으로 회귀계수를 만들지 않음.
- **미래 예측불능과 불확실성**: 과거 여론조사 체계적 편향/주별 오차 공분산, 미결정층·기권·조기투표, 후보자금 최신성과 2026-10 후속 사건. 2026 결과/승률 모델이 없으므로 **확정 의석수·승리확률 작성 안 함**.
- **강한 경쟁 설명을 뒤집을 새 자료가 있다면**: 동일 개인에게 정책책임/선호를 독립적으로 조사한 패널과 실제 turnout 검증, 정책노출별 자연실험, 현 지도와 동일 기준 district panel, 새 제재/외교합의 실행 및 사건 전후 동일문항 반복. 현재 자료로 원인별 포인트 분해를 불가능하다고 밝히는 것은 조사의 실패가 아니라 정직한 결론.

## 12. 현 시점에서 독자가 이용할 수 있는 종합 판단 (시나리오·불확실성)
### 신뢰 높은 관측
1. **장기 지지율 하락**은 2025~26 기관별 반복 조사와 같은 2024 투표집단 내부 평가에서 대체로 확인. 전쟁만의 결과 아님.
2. **생활비/경제**는 유권자 중 가장 폭넓게 중요한 문제이며, 트럼프 경제정책이 악화시켰다는 인식이 증가. 당파적 정체성만으로 설명되는 일률적 평가 아님(공화 성향 악화35).
3. **2024 Trump 지지자의 민주 하원 직접 선택은 5%**라는 사전 조사값, 미결정/다른 후보/국정불만은 별개.
4. **민주당 유리한 선거환경**: 전국 Pew RV 하원 D+8, Cook 경쟁지 LV D+2, 민주 후보지지층 동기 더 높음. 그러나 모든 하원/상원 실제 승리 확정 안 됨.
5. **양당 자체 비호감**: 반트럼프 정서·의회 견제 동기와 민주당 정책·후보에 대한 긍정 지지가 혼합.

### 조건부 시나리오 — 자체 확률·의석수 아님
- **민주당에 유리한 현실화 경로**: 현재 민주당 후보 우세 + 상대적으로 강한 실제 turnout + 경합지역 내 후보 경쟁력/지구 경계에서 구조적 우위가 겹칠 때. 이는 설명의 경로이지 자동 승리 예측 아님.
- **공화당 방어 경로**: 트럼프 국정 불만층도 GOP 하원 후보를 선택(현재 Trump2024 GOP77), 2026 미결정·기타층의 공화 재결집, 이민 신뢰/현역/선거자금 이점, 하원 선거구 경계/상원 주별 구조가 국지적으로 작용할 때.
- **불확실성 지속 경로**: 2026-10 후속 외교·경제 사건, 투표/여론 응답 비대칭, 경합 상원의 매우 좁은 선호 차이로 지역별 승패가 갈릴 때. Cook 하원 전망과 Siena 상원 단면은 **시점 조건이 붙은 전문가/설문**으로만 인용.
- **비전형적 변수**: 데이터센터 관련 지역 전력비·개발 갈등은 Ohio/PA08 등에서 추가 중요할 수 있지만 미국 전체 표의 방향을 판정할 결정적 증거 아님.

## 13. 결과별 보존·시각자료/근거 대조와 미래 Full Report 수록 후보
| 정본·근거 묶음 | 이 W7의 실제 설명 위치 | 중요 그림 실물 또는 표 | Stage 5 이후 상세 반영 감사 항목 |
|---|---|---|---|
| W1 Gallup/Pew/Ipsos | §1, §10 H1 | W1-VIS-F01/F02/F03 | 기간별 실제 수준·반등·기관/모집단 |
| W2 CPI/EIA/BEA/관세 | §2~3, §10 H2/H3 | W2-VIS-F01/F02, **W7-VIS-F02/F03 신설** | 전쟁 전 하락, 유가 관측/인과 구별, CPI 결측, 경제정책 직접 인식 |
| W3 이란/중국/우크라이나/NATO | §3~4, §10 H2/H5 | W7-VIS-F01/F04, W3-VIS-F04, W3_W4-VIS-F01 | 이란 당파별 전쟁 지지 변화, 동맹 합의 목표·성과 차이 |
| W4 ICE/사법·재정/보건 | §5, §10 H4/H6/H7 | W4-VIS-F02/F03 | 목표 vs 집행, 법원권한 범위, CBO 전망 연도 |
| W5 2024 투표 연합·의욕 | §6~7, §10 H8/H9 | W5-VIS-F01~03, W5C-VIS-F01/F02 | 기존 지지층의 미결정·선호 vs 기권/실현 |
| W6 전국/지역/상원 | §8, §10 H10 | W6-VIS-F01/F02 | 전국 RV/경합 LV/상원 각주, Cook 전망·실제 결과 구분 |
| A 선거구 경계 | §9 A, §11 | 원문 Census, 신규 지도 부재(동일지도 조건을 문장으로 명시) | 미주리 판결 시차·새 지도와 구지도의 교차 |
| B 조사오차 | §9 B, §11 | 원문 Pew 정치가중 설명 | 2024 오차를 2026 숫자에서 임의로 빼지 않음 |
| C 역사투표율 | §7, §9 C | W5C-VIS-F01/F02 | Census CVAP vs Pew VEP 따로 유지 |
| D 후보/선거자금 | §8~9 D | W6D-VIS-F01 | FEC 후보/PAC 시점 차이, FL14 광고만 지역 사례 |
| E 민주당 정당호감 | §9 E, §10 H11 | W5E-VIS-F01 | 실제 하원 후보 선호와 전체 정당호감 분리 |
| F 지역데이터센터 | §9 F, §10 H12 | W4F-VIS-F01 | 지역 전력비·산업편익·전국화 금지 |

- 위 표는 **연구자료→W7 원문 연결의 실제 근거 범위 확인**, 아직 존재하지 않는 `FINAL_REPORT.md`에 반영 완료되었다는 뜻은 아님. Stage 5에서 사용자 편집 선택을 받고 Stage 6/7 최종 원고에서 **본문/상세부록의 실제 서술**을 양방향 대조해야 한다. 최초 W-ID와 승인된 A~F를 동등 취급한다.
- 이 W7 본문에서 W1~W6 기존 원자료/추가 보완의 독립 정보가 모두 다시 재현된 것은 아니지만 각 결론의 관련 파일·불리한 반론·미확인 경계를 설명해 최종 수록 후보로 연결. **최종 Full Report 상세형은 각 주제의 고유 내용을 단순 링크 목록으로 축약할 수 없다.**

## 14. W7 완료 게이트·남은 작업
- **W7 실질 통합검증 판정: 조건부 완료** (연구자료·독립기관 근거·원문을 대조한 다원 인과한계·행동전환/예측한계 검증 완료). 전체 여론/정치 인과 계량 식별·435개 선거구 모델·실제 11월 투표는 현재 W7 목적 밖/기준일 미발생으로 보류. 핵심 사실과 반례를 조사 결과로 설명 가능.
- **선택적으로 국소 재검증 가치:** 원문 설계가 미확인인 개별 상원 접전조사, Cook 지도효과 모델 구판 수정, 최근 대러시아/우크라이나 제안 실제 이행, FEC 최신 후보 현금·전력비 실측. 이를 보류 사실로 표시하고 가용 자료로 조건부 결론을 제시. 단, 더 강한 의석/외교 결과를 최종 결론으로 주장할 경우 해당 분야는 A로 격상하여 확인해야 함.
- **W1~W6** 기존 핵심 본조사의 '조건부 완료' 판정 유지, 승인 보완 A~F는 위 내용으로 반영. **Stage 5** 연구 종료가능성·사용자 Full Report 상세 수록 수준/장별 중요도·압축/상세부록/제외의 중요 편집 선택은 **미실시**. **W8** 최종원고·확정·외부 게시는 **미착수**.
- **다음 한 작업:** W7 결과를 사용자에게 공유한 뒤 Stage 5 종료 가능성 및 실질 결과 기반 편집 선택 제안. Stage 5 원문 파일 목록에는 W1~W6뿐 아니라 위 **6개 A~F 단독 파일과 최신 W7 증거/시각자료**를 포함한다. 출처 불충분 영역을 조건부로 처리하며, 선택받지 않은 별도 G(선거관리 확대) 같은 신규 작업을 자동 시작하지 않는다.

## 직접 독립 대조한 주요 출처 (중복 링크는 상위 본문에 있음)
- Pew 국정승인/정책 신뢰: https://www.pewresearch.org/politics/2026/10/08/trumps-approval-rating-drops-as-fewer-americans-are-confident-in-his-handling-of-the-economy-other-issues/
- Pew 비용·트럼프 경제정책 책임 평가: https://www.pewresearch.org/politics/2026/10/08/cost-concerns-dominate-as-publics-economic-ratings-turn-more-negative/
- Pew 이란 분기 평가: https://www.pewresearch.org/short-reads/2026/10/08/iran-conflict-remains-deeply-unpopular-as-many-americans-expect-it-to-go-on-for-months/
- Pew 2026 총선 하원후보/기존 연합: https://www.pewresearch.org/politics/2026/10/08/with-americans-in-a-sour-mood-democratic-voters-are-more-engaged-in-midterms/
- Pew 16개 의제: https://www.pewresearch.org/politics/2026/10/08/economy-ranks-as-top-issue-in-midterms-for-all-voters-but-partisans-differ-over-the-importance-of-other-issues/
- Pew 가중치: https://www.pewresearch.org/methods/2026/09/16/weighting-polls-on-party-affiliation-and-past-vote/
- Pew 정당호감/정책신뢰 부록: https://www.pewresearch.org/politics/2026/10/08/midterms-2026-appendix-additional-charts/
- Census 지구(2026 실제): https://www.census.gov/programs-surveys/decennial-census/about/rdo/congressional-districts.html
- Census 투표율: https://www.census.gov/newsroom/press-releases/2024/congressional-election-voting-report.html
- Pew 과거 참여: https://www.pewresearch.org/politics/2023/07/12/republican-gains-in-2022-midterms-driven-mostly-by-turnout-advantage/
- EIA 휘발유: https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?f=W&n=PET&s=EMM_EPMR_PTE_NUS_DPG
- KFF 의료: https://www.kff.org/public-opinion/kff-health-tracking-poll-health-care-issues-in-the-lead-up-to-the-2026-midterm-election/
- CBO 전망: https://www.cbo.gov/publication/62105
- Cook 경합지 여론: https://www.cookpolitical.com/survey-research/2026-battleground-district-project
- Cook 10/09 전문가 판정: https://www.cookpolitical.com/analysis/house/house-overview/eighteen-more-house-race-ratings-move-democrats-favor
- Siena Senate 10/03: https://sri.siena.edu/2026/10/03/nytimes-siena-poll-of-likely-voters-senate-races/
- FEC 선거자금: https://www.fec.gov/updates/statistical-summary-of-18-month-campaign-activity-of-the-2025-2026-election-cycle/
