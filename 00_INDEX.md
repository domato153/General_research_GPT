# Universal Research Harness — INDEX / Optimized

## 역할

이 파일은 전체 하네스의 **라우터**다.  
자세한 절차·템플릿·검증표를 이 파일에 넣지 않는다. 필요한 파일만 골라 보게 한다.

---

## 조사형 요청 인식

아래 요청에는 이 하네스를 적용한다.

- “~~에 대해 조사하고 싶다”
- “~~가 맞는지 검증해줘”
- “~~ 최신 기준으로 정리해줘”
- “~~ 비교해줘”
- “~~ 평가가 어떤지 봐줘”
- “~~ 실제로 되는지 확인해줘”
- “최종보고서로 정리해줘”
- “레포트형으로 정리해줘”
- “대학 과제처럼 써줘”
- “칼럼이나 보고서처럼 읽을만하게 써줘”
- “내용 많이 담아서 최종본으로 다듬어줘”
- “최종 결과물을 장문 보고서로 만들어줘”
- “10페이지 이상급 보고서를 나눠서 출력해줘”
- “긴 보고서는 Part로 나눠서 복붙하기 좋게 줘”

단순 사실 질문이면 전체 하네스를 돌리지 말고 바로 답한다.

---

## 항상 먼저 볼 파일

조사를 이어갈 때는 아래만 우선 본다.

1. `10_CURRENT_SUMMARY.md`
2. `11_DELTA_LOG.md`
3. `02_RESEARCH_PIPELINE.md`
4. `01_CORE_RULES.md`

필요할 때만 추가로 본다.

- 검토 필요: `03_REVIEW_MODULES.md`
- 상태 갱신 필요: `04_STATE_MANAGEMENT.md`
- 복붙 템플릿 필요: `04A_UPDATE_TEMPLATES.md`
- 갱신 검증 필요: `04B_VALIDATION_RULES.md`
- 분야별 기준 필요: `05_DOMAIN_MODULES.md`
- 최종 산출물 양식 선택/보고서 템플릿 확인: `13_FINAL_REPORT.md`
- 과거 근거 추적: `12_ARCHIVE_LOG.md`

기본 원칙: **Archive와 긴 템플릿 파일은 매번 읽지 않는다.**

---

## 전체 단계

```text
Stage 0   — Intake / 요청 접수
Stage 0.5 — Scope & Output Proposal / 조사 범위·최종 산출물 제안
Stage 0.7 — Investigation Plan / 조사 작업계획과 최종 산출물 설계도
Stage 1   — Initial Research / 1차 조사
Stage 2   — Adversarial Review / 공격적 검토
Stage 3   — Evidence & Freshness Check / 근거·최신성 검증
Stage 4   — Revision & Delta Update / 수정·델타 갱신
Stage 5   — Closure Readiness Check / 종료 가능성 판정
Stage 6   — Final Report Draft Assembly / 최종보고서 초안 조립
Stage 6.5 — Report Expansion & Polishing / 보고서 확장·문체 다듬기
Stage 7   — Final Report Review / 최종보고서 검토
Stage 8   — Final Report Confirmation / 최종보고서 확정
Stage 9   — Closeout / 상태 정리
```

---

## 핵심 분기

### 처음 조사 시작

1. Stage 0으로 요청을 요약한다.
2. 넓은 주제면 Stage 0.5에서 조사축을 제안한다.
3. 최종 산출물 형식이 중요하면 Stage 0.5에서 **양식 후보와 추천안**을 함께 제시한다.
4. 조사축이 3개 이상이거나 누적 조사면 Stage 0.7에서 작업계획과 Final Output Blueprint를 만든다.
5. 사용자가 승인하거나 “진행/추천대로/알아서”라고 하면 추천안을 기본값으로 Stage 1을 실행한다.

### 최종 산출물 형식이 중요한 조사

사용자가 “레포트형”, “보고서형”, “칼럼”, “대학 과제”, “내용 많이”, “읽을만하게”, “최종적으로 다듬어서”라고 말하면 Stage 0.5에서 최종 산출물 형식을 먼저 제안한다.

기본 추천 기준:

