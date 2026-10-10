# v2 릴리스 시점 브랜치 인벤토리 — 2026-10-11

이 표는 **조회 시점 HEAD 스냅샷**이며 삭제나 삭제 승인이 아니다. 운영 `main`은 공통 조사 템플릿으로 유지한다. 개별 `research/*`의 원고·증거·실험 자료는 `main`에 병합하지 않았다.

| 브랜치 | 조회 당시 HEAD |
|---|---|
| `archive/research-v2-development-20261011` | `183e67163a86a17d5136cacb601c0268b4eaf0cf` |
| `audit/v2-e2e-hardening-20261010` | `3e49c08cd8010943e70a3741b5e6987a2573a1aa` |
| `design/20261011-pdf-style-smoke` | `0b34dcfa02a88d687ef25a474a84c9a924396dd5` |
| `design/handoff-fidelity-review-20261011` | `90290ee93b907069dd9b48ee4ed1103c59a22485` |
| `design/research-v2` | `44bd894cb464229a6d8b926f152113dd0f1bbbae` |
| `main` | `6eef107c6b080b30fa54ecb16eda3ebbcb6daba0` |
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

## 향후 브랜치 정리 전 확인 사항

1. 삭제 직전 각 브랜치 HEAD를 다시 조회해 최신 상태를 비교한다.
2. 고유 연구 원고·원자료·검증 이력이 실재하는 **보존 브랜치/태그 또는 독립 백업**으로 복구 가능한지 확인한다. 공통 개발 역사 브랜치는 모든 `research/*`의 고유 자료를 보존하지 않는다.
3. SHA를 문서에 기록하는 것만으로 삭제한 브랜치의 Git 객체가 영구 보존되지는 않는다. 실제 보존 ref 생성과 재조회가 선행되어야 한다.
4. `main`, 역사 보존 ref, 유지할 연구 브랜치는 보호한다. 삭제는 사용자 지시에 따라 별도 실행한다.
5. 최초 FAIL, 후속 회복, 결정·반려·보류·미검증은 보존된 당시 기록을 소급 변경하지 않는다.
