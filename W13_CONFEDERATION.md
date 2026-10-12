# W13 — 트로그 9.0.3 노스카 강제 합병·울프릭·사일 승계 1차 조사 (2026-10-12)
**상태:** 사용자 승인 D3, 9.0 공개 원시 Lua·7.0 공식 개편·2026 후기 교차, 1차 조사/조건부. **사일 고유 기능 승계 여부/결과 및 모든 초기 전쟁·건물 변환은 9.0.3 런타임 직접 재현 전 미확인.**

## 1. 실제 노스카 지도자 격파 연방 통합 절차(9.0 원시 스크립트)
- `script/campaign/wh3_campaign_subjugation.lua`: `SubjugationBattleComplete_Norsca`는 전투 공격·방어 측이 모두 문화 키 `wh_dlc08_nor_norsca`이고 **패배자의 군주가 세력 지도자**이면 `trigger_norsca_confederation_dilemma` 실행. 일반 장군 패배만으로 전체 진영 강제합병이 발동하지 않음.
- 거부 조건에는 인간 플레이어 대상, 다른 인간 플레이어의 속국, 무효 특정 AI 진영, 대상이 혼돈의 전사(WoC) 문화 종속 속국인 경우가 있음. **전투에서 지도자 승리했다고 무조건 이벤트가 뜬다는 보장은 없음**.
- `loser_fm:character_details():is_unique()`가 true면 `execute=false`; 지휘관을 처형하는 선택지가 아닌 부상 처리(최소 10턴)가 분기되고, 일반 군주와 구별. 동맹 선택(`choice == 2`), 처형·부상(`choice == 3`)이 코드에 존재하며 연방 선택지와 구분. 병합을 선택하면 영토·기존 군단이 넘어오지만, 이전 진영의 확장 메커니즘까지 자동 이식되는 것은 아님. 정확한 선택지 배열/캠페인 패널 표시 여부는 UI 확인 필요.
- 토벌 방식은 **북부 노스카 지도자 합병**으로 먼저 활용, 패배 세력의 재정 적자 군단·불필요한 외교전선 유입을 즉시 점검.
- 9.0 스크립트: https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/script/campaign/wh3_campaign_subjugation.lua

## 2. 울프릭을 트로그에 합병: 강력한 긍정 근거
- CA 공식 7.0: 울프릭 개인이 Seafang으로 **바다에서 공개된 항구로 즉시 순간이동**, 그 주위의 **아군 군단 일부도 함께 이동** 가능. 데려가는 유닛/군단 수에 따라 재사용 대기 변화. 공식 https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/84-total-war-warhammer-iii-patch-7-0-introducing-the-free-content-and-the-masque
- 공개 9.0 `db/seafang_teleportation_ritual_cooldowns_tables/data__.tsv`: 동반 유닛 수 1→2턴, 5→4, 10→6, 15→8, 20→10, 25→12, 30→14, 35→16, 40→20, 60→30, 80→40, 99999→100(상한값 정의). 실제 UI의 슬롯 계산 및 어떤 범위의 군단이 유효한지 별도 검증 전에는 **'군단 1개 2턴'으로 해석 금지**, 테이블 단위는 `num_units`.
- 2025-12~2026-06 이용자 복수의 독립 사례는 트로그가 울프릭을 패배·합병해도 **울프릭 개인 Seafang 보존**, 트로그/다른 개별 군주에게 능력 일괄 이전은 아님. 관련:
  https://www.reddit.com/r/totalwar/comments/1px8aua/who_is_the_best_ll_to_learn_how_ti_play_norsca/
  https://www.reddit.com/r/totalwarhammer/comments/1tx76x4/advice_for_playing_norsca/
- 따라서 트로그의 Troll Empire 세력 기반 위에 울프릭 Seafang 이동을 덧붙이는 운영이 **실전 추천**. 다만 울프릭 초기 해역/북부 출몰 턴은 게임마다 달라 10턴 고정 공략 금지.

