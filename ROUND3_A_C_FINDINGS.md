# ROUND3_A_C_FINDINGS — CVE-2024-6387

조사일: 2026-10-11. W2 실제 악용과 W4 배포·잔존을 기존 조사 W1·W3 결과에 연결. 최초 공개 시점과 현 시점, 이론/시험/사고/스캔/배포/설치를 구분함. 제3자 공격·동적 익스플로잇 재현·인터넷 스캔은 수행하지 않음.

## W2: 공격 위험과 실제 사례
- Qualys 2024-07-01 원문: Debian 12.5 i386/glibc에서 인증 없는 root RCE 입증. 특정 조건에서 경쟁 상태 평균 약 1만 회 시도, ASLR 포함 원격 root shell까지 평균 6~8시간. 연구진 당시 64-bit amd64 공격은 미실증. https://www.openwall.com/lists/oss-security/2024/07/01/3
- NVD: CVSS 3.1 8.1 High, AC:H·PR:N·UI:N·C/I/A:H. 심각성과 난이도를 동시에 평가. https://nvd.nist.gov/vuln/detail/CVE-2024-6387
- OpenSSH 개발자 Damien Miller 2025-08-07 답신/08-08 공개: 2020 merge 과정에서 Portable 전용 두 줄의 보호 조건을 누락한 사람 실수라고 설명. 1년 뒤에도 자신이 아는 64-bit exploit 성공은 없었다고 발언. 개인적 2025 시점 지식으로, 2026의 부재나 수학적 불가능 증명 아님. https://lists.mindrot.org/pipermail/openssh-unix-dev/2025-August/042028.html
- Palo Alto Networks Unit42는 2024-07-02 당시 실전 악용 알지 못하고 외부 공개 PoC로 RCE 재현에 실패. 이는 Qualys의 자체 성공 결과와 다른 도구·환경. https://unit42.paloaltonetworks.com/threat-brief-cve-2024-6387-openssh/
- 2024 Veriti의 'in the wild' 주장은 스크립트 호스팅/스캔·IP 목록 등이 주된 증거이고 OpenSSH 7.4 등 회귀 영향 범위 밖 호스트 분류도 포함. 성공한 root 탈취의 사고 포렌식·대상별 검증 자료가 부족. https://securityboulevard.com/2024/07/regresshion-cve-2024-6387-a-targeted-exploit-in-the-wild/
- 2026-06 ngCERT 보안 재경고는 권고이지 새로운 실전 침해 성공 보고가 아님. https://cert.gov.ng/advisories/unauthenticated-remote-code-execution-flaw-in-openssh-server-regresshion
- 2026년 공개 추적기(OpenCVE, StackRadar)는 CISA KEV 미등재를 표시. CISA 공식 GitHub 미러는 2026-10-08 갱신 확인. 공식 전체 CSV의 CVE별 전수 열람은 제한되어 직접 자체 대조로 표기하지 않음. 비등재도 전세계 침해 0건 증거가 아님. https://github.com/cisagov/kev-data ; https://opencve.stars-end.org/cve/CVE-2024-6387
- 2024~2026 공개 조사 범위에서 신뢰할 수 있는 원격 root 권한 탈취 실전 피해를 특정하는 독립 사건 보고는 확보하지 못함. 총 건수 미식별, 0건 단정 금지. PoC·공격 시도·스캔은 성공 침해와 구분.

## W4: 배포판 수정과 인터넷 관측
- OpenSSH upstream 9.8p1 2024-07-01 안전하지 않은 signal-handler 로깅 경로 변경.
- Debian 12 Bookworm DSA-5724-1, 2024-07-01, 첫 수정 1:9.2p1-2+deb12u3. 2026 Debian Tracker bookworm fixed, Debian 11 bullseye not affected. https://lists.debian.org/debian-security-announce/2024/msg00135.html ; https://security-tracker.debian.org/tracker/CVE-2024-6387
- Ubuntu USN-6859-1 2024-07-01: 22.04 Jammy 1:8.9p1-3ubuntu0.10, 24.04 Noble 1:9.6p1-3ubuntu13.3 fixed, 20.04 Focal not affected; Noble systemd activation 특수성으로 최초 Qualys 공격법 적용이 달라질 수 있으나 패치 제공. https://ubuntu.com/security/notices/USN-6859-1 ; https://ubuntu.com/security/CVE-2024-6387
- RHEL 9 2024-07-03 RHSA-2024:4312, x86_64 서버 패키지 8.7p1-38.el9_4.1 수정. 2024-07-10 RHSA-2024:4457은 별도 CVE-2024-6409 보완. RHEL8는 해당 회귀 영향 밖. https://access.redhat.com/errata/RHSA-2024:4312 ; https://access.redhat.com/errata/RHSA-2024:4457
- Amazon Linux 1/2 OpenSSH 7.4p1이라 회귀 영향 없음, Amazon Linux 2023 2024-07-01 ALAS2023-2024-649. https://alas.aws.amazon.com/cve/html/CVE-2024-6387.html
- 배포판 fixed=수정 가능한 패키지 공표(또는 배포판 저장소 상태); 실제 각 설치 시스템에 패치·서비스 재시작이 이뤄졌는지와 다름.

## 노출 통계: 다른 측정단위로 비교 금지
- Palo Alto Unit42 Xpanse 2024-07-01 관측: 전체 OpenSSH 버전의 인터넷 노출 인스턴스 약 2,300만, 8.5p1~9.7p1 배너 약 700만, 4.3p1 이하 포함 약 730만. 제조사 스스로 backport·OS·설정 미반영으로 실제 취약 수를 과대평가 가능하다고 명시. https://unit42.paloaltonetworks.com/threat-brief-cve-2024-6387-openssh/
- Qualys 초기 분석: Censys/Shodan 검색에 기초한 잠재 취약 인터넷 서버 1,400만 이상; 별도 Qualys 고객 CSAM EASM에서 외부 노출 취약 분류 약 70만, 그 고객 표본 인터넷 공개 OpenSSH 중 약 31%. 이 수치들의 분모/대상/식별법이 다르며 전세계 실제 취약 1,400만대 또는 전체 미패치 31%라는 뜻 아님. 날짜 표기는 2024 공개 분석에 기반하며 편집된 현재 웹페이지의 갱신 날짜와 구별. https://blog.qualys.com/vulnerabilities-threat-research/2024/07/01/regresshion-remote-unauthenticated-code-execution-vulnerability-in-openssh-server
- Censys는 알려진 패치된 Ubuntu/Debian 버전 식별자를 필터에서 제외할 정도로 배너 오류와 백포트를 인식함. 그래도 패치된 바이너리 상태의 직접 증명이 아니다. https://censys.com/advisory/cve-2024-6387
- 일관된 모집단/버전·OS·실제 패치 추적을 사용하는 2025~2026 글로벌 잔존 취약 시스템 및 실제 설치률을 확인할 독립 시계열 확보 실패. 출처마다 이질적인 단발 스냅샷 숫자로 패치률이나 변화율 계산 금지.

W2 조건부 완료: 실제 기술적 exploit 가능성 입증, 인터넷 대량 침해 증거는 확인 불가(0건 뜻 아님).
W4 조건부 완료: 신속한 수정 패키지 배포 확인, 실제 운영 현장 전수 패치 완결 여부는 미식별.
