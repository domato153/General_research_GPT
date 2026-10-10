# W1_DATA_AUDIT — 한·미 충전시설 및 전기차 신규보급 데이터 1차 검증
- 기준일: 2026-10-11 (Asia/Seoul)
- 승인 연구: `research/20261011-kr-us-ev-charging-adoption`; 기준 커밋 `ac4675d50bc0355b0939f7eb32b6fd72605acfb4`
- 단계: W1 **부분 완료**, 최종 식별자료 구축과 W2/W3 분석은 아직 실시하지 않음.
- 출처: 정부/공공기관 원문과 데이터사양을 우선 확인. 웹 페이지에 표가 있다는 사실과 CSV/XLSX 원자료를 실제 다운로드·정합검사했다는 사실을 구분.

## 1. 한국 전기차 등록자료
1) 국토교통부 `자동차등록현황보고` 통계메타: 월별, 기준월 말일, 지역별 차량, 자동차관리정보시스템 집계, 다음달 말 공표. 2018-01~2025-12 각 월의 자동차등록 통계 엑셀 파일 목록이 웹페이지에 있음. `https://stat.molit.go.kr/portal/cate/statMetaView.do?hFormId=1244&hRsId=58`
2) 해당 통계 페이지에서 '월별 파일 존재' 확인. **각 파일 내부에 승용 BEV '신규 등록'과 시군구 교차표가 모두 존재하는지는 미검증**. 등록 보유량(월말 stock)을 월별 차분해 신규 구매 flow로 간주하지 않을 것.
3) 국토교통 통계누리 OpenAPI: JSON/REST이며 발급 키와 신청/승인 절차가 필요, 너무 긴 범위 호출 주의; 화면 API 설명은 한 번에 최대 5년 시계열 조회 제한을 표시. `https://stat.molit.go.kr/portal/openapi/apiInfoView.do`; `https://stat.molit.go.kr/portal/api/apiList.do`

## 2. 한국 충전시설
1) 한국환경공단 `전기자동차 충전소 정보` 데이터셋: 충전소·충전기 ID, 종류, 주소, 위경도, 충전 용량/방식, 이용제한, 삭제여부, 상태갱신 시간 등 제공. REST/XML, 무료, 실시간 업데이트, 개발단계 자동승인, 공공 및 민간 충전기 조회. `https://www.data.go.kr/data/15076352/openapi.do` (페이지 수정일 2026-07-21).
2) 현 API 문서의 시간범위는 '-'이며, **2018–2025 시군구별 과거 설치·폐쇄 이력 보존은 확인되지 않음**. 현재 조회 데이터를 과거 설치량으로 소급하면 생존편향·백필 오류.
3) 정부 보도자료의 별도 과거 전국 누적치 존재: 2025-11-13 당시 발표된 전기차 보급 기사(2025 보급은 11월 13일까지, 충전기 2025값은 10월까지)에서 급속 누적(만 기) `2020:1.0, 2021:1.5, 2022:2.1, 2023:3.4, 2024:4.7, 2025-10:5.2`; 완속 누적(만 기) `2020:5.4, 2021:9.2, 2022:18.4, 2023:27.1, 2024:36.8, 2025-10:42.0`. 출처: 기후에너지환경부 2025년 전기차 연간 보급 20만대 발표 `https://mcee.go.kr/home/web/board/read.do?boardId=1820170&boardMasterId=1&maxIndexPages=10&maxPageItems=10&menuId=10357&pagerOffset=110`. 웹 검색 결과 원문 문구 확인; 웹 원문 직접 열람 시 동적 링크 오류가 발생해 첨부 자료 내용까지 재검증은 수행하지 못함.
4) 동 정부 발표의 전기차 연간 보급량(전 차종 합계, 만 대) `2023:16.3, 2024:14.7`. 충전시설 누적 증가와 동시 보급 감소가 확인되는 기초 반례. 이는 충전기 보급의 인과효과가 음수라는 뜻은 아님. 연간 보급은 **승용 BEV 신규등록**과 정의가 같다고 가정하지 않음.