## 3. 사일(Dolgan)의 합병/고유 시스템 승계 경계
- CA 공식: Sayl은 일반 `Allegiance` 시스템을 사용하지 않고, 별도의 Dark Ritual·Manipulations/카오스 제단 체계를 갖는 이례적인 노스카 진영.
- `wh3_dlc27_sayl_narrative.lua`의 핵심 `faction_key = "wh3_dlc27_nor_sayl"`; `wh3_dlc27_nor_sayl_manipulation.lua`도 **사일 진영 키**로 초기화되는 별도 메커니즘. **트로그가 사일을 합병해도 고유 Dark Ritual·Manipulations가 트로그에게 그대로 귀속된다고 주장할 근거 없음**. 사일이라는 군주 개인의 마법/스킬과 진영 메커니즘은 분리할 것.
- 9.0.3 Dolgan은 Dark Tower(Mountain's End)에 출발 (TWDatabase `https://twdatabase.com/factions/dolgan`), 트로그 윈터투스 북부 시작지와 멀다. **북방 초반 내정·합병보다 즉시 사일 원정이 더 좋은가?** 일반적으론 아니며 외교·경로·DLC 상황에 따라 후반 선택.
- `subjugation` 문화조건은 노스카 → 노스카 같은 문화에서 세력 지도자 격파 시 분기하도록 구성되어 있고, 사일은 노스카 플레이 세력이지만, **소유 DLC 유무에 따른 정확한 합병 이벤트·사일 영구 모집 재활성·캠페인 UI의 최종 허용**은 9.0.3에서 직접 검증되지 않았다. 무조건 가능·불가능 둘 다 단정 금지.
- 2025-11 Steam 커뮤니티 DLC 합병 소유권 예측은 엇갈림. 일부는 'subjugation은 소유권 우회 가능'이라 하고 일부는 'DLC 없으면 LL 부상 후 재모집 불가'라고 함. 출시 전 추측이므로 **현재 9.0.3 확정 근거 아님**: https://steamcommunity.com/app/1142710/discussions/0/685237458700616159/

## 4. 합병·건물 전환 관련 보고의 해석
- CA 버그 신고 2026-01 `7.0.3`: 사일로 울프릭을 강제 연방통합 후 캐세이 대관문에서 티어 3 제단 일부가 티어 1로 돌아가는 현상. 링크 https://community.creative-assembly.com/total-war/total-war-warhammer/bugs/11939-norsca-altar-tier-reset-after-confederation-sayl-the-faithless
- 2026-09 `9.0~9.0.1` 워리어 오브 카오스(WoC) 연방통합에서 Dark Fortress→Chaos Altar 변경 버그 신고 존재. 링크 https://community.creative-assembly.com/total-war/total-war-warhammer/bugs/bugs-redirect/14388-new-archaon-confed-causes-dark-fortress-to-turn-into-altar
- 둘은 서로 다른 조건·세력. 트로그 9.0.3도 동일하게 손상된다는 일반화 금지. 그러나 **직전/직후 건물 티어·유형·특수 건물 슬롯 스냅샷**과 재정/군단 변화를 확인하는 실전 안전 점검은 정당.
- 직접 합병 시 외교적 적대 관계·군단의 고용/해체·지역 수익이 넘어오는 기본 행동은 게임 시스템 기대지만, 획득한 **모든 기존 전쟁·동맹 조약이 그대로 넘어오는지**는 고정 표로 확정하지 않음.

## 5. 1차 실전 추천 및 B/W13 잔여
1. 트로그 본국 코어/트롤족 생산 → 북방 소부족 지도자 합병 → 지형·외교 안정 후 울프릭 합병 기회 포착. **울프릭은 Seafang 원정 전용 지휘관**으로 계속 운용 가능성이 높다.
2. 사일은 '마법 전설군주 개인' 획득 가능성이 목적일 때만 추가 검토하고, **트로그가 사일의 Dark Ritual/Manipulations를 얻는다고 기대해 원정할 필요는 없다**.
3. 다음 검증: Wulfrik Seafang 실전 합병 뒤 UI, 사일 합병 가능 여부(소유권 분기), 동반군단 제한, 강제합병 직후 제단 전환 오류 9.0.3, 선행 동맹/전쟁 상태 이동, 사일 패배시 LL 생존과 재모집.

## 6. [2차 사용자 실전평] 강제 합병과 전선/개인 군주 가치
- 2025-12-27 r/totalwar Norsca 군주 선택 댓글 **137 추천**(공유 당시): 트로그가 종족 트롤제국 능력을 갖고 출발해 울프릭을 **지도자 격파 후 합병**하면 Seafang은 **울프릭 개인에게만 유지**. 약 턴10 중앙 산맥 출몰·마라우더 위주 군단이라는 것은 개별 사례(맵 진행 랜덤)이지 고정 스폰 아님. https://www.reddit.com/r/totalwar/comments/1px8aua/who_is_the_best_ll_to_learn_how_ti_play_norsca/
- 2026-06-05 r/totalwarhammer 156 추천 플레이어: **트로그 시작→울프릭 합병**, 트로그 Troll Empire+울프릭 순간이동·항구 경제 조합 추천. 전투 수입이 우선이고 일반 노스카 수동 내정 수익은 한정적이라고 강조. https://www.reddit.com/r/totalwarhammer/comments/1tx76x4/advice_for_playing_norsca/
- 2026-02-12 r/totalwarhammer **실제 트로그 클리어 후기**, 캠페인 Normal/전투 Hard, **Victory Conditions Overhaul 모드**, Sayl DLC 미소유. 초반 말라카이 격파·울프릭 합병 후 기동성 좋은 늑대두겁 4~5가 전투 핵심이라고 평가. **2026년 2월 일부 턴 젠취 버그 적용**이라고 스스로 밝힘, 9.0.3 정확 증거로 오용 금지. https://www.reddit.com/r/totalwarhammer/comments/1r2zdri/throgg_campaign_retrospect/
- 2026-03-26 유저 Wulfrik 캠페인 한 건 '40턴 3군단 40지역' 경험은 연방통합 스노우볼 가능성의 표본이지 트로그에서도 보장되는 최적 성과 아님. https://www.reddit.com/r/totalwarhammer/comments/1s48jww/chaos_factions_confederation/
- **반례:** 2026-05 유저는 보잘것없는 바나하임링 부족 AI가 울프릭·트로그를 역으로 합병했다고 보고. 리더 패배 시 **자기 주군도 연방통합 대상이 될 수 있음**. https://www.reddit.com/r/totalwarhammer/comments/1t6p71m/perhaps_the_most_bizarre_campaign_ive_ever_played/
- 2026-03 플레이어는 트로그로 트롯(클랜 몰더) 동맹 시 전선 보호 vs **동맹의 불필요한 원거리 전쟁 소환**이라는 손익을 제시. 이 선택은 판본·외교 차이 때문에 고정 명령으로 확정하지 않음. https://www.reddit.com/r/totalwar/comments/1rpgqxl/a_couple_questions_for_norsca_throgg_and_sayl/
- **조건부 2차 판정:** 트로그의 고유 트롤 경제를 포기하고 울프릭으로 새 캠페인을 시작할 이유보다, **트로그로 울프릭을 추가하는 기회이익**이 강하게 뒷받침됨. 그러나 세력 지도자 합병 직후 **전쟁·영지·적자 군단·건물 및 제단 등급** 대조가 필요. 사일의 Dark Ritual 소속 키가 고정되어 있으며, 사일 합병 뒤 트로그로 이식된다는 실제 플레이 후기를 찾지 못함 → 여전히 UNKNOWN; 스크립트 구조상 이식되지 않을 가능성이 크다는 **추론**만.
