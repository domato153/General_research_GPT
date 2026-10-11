# 2026-10-12 새 조사 엔진 적용 및 과거 W-ID·시각자료 보존 감사
- 저장소 `domato153/General_research_GPT`, 대상 `research/20261011-trump-midterms-opinion`. 기준 공통 `main` `9d80a40a3dd5e2b58d2afa9b767a947d685f4f63`, 반영 이전 연구 HEAD `0da012b3b9e7b4b57e20a132000225a87b6d329e`.
- 출처 규칙: 새 `PROJECT_BOOTSTRAP.md` 중요 시각자료 실물 백업, `02_RESEARCH_PIPELINE.md` 파일/임베드/CSV 대조, `04B_VALIDATION_RULES.md`의 `RAW_DATA_SAVED`와 `VISUAL_ASSET_SAVED` 구별. `main`은 수정하지 않으며 현재 연구 브랜치에만 병합·보정.
- 실제 검증 범위: 현재 이 대화에서 확인할 수 있는 사용자 선택·채팅 보고·보존된 8개 W-ID/계획·실제 SVG/CSV. 자료와 그림의 수치/단위/결측, 모집단 및 인과 해석 양방향 대조. **과거 UI의 모든 표시 픽셀·원본 동적 툴팁, 다른 ChatGPT 스레드의 실사용 E2E는 미확인**. 이번 단계는 기존 조사 보존 및 근거 일관성 감사이며 새 국제정세/경제 시점 이후의 전면 검색·자료 갱신은 아님.

## 실제 그래프 체크포인트
| ID | 조사 내용 | SVG | CSV/데이터 | W-ID |
|---|---|---|---|---|
| W1-VIS-F01 | Gallup 2025 승인율·반등 12관측 | assets/W1-VIS-F01_gallup_2025_approval.svg | .csv 12행 | W1_SURVEY_TIMELINE |
| W1-VIS-F02 | Pew 2025~26 승인율 9관측 | assets/W1-VIS-F02_pew_2025_2026_approval.svg | .csv 9행 | W1_SURVEY_TIMELINE |
| W1-VIS-F03 | Reuters/Ipsos 2026 월별 대표 10관측 | assets/W1-VIS-F03_reuters_ipsos_approval_2026.svg | .csv 10행, 기존 보존 | W1_2026_IPSOS_MONTHLY_RECHECK |
| W2-VIS-F01 | 미국 CPI-U 2025~26 | assets/W2-VIS-F01_cpi_2025_2026.svg | .csv 20월 위치, 19개 값+1개 결측 | W2_ECONOMIC_TIMELINE |
| W2-VIS-F02 | 미국 주간 일반휘발유 가격 | assets/W2-VIS-F02_gasoline_2025_2026.svg | .csv 13개 선택 주간값 | W2_ECONOMIC_TIMELINE |
| E6-VIS-F01 | Pew 중간선거 의제 중요도 | assets/E6-VIS-F01_midterm_issue_importance_2026.svg | .csv 7개, 등록유권자 | W1_W3_INITIAL_EVIDENCE |
| E2-VIS-F01 | Pew 2024 Trump 투표 검증집단 국정 승인 비교 | assets/E2-VIS-F01_trump_2024_voters_approval.svg | .csv 2개, 득표전환 아님 | W1_W3_INITIAL_EVIDENCE |
| W7-VIS-F01 | Ipsos 해외분쟁 최대 국가문제 1/14/8 | assets/W7-VIS-F01_war_issue_salience_2026.svg | .csv 3개, 기존 보존 | W7_ALTERNATIVE_EXPLANATIONS_ROUND3 |
| W3-VIS-F01 | 전쟁·관세 → 생활비 → 국정/투표 판단 **가설 구조** | assets/W3-VIS-F01_foreign_policy_cost_of_living_hypothesis.svg | 관계·주석, 확정 인과아님 | W3_W7_EVENT_CAUSAL_REVIEW |

