# W15 — 2026 트로그·노스카 실전 사용자 평가와 9.0.3 근거 구분 (2026-10-12)
**상태:** 승인 D2/D3/D4의 2차 비교근거 종합, D1 상세 괴수 사냥 제외. 이 문서는 실전평을 성능/패치 고정 수치로 환산하지 않음.

## 유저의 목표와 평가 방법
현재 사용자 중점은 **캠페인 기술 연구가 빠르고 성장도 빠른 선택**. 9.0.3 기준 판단 시 '초반 연구 완료→성장/모집 기술 선점→중반 영토·트롤족/수익 확장'의 시간 누적 가치를 우선. 단순 전투 최종 승률이나 군주·영웅 전투력, 후반 유지비 할인만으로 신앙 순위를 매기지 않음. 전투 빈도, 제단 주변 실제 전투 위치, 정착지 슬롯 희생, DLC, 난이도/모드, 버그 수정 시점을 함께 기록.

## 근거 계층
- A: 공식 핫픽스/9.0.3 패치 안내 (최신 버전 동작 주장).
- B: 9.0.3 TWDatabase 장치·9.0 Lua 보조 (정적 현재판 또는 준현재 메커니즘).
- C: Reddit/Steam 2026 실제 플레이 경험 (조건/패치/버그/모드별 관찰과 반대 의견).
- 부정: 7.0/7.0.3의 **해결된 버그**를 9.0.3 정규 플레이 최적루트의 재현 가능 값으로 사용하는 오류.

## D2 실전 사례, 상충 의견과 조건
1. 2025-12-10 r/totalwar <Norsca research rate bug>: 특정 승리마다 영구 연구 속도 +5 * 제단 수가 계속 누적되어 턴30에 5000%로 올랐다고 사용자 보고(당시 7.0 버그). **현재값 아님**. https://www.reddit.com/r/totalwar/comments/1pj4em3/norsca_research_rate_bug_im_currently_with_5k/
2. 2026-01-15 r/totalwar <So with 7.0.3 Norsca researches even faster now>: 턴9 전투 1회로 5턴 기술 2개 등 댓글 다수, 실 버그/과대 연구 포인트 문제가 관련됐고 7.1 공식 후속 수정. **9.0.3 단일 전투당 정확한 진도 증거 아님**. https://www.reddit.com/r/totalwar/comments/1qdwtkh/so_with_703_norsca_researches_even_faster_now/
3. 2026-06-11 r/totalwarhammer <Best/Preferred approach to Norscan Altars?>: 독수리 제단을 전투 잦은 전선에 여러 개 두어 연구를 증폭·중첩한다는 후기; 트로그 직접 경험에서 '전투당 연구 1턴' 주장도 있으나 세이브·정확 버전 미제시. 신앙 모두 끝내도 제단 부근 전투 승리가 중요. 다른 플레이어는 **사냥개의 행동력 회복이 연구보다 더 강함**, 또 다른 이는 **너글 성장 보너스가 Spoils 건설/점령 인구 기술 때문에 체감이 약함**이라고 평가해 **만장일치 아님**. https://www.reddit.com/r/totalwarhammer/comments/1u34qwe/bestpreferred_approach_to_norscan_altars/
4. 2026-06-15 r/totalwar <Norsca rework bloated>: 기회비용 반례. 트로그 'Troll Empire'를 키울 도시는 일반 건물 슬롯 중요 → 제단 유행에 따라 2슬롯 도시로 바꾸면 왕국 생산성을 손상하고 후반엔 이미 과도한 강력함에 보너스가 필요 없다는 의견. https://www.reddit.com/r/totalwar/comments/1u6jiln/norscas_rework_is_such_a_bloated_mess_that_ca/
5. **공식으로 확인된 시점:** 7.0.3 연구 속도 영구증가→일회 연구 보너스 25/50/75/100; 7.1 무한 연구 버그 수정; 9.0.3 TWDatabase Eagle 제단 전투 승리 후 +25~100 Research Rate Points(인접 속주), 성장 +20/30/40(해당 건물 레벨). https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/93 ; https://twdatabase.com/buildings/norsca

