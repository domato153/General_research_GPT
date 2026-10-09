# Universal Research Harness — State Management / Optimized

## 역할

이 파일은 상태 관리의 **짧은 운영 규칙**만 담는다.  
복붙용 긴 템플릿은 `04A_UPDATE_TEMPLATES.md`, 엄격한 검증표는 `04B_VALIDATION_RULES.md`를 참고한다.

---

## 상태 파일

```text
10_CURRENT_SUMMARY.md  ← 항상 먼저 보는 최신 요약
11_DELTA_LOG.md        ← Summary 이후 변화분
12_ARCHIVE_LOG.md      ← 오래된 로그와 Closeout 보관
13_FINAL_REPORT.md     ← 최종 산출물 / 최종보고서 템플릿 기준
```

---

## 참조 우선순위

1. `10_CURRENT_SUMMARY.md`
2. `11_DELTA_LOG.md`
3. 필요할 때만 `13_FINAL_REPORT.md`
4. 정말 필요할 때만 `12_ARCHIVE_LOG.md`

원칙:

- 매번 Archive를 보지 않는다.
- 현재 판단은 Current Summary 기준으로 한다.
- Summary 이후 변화만 Delta Log에서 확인한다.
- Final Report는 결과물이고, 진행 상태 관리는 Summary/Delta가 맡는다.
- 최종 산출물 형식은 Summary와 Stage 0.7 Plan에 남긴다.

---

## 갱신 블록 종류

| 종류 | 파일 | 방식 | 사용 시점 |
|---|---|---|---|
| Scope Update | `11_DELTA_LOG.md` | append | Stage 0.5 이후 |
| Investigation Plan | `11_DELTA_LOG.md` | append | Stage 0.7 이후 |
| Delta Update | `11_DELTA_LOG.md` | append | 중간 조사 결과 |
| Current Summary | `10_CURRENT_SUMMARY.md` | 전체 교체 | Delta 압축/중간 정리 |
| Final Report | `13_FINAL_REPORT.md` | 전체 교체 | 최종보고서 확정 |
| Archived Delta Batch | `12_ARCHIVE_LOG.md` | append | Delta를 Archive로 이동 |
| Closeout | `12_ARCHIVE_LOG.md` | append | 조사 종료 |
| Reopen Update | `11_DELTA_LOG.md` | append | 종료된 조사 재개 |

템플릿은 `04A_UPDATE_TEMPLATES.md`를 사용한다.

---

## Final Report 상태값

Final Report 상태는 아래 중 하나로 적는다.

- 미작성
- 양식 추천 완료
- 초안 작성 가능
- 초안 조립 완료
- 확장·문체 다듬기 필요
- 후보 작성 완료
- 검토 필요
- 확정 가능
- 확정 완료
- 업데이트 필요

“초안 조립 완료”와 “확정 완료”를 혼동하지 않는다.  
레포트형·장문·칼럼형 요청에서는 Stage 6.5 확장·문체 다듬기를 거치기 전까지 확정 완료로 닫지 않는다.

---

## 갱신 전 필수 검증

모든 갱신 블록은 출력 전에 `04B_VALIDATION_RULES.md`의 **블록 유형별 검증**을 통과해야 한다.

공통 최소 확인:

- 날짜
- 주제
- 블록 유형
- 붙일 파일
- 붙일 위치
- append-only 또는 replacement 구분

세부 필드는 블록 유형별 규칙을 우선한다.  
예를 들어 Delta Update는 새 정보 여부와 바뀐 판단 여부가 필요하지만, Scope Update와 Investigation Plan에는 항상 필요하지 않다.

최종 산출물 형식이 중요한 요청에서는 `04B_VALIDATION_RULES.md`의 Final Output Mode 검증도 통과해야 한다.

---

## 태그 규칙

주장에는 아래 태그 중 하나를 붙인다.

```text
[확실]
[공식]
[유력]
[추론]
[체감]
[불명확]
[충돌]
[구버전 가능]
[폐기]
[보류]
[추적 필요]
[재검증 필요]
```

태그 없는 주장은 갱신 블록에 넣지 않는다.

---

## Delta 관리 규칙

### Delta에 기록할 것

- 새로 확인된 사실
- 바뀐 판단
- 폐기된 판단
- 새로 발견된 조사축
- 작업계획의 상태 변화
- 최종 산출물 설계 변화
- 다음 작업
- 근거 상태 변화

### Delta에 길게 쓰지 말 것

- 이미 Summary에 반영된 설명
- 오래된 배경 설명
- 반복되는 근거
- 최종보고서용 긴 문장

---


## Lightweight State Sync Check

조사가 길어져도 매번 긴 상태파일을 만들지는 않는다. 다만 아래 조건 중 하나라도 해당하면 답변 끝에서 MD 갱신 필요 여부를 반드시 판정한다.

### 체크 트리거

- 같은 주제로 3턴 이상 이어졌다.
- 조사축 2개 이상을 완료했다.
- 사용자가 범위, 제외 항목, 비교 기준을 수정했다.
- 최종 산출물 형식 또는 Final Output Blueprint가 정해졌다.
- 조건부 추천, 비추천, 보류 같은 임시 결론이 나왔다.
- 실사용 리스크 또는 경쟁 비교가 한 번 이상 정리됐다.
- 다음 단계가 Final Report 초안 작성이다.
- 새 스레드로 이어가면 맥락 손실 위험이 있다.

### 판정값

답변 끝에 아래 중 하나를 짧게 남긴다.

- `11_DELTA_LOG.md` append 필요
- `10_CURRENT_SUMMARY.md` replacement 권장
- `13_FINAL_REPORT.md` 초안 작성 가능
- 아직 갱신 불필요

