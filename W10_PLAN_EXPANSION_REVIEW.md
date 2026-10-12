# W10 — 승인 계획 밖 고가치 조사축 검토 (2026-10-12)
**상태: 확장 후보 검토 및 사용자 선택 제안, 신규 본조사 미착수.** 기존 9.0.3 트로그 통합 공략 / W01~W08과 RESEARCH_PLAN·FINAL_REPORT.md 대비. 사용자가 '계획 확장 고려해봤나?'라고 명시 지적하여 누락 관문 복원. W09는 기존 개정 초안 작성 진척을 의미함.

## 계약 근거
main/06_COLLABORATION_WORKFLOW.md 23: 주요 묶음 완료/종합 전환 전에 고가치 누락축 독립 확인; 후보들은 개수 제한 없이 공개하며 2~3개는 권장 실행 조합의 개수. main/02_RESEARCH_PIPELINE.md 190~197 및 269~277: 신규 후보 D와 기존 필수 A/보강 B/기승인 미래 C를 구분. 미승인 새 조사축은 바로 필수 W-ID로 착수하지 않음. 기존 범위에 '영토 확장'을 사용자가 추가한 것만으로 계약상 계획 밖 조사축 탐색을 수행한 것으로 간주하면 오류.

## A 기존 필수 오류: 트로그 장기 승리 'Troll Dens' 조건
- 원시 9.0 victory_objectives.lua(공개 9.0 덤프) script_key throgg_capture_troll_dens, total3. RegionFactionChangeEvent에서 region:resource_exists('res_bile_trolls' / 'res_chaos_trolls' / 'res_river_trolls' / 'res_stone_trolls')를 판정하며, 해당 지역 소유가 트로그로 변경될 때 count+1, 소유권 상실 시 -1.
- 따라서 **일반 모집 건물 '트롤 둥지' 3개 건설 조건 아님, 4종의 지정 트롤 특수 자원을 가진 지역 3곳의 소유 조건**. 같은 유형 3지역이라도 각각 자원 지표가 있으면 인정될 수 있음; 2026-01 Steam 유저 경험과 독립 일치.
- 출처 1차 https://github.com/Shazbot/WH3-Dump/blob/8a4f7e64714cf971b44988a4b59f218af6d04ff2/script/campaign/main_warhammer/victory_objectives.lua
- 실플레이 https://steamcommunity.com/app/1142710/discussions/0/688619659067678263/
- 판본: 루아 9.0, TWDatabase 9.0.3 long-victory에서 세 곳의 Troll Dens 항목 확인. 9.0.3 정확 루아 동일 여부 직접 실험은 없음. 기존 FINAL_REPORT.md/관련 W-ID에서 '트롤 둥지 3개'만으로 해석 여지를 제거해야 함.

## B 기존 승인 조사 내 설명/실행성 보강 (새 계획 확장 아님)
- 특수 트롤 지역 소유의 정확한 지도상 정착지 목록·한국어명·최적 소유 동선/승리 조건 달성 시퀀스 (W08와 지역형 W04에 관한 실전 필수 설명). 최초 시작 영지 실제 건물 슬롯·병종 모집 가능 조건·직접 1~N 턴 실행.
- 한국어 공식 기술·스킬·정착지 명칭과 실제 9.0.3 게임 .loc/툴팁 (W04/W06 기존 미완료). 확인 불가할 때 '미확인' 고지하여 조건부 진행 가능.
- 위는 중요 A 정정 + 기존 승인 범위의 B 완성도 개선이며 사용자에게 신규 승인 요구할 일이 아님.