## 3. 미국 충전시설
1) DOE AFDC `Data Downloads`: Station Locator의 과거 데이터는 2014-01-20부터, 특정 하루의 published locations snapshot 또는 특정 시설의 변경 이력 제공. `https://afdc.energy.gov/data_download`
2) 과거 파일 사양: `historical_change_at`, `historical_published`; `access_code=public/private`, `status_code=E/P/T`, `ev_level2_evse_num`(Level 2 **ports**), `ev_dc_fast_num`(DC fast **ports**), `open_date`, 위경도 포함. `open_date`는 추정값일 수 있고, 네트워크가 날짜를 제공하지 않을 때 Station Locator에 나타난 날짜이므로 실제 개소일과 다를 수 있음. `https://afdc.energy.gov/data_download/historical_stations_format`
3) `Alternative Fueling Station Counts by State` 페이지는 과거 날짜 설정과 주별 station locations/Level 1·2·DC fast ports 수를 함께 제공, 예시로 2025-12-31 snapshot 확인. `https://afdc.energy.gov/stations/states?count=public&date=2025-12-31`
4) 과거 기간 조회 및 파일 다운로드 페이지는 접근되지만 **2018–2025 전 기간/전 주의 원자료 다운로드·결측 검사 및 포트별 추세 재구성은 미실행**. 페이지 다운로드에 이름/이메일 등 기입 항목이 있고 이용조건도 있으므로 현재 직접 다운로드 여부는 추가 확인 필요.

## 4. 미국 BEV 등록
1) DOE AFDC `Vehicle Registration Counts by State`: 2025년 Light-Duty Vehicle Registration Counts by State and Fuel Type. National Laboratory of the Rockies와 Experian의 VIN 기반, **연말 보유량**이며 100대 단위 반올림. EV(순수 EV)와 PHEV/HEV 구분. `https://afdc.energy.gov/vehicle-registration`
2) 2025년 기준 미국 전체 BEV 보유량 5,689,100대(반올림 수치). 신차 판매량이나 연간 신규 등록이 아님.
3) 해당 데이터가 연도 선택 기능을 제공하는 것은 확인했으나 원하는 모든 연도·카운티별 일관된 신차 등록 flow가 있는지 불명확. `https://afdc.energy.gov/data/search?q=Electric+vehicle+registration+by+state`의 대시보드(2023년 12월말)는 2025년 보유량과 다른 판본이므로 같은 해 데이터처럼 합치지 않음.

## 5. 한미 비교에서 해결해야 할 측정 간극
- 한국 충전기 = 충전기 개별 장치/기 단위; 미국 AFDC = charging ports / station locations. 동일한 전기 공급 능력으로 간주하지 말고 별도 지표로 분석.
- 한국 API = 공공/민간, 이용제한·상태; 미국 = access_code public/private, E/P/T. '공용' 정의와 공동주택 접근성을 맞추고 실효 접근성 별도 점검.
- 한국 자동차등록 = 월말 stock일 가능성과 신규등록 flow 구분 필요; 미국 주별 EV count = 명시적으로 연말 stock. stock 차분을 신규 판매/등록으로 치환 금지.
- 한국 전기차 정부 연간 '보급' 수치에는 승용 외 차량 포함; 최종 BEV 승용 신규등록 지표와 혼합 금지.
- 설치 이후 시차 분석 시 US AFDC `open_date` 대체일자와 한국 과거 설치일자의 결측 가능성 검토.
- 국토교통부 통계누리 API는 키 신청 필요, 한국환경공단 API도 승인된 API 키 필요. AFDC 공개 데이터 다운로드 절차에 이용자 정보/약관 입력 단계 존재; 대량 원자료 직접 취득은 아직 미완료.
- 원인 변수(구매/설치 보조금, 가격, 소득, 유가, 신차 공급, 충전기 이용률)는 **후속 W1 미확보 상태**. 국가별 연도/지역 변수 가용성 확인 필요.

## 6. 첫 결과 판정
- 확인: 한국 2018–2025 월별 자동차등록 보고서 파일이 열거됨. 한국환경공단 충전소 현재정보 API 존재. 한국 전국 연도별 급속/완속 누적 공식 발표. 미국 AFDC 충전시설 2014 이후 역사가능성과 2025 주별 BEV 누적 등록자료 존재.
- 미확인: 한국 시군구·월별 충전시설 과거 패널, 동일 기간 한국 승용 BEV 신규 등록 원자료, 미국 주·카운티 신규등록 flow 2018–2025, 교란변수 패널, 접근제한 없는 원자료 완전 다운로드.
- **W1 부분 완료; W2/W3 아직 시작 전.** 충전시설 확대의 인과효과는 아직 수치로 추정하지 않음.
- 다음 검증 경로 사용자 선택 예정: (A, 추천) 원자료 접근·변수 정의 보완; (B) 선행연구 데이터/준실험 우선 조사; (C) 연 단위 시도·주 단위로 우선 축소하고 보조 결과로 간주.
