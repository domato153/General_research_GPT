# W12 — 트로그 9.0.3 신앙·제단·트롤 경제 1차 조사 (2026-10-12)
**상태:** 신규 승인 D2, 1차 게임 원시 코드+공식 원문+9.0.3 자료 대조/조건부 완료. 기술·UI 문자열·효과 누적의 최종 9.0.3 게임 실측은 미완. 괴수 사냥 D1 상세 조사는 사용자가 제외함.

## A. 유효한 시스템 / 자료 판본
- 개발사 2025-12-02 Update 7.0 공식 설명: Norsca의 Chaos Altar 점령 선택을 하면 **2슬롯 정착지**(하나는 제단, 하나는 제한 건축)가 생성. 각 신 제단은 신앙 진행에 기여. 최대 신앙 도달 시 그 신의 특수 군주/영웅 영입 여부 선택. 한 신의 챔피언을 받으면 타 신의 챔피언 영입은 배제되나 **타 신의 신앙 진척은 7.0 이후 지속 가능**. Sayl 본인은 일반 Allegiance(신앙) 시스템을 사용하지 않으며 별도 Dark Ritual로 대체.
  공식: https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/84-total-war-warhammer-iii-patch-7-0-introducing-the-free-content-and-the-masque
- 공개 9.0 게임 Lua `wh_dlc08_norscan_gods.lua`는 **Wintertooth+World Walkers 두 세력만** 일반 신앙 관리 목록에 명시. 신별 발전은 building의 `cm:get_factions_bonus_value` 재계산, 레벨 문턱 `{5,10,15}`; 5/10/15는 누적 제단 효과에 따른 기준이므로 각 건물을 반드시 15개 지어야 한다는 게임 상황의 예외(영지 상실/건물 계수)는 UI 참조.
  원본 https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/script/campaign/main_warhammer/wh_dlc08_norscan_gods.lua
- 9.0 소스의 최근성: 공식 9.0.3 변경 공지에서 이 기제 변경은 확인되지 않았으나 최종 런타임 동일성 증명 아님.

## B. 신별 선택과 실제 트로그 경제/전투의 관련성
원시 신앙 스크립트는 해금 및 침공에 집중하므로 **아래 효과 수치는 7.0 이후 팬위키 갱신 자료(9.0.3 직접 독립 재계산 전)**. 한국어 기술 이름은 공식 인게임 대조 전 임의 확정하지 않음.
- **사냥개 / 코른 (Hound, Khorne)**: 신앙 2/3/최대에서 전군 무기 피해 +3/+6/+10%, 특정 신 제단 주변 전투 승리 후 추가 이동력 효과(+10/+15/+25%) 및 경험 축적; 특별 보상은 25레벨 **Killgore Slaymaim** 영웅(원시 Lua `wh3_main_ie_nor_killgore_slaymaim`). 얼음 트롤과 늑대두겁을 포함한 대규모 교전 **전군 공격력**에 실질적으로 연동될 가능성이 높음. 이동 효과는 *제단 인접 지역 승리시 조건부*이지 세계 전체 이동력 버프가 아님.
- **까마귀 / 너글 (Crow, Nurgle)**: 신앙 2/3/최대에서 모든 지역 건물 수입 +4/+7/+10%, 전 속주 성장 +10/+20/+40, 제단 인접지역 교전 승리 뒤 충원 효과. 최종 **Burplesmirk Spewpit** 전설 군주(원시 Lua subtype `wh3_main_ie_nor_burplesmirk_spewpit`, 모집 풀 해제·spawn rank 25). **트로그 트롤 왕국 경제/항구 확장과 조합하면 주도 성장/현금 기반을 강화**하는 범용 선택. 수입 +10%가 모든 트롤족 자원+10%라는 뜻은 **아님**.
- **뱀 / 슬라네쉬 (Serpent, Slaanesh)**: 신앙 2/3/최대 전군 유지비 -5/-10/-15%, 모든 캐릭터 물리저항 6/12/20%. 최종 25레벨 **Kihar the Tormentor** 마법 영웅 (`wh_dlc08_nor_kihar`). 대규모 트롤·늑대두겁 군단을 여러 개 굴릴수록 유지비 절감 강력. **'모든 캐릭터 물리저항'은 '모든 트롤 부대 물리저항'이 아님.**
- **독수리 / 젠취 (Eagle, Tzeentch)**: 신앙 2/3/최대 모든 군단 마법 재사용 대기 -5/-10/-20%, 마법의 바람 저장 상한 +5/+10/+20, 제단 인근 승리로 연구 점수 획득. 최종 25레벨 **Azrik the Maze Keeper** 전설 군주(`wh_dlc08_nor_arzik`). 마법사 여러 군단/연구 병목 상황에 유리하나 초기 무마법 트롤 위주 운영에는 기회비용.
- 팬위키의 매우 세부값과 달리 게임 스크립트에서 확인된 **강한 1차 확정**은 신별 최고 보상의 타입·키, 5/10/15, 신 선택 로직이다. 팬위키 현재 자료: https://totalwarwarhammer.fandom.com/wiki/Allegiance_to_the_Gods .
- **1차 잠정 결론(2차 조사로 수정됨, 역사 보존):** 당초 너글·슬라네쉬를 우선했으나 젠취 제단의 **전투 후 즉시 연구 진도 증가**를 거의 반영하지 못한 점이 사용자 지적과 독립 검증으로 확인됨. 현재 유효한 판정은 아래 2차 검증 절을 따른다.