## D3 실전평
6. 2025-12-27 r/totalwar <Who best Norsca LL?>: 트로그 시작 후 울프릭을 전투로 병합해도 Seafang은 **울프릭 개인**에 남는다는 다수 댓글; 반대 방향(울프릭→트로그)은 Troll Empire 진영 고유 기능을 얻지 못한다고 증언(공식 루아와 완전한 합병 실측은 별개). https://www.reddit.com/r/totalwar/comments/1px8aua/who_is_the_best_ll_to_learn_how_ti_play_norsca/
7. 2026-06-05 r/totalwarhammer <Advice playing Norsca?>: 트로그+울프릭 개인 이동력 + 항구/전투 수입을 권고. 한두 큰 군단 + 이동/합병 등 초반 운영 중요. https://www.reddit.com/r/totalwarhammer/comments/1tx76x4/advice_for_playing_norsca/
8. 2026-03-26 r/totalwarhammer <Chaos factions confederation>: 울프릭으로 40턴 40정착지/3군단 경험은 **사례 하나**; 2026-05 다른 전황에서 소부족이 울프릭/트로그를 흡수한 보고도 있어 고정 합병 턴으로 안내 금지. https://www.reddit.com/r/totalwarhammer/comments/1s48jww/chaos_factions_confederation/ ; https://www.reddit.com/r/totalwarhammer/comments/1t6p71m/perhaps_the_most_bizarre_campaign_ive_ever_played/

## D4 실전평 및 9.0.3 예외
9. 2026-02-12 r/totalwarhammer <throgg campaign retrospect>: **Sayl DLC 미소유**, Normal/Hard, 승리 조건 모드, 옛 젠취 버그 일부. 얼음트롤/4~5 늑대두겁, 울프릭 합병으로 성공. 기본 노스카 DLC의 **실행 가능한 군단**이라는 사례이며 정식 9.0.3 최적 수치는 아님. https://www.reddit.com/r/totalwarhammer/comments/1r2zdri/throgg_campaign_retrospect/
10. 2026-03-22 r/totalwar <Norsca Army Comps?>: Sayl 확장 군단 Chimera+ Dread Maw로 후열 교란 조합 좋다는 실전 코멘트. DLC 소유·건설 선행 조건 확인이 필요하며 다수 유저 독립 합의는 아님. https://www.reddit.com/r/totalwar/comments/1s09yh4/norsca_army_comps/
11. **9.0.3 신규 내용:** 공식 패치 'Styrkaar now available to all Norscan factions'은 활용 가능한 **진영 제한 변경**이고, 게임 상품 소유권(Dechala/Slaanesh 개별 DLC가 필요한지)은 확인 미완. https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/16126-total-war-warhammer-iii-patch-9-0-3

## 사용자 목표에 따른 2차 추천
- 초반: 최우선 **전선 근처 젠취(독수리) 제단 선행**, 빨리 연구 완료하는 기술을 통해 트롤 병력 강화 및 성장·점령 이익 확보. 대미지·마법 보너스 자체가 핵심 이유가 아니라 **전투 후 연구 진도 보너스**.
- 핵심 트롤 왕국·항구·성장 건물 거점은 **일반 점령** 유지. 새 제단은 **전투 많은 주변 일반 영지**, 약탈·파괴한 비핵심 지역 중심. 전선 이동으로 더 이상 해당 제단 주변 전투가 없으면 신규 투자가치 하락.
- 중반: 성장/내정 병목이면 **너글** 확대(성장 자체 및 건물 수입), 다중 고급 군단 적자면 **슬라네쉬**, 연속 정복·이동력 차례 이득이 크면 **코른**으로 전선 제단 혼합. 강한 사용자 간 반론을 근거로 군단·전쟁 상황에 따라 교체.
- 군단/확장: 트로그 시작 → 울프릭 지도자 병합/Seafang 전용 원정, 사일 DLC 없으면 기존 얼음 트롤+장갑 늑대두겁+피미르 마귀 조합, DLC 있으면 피미르 귀족·키메라/아가리 군단 확장.
- **9.0.3 고정 패치 실사용 E2E 없음**. 젠취 1제단 전투 1회당 실제 연구 포인트·제단 중복 배율·현 UI 기술 턴 예측/성장 영향, 사일 군주 비보유 합병/스티르카르 소유권은 직접 확인 대기.
