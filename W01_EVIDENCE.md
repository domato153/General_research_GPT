# W01 — 확인 자료·주장·반증 상태 (2026-10-12)
## 판본 및 출처 우선순위
- 9.0.3 공식 패치 (2026-10-09): https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/16126-total-war-warhammer-iii-patch-9-0-3
- 노스카 시스템 공식 7.0 개편: https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/84-total-war-warhammer-iii-patch-7-0-introducing-the-free-content-and-the-masque
- 9.0.3 추출 윈터투스 효과·승리 스크립트: https://twdatabase.com/factions/wintertooth
- 9.0.3 노스카 건물: https://twdatabase.com/buildings/norsca
- 9.0.3 병종표: https://twdatabase.com/races/norsca
- 9.0.3 기술: https://twdatabase.com/technologies/norsca
- 9.0.3 트로그 기술: https://twdatabase.com/units/throgg
- 9.0.3 vs 9.0.2 변경 비교: https://twdatabase.com/patch/9-0-3
- 2026-06 실사용 장단점/노스카 경제: https://www.reddit.com/r/totalwarhammer/comments/1tx76x4/advice_for_playing_norsca/
- 2024-05 구버전 공략: https://www.reddit.com/r/totalwar/comments/1cxer7y/ (7.0 이전으로 최신 숫자 적용 금지)
*검증 범위*: DB가 '2026-10-09 데이터 테이블'이라고 명시함. 독자 기동 실험이나 원시 PAK 직접 검증은 하지 않았음. DB 건물 추출이 Throgg 스크립트 Troll Empire 내역 전부를 포함하지 않을 수 있음.

## 정적 수치
- Throgg faction: post-battle +10% gold, all trolls physical resist +15%, upkeep -20%, allegiance champions recruitment rank +24, regional Bile/Chaos/River/Stone trolls; Monolith of Flesh 시작.
- Norsca standard Ice Troll Lair: Gold 2000, 2 turns, level 2 capital/settlement prereq, both Norscan/Ice Trolls recruit. 일반 건물이며 Troll Empire의 Trollkind 전용 건물과 혼동하면 안 됨.
- Beast Tanner: 1000 gold -> income +160; Cultist Camp Gold: 750 -> +300 on applicable resource. 수익 회수 계산은 다른 보너스 전 기본액 기준.
- Ultra unit size unbuffed rank0:
  - Norscan Trolls (16): HP 7904, armor 40, MA 34, MD 32, WS 100, upkeep 200
  - Norscan Ice Trolls (16): HP 7904, armor 60, MA 38, MD 32, WS 120, upkeep 238
  - River Trolls (16): HP 7904, armor 40, MA 34, MD 40, WS 105, upkeep 225
  - Chaos Trolls (16): HP 7904, armor 40, MA 34, MD 32, WS 100, upkeep 200
  - Chaos Trolls (Armoured) (16): armor110 MA34 MD32 WS100 upkeep238
  - Bile Trolls (16): HP 8672, armor60 MA29 MD45 WS115 upkeep250
  - Stone Trolls (16): HP7904, armor70 MA36 MD32 WS120 upkeep275
  - Fimir Warriors: HP8224 armor110 leadership70 MA30 MD42 WS100 upkeep300.
- Technology:
  - Natural Selection (200 research) leadership +4, recruit rank +1 Troll/Fimir/Skin Wolf etc.
  - Elder Trolls (400, after Natural Selection) BvI +5, melee defense +4 troll
  - Blood-Fuelled Hunger skinwolves physical res +10, vigour loss -50%
  - Violent Evolution (after Blood-Fuelled Hunger and Occasional Appeasement) armor +10 Trolls, Fimir, wolves; rank7+ missile res 15%
  - Sea Marauder's Tools global recruit duration -1 all units, global cap +1.
  - Master of Beasts rank7+ monsters ward save +5 and recruit improvements.
  - Rally the Tribes recruitment cost -25%, upkeep -5%, local recruit capacity +1.