## C. 제단 vs 정착지 vs 트롤 전용 건물
- 제단은 **2슬롯**. 첫 슬롯은 제단이 선점해 일반 트롤 왕국 성장/모집·항구·수입 건물 전부를 한 제단에 집어넣을 수 없다. 트로그는 일반 점령 거점에서 생성하는 Trollkind 생산 특수 건축을 우선시하는 경우가 있으므로 **거점별 슬롯 기회비용**이 존재.
- 기존 북부 본거지/특수 트롤자원 지역/바위 왕좌 랜드마크: **일반 점령·운영 우선**. 긴 원정 끝의 일반 정착지: 전리품 수송이 가능하면 약탈 파괴, 신앙 최고 보상이 급하면 제단 건립의 지역가치 대조. 해외 직접 점령에 Spoils 자원 필요(공식 7.0).
- '제단이 일반 소유 거점으로 업그레이드/전환되는지', 합병 받은 제단 건물 2슬롯이 어떻게 처리되는지, 제한된 제단 부속 건물의 9.0.3 정확한 세트는 원자료 추가 대조 필요.
- 참고 https://twdatabase.com/buildings/norsca 와 기존 W08_EXPANSION_STRATEGY.md.

## D. 보상 선택과 보복: 공식 설명 vs **원시 스크립트 간 차이**
- 공식 7.0 안내 '나머지 세 신들이 보복하여 수도로 공격'이라는 압축 서술.
- 9.0 `norscan_gods:champion_dilemma_handler`: `choice == 0`(특별 챔피언 받아들임) → 해당 신의 반대 라이벌 **한 신**(`Khorne↔Slaanesh, Nurgle↔Tzeentch`) 침공을 spawn, 챔피언 1명 영입 후 선택 잠금. `choice ~= 0`으로 4신 챔피언 제안을 모두 거절하면 4신 침공이 spawn되며 `wh3_dlc27_nor_allegiance_ultimate_refusal` 임무 처리. '한 신 선택 즉시 3군단 고정'이라고 단정하지 않음.
- 4신 전부 거절 후 챌린저 토벌 보상은 원시 Lua 번들 `wh3_dlc27_bundle_nor_allegiance_ultimate_refusal`; 팬위키는 모든 군단 15% ward save·질서세력 상대 유지력·모집 정원을 기술하나 **실제 9.0.3 세부효과 재검증 전 조건부**, 부가 전투부담도 커서 빠른 캠페인 승리 목적으로는 일반 추천 불확정.
- 이는 **판본/공식 개요 충돌 검증 포인트**: 9.0 Lua는 관련 코드 외에 다른 이벤트의 추가 침공이 있는지, 9.0.3 런타임 변형 여부를 독립 대조해야 함. 2026-10-01 Reddit은 '4신 중 1명 챔피언 혹은 전부 거절 보너스' 경험을 보고. https://www.reddit.com/r/totalwar/comments/1wv5len/norsca_chaos_rewards/

