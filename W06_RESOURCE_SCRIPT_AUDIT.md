# W06 — 트로그 트롤족 스크립트·건물 자원 비용·한국어명 표적 재검증
2026-10-12; **9.0 공개 게임 덤프 + 9.0.3 공식 패치 공지/데이터 비교**. 사용자 승인된 A+B 정밀 보강; 최종보고서 확정 지시 아님.

## 검증 경계
- 공식 개발자 7.0 노스카 개편: https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/84
- 9.0.3 공식 패치: https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/16126-total-war-warhammer-iii-patch-9-0-3 (관련 Trollkind 값 직접 명시 없음)
- 9.0.3 정적 DB: https://twdatabase.com/factions/wintertooth ; https://twdatabase.com/buildings/norsca ; https://twdatabase.com/patch/9-0-3
- 가장 구체적인 캠페인 루아와 리소스 비용표는 '9.0 patch'로 명시된 공개 덤프 커밋 **8a4f7e64714cf971b44988a4b59f218af6d04ff2**. 따라서 9.0.3 게임에서 값이 100% 유지된다고 확언하지 않는다. 최신 9.0.3 설치 클라이언트 로컬 파일 직접 조회와 실플레이 시뮬레이션은 수행하지 못함.
- https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/script/campaign/wh3_dlc27_nor_kinfolk.lua
- https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/db/resource_cost_pooled_resource_junctions_tables/data__.tsv
- https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/db/resource_costs_tables/data__.tsv
- https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/db/rituals_tables/data__.tsv
- https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/db/scoped_resource_cost_items_tables/data__.tsv
- 한국어 게임 문자열/건물 ID 제3자 미러: https://www.honga.net/totalwar/ko/warhammer3/factions/wh_dlc08_nor_wintertooth/buildings . 이 미러는 9.0.3 전수 최신화 보장하지 않음.

## 9.0 코드에서 직접 확인된 트롤족 수급 (근거 높은 9.0 사실, 9.0.3 조건부)
- kinfolk_unit_gain=1, kinfolk_throgg_multiplier=2.
- Throgg 본인이 군주면 +1/턴, 같은 군단의 wh3_dlc27_nor_kinfolk_units 집합 소속 1부대당 +2/턴, 다른 군주 군단의 같은 집합 1부대당 +1/턴. 주둔군·군주 없는 군단은 0.
- 스크립트는 FactionTurnStart에서 해당 총량을 자원에 더함. 트로그+트롤 8 = 17/턴 (기타 건물 보너스 제외); 트로그+트롤 10 =21/턴.
- **소집 성공 시 stop_kinfolk_gain 효과를 10턴 적용**: kinfolk_stop_gain_effect_duration=10. 효과가 지속되면 신규 유닛 생산 계산이 차단되고, 건물에도 'Income of Trollkind is blocked for a while after Call' 설명. 지원 부대 전멸 시 이 효과를 제거하는 별도 처리도 존재. 다만 그때 재개 타이밍과 모든 건물의 실제 UI 경험은 9.0.3 직접 실험 미실시.
- 성장 6단계 경계: kinfolk_levels threshold 20,40,60,80,115; 이는 **트롤 왕의 영역 단계 경계이지 트롤족 현금 잔고 요구치가 아님**.

## 괴수 무리 소집의 9.0 데이터 (플레이어 ritual / AI 별도 구분)
- rituals_tables 6개 ritual cooldown_time: 1단계10, 2단계12, 3단계14, 4단계16, 5단계18, 6단계20턴.
- 각각 required_resources·expended_resources ID가 동일한 ritual key. resource_cost_pooled_resource_junctions에서 2단계 -60, 3단계 -90, 4단계 -120, 5단계 -150, 6단계 -200 Trollkind가 확인. 1단계 항목은 해당 비용표에 없음(무료라고 9.0.3 확정 X).
- 중요: kinfolk.lua 내 ai_spawn_armies_to_bundles_thresholds_and_cost = 20/40/60/80/100/140은 **AI 군단 생성용 데이터**이므로 인간 플레이어 소집 비용으로 인용하면 오류.
- 소집 후 트롤족 수입 정지 10턴과 '재사용 대기시간 최대 20턴'은 다르며 함께 적용될 수 있음. 9.0.3 직접 확인은 보류.

