# W16 — 트로그 9.0.3 통합 공략 최종 내용 감사
**2026-10-12 / 판정: 수정 후 조건부 내용 감사 PASS, 보고서 확정은 미승인**. 본 요청은 감사이지 D1 사냥 상세 조사 재개·최종 배포·main 병합 위임이 아님.

## 실제 확인한 정본과 방법
- 연구 브랜치 FINAL_REPORT.md 원고 §1~§10과 RESEARCH_PLAN.md, W01·W02·W04·W05·W06·W07·W08·W10·W12·W13·W14·W15 개별 근거를 조회·대조. W03는 이전 통합 초안 상태, W11은 운영 규칙 롤아웃이며 별도 새 조사 근거로 중복 계산하지 않음.
- 9.0.3 공식 패치 https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/16126-total-war-warhammer-iii-patch-9-0-3 ; CA 7.0.3 젠취 연구 수정 https://community.creative-assembly.com/total-war/total-war-warhammer/forums/7-patch-notes-amp-announcements/threads/12797
- 9.0.3 공개 게임 데이터 https://twdatabase.com/technologies/norsca ; https://twdatabase.com/units/throgg ; https://twdatabase.com/buildings/norsca ; https://twdatabase.com/factions/wintertooth ; https://twdatabase.com/patch/9-0-3 .
- 보조 9.0 원시 https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/script/campaign/wh3_dlc27_nor_kinfolk.lua ; https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/script/campaign/main_warhammer/victory_objectives.lua .
- 2026 직접 플레이 https://www.reddit.com/r/totalwarhammer/comments/1r2zdri/throgg_campaign_retrospect/ (Normal/Hard, 승리 조건 모드, 당시 젠취 버그 인정); https://www.reddit.com/r/totalwarhammer/comments/1u34qwe/bestpreferred_approach_to_norscan_altars/ (젠취 연구가속 vs 코른 이동력); https://www.reddit.com/r/totalwar/comments/1u6jiln/norscas_rework_is_such_a_bloated_mess_that_ca/ (트로그 2슬롯 제단의 고유 건물 기회비용).
- 검증 방식: 실제 파일 읽기·섹션별 주장 매핑·원시 Lua 조건/9.0.3 게임 데이터·공식 패치·실사용 사례/반례 비교. 9.0.3 게임 클라이언트 직접 구동이나 한국어 loc/pack 현행 파일 체크는 시행하지 않음.

## A. 사실상 오류가 확인되어 직접 수정한 2건
1. **Lord of Beasts 유지비 감소 범위:** 이전 원고는 '자기 군단 유지비 -10%'로 서술하여 모든 유닛에 적용되는 듯하지만 정확한 9.0.3 원문은 트롤·피미르·늑대두겁 (트로그 군단) 부대에만 -10%. FINAL_REPORT §6, W01 국소 수정. https://twdatabase.com/units/throgg
2. **Mutant Regeneration 사격저항 범위:** 이전 원고는 피미르를 포함한 전체 군단처럼 읽혔으나 +20% 사격저항은 트롤·늑대두겁(트로그 군단)에만 적용. 피미르는 일반 재생만 부여. FINAL_REPORT §6, W05 국소 수정. https://twdatabase.com/units/throgg

## B. 사용자 핵심 목표 관점의 실질 누락 2건 보강
3. **젠취 가속과 성장기술 선택 미연결:** §5에 젠취 연구 보너스를 추천했으나 바로 뒤 1~4위가 모두 전투 기술이어서 '연구와 성장 빨리'라는 사용자 평가조건이 실전 클릭 순서로 이어지지 않았음. 9.0.3 기술로 성장 경로 Untiring Sentries(200)→Beware the Crow(400, Growth +15)→A Reminder of Strength(500, Marauders to Builders 명령 성장 +10)를 추가. 건설 A Taste of Bloody Triumph(복수 선행, 건설 비용 -20%·시간 -1)→The Eyes of the Four→Under Their Gaze(새 점령 정착지 인구잉여+1) 별도 경로. 위험한 전선은 Natural Selection(200)→Elder Trolls(400) 우선하도록 조건부 추천. https://twdatabase.com/technologies/norsca
4. **최종 고유 스킬 Lord of Monstrosities 누락:** 복수 선행 후 세력 전체 트롤/피미르/늑대두겁 전역 모집시간 -2턴, 노스카 괴수 무기 피해 +10% 세력 전체, 트로그 공포 유발; §6 및 W05 반영. https://twdatabase.com/units/throgg .

