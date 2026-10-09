# 11_DELTA_LOG

## 목적

이 파일은 `10_CURRENT_SUMMARY.md` 이후 새로 쌓인 조사 변화분만 기록한다.
Summary에 반영되지 않은 최신 변화, 조사 범위 결정, 작업계획, Final Output Blueprint, 중간 조사 결과, 재개 판단을 append-only로 보관한다.

---

## 현재 남은 Delta 범위
- 아직 없음

---

## 기록 가능한 블록

이 파일 맨 뒤에는 아래 블록을 붙일 수 있다.

- Scope Update
- Investigation Plan
- Delta Update
- Reopen Update

각 블록은 `04A_UPDATE_TEMPLATES.md`의 템플릿을 사용하고, 출력 전 `04B_VALIDATION_RULES.md`의 검증을 통과해야 한다.

---

## 사용 규칙

- **상태 파일을 사용하는 장기 조사에서 중요한 새 결론·범위 변경·작업 상태 변화가 있을 때만** 맨 뒤에 해당 갱신 블록을 붙인다. 매 답변·모든 결과의 기록을 강제하지 않는다.
- 기존 내용을 중간에서 수정하지 않는다.
- Scope Update와 Investigation Plan은 필요할 때 이 파일에 append하며, **제안과 사용자 합의/AI 위임을 구분**한다. 별도 계획 파일을 쓰면 해당 파일 경로도 진입점에 연결한다.
- 최종 산출물 양식 제안이나 Final Output Blueprint가 정해지면 이 파일에 남긴다.
- Delta Update가 5개 이상 쌓이거나 결론이 크게 바뀌면 `10_CURRENT_SUMMARY.md` 갱신을 권한다.
- 최종 산출물 형식, 예정 목차, 문체 방향이 바뀌면 `10_CURRENT_SUMMARY.md`의 `최종 산출물 설계` 갱신을 권한다.
- Summary에 반영된 Delta는 `12_ARCHIVE_LOG.md`로 옮긴 뒤 이 파일에서 제거한다.
- Final Report 확정 뒤 필요하여 Closeout을 수행했다면, **기존 Delta 원문 또는 불변 커밋을 통한 복구 경로가 검증된 경우에만** 초기화한다. Closeout 없는 일반 조사에는 초기화를 강제하지 않는다.

---

## 참조 규칙

- 먼저 `10_CURRENT_SUMMARY.md`를 확인한다.
- 이 파일에서는 Summary 이후 새로 생긴 변화만 확인한다.
- 과거 Delta와 Closeout은 `12_ARCHIVE_LOG.md`에 보관한다.
- Archive는 과거 판단의 근거 확인, 폐기된 주장 추적, 오래된 출처 재검증, Closeout 확인이 필요할 때만 확인한다.

---

<!-- 새 Scope Update / Investigation Plan / Delta Update / Reopen Update는 이 아래에 붙인다. -->
---