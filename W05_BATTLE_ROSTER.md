# W05 — 9.0.3 트로그 군단·전투 조합 보완 (2026-10-12)
상태: 게임 데이터상 수치 + 개편 이후 2026 유저 사례/반례 조사. 독자 게임 기동 실측·정확한 DPS 전투 재현 미실시. 최종 확정 아님.

## 한국어 병종/모집 건물 확정도
- 노스카 얼음 트롤 (Norscan Ice Trolls), 노스카 트롤, 늑대두겁 (Skin Wolves), 늑대두겁 (장갑 무장), 피미르 전사(대형 무기), 재앙의 마귀 피미르 (화염), 피미르 귀족, 키메라, 강가 트롤, 돌 트롤, 담즙 트롤: Honga Warhammer III 한국어 유닛 key 대응(해당 사용자에게 한국어 우선). 워해머 I의 Skin Wolves=스킨 울프 명칭은 최신 Warhammer III 자료에서 늑대두겁인 점에 유의. Honga 일부 전투 수치는 9.0.3 이전 값이므로 게임 데이터 수치는 TWDatabase 9.0.3 사용.
- 늑대두겁 모집 '군견 보관소' L1 (500골드/1턴, 군견), '전투 늑대 소굴' L2 (1000골드/3턴, 늑대두겁/얼음 늑대 가능), '암흑 공물의 동굴' L3 (2000골드/4턴, 장갑 무장 늑대두겁 모집 가능): 해당 체인은 총 3500골드/8 건설 턴, 본도시 3티어 주성 업그레이드 비용 별개. 일반 건물 슬롯 및 코어 정착지에서 가능한지 확인할 것. Honga 한국어 건물 데이터, TWDatabase 9.0.3 units unlock cumulative 3500/8 turns/main building level3. 2026-10-12 버전 업그레이드 비용은 Honga 데이터와 현재 DB가 이 체인에서는 일치. https://www.honga.net/totalwar/ko/warhammer3/factions/wh_dlc08_nor_wintertooth/buildings ; https://twdatabase.com/buildings/norsca
- Fimir Balefiend (Fire) 국내 한국어 '재앙의 마귀 피미르 (화염)', 9.0.3 실제 모집 경로/필요영웅수용량 미검증. 이름만 확인해 두고 즉시 모집가능하다는 지시 금지.