## E. 남은 실제 검증
1. 최신 9.0.3 effects 직접 테이블/클라이언트 UI에서 신별 보너스 수치 및 누적 여부·신앙 마이너스 영향을 원시 행으로 독립 검증.
2. 특별 영웅/군주 영입 가능 조건(현 DLC 소유 여부), 선택 거절 후 재도전 규칙/챌린저 세력의 실제 수도 포위 위치.
3. 트로그 시작지 일반 점령 vs 제단/항구 지형별 슬롯·두 번째 건설 슬롯의 가능한 건물 개수.
4. 너글 +10% 건물 수입 vs 슬라네쉬 -15% 유지비를 주력 군단 수·건물 순수익에 따라 수치 비교(단위와 선행조건 검증).

## F. [2차 교차검증] 9.0.3 독수리(젠취) 제단 **연구 선행 전략** — 1차 우선순위 정정

### 직접 근거 및 기능
- 9.0.3 기준 공개 TWDatabase의 일반 독수리 제단(Altar of the Eagle)은 **2티어 750금/2턴**부터 `전투 승리 후 +25 / +50 / +75 / +100 Research Rate Points`를 신앙 단계에 따라 표시하며, 효과 범위는 **인접 속주에서 싸우는 자군의 승리**임. 특정 특수 정착지 유형은 750금/1턴 등 별도 체인이 있으므로 **모든 제단을 2턴으로 단정하면 오류**. +25/+50 등은 **연구 진도 포인트**, +25% 영구 연구속도나 매 턴 상시 +25가 아님.
  https://twdatabase.com/buildings/norsca
- 9.0 공개 원시 Lua `script/campaign/wh3_campaign_bonus_values.lua` `research_bonus_post_battle_win` listener: `CharacterCompletedBattle` 승리→`cm:get_characters_bonus_value(...,"research_bonus_post_battle_win")`→`cm:grant_research_points(faction, value)`. 영구 연구속도는 별도 `research_rate_bonus_post_battle_win`와 `grant_research_rate_points`. 즉 메커니즘상 **전투 보상으로 연구 진도를 밀어주는 기술성장 촉매**이므로 기존 '마법 위주라 후순위' 평가는 핵심을 누락함.
  https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/script/campaign/wh3_campaign_bonus_values.lua
- 공식 7.0.3 패치는 Eagle의 영구 연구 속도를 **Research Points Surplus**로 바꾸고 보상 단계를 `5/10/15/25→25/50/75/100`으로 재조정. 7.0.3 이후에도 `grant_research_points` 함수 관련 추가 과다 지급이 관측됐으며, **공식 7.1 패치는 'Eagle Altar infinite research fixed'**로 이를 다시 수정함. 공식 9.0.3에서는 Eagle 재변경 언급을 찾지 못함. **2025-12 영구 +5000 연구 속도 / 2026-01 단일 전투로 2~8기술 자동 완료를 9.0.3 일반 성능으로 쓰지 않음.**
  https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/12797
  https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/93
  https://community.creative-assembly.com/total-war/total-war-warhammer/bugs/12154-norsca-s-altar-of-the-eagle-allows-to-immediately-research-techs
  https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/16126-total-war-warhammer-iii-patch-9-0-3
- DB/스크립트 범위 확인은 **정적/조건부 PASS**이고 9.0.3 라이브 전투에서 실제 기술 한 개를 몇 번의 승리로 완료하는지 직접 재현한 것은 아님. 포인트 25/50/75/100을 정확한 기술 한 턴·한 연구 비용으로 자동 등치하지 않음.