## 건설 비용: 금0과 별도의 트롤족 9.0 차감 키를 발견 (UI 최종 단계 매핑은 유력/미확정)
리소스 비용표(resource_cost_pooled_resource_junctions)에서 다음 키·가격:
- wh3_dlc27_ritual_nor_throgg_troll_woods_building → -20 Trollkind
- wh3_dlc27_ritual_nor_throgg_troll_deep_woods_building → -35
- wh3_dlc27_ritual_nor_throgg_troll_deep_woods_building_3 → -50
- wh3_dlc27_ritual_nor_throgg_troll_shelter_building → -30
- wh3_dlc27_ritual_nor_throgg_troll_shelter_building_1 → -40
- wh3_dlc27_ritual_nor_throgg_troll_caves_building → -30
- 위 비용의 데이터 타입은 CONSTRUCTION_BUILDING이고, 별도 GOLD treasury_cost=0.
- **리소스 비용 키 ↔ 정확한 건물 단계 UI 키의 직접 연결 표를 아직 찾지 못함**. 문자상 woods L1 20, deep woods L2 35, deep woods L3 50, shelter L1 30 L2 40으로 읽는 것은 **유력 추론이지 9.0.3 확인된 개별 건물 요금표 아님**. 한국어 이름과 건물별 투자 지시는 금0 숫자가 아니라 조건부로 유보.
- 해당 원본에 *별도로* wh3_dlc27_nor_throgg_troll_shelter_building_on_completion_transaction (+2 Troll King's Dominion), _2 (+4), woods completion (+2), _2 (+4), _3a (+10), _3b (+4) 기록. 사용/차감 비용과 건물 건설 완료로 증가하는 Dominion을 혼동하면 안 됨.
- 9.0.3 실제 비용은 단기승리 이후 특전(건설 Trollkind 비용 -20%)·개별 이벤트 버프 등에 따라 변동 가능.

## 한국어명 대조 (실제 언어 미러 텍스트)
- 트롤족 Trollkind, 트롤 왕의 영역 Troll King's Dominion.
- 트롤 왕국 계열: 트롤 굴 L1→트롤 땅굴 L2. 소굴/자원 및 성장용 건물.
- 거대한 요새의 폐허 건물 계열: 트롤 동굴 L1→돌투성이 소굴 L2→3단계 미궁 둥지/거대한 요새의 폐허 분기.
- 별도 병종 모집: 트롤 둥지 L1(일반 노스카 트롤)→L2(표시 L2로 공식 한국어명 미확인, 얼음 트롤); 일반 노스카 건물 얼음 트롤 둥지와 혼동 금지.
- 늑대두겁 모집: 군견 보관소→전투 늑대 소굴→암흑 공물의 동굴.
- 영어 스킬/연구 이름 전체를 9.0.3 직접 한국어 UI와 일대일 검증 못함; Honga와 2차 한글 위키 용어는 출처 태그 유지, 명칭을 새로 직역하지 않음.

## 이 단계에서 따르기 가능한 **조건부** 건설 지침
1. 먼저 현재 정착지의 일반 건물 슬롯/정착지 타입에서 '트롤 둥지' 750골드/1턴을 건설할 수 있는지 확인해 노스카 트롤을 조기 개방.
2. 게임 화면 상단 트롤족 자원 수급을 확인; 트로그 군단의 해당 트롤 1부대가 +2/턴인 9.0 룰을 참고해 가능한 한 트로그 군단에 집중.
3. 트롤 왕국 계열 '트롤 굴' 또는 조건이 맞는 '트롤 동굴'에 지출하기 전 **게임 툴팁 실제 트롤족 가격**을 확인. 소굴은 L1→L2; 특수 동굴은 L1→L2→빠른 지배 성장(미궁 둥지) / 트롤족 생산(거대한 요새의 폐허) 분기.
4. 1~2티어 구간에 소집 기능을 바로 발동하면 트롤족 생산이 10턴 동안 멈추는 설계. 긴급 방어가 아니면 트롤 건설·단계 상승용 지출을 먼저 끝낸 후 대규모 전쟁 직전 사용.
5. 9.0 기준 소집 6단계는 트롤족 비용 -200 / 쿨다운20턴. 9.0.3에서는 툴팁 확인 전 확정 수치로 쓰지 않음.

## 미확인/추가 검증 한계
- 9.0.3 raw .pack/current Korean localisation .loc 미열람, 현행 게임 직접 실행 불가. 연결된 Desktop Commander 장치는 이 조사 시 오프라인임을 별도 확인. 로컬 파일을 확인했다고 주장하지 않음.
- 특수 '트롤족' 금 외 차감 키 ↔ 개별 건물의 정확한 cost tooltip 일대일 검증 부족.
- 9.0.3 현행 UI에 표시되는 모든 고유 스킬·연구 한국어명 검증 부족. 최신 한국어 클라이언트 화면이 없으면 공식명 미확인 표시.
- 모든 시작 영지 초기 건물/슬롯, 건설 수용량, 호출 조기 종료 시 정확한 수입 회복, 특수 지역 모집 상한.
- 이 한계가 있다고 9.0 데이터 원문 검증과 운영 방향까지 폐기하지는 않음.

## 현재 사용자 협의 경계
사용자는 A+B 추가 검증→C 1차 검증 후, 다시 한국어명·건설 실제 비용을 표적 재검증하는 방식을 승인. 본 W06이 해당 표적 조사 결과. 최초 FINAL_REPORT.md는 초안, 최종 확정/최종화 위임 없음. 중요한 미확인 상태와 권고 변경 부분을 사용자에게 중간 공개하고 추가 필요 자료·종합검수 전환 선택을 받는다.