## D 새로 드러난, 기존 계획에서 독립적으로 상세 조사하지 않은 후보 (사용자 선택 대기)
D1. **24개 괴수 사냥별 임무·위치/기후·보상·우선순위 및 네임드 괴수 활용**. 공식 7.0 개편은 Glorious/Taming/Trophy 3종, 기후별 위치 변화를 명시하고 트로그 단기 목표는 4 사냥. 현재 보고서는 총24개/4개 완료만 다룸. 실제 임무 난이도·전리품/특수 병종·턴별 군단 준비를 추적하면 최적 4개 경로와 보상 선택에 직접 영향. 방법: 공식/스크립트/미션·한국어명/2026 전투 사례를 교차. 조사량 중간~큼. 우선 높음.
  - https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/84-total-war-warhammer-iii-patch-7-0-introducing-the-free-content-and-the-masque
  - https://twdatabase.com/factions/wintertooth
D2. **네 카오스 신별 신앙 보상·제단/트롤 경제 슬롯 기회비용·수도 보복 대응**. 기존은 '신을 택하면 다른 3신 보복/알터 슬롯 충돌'만 소개. 어떤 신을 선택해야 트롤/늑대두겁 군단과 경제 시너지가 좋은지, 역으로 소집기·트롤 왕국 방해가 있는지 모름. 공식은 최종 충성 후 다른 세 신 수도 공격을 확인. 방법: 현행 효과·지역 슬롯 원자료/전투 사례. 조사량 중간, 우선 높음.
  - https://community.creative-assembly.com/total-war/total-war-warhammer/blogs/84-total-war-warhammer-iii-patch-7-0-introducing-the-free-content-and-the-masque
D3. **울프릭·사일 등 전설 군주 연방 통합의 실제 승계 내용과 제단 전환 / 전선 재편**. 기존에는 울프릭 Seafang 개인 능력만 실전 보고 인용. 외교·영지·전쟁 인계 및 다른 제단 유형 변환, faction-only 능력 보존 한계가 초반 압박/경제를 바꿀 수 있음. 방법: 9.0 캠페인 confederation·altar conversion 스크립트와 게임 기록 대조. 조사량 중간, 우선 중간.
  - https://github.com/OwenTanzer/CTW-data/blob/0035c25fb0e7fca8f7bb49b0535edafafa708e82/data/faction_guides/races/norsca.md
D4. **DLC 소유·비소유 분기(사냥 몬스터 대체 보상, 특수 유닛·영웅 획득 가능성), 바닐라 실행 대체군단**. 현재 W05의 'DLC 조건' 경고는 개별 선행조건 검증 미완료. 사용자의 소유 DLC를 묻기 이전에 기본 본편/7.0 FLC 활용 가능한 표와 선택 DLC별 추가 가치를 대조하면 공략에서 가용 불가능한 유닛 추천을 방지. 방법: DLC unlock/mission/recruit data + 공식 안내. 조사량 중간, 우선 중간.
  - https://github.com/OwenTanzer/CTW-data/blob/0035c25fb0e7fca8f7bb49b0535edafafa708e82/data/faction_guides/races/norsca.md
새 후보별 현재 상태 모두 **제안/D**, 사용자 승인 전 연구 착수 아님. 사용자에게 개별 조합·축소·제외 및 지금 근거로 조건부 초안 검수하는 대안 선택권을 제공한다.

## 추천 경로
1. 기존 A 트롤굴 승리 판정 오류는 자동 수정.
2. 이후 **D1 괴수 사냥 우선순위 + D2 카오스 신앙 시너지** 결합 추가 조사를 가장 추천. 트로그 단기 승리와 경제·군단 성능에 직접 기여하는데 현재 원고는 너무 얕음.
3. D3는 사용자가 울프릭 합병 플레이 중심을 원하면, D4는 DLC 여부/가용 병종 제약을 특히 중시하면 추가 선택 가능. 이를 삭제/거절했다고 임의로 간주하지 않음.
4. 대안: 신규 D 축 없이 B 실전 건설/한글 표기 완성도를 올린 다음 현 근거로 조건부 종합검수·최종 승인 관문 진행.

## 실행 경계
현재 작업은 '계획 확장 검토 및 제안'이며 D1~D4 본조사나 최종 작성·확정 명령으로 처리하지 않음. 사용자의 실제 선택을 듣고서 기준 계획의 승인이 필요한 변경을 기록한다.
