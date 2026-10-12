# W14 — 트로그 9.0.3 DLC 소유권·무DLC 군단·예외 획득 경로 1차 조사 (2026-10-12)
**상태:** 사용자 승인 D4, 9.0 실제 소유권 테이블·공식 판매·9.0.3 인덱스 근거 1차 확인. 개인 보유 DLC는 사용자 미지정이므로 조건부로 구분; 사냥 24종 상세 D1 조사 **제외**.

## 1. DLC 단위부터 구분해야 할 사항
- **노스카 DLC (원래 WH1 Norsca)**: 트로그 `wh_dlc08_nor_throgg`와 울프릭 `wh_dlc08_nor_wulfrik`, 윈터투스`wh_dlc08_nor_wintertooth` 등, 기본 트롤·피미르 전사·늑대두겁·얼음 트롤·맘모스 등.
- **무료 Update 7.0**: 해당 노스카 콘텐츠를 소유해 캠페인을 시작한 플레이어에게 노스카 공통 Pillaging·Spoils·신앙과 트로그의 Troll Empire/울프릭 Seafang 개선. FLC **개편 = 트로그 진영 자체의 무료 잠금해제**가 아니다.
- **Tides of Torment – Norsca(사일 개별 팩)**: Sayl, 영웅 Beorg Bearstruck, 영웅 Fimir Noble, 새 군주 Great Shaman-Sorcerer(Death/Fire/Metal), Marauder Bearmen(2), Kurgan Horsemen(2), Curs'd Ettin(2), Chimera, Dread Maw 등. 다른 두 개별 팩(Aislinn High Elves, Dechala Slaanesh)은 노스카 신규 병종 해금 용도의 대체품이 아님.
- CA 공식 https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/85 ; Steam 사일 독립 DLC https://store.steampowered.com/app/3450970/ ; 9.0.3 테이블 인덱스 https://twdatabase.com/dlc/norsca ; https://twdatabase.com/races/norsca .

## 2. 9.0 공개 게임 DB 소유권 키 *직접 확인*
원본:
https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/db/agent_subtype_ownership_content_pack_junctions_tables/data__.tsv
https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/db/faction_ownership_content_pack_junctions_tables/data__.tsv
https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/db/main_unit_ownership_content_pack_junctions_tables/data__.tsv

- `wh_dlc08_nor_throgg / wh_dlc08_nor_wulfrik` → `wh1_norsca`; `wh_dlc08_nor_wintertooth` → `wh1_norsca`.
- `wh3_dlc27_nor_sayl` → `wh3_dlc27_tides_of_torment_nor`.
- `wh3_dlc27_nor_fimir_noble`, `wh3_dlc27_nor_beorg_bearstruck`, `wh3_dlc27_nor_great_shaman_sorcerer_{death,fire,metal}` 모두 **`wh3_dlc27_tides_of_torment_nor`**. 이 정보는 '트로그+모든 기본 노스카 DLC만 소유해도 Fimir Noble 사용할 수 있다'는 기존 20군단 가정을 **반박**한다.
- `wh3_dlc27_nor_inf_marauder_bearmen`, `_greatweapons`; `wh3_dlc27_nor_cav_kurgan_horsemen_{dualweapons,greatweapons}`; `wh3_dlc27_nor_mon_{chimera,cursd_ettin,cursd_ettin_runecaller,dread_maw,dread_maw_underground}`은 Tides of Torment – Norsca에 묶여 있음.
- **예외 발견:** `wh3_dlc27_nor_mon_chimera_monst_arcanum_reward`는 **`core_base_norsca`**로 표기되며 통상 모집 키메라 `wh3_dlc27_nor_mon_chimera`의 사일 DLC 소유권과 다름. 즉 괴수 보상의 특별 변종은 기본 노스카 관련 제품으로 표시되어 있으나 실제 인게임에서 비소유 시 사냥 보상 지급이 정상인지, 다른 DLC 제품 조합 예외가 있는지는 추가 실측 필요. **사용자 제외 D1의 24종별 괴수 사냥 분석으로 확장하지 않는다.**
- **또 다른 예외/버그:** 7.0.3 CA 공식 Hotfix는 **울프릭 Mock-God 건물이 Sayl 미소유자에게도 Khorne(쌍수) 카오스 전사를 정상 제공하도록 수정**했다고 명시. https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/12797 . 2026-08 8.1.1 CA 버그 보고는 '노스카 Slaanesh Chaos Spawn이 잘못 Dechala DLC에 묶여 모집 안 됨'이라고 주장하며 담당 개발자는 당시 재현 요청. https://community.creative-assembly.com/total-war/total-war-warhammer/bugs/bugs-redirect/14079-cannot-recruit-spawn-of-slaanesh-as-norsca . **현재 9.0.3 수정 여부 별도 확인 전**.
- 특정 Sayl/Dolgan 진영전용 유닛(카오스 전사 3변종/카오스 스폰 등)이 다른 기본 노스카 진영에 무조건 해당 DLC만으로 해금된다고 가정 금지. 원시 DB상 소유권과 `unit_to_faction/group` 사용허가가 별도, '소유권 있음≠트로그에서 일반 모집 가능'.

