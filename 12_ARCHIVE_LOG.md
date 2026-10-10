# 12_ARCHIVE_LOG

## 목적

이 파일은 `10_CURRENT_SUMMARY.md`에 이미 반영된 오래된 Delta 원문, 폐기된 판단, Archived Delta Batch, Final Report 확정 후 Closeout 기록을 보관한다.

Archive는 현재 판단을 만들기 위한 기본 작업 공간이 아니라, 과거 판단의 근거와 변화 이력을 확인하기 위한 보관소다.

---

## 참조 규칙

이 파일은 기본적으로 매번 보지 않는다.

참조하는 경우:

- 과거 판단의 근거 확인
- 왜 결론이 바뀌었는지 확인
- 폐기된 주장 추적
- 오래된 출처 재검증
- Final Report 확정 당시 Closeout 확인
- 사용자가 과거 기록을 직접 요청

---

## 기록 가능한 블록

이 파일 맨 뒤에는 아래 블록을 붙일 수 있다.

- Archived Delta Batch
- Closeout

각 블록은 `04A_UPDATE_TEMPLATES.md`의 템플릿을 사용하고, 출력 전 `04B_VALIDATION_RULES.md`의 검증을 통과해야 한다.

---

## 사용 규칙

- Archive 대상인 오래된 Delta는 **원문 또는 정확한 불변 커밋 SHA·파일 경로·대상 범위**로 복구할 수 있는 형태로 Archived Delta Batch에 보존한다. 요약만 남기고 원문을 추적 불가 상태로 만들지 않는다.
- 상태 파일을 운영했고 실제 기록 정리가 필요하여 Closeout을 수행한다면 그 블록을 append한다. **Final Report 확정 자체만으로 Closeout은 의무가 아니다.**
- Archive에 들어온 내용은 현재 결론을 장황하게 반복하지 말고, 왜 이동했는지와 어떤 판단이 보관되는지 중심으로 정리한다.
- 새 조사를 진행할 때는 먼저 `10_CURRENT_SUMMARY.md`와 `11_DELTA_LOG.md`를 보고, 필요한 경우에만 Archive를 확인한다.

---

## Archive Index

| 날짜 | 주제 | 블록 유형 | 포함 범위 | 비고 |
|---|---|---|---|---|
| - | 아직 없음 | - | - | - |

---

<!-- Archived Delta Batch / Closeout은 이 아래에 붙인다. -->