### 2026 실전평(평가자가 직접 플레이했는지/버전/모드 분리)
1. 2026-06-11 r/totalwarhammer 'Best/Preferred approach to Norscan Altars?': 여러 의견에서 **'전투 많은 곳에 젠취 제단, 인접 지역에서 승리 시 연구 보너스 중첩'**을 핵심. 트로그 캠페인 1전투≈1턴 연구 체감이라는 직접 사례도 있으나 게임 버전/세이브 실측 부재. 한 유저는 '제단이 부근에 없으면 전투 보너스가 없다'고 주의. 또 다른 유저는 **코른 제단의 이동력 재충전이 최고**, **너글 성장의 한계효용은 전리품을 통한 고티어 건축 및 점령 인구 증가 연구 때문에 낮아질 수 있다**고 반론. 따라서 커뮤니티를 만장일치 순위로 왜곡하지 않음.
   https://www.reddit.com/r/totalwarhammer/comments/1u34qwe/bestpreferred_approach_to_norscan_altars/
2. 2026-06-15 r/totalwar 'Norsca rework bloated': **트로그의 Troll Empire 전용 건물 슬롯을 제단이 잠식**, 제단 확보 시점엔 이미 승리 중인 'win-more' 시스템이라는 반론. 특히 코어 도시를 제단으로 바꾸는 것을 경계하는 독립 증거.
   https://www.reddit.com/r/totalwar/comments/1u6jiln/norscas_rework_is_such_a_bloated_mess_that_ca/
3. 2026-01-15 r/totalwar 7.0.3 전투 1회→2개 이상 기술 완료 사례 및 2025-12 20k 연구 속도 스크린샷은 당시 **버그와 겹쳐 현재 9.0.3 효과량 입증 불가**, 역사적 과잉성능/수정 이유의 증거로만 보존.
   https://www.reddit.com/r/totalwar/comments/1qdwtkh/so_with_703_norsca_researches_even_faster_now/
4. 2026-04-11 Legendary 트로그 캠페인 개인 후기: 얼음 트롤로 빠른 확장, 젠취 구 연구 버그를 과거 체험했다고 분명히 명시. 코른 숭배로 정착지 파괴 후 이동력 강력했다는 반론도 있음.
   https://www.reddit.com/r/totalwarhammer/comments/1si5ihh/i_forgot_how_fast_throgg_snow_balls/

### 사용자 기준(캠페인 연구·성장 최우선)으로 다시 권고
- **첫 번째 실전 추천: 젠취(독수리) 제단 선행**. 영토 핵심 슬롯을 버리지 않는 인접 교전 지역에 제단 1~여러 개를 세우고, 그 범위에서 가능한 한 자주 승리. 비용 대비 연구 시간 절약을 기술 누적/성장·군단 성능 증강에 우선 사용. 중요한 차이는 '젠취 신앙을 반드시 최대로 올리고 영웅을 뽑은 뒤 다른 신을 시작한다'가 아니라 **젠취 제단의 연구 진도 혜택을 일찍 활성화**한다는 것. 승리 목표/자원 코어 건물은 정상 정착지로 유지.
- **두 번째: 너글(까마귀) 성장·내정**. 연구와 함께 성장 목표를 충족하도록 일부 내정 제단·일반 트롤 굴(성장과 Trollkind 동시 생산) 투자. 성장 +10/20/40 등 **전 속주 성장** 효과와 일반 제단의 지역 성장은 별개. 수입+%는 트롤족 자원에 대한 곱셈 보너스 아님.
- **세 번째/대안: 코른(사냥개) 연전 이동력, 슬라네쉬(뱀) 군단 다수 유지비·영웅 경험**. 전쟁을 연속 수행하는 고난이도/기동 중시 유저는 코른 이동력의 한계효용이 1순위로 역전될 수 있음. 슬라네쉬 제단의 전투 후 캐릭터 경험 추가와 신앙 유지비 할인도 적절히 계산.
- 기술 속도는 영속 완전연구 후 한계효용이 감소하므로, **중반부터 신규 제단을 무한 반복하지 않고** 성장/항구/코어 트롤 왕국 투자로 분기. 젠취 제단이 없는 후방이나 이미 기술을 거의 완료했다면 너글·슬라네쉬·코른의 상대 가치 증가.
- **검증 미완:** 실제 젠취 제단 원수·인접 속주 공간 범위 및 연구대기열 처리, 현행 9.0.3 전투 1회당 진도 적용의 연산 정확도, 성장·연구의 실제 최단 턴/비용과 점령 재인구 증가 기술의 정확한 선행 조건. '젤 사기=현재 단판 즉시 2기술'로 보장하지 않음.
