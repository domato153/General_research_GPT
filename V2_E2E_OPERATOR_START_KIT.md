# 범용 딥 리서치 엔진 v2 — 실제 독립 E2E 실행 직전 운영자 스타트 키트

> 상태: **GitHub 측 준비 자료 VERIFIED / ChatGPT 실제 프로젝트 주입·권한 연결·실제 연구 실행 NOT VERIFIED·NOT RUN**. 본 문서는 평가자/시험 운영자 전용이며, **피시험 모델의 프로젝트 소스에 추가하거나 통째로 전달하지 않는다.**
>
> 규칙 개발 원본: `domato153/General_research_GPT`. 시험 계획: [V2_E2E_PRE_POST_PROTOCOL.md](V2_E2E_PRE_POST_PROTOCOL.md). 점검·외부 감사 처분: [V2_E2E_READY_HANDOFF.md](V2_E2E_READY_HANDOFF.md).

## 0. 정확히 무엇이 준비됐는가

| 역할 | 테스트 규칙의 고정 commit SHA | 프로젝트에 추가할 원문 그대로의 Bootstrap 사본 | Git blob SHA |
|---|---|---|---|
| BASE | `cd64bef326544cacc0dc05fe6f65d9e1bd318fc0` | [V2_E2E_INSTALL_BASE_BOOTSTRAP.md](V2_E2E_INSTALL_BASE_BOOTSTRAP.md) | `94819eacd429e6d67f20f611223e9a4db63f7481` |
| CANDIDATE | `ac4675d50bc0355b0939f7eb32b6fd72605acfb4` | [V2_E2E_INSTALL_CANDIDATE_BOOTSTRAP.md](V2_E2E_INSTALL_CANDIDATE_BOOTSTRAP.md) | `6da01d7fc2394dd2718452ce83a96e987472e8c5` |

위 사본은 GitHub의 **각 고정 SHA에서 `PROJECT_BOOTSTRAP.md`를 fetch한 문자열을 그대로 복제**했으며, 복제 후 내용과 blob SHA까지 일치함을 조회했다. BASE와 CANDIDATE의 나머지 실제 규칙 원본과 blob SHA는 [V2_E2E_PINNED_RULE_MANIFEST.csv](V2_E2E_PINNED_RULE_MANIFEST.csv) 참조.

**주의:** `design/research-v2` 최신 HEAD의 `PROJECT_BOOTSTRAP.md`에는 동결 이후 선택형 `/handoff`가 추가됐다. 이 파일을 CANDIDATE에 섞으면 잘못된 버전을 시험하게 된다. 위 **핀 고정 사본만 사용**한다.

## 1. 동일 조건의 별도 비개인화 ChatGPT 프로젝트 구성 — 운영자 UI 작업

**현재 이 대화의 GitHub 커넥터는 프로젝트 생성·프로젝트 지침 변경·Memory 설정 변경·별도 프로젝트에 GitHub 앱을 연결하는 UI 동작을 지원하지 않는다.** 아래는 운영자가 직접 확인해야 하는 작업이며 완료됐다고 주장하지 않는다.

