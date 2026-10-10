# FINAL_REPORT_COUNTERARG_AUDIT — 완성본의 핵심 반론·비교 연구 누락검사 및 국소수정
검토일: 2026-10-10. 원규칙: `domato153/General_research_GPT@fb22fe86834893e607072b41885277d29cfc57fc`.
연구 브랜치: `research/20261010-ai-employment-kr-us-1538-fb22`. 사용자 지시: 완성된 `FINAL_REPORT.md`에서 중요한 반론·비교 연구의 누락만 확인하고 필요한 곳만 고친다. 새로운 조사축·원자료 통계 재집계 없이 **기존 W02/W04/W05 기록의 빠진 근거**를 원출처로 확인.

## 검사 범위와 발견
- W02 원문 섹션 [US1~US6], [DK1~DK2], [GLOBAL1~GLOBAL2]; W04 '기타 직종 및 경력 반례'; W05 'Hiring expansion mechanism 41 countries'와 최종본 인과장·경력장·순고용장, 부록 및 A안 편집 선택안을 문장 단위로 대조.
- 기존 본문에 존재하여 **수정 불필요**: Stanford 19% 상대격차 ≠ AI 인과 해고 19%, Census QWI 입직감소/이직감소, Yale 광범위 평균 무효과, NY Fed 공고 하락의 선행추세, Frank 2022초 선행악화, 한국 청년 인구 분해, KLI 바우처 엄격 대조 무효과, Block/KT/Amazon 복합 감원원인, Hui 프리랜서 예외, Hampole 고용상쇄의 전국 식별 불가능, 직업고용 stock vs AI 인과 신규일자리.
- **실제 누락 1 (핵심):** Chandar/Klein Teeselink 2026-09의 41개국 구인공고 12.5억·고용자료 1.54억, 다국적회사 해외 자회사에서 신입 비중 하락 주원인이 **경력자 절대고용 증가**였다는 반례. `FINAL_REPORT.md` 4.3에 복원. 채택은 GenAI 관련 공고 기반 간접 대리, 해외자회사/비교군에 제한, 미국/한국 경제로 외삽 금지.
- **실제 누락 2:** 덴마크 중앙은행 WP223 2026-09, 2023 AI 채택기업 vs 미채택기업 월별 행정자료의 고용성장 격차 약 **-11% 상대**, 소규모 기업 및 **신규채용 감소** 중심, 국가 총고용 유의한 쇼크는 발견되지 않음. -11%를 기존 직원 해고율 또는 기업 실제 총원 -11%로 환산 금지. NBER WP33777 Humlum/Vestergaard 2026.3 개정의 **임금·시간 평균 무효과**는 종속변수가 달라 정면충돌이 아님. `FINAL_REPORT.md` 3.4 신설, 기존 프리랜서 절은 3.5로 번호 이동.
- **실제 누락 3:** 미국 Census CES-WP-26-25의 2025.11~2026.1 실제 기업 AI 사용: 사업 기능 사용 기업 18%, 고용 가중 32%, 도입기업의 66%는 증강만, 전체 기업의 2%가 AI 관련 고용 감소 자체보고. 노출 지표≠실제 채택 입증의 대조. 기업응답비중≠AI로 해고된 인원비율. `FINAL_REPORT.md` 3.3에 복원.
- **실제 누락 4 (측정충돌 방지):** NBER WP34836 미국/영국/독일/호주 경영진 약 6천명 설문에서 약 69% 기업 AI 사용, 90% 이상 과거 3년 고용효과 없음 자체보고. Census 18%와 다른 국가·조사대상·도입 정의·설문 설계이므로 **한 모집단의 상충 수치로 비교하지 않는다**. 이전 W02 [US6]에 있던 내용. `FINAL_REPORT.md` 3.3에 짧게 복원.
- 각 연구를 핵심 주장 바로 뒤에서 인용하고 부록 B 비교표 및 부록 D 원출처 링크 갱신.
- 검증에 사용한 해당 기관 원문:
  * https://digitaleconomy.stanford.edu/publication/how-does-ai-change-labor-demand/
  * https://www.nationalbanken.dk/en/news-and-knowledge/publications-and-speeches/working-paper/2026/ai-adoption-and-firm-size-employment-effects-in-monthly-administrative-data
  * https://www.nber.org/papers/w33777
  * https://www.census.gov/library/working-papers/2026/adrm/CES-WP-26-25.html
  * https://www.nber.org/papers/w34836

## 무수정·제외 판정
- A안 편집에서 본문에 반드시 포함할 반론으로 선정했던 Frank·Yale·NYFed·Hui·KLI와 Block/KT/Amazon의 경영상 복합원인, 한국 BOK 업종 vs 직업의 분모차이는 이미 완성본 본문에 존재. 중복 서술을 늘리지 않음.
- W02에 있던 2017~20 프랑스 일반 AI 채택 연구는 **생성형 AI 2022 이후 직접 연구가 아니고 국내/미국 결론을 바꾸지 않아** 이번에 장문 복원하지 않음. 한국 AI 보조금 SSRN 초록만 확인된 연구도 동일 국가 결과의 중복·식별불확실성 때문에 본문에 억지로 추가하지 않음.
- NBER CEO 설문 장래고용 전망은 연구 종료 조건상 실제 고용 결과가 아니므로 보고서에 확장하지 않음.
- AI 때문에 한국·미국 전체 고용이 몇 명 순감했는지, 신규고용이 손실을 상쇄했는지는 **여전히 식별되지 않음**. 새로운 조사축/국가별 순고용 추정치를 발명하지 않음.

## 수정·재검토 결과
- 원본 `FINAL_REPORT.md` blob SHA: `506d2e6c15d181cdb59950c3782c1d6e06ed6795` (26,710자).
- 보완 저장 커밋: `4ae44e9a49e200bf0ac8ba6173695cc076963183`, `68d54aa63e8734e739316a65b78db512bd2861bc`.
- **수정 최종파일 blob SHA:** `827bfb87428265323c5048f1cc92ec97fbb35adc` (30,379자). 기존 7개 본문 장/부록 A~D 유지, 인과장 3.4·3.5 및 4.3에 설명을 국소 삽입, 부록 B·D만 복원. 다른 장의 수치·판정 미변경.
- Stage 7 재검토: 주요 기존 8개 연구, 4개 복원 비교, 모든 원출처, AI 인과·순고용 미식별, 7장·4개 부록 **기계검사 17항목 전체 통과**. GitHub 저장본 재조회로 실제 내용 일치 확인.
- **최종 감사 판정: 반론·비교 연구의 중요한 편집 누락 보완 완료.** 기존 전체 핵심 결론 변경 불필요. 연구 범위 확대·운영 main·타 연구 브랜치 변경 없음. 현재 GitHub `FINAL_REPORT.md`가 보완된 최신 완성본.