## 3. 실제 적용: DLC 두 시나리오
### A. 원래 Norsca만 보유 / Tides of Torment – Norsca 미보유
- 주군 트로그1 + 마법영웅 **피미르 마귀(화염·그림자)** 1(기존 노스카 콘텐츠) + 기본 얼음 트롤 9~11 + 기본 **늑대두겁(장갑 무장)** 3~5 + **피미르 전사** 2~3 + 마라우더 사냥꾼/기마 척후병 나머지 칸. 대형 괴수는 기존 노스카 맘모스/서리 용·만티코어, 특수 트롤족 모집에서 선택.
- **Fimir Noble·Beorg·Sayl·신규 Curs'd Ettin/일반 Chimera/Dread Maw/Kurgan Horsemen/Marauder Bearmen는 없는 상태로 계획**. 기존의 20칸 추천에서 '피미르 귀족1'을 '초기 가용 영웅/트롤1'로 대체.
- 노스카 기본 얼음 트롤·장갑 늑대두겁 중심 주력은 변하지 않아 D2 신앙 보너스 수혜도 있음.

### B. 원래 Norsca + Sayl 개별 DLC 보유
- 기존 혼합 20칸 트로그1, 피미르 마귀1, **피미르 귀족1**, 노스카 얼음 트롤10, 장갑 늑대두겁4, 피미르 전사2, 기동 병력1의 **편성 가용성**이 커짐. 다만 건물·영웅 수용량/턴 조건을 충족해야 하며 이 구성의 최적성이 검증된 것은 아님.
- 적의 원거리 공세가 강하면 9.0.3 공개 새 괴수 **키메라** (비행 교란), **공포의 아가리 Dread Maw** (지하 공격/원거리 견제), 저주받은 에틴, 마라우더 곰 전사로 군단 다양화. 원본 9.0.3 수치는 동시 9.0.2와 다를 수 있으므로 공개 DB 현재값 우선.
- 사일 군단 영입 가능성과 영웅 Beorg의 획득 조건·진영 상관 관계는 DLC 해금 테이블 외 **실게임 조건** 별도(구매=즉시 소환이 아님).

## 4. 함정과 고위험 혼동
- `노스카 DLC`와 `Tides of Torment 전체 번들`과 `Sayl 단독 파트`는 별개. 노스카 새 병종 때문에 Aislinn/Dechala 단독 파트를 살 필요 없음.
- 전투에서 DLC 비소유 군주/병력을 획득하는 일부 강제 합병 우회 사례 2025-11 Steam 토론은 합치되지 않는 증언이라 9.0.3 보편 규칙 아님. 9.0 캠페인 스크립트는 불허 보편문구 대신 패배 지도자/문화/속국 등 실질 조건을 검사하지만 재모집·장비/UI 제한은 소유권 검사 가능. https://steamcommunity.com/app/1142710/discussions/0/685237458700616159/
- 무료 괴수 사냥 추가 업데이트를 '모든 신규 일반 괴수·영웅 즉시 소유'로 오해하지 않기.
- 공개 9.0 소유권 원본과 9.0.3 데이터 사이에 충돌이 실제 확인된다면 최신 9.0.3 원본/실제 UI 우선. 현재 위의 주요 소유권은 9.0 게임 dump+9.0.3 TWDatabase와 일치.