### 실행 원칙

- `11_DELTA_LOG.md`는 조사 범위 결정, 작업계획, 중간 결론, 바뀐 판단이 생겼을 때 우선한다.
- `10_CURRENT_SUMMARY.md`는 같은 주제로 길게 이어졌거나 다음 대화에서 이어받기 어려울 때 우선한다.
- `13_FINAL_REPORT.md`는 최종 산출물 모드가 정해지고 핵심 질문에 답할 수 있을 때 초안으로 간다.
- `12_ARCHIVE_LOG.md`는 Summary 압축 이후나 Final Report 확정 이후에만 쓴다.
- 갱신 블록이 필요하면 `04A_UPDATE_TEMPLATES.md`와 `04B_VALIDATION_RULES.md`를 적용한다.

---

## Summary 갱신 트리거

아래 중 하나라도 해당하면 `10_CURRENT_SUMMARY.md` 교체용 요약을 만든다.

- Delta Update가 5개 이상 쌓임
- 같은 주제로 3턴 이상 이어짐
- 결론이 크게 바뀜
- 출처 충돌이 해결됨
- 불명확 항목이 확실/유력으로 승격됨
- 사용자가 “정리해줘”, “이제 결론 뭐냐”고 물음
- Delta가 길어져 다음 대화에서 참조하기 어려움
- Final Report 작성 직전
- Investigation Plan의 작업 상태가 크게 바뀜
- 최종 산출물 형식이나 목차가 바뀜

Summary 갱신 후에는 이후 작업에서 **새 Summary + 이후 Delta만 우선 참조**한다.

---

## Archive 이동 규칙

Summary로 압축했거나 Final Report를 확정했으면, 오래된 Delta는 `12_ARCHIVE_LOG.md`로 이동한다.

이후 `11_DELTA_LOG.md`는 새 Delta 기록 대기 상태로 초기화한다.

Archive는 다음 경우에만 본다.

- 과거 판단의 근거 확인
- 폐기된 주장 추적
- 오래된 출처 재검증
- Final Report와 과거 로그 충돌 확인

---

## Final Report 종료 규칙

조사를 끝낼 때는 아래를 수행한다.

1. `13_FINAL_REPORT.md` 전체 교체용 Final Report 제공
2. `10_CURRENT_SUMMARY.md` 전체 교체용 Summary 제공
3. 기존 `11_DELTA_LOG.md`를 `12_ARCHIVE_LOG.md`로 이동
4. `11_DELTA_LOG.md` 초기화
5. `12_ARCHIVE_LOG.md`에 Closeout 블록 append
6. 재개 조건과 Watchlist 남김

레포트형·장문·과제형·칼럼형 요청에서는 Stage 6.5와 Stage 7 검토를 통과하기 전까지 위 절차로 닫지 않는다.

---

## 프로젝트 소스 적용 규칙

이 하네스의 MD 갱신 블록은 기본적으로 로컬 파일 저장용이 아니라, 사용자가 프로젝트에 등록해 둔 **프로젝트 소스** 갱신용으로 안내한다.

사용자가 “프로젝트 소스에 넣고 쓴다”, “프로젝트 소스 갈아끼운다”, “소스에 반영한다”라고 말한 경우에는 아래 원칙을 따른다.

- append-only 블록은 프로젝트 소스의 같은 파일명 문서 맨 뒤에 추가하라고 안내한다.
- replacement 블록은 프로젝트 소스의 같은 파일명 문서 전체를 교체하라고 안내한다.
- 파일명은 임의로 바꾸지 않는다.
- 로컬 다운로드 파일을 제공하더라도, 최종 적용 대상이 프로젝트 소스라면 “다운로드 후 보관”보다 “프로젝트 소스에서 해당 파일을 교체/추가”를 우선 안내한다.
- 여러 파일을 갱신해야 하면 적용 순서와 대상 파일을 먼저 말한다.
- 사용자가 별도로 요청하지 않는 한, “로컬 파일만 저장하면 끝”인 것처럼 안내하지 않는다.

---

## 장문 Final Report 프로젝트 소스 적용 규칙

`13_FINAL_REPORT.md`를 여러 Part로 나눠 출력한 경우, 각 Part는 최종 파일을 만들기 위한 조립 조각이다.

- Part 1부터 마지막 Part까지 순서대로 이어 붙인다.
- 모든 Part를 합친 뒤 프로젝트 소스의 `13_FINAL_REPORT.md` 전체를 교체한다.
- Part 일부만 붙인 상태를 최종 확정본으로 보지 않는다.
- 마지막 Part 출력 후에는 누락, 중복, 목차 번호, 결론 일관성 검증을 수행한다.
- 사용자가 프로젝트 소스에 바로 순차 붙여넣기를 원하면 Part 1은 파일 앞부분, Part 2부터는 바로 뒤에 이어 붙이라고 안내한다.
- 분할 출력은 `13_FINAL_REPORT.md`에만 적용한다. `10_CURRENT_SUMMARY.md`, `11_DELTA_LOG.md`, `12_ARCHIVE_LOG.md`는 기존 append/replacement 규칙을 따른다.

---

## 출력 안내 규칙

사용자에게 갱신 블록을 줄 때는 먼저 적용 순서를 말한다.

예:

```text
적용 순서:
1. 프로젝트 소스의 `11_DELTA_LOG.md` 맨 뒤에 아래 블록 추가
2. 프로젝트 소스의 `10_CURRENT_SUMMARY.md` 교체는 아직 필요 없음
3. 다음 단계는 Stage 2 공격적 검토
```

여러 파일을 갱신할 때는 파일별로 블록을 분리한다.  
한 블록 안에 append용과 전체 교체용을 섞지 않는다.