| 요청/목적 | 기본 추천 양식 | 결과물 성격 |
|---|---|---|
| 빠른 결론, 짧은 검증 | Brief Final Report | 핵심 판정표와 요약 중심 |
| 역사·정책·인물·사회 쟁점 장문 조사 | Full Report | 서론-본론-결론, 배경, 쟁점, 부록 포함 |
| “대학 과제”, “레포트”, “조사해서 제출” | Academic-style Report | 연구 질문, 조사 범위, 장별 본론, 참고 출처 포함 |
| “칼럼처럼”, “읽을만하게” | Essay-Column Report | 자연스러운 서술형 글, 통념 검증과 해석 중심 |
| 구매·선택·실무 판단 | Decision Report | 추천/비추천, 대안, 리스크 중심 |
| A와 B 비교 | Comparison Report | 기준표, 항목별 비교, 종합판정 중심 |
| 출처·근거 모음 자체가 목적 | Source Dossier | 출처별 요약, 근거 등급, 인용 후보 중심 |

출력 형식은 아래처럼 안내한다.

```md
## 최종 산출물 양식 제안

추천: [양식명]

이 방식을 쓰면:
- 결과물은 ...처럼 나온다.
- 장점은 ...이다.
- 한계는 ...이다.

다른 선택지:
| 양식 | 이렇게 나옴 | 적합한 경우 | 비고 |
|---|---|---|---|
| ... | ... | ... | ... |

제 추천 이유:
- ...
```

막연히 “어떤 양식으로 할까요?”라고 묻지 않는다.  
기본 추천을 먼저 제시하고, 사용자가 답하지 않아도 진행 가능한 기본값을 둔다.


### 장문 Final Report 분할 출력

`13_FINAL_REPORT.md`가 한 번에 안정적으로 출력하기 어려울 정도로 길어질 때는 Stage 6.5~8에서 Segment Plan을 먼저 만든 뒤 Part 1부터 순서대로 출력한다.

적용 조건:

- 사용자가 10페이지 이상, 20페이지급, 딥 리서치 보고서, 장문 보고서를 원한다.
- 최종보고서의 주요 섹션이 8개 이상이다.
- 한 번에 출력하면 누락, 중복, 앞뒤 결론 불일치, 근거 없는 확장이 생길 위험이 있다.

원칙:

- 분할 출력은 내용 축약이 아니라 안전한 출력 방식이다.
- Part는 최종보고서의 실제 순서 그대로 앞에서 뒤로 출력한다.
- 각 Part의 포함 섹션을 먼저 고정한다.
- 마지막 Part 이후 누락, 중복, 목차 번호, 결론 일관성, 최종 조립 방식을 검증한다.
- 프로젝트 소스 적용 시에는 모든 Part를 이어 붙인 뒤 `13_FINAL_REPORT.md` 전체를 교체한다.

### 조사 중간

- 중간 결과는 `11_DELTA_LOG.md`에 append한다.
- Delta가 길어지면 `10_CURRENT_SUMMARY.md`를 교체용 요약으로 갱신한다.
- 이후에는 Summary + 최신 Delta만 우선 참조한다.
- 최종 산출물 형식이 정해졌다면 Summary에 그 설계를 남긴다.


### 중간 검증 게이트

조사축 하나가 끝났거나 공식 근거와 사용자 체감이 함께 쓰였거나 구매/추천/보류 판정이 나오면, 다음 조사축으로 넘어가기 전에 `02_RESEARCH_PIPELINE.md`의 **Stage 3.5 — Mini Review Gate**로 5줄 이내 검증을 한다. 문제가 있을 때만 `03_REVIEW_MODULES.md`의 상세 검토 모듈을 연다.



### 중간 상태 갱신 체크

조사 중에는 매 답변마다 긴 상태파일을 만들지 않는다. 대신 아래 조건 중 하나라도 해당하면 답변 끝에서 **MD 갱신 필요 여부**를 반드시 판정한다.

- 같은 주제로 3턴 이상 이어졌다.
- 조사축 2개 이상을 완료했다.
- 사용자가 조사 범위, 제외 범위, 비교 기준을 수정했다.
- 최종 산출물 형식 또는 Final Output Blueprint가 정해졌다.
- 조건부 추천, 비추천, 보류 같은 임시 구매/실사용 판정이 나왔다.
- 실사용 리스크 또는 경쟁 비교를 한 번 이상 정리했다.
- 다음 단계가 Final Report 초안 작성이다.

판정은 아래 중 하나로 짧게 낸다. 필요할 때만 `04A_UPDATE_TEMPLATES.md`와 `04B_VALIDATION_RULES.md`를 열어 복붙 블록을 만든다.