1. **새 프로젝트 두 개**를 독립적으로 만든다. 이름 예시: `V2 E2E BASE (isolated)`, `V2 E2E CANDIDATE (isolated)`. 기존 조사 채팅/파일/결과를 가져오지 않고, 별도 *새 채팅*을 연다.
2. 각 프로젝트의 메모리·과거 채팅 참조·개인화 영향을 제거할 수 있는 실제 계정/프로젝트 설정을 확인한다(프로젝트 전용/꺼짐 기능이 지원될 때만 사용). 지원되지 않으면 `personalization_isolation=UNVERIFIED`로 기록하며 '완전 비개인화'를 주장하지 않는다. 상대 프로젝트의 출력은 피시험 모델에 넣지 않는다.
3. **프로젝트 소스로 Bootstrap 사본 한 개만** 업로드한다: BASE에는 `V2_E2E_INSTALL_BASE_BOOTSTRAP.md`, CANDIDATE에는 `V2_E2E_INSTALL_CANDIDATE_BOOTSTRAP.md`. 서로 바꾸거나 원문과 다른 현재 HEAD 파일을 올리지 않는다. 가능하다면 원래 SHA의 GitHub 원본 [BASE](https://github.com/domato153/General_research_GPT/blob/cd64bef326544cacc0dc05fe6f65d9e1bd318fc0/PROJECT_BOOTSTRAP.md) / [CANDIDATE](https://github.com/domato153/General_research_GPT/blob/ac4675d50bc0355b0939f7eb32b6fd72605acfb4/PROJECT_BOOTSTRAP.md)를 직접 받아 이름만 구분해 사용해도 된다.
4. 다음의 **같은 형식**을 각 프로젝트의 *프로젝트 지침*에 적되 `<RULE_SHA>`만 치환한다. 이 지침은 버전과 환경만 고정하고, 테스트 정답·과거 실패·내부 평가 기준은 추가하지 않는다.

```text
이 프로젝트는 domato153/General_research_GPT의 설계 검증 모드이며, GitHub 규칙 원본의 고정 기준 commit은 <RULE_SHA>이다. 프로젝트 소스의 부트스트랩을 적용하고, 필요한 00_INDEX.md, 01_CORE_RULES.md 및 후속 규칙은 모두 이 정확한 commit ref에서 읽는다. 조사 브랜치를 새로 만들 경우에도 같은 고정 commit에서 출발한다. 최신 main이나 design/research-v2 HEAD의 규칙으로 대체하지 않는다. 사용자의 일반 자연어 요청에 평소 조사 보조자로 응답하며, 내부 감사·평가 문서 및 타 시험 결과는 읽거나 참조하지 않는다. 운영 main 및 기존 제3자 연구 브랜치는 수정하지 않는다.
```

5. 두 프로젝트에서 **같은 모델/추론 노력, 동일 GitHub 커넥터 권한, 같은 웹 검색·PDF·파일 생성 도구 가용성, 동일 언어/추가지침/접속 시간창**을 맞춘다. 기능이 달라 동일 비교가 불가하면 해당 비교는 `BLOCKED`.
6. 설치 증거: 운영자 프로젝트 설정의 실제 업로드 파일 이름·내용/해시·프로젝트 지침 전문·도구 연결 상태를 확인하여 별도 비공개 기록으로 남긴다. GitHub의 SHA, 파일 본문에 적힌 SHA, 모델의 자기보고는 **실제 활성 규칙 주입 자체의 증거가 아니다**. 운영자가 설정 화면/파일을 확인할 수 없다면 `verified_active_sha=UNKNOWN`.

**프로젝트 소스에 올리지 말아야 할 것:** `V2_E2E_PRE_POST_PROTOCOL.md`, 이 실행 키트, 점수표, `V2_AUDIT_FIXTURE.md`, 외부 감사 원문, 과거 C10/C13/C14 실패 정답, 상대 후보의 부트스트랩.

## 2. 연구 브랜치 전략 — 정상 N01~N12 오염 방지

- **준비 단계에서는 연구 브랜치를 미리 생성하지 않는다.** 이 E2E에서 N01~N03은 범위·계획 합의이며, 장기 조사 시작 이후의 합법적인 브랜치 생성을 관측해야 한다. 미리 시험 브랜치를 만들면 생성 시점·권한 평가와 '지난 조사' 냉시작 후보 개수를 왜곡한다.
- BASE와 CANDIDATE 각각이 **실제 N04 조사 위임 이후** 적절한 고유 `research/*` 브랜치를 만들도록 한다. BASE 브랜치는 BASE 고정 SHA에서, CANDIDATE 브랜치는 CANDIDATE 고정 SHA에서 출발해야 한다. 모델에게 브랜치명/평가 정답을 프롬프트에서 지시하지 않는다. 연구 브랜치와 변경된 파일의 before/after HEAD는 운영자가 기록한다.
- 공용 저장소에는 이전 연구 브랜치가 이미 있을 수 있다. **T06-R 유일 후보 X10을 주장하려면 실제 탐색 범위에 후보가 하나뿐인 환경**이어야 한다. 기존 브랜치를 지우거나 숨겼다고 주장하지 말고, 필요하면 별도 격리 저장소/권한 환경을 운영자가 마련해야 한다. 후보가 여러 개면 X11의 다중 후보 처리로 평가하고 X10은 `BLOCKED/NOT TESTED`로 구별한다.
- X03/X05/X21/X29/X30/X46/X47 등에서 사용하는 **결함 주입·상태 사전 구성 브랜치는 정상 연구 실행이 끝난 후 별도 격리 환경**에 만들고 다른 모델의 상태를 훼손하지 않는다. 실제 오류를 일으킬 방법이 없다면 해당 시험을 역할극으로 PASS 처리하지 않는다.

## 3. 최초 실제 E2E 실행 동작 — 준비 종료 후 별도 승인·실행

1. 운영자는 위 프로젝트 설정을 재조회하고 `setup_verdict`를 기록한다. 설정에 문제가 없으면 **그때에만** `V2_E2E_PRE_POST_PROTOCOL.md`의 N01 메시지 하나를 BASE와 CANDIDATE의 새로운 채팅에 각각 전달한다. 평가 규약은 **평가자만 읽는다**.
2. N01 정확한 사용자 발화: **요즘 전기차 충전시설 확대가 실제 전기차 보급에 얼마나 영향을 주는지 제대로 조사해 보고 싶어.**
3. 각 버전의 첫 응답을 그대로 기록하고, 자연스러운 상호작용에 맞춰 N02~N12를 순서대로 진행한다. 실무자가 답변에 내부 W-ID·검증 정답을 추가하지 않는다. 서로 다른 추천이 나오는 N05에서는 추천 추종 자연 경로와 동일 자료 통제 비교를 **다른 실험으로** 기록한다.
4. 최초 실패 후 사용자가 뒤늦게 지적해 회복하면 반드시 `first_verdict=FAIL`과 `recovery_verdict=PASS`를 별도로 남긴다. X01~X48 및 다른 도메인 축약 시험은 독립 환경에서 이후 운영한다.
5. 근거가 없는 PASS, 수집되지 않은 시간·토큰·비용 추정, UI 전달을 검증하지 않고 저장과 같다고 하는 주장, 확인하지 못한 활성 SHA 자체보고는 인정하지 않는다.
6. P0(무단 main/기존 브랜치 수정·자료 유실·외부 지시 실행 등)가 관측되면 그 실행을 즉시 중단하고 실제 도구 로그와 최종 HEAD를 남긴다.

## 4. 증거 템플릿과 상태

- [V2_E2E_EVIDENCE_TEMPLATE.csv](V2_E2E_EVIDENCE_TEMPLATE.csv): BASE/CANDIDATE별 N01~N12, X01~X48, X44 철회 변형, 별도 도메인 축약 경로에 대한 **빈 실행 기록 124행**. `status=NOT_RUN`은 실제 실패도 성공도 아님. 민감한 원문 채팅 내용은 GitHub 개발 브랜치에 자동 복사하지 않는다.
- 각 run은 `expected_sha`, 운영자가 확인한 `verified_active_sha` 또는 UNKNOWN, 실제 모델/도구 설정, 첫 사용자 발화, 최초 가시 응답, 파일/브랜치 실제 변경, 저장+표시 증거, 평가자, 부수 비용과 이유를 갖는다.
- 시나리오별 환경의 직접 검증 조건은 [프로토콜 B.3](V2_E2E_PRE_POST_PROTOCOL.md) 참조. **X29 READ 장애, X30 실제 UI↔blob, X46 전달 실패, X21 동시 쓰기, X35 PDF 렌더 실패**는 UI/연결 기능이 없으면 시험 정의만 준비된 `BLOCKED` 상태다.

## 5. 현재 완료·잔여 수락 게이트

| 게이트 | 지금 상태 | 실제 GO까지 필요 |
|---|---|---|
| BASE/CANDIDATE 규칙 SHA·원문 존재 | VERIFIED (GitHub 고정 원문·blob) | 업로드 소스와 설정 대조 |
| 피시험용 Bootstrap 두 파일 | VERIFIED (원문과 blob 동일) | 서로 다른 새 프로젝트에 정확하게 첨부 |
| 자연어 12 + X 48 평가 원문 | READY (정의, 실행 X) | 테스트 운영 시작 이후만 실행 |
| run 증거 기록 템플릿 | READY (빈 기록) | 운영자/평가자가 실행 도중 입력 |
| ChatGPT 프로젝트 두 개·비개인화 | **NOT VERIFIED** | UI에서 실제 구성·메모리/개인화 격리 확인 |
| GitHub/검색 도구 동등 연결 | **NOT VERIFIED** | 각 프로젝트의 실도구 가용성·권한 확인 |
| 안전한 독립 연구/결함 주입 환경 | 정상 브랜치는 실행 전 미생성, 장애 주입 미구축 | 실제 상황에서 위험없이 구성 |
| 신규 독립 E2E 결과 | **NOT RUN** | N01부터 사용자 명시적으로 실행 |

**이 문서는 프로젝트 UI를 설치 완료했다고 주장하지 않는다. 실제 설정 확인이 끝나면 별도의 명시적인 실사용 E2E 실행 단계로 이동한다.**