## 군단 실전 판정 및 9.0.3 기초 스탯
- 트로그 all-Troll +15% physical resistance faction, upkeep -20% faction. 트로그 고유 Lord of Beasts rank12 prerequisites, Mutant Regeneration Horrible Regeneration trolls+wolves, +20% missile resist own army, Fimir normal regen; Monstrous Fiends +8 MD trolls/fimir/wolves, frenzy trolls/fimir. Battle-Hardened rank18 heal cap+15% faction and replenishment+8% own. Unite Creatures rank22 extra +2 horde summon and +10% phys resist special Troll faction. 현재 9.0.3 출처 https://twdatabase.com/units/throgg .
- 9.0.3 ultra rank0 Trolls 16 entities, Ice Troll armor60 MA38 MD32 WS120 cost950 upkeep238, River Troll armor40 MA34 MD40 WS105 cost900 upkeep225, Bile armor60 HP8672 MA29 MD45 WS115 upkeep250, Stone armor70 MA36 MD32 WS120 upkeep275, Fimir Warriors greatweapons heavy AP front support. 수치가 전투 DPS 아님.
- 늑대두겁 기본 24개체 HP7416 armor15 speed75 MA32 MD28 WS60, 기본 장갑 무장 24개체 HP7416 armor70 speed65 MA32 MD28 WS60. Korean Honga 일부 값은 참고이고 9.0.3 TWDatabase 기준 구체 가격 대조 필요. 늑대두겁은 기동+대대형 측후방 타격 역할, 사격/고장갑 유닛엔 별도 판단.
- 추천 20슬롯 예시(후보, 우위 직접 재현X): 트로그1, 마법 영웅1, 피미르 영웅1, 얼음트롤10, 늑대두겁4, 피미르전사2, 기마투척/원거리1 =20. 초반 부족하면 트롤7~9 + 늑대두겁2 + 저렴한 보병/사격. 늑대두겁 4~5 체감 추천이 2026-02와 2026-03 커뮤니티에 복수 확인됨. 사용자가 높은 마이크로 부담을 싫어하면 늑대두겁 2~3으로 줄이고 트롤 늘리는 선택 가능.
- 실전 방면: 적 장거리 화력(말라카이 드워프, 스케이븐 워프화염/래틀링, 키슬레프 하이브리드, 제국 포병)에는 트롤 일렬 정면 진격 비추천. 엄폐/전선 분리·군단 후방으로 늑대두겁 침투·피미르 저지 역할. 화염 취약/대대형/사기 붕괴·재생상한 중요한 반례. 재생의 개체 부활 가능(Horrible)도 9.0.3 인게임 재현 필요.
- DLC 조건: 키메라와 공포의 아가리/저주받은 에틴은 추가 DLC·사냥 보상 경로에 따라 획득 가능성이 달라짐. 단순히 전원 확보 가능한 기본 트로그 군단으로 혼동 금지.
## 교차검증된 커뮤니티 사례
- 2026-02 Throgg campaign retrospect: 난이도 일반/전투 어려움, Victory Conditions Overhaul 모드, DLC Sayl 없음, 초기 일부 버그 경험, 늑대두겁 4~5대/군단이 전투에서 주역이었다고 명시. 신뢰 경계: 모드/난이도 개인 경험이지 9.0.3 최적편성 보장은 아님. https://www.reddit.com/r/totalwarhammer/comments/1r2zdri/throgg_campaign_retrospect/
- 2026-03 Norsca army comps: 얼음트롤+기마척후+마법사, 혹은 얼음트롤+갑주 늑대두겁+피미르+키메라 합성 조합 추천. 키슬레프 이용자의 상대 관점에서 트롤 화력집중에 약하고 늑대두겁은 사격진 침투 위험. https://www.reddit.com/r/totalwarhammer/comments/1s09y77/norsca_army_comps/
- 2026-04 일반 노스카 전력은 얼음트롤/갑주 늑대두겁/피미르, 키메라 제한적 지원; 맘모스/에틴은 총병에 취약. https://www.reddit.com/r/totalwarhammer/comments/1sl82zw/norsca_army/
- 2026-06 진영 경제/울프릭 합병/항구: https://www.reddit.com/r/totalwarhammer/comments/1tx76x4/advice_for_playing_norsca/
- 2026-09 추가 트롤 다양성 논의는 현재 트롤 병종 역할의 비대칭/하위 계열 다양성 제한과 맞닿음. https://www.reddit.com/r/totalwar/comments/1w4znng/should_throgg_get_more_trollmonster_infantry_units/
- 상반된 반론: 대량 트롤만으로도 초반 정복 충분(2025-12 유저), 하지만 마이크로·항공/사격 대응엔 늑대두겁/키메라/피미르 지원이 체감상 유리. 최적 계량 DPS·난이도별 전투 재현 없음.

## 미확인·재검증 필요
- 기술·고유스킬의 정확한 9.0.3 공식 한국어 표시명; Honga unit page는 스킬 항목 노출 부족. 한국어명 확인 없이 영어를 마음대로 번역 금지.
- 일반 노스카 건설 체인을 트로그 특정 지역/카오스 제단에서도 동일하게 지을 수 있는지; 시작 정착지의 기존 건물 슬롯/건물 없는 상태; DLC 유닛 획득 루트; 실제 소집 중 트롤족 자원 정지 턴수.
- 골드·트롤족·전리품 비용이 9.0.3 최신 인게임 표기와 충돌할 가능성. 동일 조건 전투 실측 데이터 부족.

## 2026-10-12 D4 공개 소유권 원시 테이블에 따른 A 정정
- 이전 '피미르 귀족 1'이 모든 트로그 플레이어의 보편 기본 가용성인 것으로 읽히면 오류. 9.0 게임 DB `db/agent_subtype_ownership_content_pack_junctions_tables/data__.tsv`: `wh3_dlc27_nor_fimir_noble → wh3_dlc27_tides_of_torment_nor`. **사일 DLC 소유 필요**. `피미르 마귀`와 구분.
- **사일 미보유 기본 20칸:** 트로그 1 + 기본 피미르 마귀 1 + 얼음 트롤 11 + 장갑 늑대두겁 4 + 피미르 전사 2 + 기동 사격 1 = 20.
- **사일 보유 20칸:** 트로그 1 + 피미르 마귀 1 + 피미르 귀족 1 + 얼음 트롤 10 + 장갑 늑대두겁 4 + 피미르 전사 2 + 기동 사격 1 = 20. 실제 영웅 수용량/건설 티어 조건 별도. 근거 `W14_DLC_AVAILABILITY.md`, https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/db/agent_subtype_ownership_content_pack_junctions_tables/data__.tsv