- Throgg skills: Lord of Beasts rank12 (leadership +12 trolls/fimir/skinwolves, upkeep -10% own army, global control+2); Mutant Regeneration Horrible Regeneration + missile res20% to trolls/skin wolves, Fimir regeneration; Monstrous Fiends frenzy Troll+Fimir, melee defense+8 trolls/fimir/skinwolves; Battle-Hardened rank18 heal cap+15% all armies, replenishment+8% own; Unite the Creatures rank22 +2 summon factionwide, special troll phys resist+10%, recruit rank+2, xp+20% own army. 해금 prerequisite 확인 필수.
- Faction victory data short: 4 monster hunts; Dominion Tier III Troll-kin March; own Lair of Troll King; landmark Cave of Rocky Throne. Reward troll-building Trollkind cost -20%, Trollkind from Troll Kingdom building +25%, all trolls upkeep -10%. Long: short plus Supreme Hunter, 3 Troll Dens, Tier VI Empire of Trolls, reward global recruit time -1 / cap +2 and Spoils +2000.
- 9.0.3 Norsca nerfs vs 9.0.2: Dread Maw campaign cost1100→1200/upkeep275→300; Marauder Horsemen recruit525→600/upkeep131→150; Horsemasters recruit750→850/upkeep188→213; Ice Wolves recruit600→625/upkeep150→156/fire resistance 0→-25%; Marauder Bearmen HP11600→11200. 대부분 트롤 기본 수치는 본 변경 목록에서 주요 변경으로 확인되지 않음; 누락이 변경 없음 증명은 아님.

## 공식 메커니즘
- Trollkind: 트롤 부대를 군대에서 쓰며 생성. 특수 Troll 건물에 소비, HUD Troll Country 계단 효과와 지역 보너스, Call the Monstrous Horde를 기간제 소집. 호드는 성장하면 강화. 강 트롤 습지/수변, 돌 트롤 산악, 카오스·담즙 트롤 카오스 황무지·오염 지역의 적합 정착지.
- Spoils: 약탈/파괴 후 별도 Pillaging Force로 본국 정착지에 배달해야 진영 자원 회수. 타 노스카 외 영토 점령/유닛 특수 모집에 소비 가능.
- Norsca defeated tribe leader allows forced confederation; Wulfrik Seafang sea→discovered port teleport with cooldown/influence region allies.
- 24 Monstrous Arcanum hunts: Glorious unique monster RoR, Taming repeatable monsters, Trophy other rewards. hunts climate-type anchored not singular coordinate.
- Chaos Altar: 2 slots (primary altar and limited building). Allegiance to one of 4 Chaos gods at max, other 3 retaliate against capital; chosen god's unique champion.

## 실전 독립 근거와 반례
- 2026-06 Reddit: 여러 사용자 'Throgg + confederate Wulfrik' 효과, Ice Troll stack low-upkeep, armoured Skin Wolves flanking and ports economy; Norsca economy를 'raids crucial' vs 'passive economy extremely strong'라고 서로 다르게 평가. Campaign difficulty, economy state differ; mixed economy recommended.
- 2025-12~2026-02 multiple Reddit: calling horde suspends Trollkind progress, special buildings consuming Trollkind hurt early, reports of 18 monster temporary army at high tier, Troll Den unit cap not increasing by multiple constructions. THESE ARE REPORTED OBSERVATIONS; **NOT verified in 9.0.3 runtime**. Needs in-game testing before universal categorical instructions.
- Some 2025 report regional troll recruitment bug and horde cooldown too long; 9.0.3 persisted status unknown. Recommend actual in-game check, not declare bug in current version.
- The 2024 guides predate 7.0 and cannot set current victory triggers, building trees, economy.

## 주요 반증 경계
1. 'mass trolls unbeatable' contradicted by concentrated flame missile, anti-large, leadership collapse, wound regen cap; reinforce support screen.
2. 'fully raze everything' contradicted by key ports/Troll Dens/landmark and loot courier recoverable value.
3. 'rush horde early' contradicted by halted Trollkind accrual report; check actual tooltip each time.
4. 'Norsca poor passive income' countered by port/extra Throgg special economy buildings; measure net rather than stereotype.
5. 'all 9.0.3 unchanged' contradicted Norsca roster cost and fire vulnerability nerfs.