## 실질 감사 내용과 반례 보존
- W1: Gallup 2025 12/12 W1·엔진 fixture CSV/SVG 동일; Pew 2025~26 9개 실측 원자료와 신규 재생성본 일치(기존 채팅 7개 선택 시점에서 **2개 실제 시점 추가**한 확대판, 가공·보간 아님); Reuters/Ipsos 2026 10개는 월별 *대표 조사 관측*, 평균 또는 동일 개인 추적 아님. 서로 다른 기관 선을 합치지 않음.
- W2: CPI 2025-10 실제 공표 지수 결측, 2026-10 전년동월비 후속 비교 제약을 BLS FAQ로 표기. 관측된 2026-08까지 CPI 19개/결측1, 전월/전년 동월 퍼센트 구분. EIA 2026-02-23 $2.937, 05-11 $4.500, 10-05 $4.354; **+53.2/+48.2%**는 전쟁 순수 인과효과가 아닌 관측가격 변화. 근거 W2 원문.
- W5·W6: 2024 Trump 투표 검증집단 승인 95→67%(−28%p)는 민주당 투표전환이 아님; 미국 등록유권자의 7개 의제 중요도도 단일 최우선 문제 표본과 다름. Pew 전국 하원 후보 민주44/공화36과 Reuters/Ipsos 민주44/공화37 등 각 조사 수치·모집단 그대로 보존.
- W3·W7: '이란 전쟁이 2025~26 전체 여론하락의 단일원인'이라는 설명은 전쟁 전 국정 승인 하락으로 반박; 전쟁→유가→체감 평가 연결 가능성과 **국정 승인 %p 인과효과의 미식별**을 W3 도식에 적시. Chicago Council 전쟁 생활비 악영향 인식 86%, 관세 81%는 정책별 기여율 아님. 2026-07 Reuters/Ipsos 지지율 반등 및 실업률 4.2%·제조업 저점 대비 증가 반례 유지.
- 경제 추가 관측: BEA 2026-08 real DPI 월 +0.0%, real PCE +0.6%; 2026-10-08 Freddie Mac 30년 모기지 금리 7.40%; 2026-09 제조업 일자리 월 +9k 및 2025-12 저점 대비 +72k는 기존 W2 3차 파일의 별도 측정지표로 보존. 서로 다른 분모/기간을 단일 원인 그래프로 임의 합성하지 않음.
- 과거 W-ID의 '실물 없음'은 **당시 보존 상태**. 새 실물 SVG들은 과거 ChatGPT UI의 픽셀·툴팁 원본 복제본이 아니라 검증된 값/관계로 만든 재생성본.
- 승인: 사용자 A 통합조사·시계열 보완·1회 추가 보완·엔진 반영 및 전수 보존 감사. **W3 중국·우크라이나·동맹 세부, W4 이민·제도·재정/사회 정책, W6 경합주 상세는 아직 계획된 미래 조사**이지 이번 감사 실패나 완료가 아님. 최종보고서 완성/외부 공개 권한 부여된 바 없음.

## 검증 한계·다음 작업
- 파일 저장→재조회·SVG/CSV 값 검산에 성공하면 파일 실물/자료 일치에 대해 PASS. 실제 브라우저 렌더/한글 폰트·원 채팅 UI 동일성/새 스레드 자동 적용은 분리해서 UNKNOWN/NOT RUN 판정.
- 외부 모든 원출처를 2026-10-12 최신판으로 전수 재검색한 것은 아니므로 **최신성 재조사 완료 아님**. Reuters/Ipsos 매월 질문지·설문설계 동일성, 2025~26 전체 월별 소득/주거/제조업 지표 및 정치·외교 전체 의제의 인과평가 미완료.
- 다음 한 작업: 이번 보존 감사 결과 보고 후 사용자와 W3/W4 확장조사 또는 W1/W2 정밀검증 우선순위 결정.
