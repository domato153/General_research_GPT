# ROUND2_PATCH_VALIDATION — CVE-2024-6387 배포판 백포트와 검증

- 조사일: 2026-10-11 (Asia/Seoul)
- 범위: 사용자가 요청한 B(W3) 우선 보완; A(W2 실제 공격 최신성), C(W4 배포·잔존) 및 W5 종합은 별도 계획 작업으로 유지
- 방법: Qualys 원문 제안 + OpenSSH 고정 릴리스 태그 직접 읽기 + Debian/Ubuntu 수정 패치 원문 + CentOS 9 계열 패치 및 Red Hat RHSA 두 건 + upstream 기존 회귀 테스트 스크립트 교차대조
- 평가: 정적 코드 수준의 핵심 경로 차단은 강한 근거; 실제 빌드·기능·공격 회귀 실행 또는 RHEL proprietary SRPM 바이너리 직접 재현은 미수행. 따라서 전체 환경 완전성은 조건부.

## 근거 B1 — 업스트림 수정과 최소 백포트는 다름
- OpenSSH 9.7p1 log.c(451~460)의 `sshsigdie()`는 `sshlogv()`를 호출한 후 `_exit(1)`. sshd.c의 `grace_alarm_handler()`는 `sigdie()`를 호출.
- OpenSSH 9.8p1 `sshd-session.c` 204~222는 signal handler에서 `_exit(EXIT_LOGIN_GRACE)`로 종료하며, `sshd.c` 365~369 부모의 `child_reap()`가 정상 문맥에서 time-out log 기록.
- 상위 버전의 구조적 분리와 달리 최소 백포트는 동일 함수를 유지하고 unsafe logging 호출만 제거. 취약점을 일으킨 glibc malloc/syslog 재진입 지점은 공통 제거되지만, 로그 보존 등 동작이 완전히 같지는 않음.
- Qualys는 대형 upstream commit 81c1099가 단독 백포트 어려우므로 `sshsigdie()`의 `sshlogv` 호출을 #if 0으로 비활성화하는 대안 직접 제안.
- https://www.openwall.com/lists/oss-security/2024/07/01/3
- https://raw.githubusercontent.com/openssh/openssh-portable/V_9_7_P1/log.c
- https://raw.githubusercontent.com/openssh/openssh-portable/V_9_8_P1/sshd-session.c
- https://raw.githubusercontent.com/openssh/openssh-portable/V_9_8_P1/sshd.c

## 근거 B2 — Debian 12 bookworm
- Debian DSA-5724-1: 2024-07-01 공개, bookworm 취약점 1:9.2p1-2+deb12u3 수정.
- Debian Sources 패치 `Disable-async-signal-unsafe-code-from-the-sshsigdie-.patch`(이후 deb12u7에서도 동일 논리): `log.c`의 `sshsigdie()` 내 `va_list/va_start/sshlogv/va_end` 네 줄 영역을 `#if 0 ... #endif`로 둘러싼 2줄 삽입. `_exit(1)`은 유지.
- 원인 경로의 불안전한 로깅이 호출되지 않는다는 정적 논거. '9.2p1' 숫자 자체로 취약 판정하면 백포트를 놓침.
- https://lists.debian.org/debian-security-announce/2024/msg00135.html
- https://sources.debian.org/src/openssh/1%3A9.2p1-2%2Bdeb12u7/debian/patches/Disable-async-signal-unsafe-code-from-the-sshsigdie-.patch
- https://security-tracker.debian.org/tracker/CVE-2024-6387

## 근거 B3 — Ubuntu 22.04 / 24.04
- Canonical 보안공지 2024-07-01: Jammy 1:8.9p1-3ubuntu0.10, Noble 1:9.6p1-3ubuntu13.3 수정, Mantic 1:9.3p1-1ubuntu3.6; Focal 이전은 이번 회귀 코드 영향 없음.
- `git.launchpad.net/ubuntu/+source/openssh/plain/debian/patches/CVE-2024-6387.patch?h=ubuntu/jammy-security` 실제 읽음: Debian과 같은 `#if 0`로 `sshsigdie()` 로깅 비활성화.
- Ubuntu Jammy/Noble 각각 공식 패키지 changelog가 동일 이름의 `CVE-2024-6387.patch: don't log in sshsigdie() in log.c` 적용 선언.
- Canonical은 Noble의 systemd socket activation 패치 때문에 Qualys의 특정 공격법이 성립하지 않을 가능성이 있다고 *조건부* 기술했지만, 보안 패치는 그래도 배포됨.
- https://ubuntu.com/security/cve-2024-6387
- https://lists.ubuntu.com/archives/jammy-changes/2024-July/031715.html
- https://lists.ubuntu.com/archives/noble-changes/2024-July/039509.html
- https://git.launchpad.net/ubuntu/+source/openssh/plain/debian/patches/CVE-2024-6387.patch?h=ubuntu/jammy-security