## C. 주장별 수록·충실도 판정
| 기존 W 파일/축 | 보고서 연계 | 판정 / 남은 한계 |
|---|---|---|
| W01 패치·트로그 종족/병종 | §1,7,9 | 원문·수치 대체로 맞음, 스킬 범위 오류 A1 정정 |
| W02 캠페인·실전 경로 | §1~10 | 영토·군단·연구 분기 수록, 성장 경로 B3 보강 |
| W03 통합 초안 | 현 FINAL_REPORT | 파일명 FINAL은 상태 확정이 아님, 이력·사용자 승인 유지 |
| W04 한글·건축 | §3,7,8 | 한국어 병종명·트로그 L1 모집 건물 실전 조건부; 9.0.3 한국어 화면/시작 슬롯 미확인 |
| W05 전투·DLC | §6,7 | 피미르 귀족 DLC와 부대 20칸 맞음; Mutant Regen 적용범위 A2 수정 |
| W06 트롤족·소집 | §3,4 | +1/+2, 일시 중단, 플레이어 소집비 II~VI와 AI 구별; 현 9.0.3 실제 팩 비교 미완 |
| W07 기존 감사 | 전장 | 이전 대표 오류 수정 이력 보존 |
| W08 확장·수송 | §2,3 | 지도자 합병·Spoils 수송·전선 선택, 고정 턴 보장 X |
| W10 계획 밖 조사축/승리 판정 | §8·계획 | 사용자 D1 제외·D2~D4 채택 반영. 트롤특수 지역 3개 소유는 9.0 Lua 직접 대조 |
| W12 신앙·제단 | §5 | 젠취 전투 연구진도 25/50/75/100, 7.0→7.1 버그 구분; 중첩 세이브 실측 X |
| W13 합병 | §2,8.5 | Wulfrik 개인 Seafang·사일 진영 전용 Lua, 실제 9.0.3 합병 세부 실측 X |
| W14 DLC | §7,8.5,9 | Fimir Noble 등 사일 DLC 조건과 9.0.3 Styrkaar 진영 접근 예외, 미소유 UI 검증 X |
| W15 실전평 | §5,8.5 | 출처별 날짜·난이도·모드/버그·반례 분리, 모집 최적해 증명 X |

## D. 버전·확정도 및 실전적 기회비용 검증
- **젠취 9.0.3 기본 건물**: 전투 승리 시 인접 속주 해당 제단 범위에서 25/50/75/100 연구 진도 포인트. 7.0/7.0.3 연구속도 누적·기술 연속 완료 버그 성능을 현재 정상 수치로 인용하지 않음. 750골드 제단 건설 턴은 지역/체인에 따라 달라 2턴 일반 예시, 포트·관문 변형 추가 조건부. https://twdatabase.com/buildings/norsca
- **비용 수치 9.0.3**: 본문 노스카 마라우더 기마병 525→600(캠페인), 마라우더 기마 숙련 750→850(캠페인), 각각 경쟁멀티 가격은 550→600 및 800→850로 다름. 원고 수치는 누락된 버그가 아니라 **캠페인 비용**이며 TWDB 각 단위의 패치 변경란이 이를 확인. 무심코 멀티플레이 비용으로 대체하지 않음. https://twdatabase.com/units/marauder-horsemen ; https://twdatabase.com/units/marauder-horsemasters
- **승리 3 Troll Dens**: 일반 Troll Den 모집건물 3개 건설이 아니라 9.0 victory Lua RegionFactionChangeEvent가 res_bile_trolls/res_chaos_trolls/res_river_trolls/res_stone_trolls 자원 표시 지역의 소유권을 추적(3곳). 9.0.3 클라이언트 직접 재현은 못함.
- **울프릭/사일**: 울프릭 Seafang 개인 이동은 2026 복수 사용자 경험과 7.0 공식. 사일 Dark Ritual/Manipulations는 faction_key Sayl이므로 트로그 합병 뒤 그대로 이관된다고 단언 금지. 조약·제단 레벨·DLC 재모집은 미확인.
- **DLC**: 원래 Norsca → Throgg/Wulfrik, 사일 추가 DLC → Fimir Noble/신규 괴수. 9.0.3 Styrkaar 전 노스카 세력 접근 허용 ≠ 상품권한 무료.
- **게임 생존성**: 초반 제단 → 성장 건물 전체 전환은 위험. 트로그 트롤족 생산지·주요 항구/승리용 거점 유지. 핵심 도시를 제단으로 바꾸면 2슬롯 제한. Reddit 효율 관찰은 버그·난이도·전선 위치 따라 가감.

## E. 아직 최종확정할 수 없는 부분
1. 현 9.0.3 **한국어 클라이언트** 공식 연구·스킬·영지명과 실제 건설 창·최초 건물 슬롯(사용자에게 한글 클릭 순서 확정 불가).
2. 소모 Trollkind resource_cost 원시 키 ↔ 한글 건물 단계 가격 1:1 대응, 특수 트롤 모집 제한량/자원 지역의 정확한 지도상 한글 목록.
3. 젠취 제단 다중 중첩의 9.0.3 실제 기술 당 턴 환산, 울프릭/사일 합병 후 실제 능력/재모집·스티르카르 보유 DLC 조건.
4. 난이도별 1~30턴 안정 전선·모집·건설 진행 직접 저장세이브 실험 없음. 일반/어려움+모드+과거 젠취 버그 플레이 후기는 실전 경향일 뿐 정식 9.0.3 최적화의 반증 불가.

## F. 결론과 승인 경계
**현재 파일은 출처·논증·분기·사용자 목적 측면에서 '조건부 내용 감사 PASS인 개정 초안'이다.** 공식 한국어 용어·정확한 비용/턴 클릭 경로 완전 검증 PASS, 9.0.3 실게임 E2E PASS, 최종보고서 확정/외부 게시 PASS를 주장하지 않는다. 사용자가 제외한 D1 상세 괴수 사냥은 진행하지 않음. 연구 결과/감사만 승인 연구 브랜치에 저장한다.