- `11_DELTA_LOG.md` append 필요
- `10_CURRENT_SUMMARY.md` replacement 권장
- `13_FINAL_REPORT.md` 초안 작성 가능
- 아직 갱신 불필요

원칙: 상태 갱신 체크는 **짧게 자주**, 실제 갱신 블록은 **필요할 때만 정확하게** 출력한다.

### 종료 시점

- 핵심 질문에 답할 수 있으면 Stage 5에서 종료 가능성을 판정한다.
- 종료 가능하면 Stage 6에서 최종보고서 초안을 조립한다.
- Brief Final Report가 아니면 Stage 6.5에서 선택한 양식에 맞게 확장·문체 다듬기를 수행한다.
- Stage 7에서 최종 산출물 형식과 실제 결과물이 일치하는지 검토한다.
- Stage 8에서 `13_FINAL_REPORT.md`를 확정한다.
- Stage 9에서 Delta를 Archive로 넘기고 상태를 정리한다.

---

## 모듈 라우팅

| 요청 유형 | 추가로 볼 파일 |
|---|---|
| 제품·기기·소프트웨어 | `05_DOMAIN_MODULES.md`, `03_REVIEW_MODULES.md` |
| 게임 메커니즘·패치·실제 동작 | `05_DOMAIN_MODULES.md`, `03_REVIEW_MODULES.md` |
| 법·정책·사회 쟁점 | `05_DOMAIN_MODULES.md`, `03_REVIEW_MODULES.md` |
| 작품·게임·영상물 평가 | `05_DOMAIN_MODULES.md`, `03_REVIEW_MODULES.md` |
| 초안 검토·개선 | `03_REVIEW_MODULES.md` |
| MD 갱신 블록 생성 | `04_STATE_MANAGEMENT.md`, 필요 시 `04A_UPDATE_TEMPLATES.md`, `04B_VALIDATION_RULES.md` |
| 최종보고서 작성 | `13_FINAL_REPORT.md`, `02_RESEARCH_PIPELINE.md` Stage 5~9, 필요 시 `03_REVIEW_MODULES.md` |
| 레포트형·칼럼형·과제형 결과물 | `13_FINAL_REPORT.md`, `02_RESEARCH_PIPELINE.md` Stage 0.5/0.7/6.5, `04B_VALIDATION_RULES.md` |
| 초장문 Final Report 분할 출력 | `02_RESEARCH_PIPELINE.md` Stage 6.5~8, `04A_UPDATE_TEMPLATES.md`, `04B_VALIDATION_RULES.md`, `03_REVIEW_MODULES.md` |

---

## 사용자 판단 지원 규칙

초안, 조사 범위, 작업계획, 개선안, 최종보고서 후보를 낼 때는 아래를 붙인다.

```md
### 사용자 확인 필요
현재 기본값:
- ...

판단해주면 좋은 부분:
1. ...
2. ...

제 추천:
- ...

선택지:
1. 추천대로 진행
2. 수정 후 진행
3. 범위 축소
```

최종 산출물 양식이 중요한 경우에는 선택지를 “결과물 모양” 기준으로 설명한다.

```md
### 최종 산출물 양식 제안
추천: ...

이 양식을 쓰면:
- ...

다른 선택지:
1. ...
2. ...
3. ...
```

막연히 “어떤가요?”라고 묻지 않는다.  
사용자가 답하지 않아도 진행 가능한 기본값을 둔다.

---

## 금지

- 큰 주제를 Scope Proposal 없이 바로 조사하지 않는다.
- 최종 산출물 형식이 중요한 요청을 양식 추천 없이 진행하지 않는다.
- 넓은 조사를 Investigation Plan 없이 즉흥 진행하지 않는다.
- 레포트형/장문/칼럼형 요청을 Brief Final Report로 닫지 않는다.
- Stage 0.7을 수행한 조사에서 Final Output Blueprint 없이 Final Report를 확정하지 않는다.
- 매번 모든 모듈을 읽지 않는다.
- Archive를 기본 참조하지 않는다.
- Delta가 길어졌는데 Summary 갱신 없이 계속 누적하지 않는다.
- 붙일 위치 없는 MD 갱신 블록을 출력하지 않는다.
- 긴 Final Report를 한 번에 무리해서 출력하지 않는다. 필요한 경우 Segment Plan 없이 Part 출력부터 시작하지 않는다.