## 근거 B4 — RHEL 9 / CentOS 계열과 CVE-2024-6409
- Red Hat 2024-07-03 RHSA-2024:4312: RHEL 9 CVE-2024-6387 수정 공지, x86_64 openssh-server-8.7p1-38.el9_4.1.x86_64.rpm 명시.
- 별도 2024-07-10 RHSA-2024:4457: RHEL 9 CVE-2024-6409 수정, x86_64 openssh-server-8.7p1-38.el9_4.4.x86_64.rpm 명시. 6387 패치 공지가 6409까지 해결했다는 의미가 아님.
- 실제 열람한 CentOS archived c9s-sig-hyperscale source patch `openssh-9.8p1-upstream-cve-2024-6387.patch`: RHEL 9 기반 8.7p1 log.c sshsigdie 내 `#if 0 ... #endif`를 추가; 별도로 sshd.c grace_alarm_handler의 비특권 privsep 자식 경로 `cleanup_exit(255)`를 `_exit(255)`로 교체. 이 파일은 2024-07-09 후속 커밋이 반영된 상태로, 초기 07-03 RHSA의 RPM 소스와 완전 동일함을 입증하는 것이 아님.
- Red Hat Bug 2295085: `cleanup_exit()`는 별도 unprivileged child 신호 경쟁 상태(CVE-2024-6409). 이 문제는 6387과 기술적으로 유사해도 별도 CVE·수정 단계.
- https://access.redhat.com/errata/RHSA-2024:4312
- https://access.redhat.com/errata/RHSA-2024:4457
- https://bugzilla.redhat.com/show_bug.cgi?id=2295085
- https://gitlab.com/CentOS/archives/git.centos.org/rpms/openssh/-/raw/c9s-sig-hyperscale/openssh-9.8p1-upstream-cve-2024-6387.patch?ref_type=heads

## 근거 B5 — 회귀 테스트 범위의 한계
- OpenSSH Portable V_9_8_P1 `regress/login-timeout.sh`: `LoginGraceTime 10s`, `MaxStartups 1` 설정 뒤 타임아웃 연결을 발생시키고 새로운 ssh 연결이 성공하는지 확인.
- 이는 종료/서비스 회복 기능적 회귀 검사이다. glibc 경쟁 상태의 취약점 재현·근본 안전성에 관한 결정적 익스플로잇 회귀 테스트가 아님.
- 이번 조사에서는 직접 `make tests`, distro autopkgtest, 패치 재빌드 또는 익스플로잇 테스트를 실행하지 않음. 벤더 보안 배포 승인과 테스트의 세부 실행 로그를 동일시하지 않음.
- https://raw.githubusercontent.com/openssh/openssh-portable/V_9_8_P1/regress/login-timeout.sh
- https://github.com/openssh/openssh-portable/blob/master/regress/README.regress

## B축 결론 / 반증 조건
- [정적 확인] Debian·Ubuntu·CentOS 9 계열 확인한 패치가 `sshsigdie` unsafe logging 경로를 막는 것은 코드상 명확함. 이 방법은 Qualys가 공개적으로 제시한 최소 수정안과 일치.
- [정적 확인] 상위 9.8p1는 해당 로깅을 신호 처리 밖으로 이동하므로 정상 로그 보존의 구현 차이가 있음.
- [조건부] RHEL 9의 6387/6409 별도 후속 수정 공지는 확인됨. CentOS branch 소스가 RHEL 9 실제 RPM 바이트와 같다는 보장은 별도 검증 없음.
- [미확인] 전 배포판의 모든 보안 패치가 모든 빌드에서 정상 운영·회귀 성능·보안 강화까지 동등함을 직접 입증하지 못함.
- [중요 반례] 패치 공지 후에도 RHEL 특정 권한 분리 경로에 6409가 추가 발견되어 별도 CVE 보완됨. 이는 CVE-2024-6387 원래 원격 root RCE 경로의 패치 실패 증거와 구별.
- [부차적 기능차] 최소 수정은 이전 신호 처리의 에러 로그를 생략하므로 upstream 9.8p1와 운영 로그 동작이 완전히 같지 않음.
- [이어갈 범위] W2(A) 2024~2026 실제 악용·침해 증거 재검증, W4(C) 구체적 유지보수 브랜치/실제 패키지 설치·잔존 현황, W5 전반 반론 종합. 사용자 승인 범위 변경 없음.