## 5. 남은 검증
- `Tides of Torment – Norsca` 소유 시 정확한 건설 슬롯/지역/영웅 수용량·부대 모집 해금 조건 vs 9.0.3 현재 UI.
- 비소유 상황에서 Fimir Noble 명확한 비노출, '기본 Norsca only' 신앙 특수 카오스 병종의 9.0.3 DLC gate 예외/버그.
- 9.0.3 특별 보상용 `core_base_norsca` Chimera 정상 획득 여부, DLC 없는 합병 군주 재모집/승계 사례. D1 상세 사냥 목록으로 확장하지 않는다.

## 6. [2차 9.0.3 패치·사용자 실전평] 접근성 차이
- **9.0.3 공식 (2026-10-09):** `Styrkaar the Sortsvinaer is now available to all Norscan factions.` 따라서 예전 게임 덤프 `wh3_dlc27_sla_styrkaar_the_sortsvinaer → wh3_dlc27_tides_of_torment_sla` 소유권 행만으로 **'트로그는 스티르카르를 절대 못 쓴다'라고 판단하면 잘못**. 그러나 '모든 노스카 진영 이용 가능'은 '모든 DLC 미보유자에게 무료' 또는 '초반 자동 지급'까지 뜻하지 않는다. 실제 획득 퀘스트/계정 소유권과 조건은 현행 인게임 확인 필요.
  https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/16126-total-war-warhammer-iii-patch-9-0-3
- **2026-02-12 실제 트로그 클리어, Sayl DLC 없음**(캠페인 Normal/전투 Hard, Victory Conditions Overhaul 모드, 당시 일부 젠취 연구 버그): 얼음 트롤과 늑대두겁 4~5로 유효한 20칸 군단을 구성하고 울프릭 합병. 즉 사일 개별 DLC 없이도 트로그 핵심 플레이 루프가 성립한다는 **실전 사례 1건**, 현재 9.0.3 성능 수치 보증은 아님.
  https://www.reddit.com/r/totalwarhammer/comments/1r2zdri/throgg_campaign_retrospect/
- **2026-03-22 사용자 병종 편성 댓글**: 추가 DLC로 Chimera(비행) + Dread Maw(지하 공격) 조합이 적 사격 후열 차단에 효과적이라는 개인 사용담; 보편 최적이 아니라 사일 보유 시 전술적 **분기**.
  https://www.reddit.com/r/totalwar/comments/1s09yh4/norsca_army_comps/
- **2026-06-05 댓글**: 비DLC 전제 트로그+울프릭의 주요 가치는 기존 노스카 스킨울프·항구 경제와 전투 수입이라는 것. '키메라 너무 좋다'는 별도 DLC 소유 가능성에 따라 정확히 분리해서 해석해야 하며 **Norsca만 샀으니 Chimera 기본 일반 모집 가능**이라는 주장은 안 됨.
  https://www.reddit.com/r/totalwarhammer/comments/1tx76x4/advice_for_playing_norsca/
- **9.0.3 판본 충돌 검증 우선순위:** 최신 공식 패치의 Styrkaar 사용가능 진영 ＞ 과거 9.0 덤프의 세력 제한 / DLC 소유권(법적 상품 제한)은 9.0.3 명시 확인 불가면 미확인. 원래 Fimir Noble·Dread Maw·일반 Chimera 사일 DLC 조건은 게임 소유권 원자료 기준 유지; 실제 미소유 플레이로 영웅 탭/모집권까지 재현한 테스트는 아님.
