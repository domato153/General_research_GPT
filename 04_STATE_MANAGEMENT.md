# Universal Research Harness — State Management / Optimized

> 이 문서는 실제로 상태 파일을 사용하는 조사 브랜치에서만 적용한다. `main`이나 ChatGPT 프로젝트 소스가 기본 저장 대상이 아니며, `13_FINAL_REPORT.md`는 양식이고 실제 보고서는 `FINAL_REPORT.md`다.

## 역할

이 파일은 상태 관리의 **짧은 운영 규칙**만 담는다.  
복붙용 긴 템플릿은 `04A_UPDATE_TEMPLATES.md`, 엄격한 검증표는 `04B_VALIDATION_RULES.md`를 참고한다.

---

## 상태 파일

```text
10_CURRENT_SUMMARY.md  ← 항상 먼저 보는 최신 요약
11_DELTA_LOG.md        ← Summary 이후 변화분
12_ARCHIVE_LOG.md      ← 오래된 로그와 Closeout 보관
13_FINAL_REPORT.md     ← 공통 보고서 양식
FINAL_REPORT.md        ← 개별 조사 브랜치의 실제 보고서
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
| Final Report | `FINAL_REPORT.md` | 결과물 작성 또는 교체 | 최종보고서 확정 |
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

상태 파일을 실제로 쓰는 조사에서만 아래 상황을 참고해 MD 갱신 필요 여부를 판단한다. 매 답변 출력은 강제하지 않는다.

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

## Final Report 종료 규칙 (선택)

- 결과물은 해당 조사 브랜치의 `FINAL_REPORT.md`에 저장하고, 양식 `13_FINAL_REPORT.md`는 변경하지 않는다.
- 실제 Summary/Delta/Archive를 운영한 조사에서만 필요에 따라 요약 갱신, Archive 이동, Delta 초기화, Closeout을 수행한다.
- 최종보고서의 근거·구성·표현 검토는 상태 파일 사용 여부와 무관하게 수행한다.

## 저장·수동 복붙

- 기본 저장 대상은 현재 `research/*` 브랜치의 지정 파일이며, 변경 전 브랜치·파일을 확인하고 변경 후 커밋·diff를 재조회한다.
- append-only 블록은 그 브랜치의 로그 말미에 추가한다. replacement는 같은 브랜치에서 지정한 **결과 파일만** 교체한다. `main`이나 ChatGPT 프로젝트 소스를 자동 교체하지 않는다.
- 사용자가 명시적으로 수동 복붙을 원할 때에는 `04A_UPDATE_TEMPLATES.md`의 기존 블록 형식을 이용하여 적용 순서와 위치를 설명한다.
- 긴 Final Report는 Part를 합쳐 누락·중복·번호·결론·출처를 확인한 후 `FINAL_REPORT.md`에 저장한다.
- 쓰기 도구가 없다면 결과를 제공하되 실제 저장 완료를 주장하지 않는다.
