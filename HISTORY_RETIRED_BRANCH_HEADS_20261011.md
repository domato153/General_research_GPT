# v2 개발 완료 브랜치 이력 보존 및 정리 대상 (2026-10-11)

## 방법
- 이 역사 브랜치의 커밋은 아래 **삭제 전 브랜치의 원래 HEAD 전부를 추가 부모(parents)로 연결한 보존 커밋**으로 구성한다.
- 추가 부모로 연결된 HEAD와 그 조상 커밋/트리는 `archive/research-v2-development-20261011`에서 Git 이력상 도달 가능(reachable)하다. 브랜치명을 삭제해도 커밋 이력을 Git 객체로 보존한다.
- **주의:** archive의 현재 파일 트리에 모든 연구 보고서가 합쳐져 보이는 것은 아니다. 아래 HEAD SHA를 통해 `FINAL_REPORT.md`, `RESEARCH_PLAN.md`, 개별 근거 파일, 해당 시점 Git 로그를 직접 열람·복원한다.
- 보호: 운영 `main` 및 이 `archive/*` 브랜치는 삭제하지 않는다. 사용자 승인에 따른 개발·시험 브랜치 정리용이며 연구 원고의 `main` 병합이 아니다.
- P1 최초 FAIL, 각 관찰 범위 PASS, R5/CAS/API/UI 및 실주입 UNKNOWN은 기존 기록과 분리/유지한다.

## 삭제 전 대상 총 26개: 연구 22개, 개발/감사 4개

| 브랜치(삭제 전) | 보존 HEAD |
|---|---|
| `audit/v2-e2e-hardening-20261010` | `3e49c08cd8010943e70a3741b5e6987a2573a1aa` |
| `design/20261011-pdf-style-smoke` | `0b34dcfa02a88d687ef25a474a84c9a924396dd5` |
| `design/handoff-fidelity-review-20261011` | `90290ee93b907069dd9b48ee4ed1103c59a22485` |
| `design/research-v2` | `44bd894cb464229a6d8b926f152113dd0f1bbbae` |
| `research/20261010-ai-employment-displacement` | `98420358e1977cfe9d09a976be7e7410a5f4f637` |
| `research/20261010-ai-employment-evidence` | `1a096a33469037a5a6f430ac78c549cd485a02b8` |
| `research/20261010-ai-employment-impact` | `7a938c049e5e0dbbbb6141f25aea498fba729ecb` |
| `research/20261010-ai-employment-korea-us` | `6cd6187b6f5a8507a344c9655e3c2f77e827c49d` |
| `research/20261010-ai-employment-kr-us-1538-fb22` | `cbe5b68d8a0fcfa355d320268ceb8b3c8e9d634b` |
| `research/20261010-ai-jobs-causal-evidence-v2` | `876e14d42ec0f17156c1bc5c6558a5dc0e52df26` |
| `research/20261010-north-sync-v2-test` | `35719fbf8caeb5a887a6c397a237d76d6fb2831d` |
| `research/20261010-v2-e2e-final` | `87af8e1933c8d98142c3391b0ebc0890d173577c` |
| `research/20261010-v2-smoke` | `bf54731f0340fb7b4747ab79b44b6319328a3d13` |
| `research/20261011-kr-us-ev-charging-adoption` | `818c7f21bdbc4ef33a66cf343c306f6b90abb9ac` |
| `research/20261011-long-lite-smoke` | `722601c8ccaadc0cb189a7e8cd5ead8a15df3c8e` |
| `research/20261011-openssh-cve-2024-6387` | `d55714adb510cbdd293ae9d92a358a22e5dc9812` |
| `research/20261011-v2-r1-from-n07` | `e6b00668652d5fe826926868ae9dba4273a6c977` |
| `research/20261011-v2-r2-draft` | `7f49301234e911bcd91e08bceb9bcdb3432df288` |
| `research/20261011-v2-r3-full-delegation` | `ba6935f5ffe0a156a045a37c16a9573e302daf9c` |
| `research/20261011-v2-r4-audit` | `f6f3721dd83bdaecf5b8d05b2cc8f3337112829b` |
| `research/20261011-v2-r6-data-execution` | `f0516806e33a144eadb2e529fec624b876928ec4` |
| `research/20261011-v2-r7-numeric-check` | `e105fb85e9aad619167f5e208a5d6b304c2ddc32` |
| `research/20261011-v2-r8-x03-untrusted` | `16dbc3130be0b8fa5ce4dc17fd41363a50e7a7df` |
| `research/20261011-v2-r8-x04-save-failure` | `13d2b90b35dac577fce72a2aa4eb68a2420e3b1f` |
| `research/20261011-v2-r8-x05-head-race` | `43be10e2fcdc373f1ef7e7b19205f07a658ee399` |
| `research/20261011-v2-r9-x29-read-gap` | `10fb514fcf801426b5f68a52611d2b0d9ad9dfef` |

## 보존 데이터 안내
- 실제 분야별 연구 결과를 포함하는 예: `research/20261010-ai-employment-kr-us-1538-fb22`, `research/20261011-kr-us-ev-charging-adoption`, `research/20261011-openssh-cve-2024-6387`.
- `research/20261011-v2-r*`, `research/20261010-v2-*` 등의 브랜치도 고유 시험·원고 파일을 담을 수 있어 일부 내용만 복사하는 대신 **원래 HEAD 전체를 부모로 연결**한다.
- 필요 시 `git show <SHA>:FINAL_REPORT.md` 등으로 직접 원고를 읽고, `git branch <새이름> <SHA>`로 삭제 브랜치를 되살릴 수 있다. 예시 명령은 Git 데이터를 사용자가 신뢰하는 로컬 저장소에 내려받았을 때만 적용한다.
- 삭제 직후 GitHub의 브랜치 목록과 이 보존 커밋의 부모 SHA 집합을 다시 대조해야 정리 완료로 판정할 수 있다.
