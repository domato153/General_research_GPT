# ROUND1_FINDINGS — CVE-2024-6387 첫 조사 묶음

- 조사일: 2026-10-11 (Asia/Seoul)
- 고정 조사 기준 커밋: 44bd894cb464229a6d8b926f152113dd0f1bbbae
- 작업 범위: W1 원인, W3 상위 코드 정적 검증, W2 2024 최초 실험·일부 독립 관측, W5 제한된 반증 선행
- 방법: 개발사/발견자 원문과 GitHub 불변 커밋·릴리스 태그의 C 소스 직접 대조; 공개 보안업체/배포판 원문과 반례 비교. 실제 서버 공격, 자체 exploit 재현, 컴파일·회귀 테스트는 수행하지 않음.
- 상태: 첫 조사 묶음 완료; 전체 A+B+C 조사 및 최종보고서 미완료. 사용자 Research Round Review 필요.

## W1 — 회귀와 직접 원인 (조건부 완료)

1. Qualys 공식 2024-07-01 oss-security 발표: 기본 LoginGraceTime=120초 경과 시 sshd의 SIGALRM signal handler가 비동기적으로 호출되고, 그 안의 sigdie/sshsigdie 경로에서 syslog 및 malloc/free 등 async-signal-unsafe 함수가 호출됨. glibc 환경에서 이미 진행 중인 메모리 관리 동작을 신호 처리기가 재진입해 상태를 훼손할 가능성이 핵심.
   - 원문: https://www.openwall.com/lists/oss-security/2024/07/01/3 (Summary, Patches and mitigation)
2. 2006년 CVE-2006-5051의 보호 패턴: `DO_LOG_SAFE_IN_SIGHAND` 전처리 가드로 signal context의 로그 동작을 제외하여 `_exit(1)`만 사용. OpenSSH 4.4p1~8.4p1 사이 이 회귀가 없는 것으로 연구진 분류.
3. 2020-10 리팩터링 commit `752250c`의 `log.c` diff에서 기존 `sigdie()` 함수의 `#ifdef DO_LOG_SAFE_IN_SIGHAND` 삭제를 직접 확인. 8.5p1~9.7p1에서 문제 재도입.
   - https://github.com/openssh/openssh-portable/commit/752250c
4. `V_9_7_P1/sshd.c` 353~368의 `grace_alarm_handler()`: process group kill 후 `sigdie("Timeout before authentication ...")`. `V_9_7_P1/log.c` 451~460의 `sshsigdie()`는 `sshlogv()` 후 `_exit(1)`. 진입 경로·실행 순서를 upstream tag 원문과 직접 대조.
   - https://raw.githubusercontent.com/openssh/openssh-portable/V_9_7_P1/sshd.c
   - https://raw.githubusercontent.com/openssh/openssh-portable/V_9_7_P1/log.c
5. glibc Linux에서 root context 원격 코드 실행이 입증되었지만 다른 libc 전체, 64비트 전체에 대한 동일 난이도 일반화는 불가. OpenBSD는 더 안전한 syslog_r 구현으로 영향 없음(연구진/공식).

## W3 — 상위 패치 경로 (부분 완료)

1. OpenSSH의 공식 릴리스 노트: 2024-07-01 9.8p1에서 critical sshd race fix 제공. 이전 취약 범위 8.5p1~9.7p1.
   - https://www.openssh.org/releasenotes.html (OpenSSH 9.8/9.8p1)
2. Qualys는 핵심 upstream fix를 2024-06-06의 `81c1099d22b81ebfd20a334ce986c4f753b0db29`로 명시. signal handler의 unsafe 작업을 sshd listener에서 동기 처리하도록 이동. 이 커밋은 sshd 구조 변경/보강인 `03e3de4`와 연결되어 백포트가 복잡할 수 있음.
   - https://github.com/openssh/openssh-portable/commit/81c1099d22b81ebfd20a334ce986c4f753b0db29
   - https://www.openwall.com/lists/oss-security/2024/07/01/3
3. 직접 소스 비교: `V_9_8_P1/sshd-session.c` 204~222의 `grace_alarm_handler`는 신호 처리에서 `sigaction`, `kill` 후 직접 `_exit(EXIT_LOGIN_GRACE)`. `V_9_8_P1/sshd.c` 334~400의 `child_reap()`가 exit code를 확인하고 `logit("Timeout before authentication...")`과 penalty를 수행. `V_9_8_P1/log.c`에는 9.7p1의 `sshsigdie`가 더는 없음. 신호 중 unsafe 로깅 경로를 제거하고 부모 프로세스의 정상 문맥에서 기록하는 구조와 부합.
   - https://raw.githubusercontent.com/openssh/openssh-portable/V_9_8_P1/sshd-session.c
   - https://raw.githubusercontent.com/openssh/openssh-portable/V_9_8_P1/sshd.c
   - https://raw.githubusercontent.com/openssh/openssh-portable/V_9_8_P1/log.c
4. 구조적 정적 검증 결론: 핵심 취약 코드 경로는 9.8p1에서 제거됨(강한 증거). 단, 본 조사에서 직접 빌드·동작·회귀 테스트하거나 전 배포판 백포트를 확인하지 않았으므로 '모든 빌드 완전 패치'는 미판정.
5. 회귀/연관 쟁점 분리: CVE-2024-6409는 RHEL 9 등 downstream `cleanup_exit()`가 privsep child의 signal handler에서 부적절하게 호출되는 별도 경로·권한 맥락 이슈. 이를 CVE-2024-6387 패치 실패라고 등치하면 안 됨.
   - https://www.openwall.com/lists/oss-security/2024/07/08/2
   - https://sig-security.rocky.page/issues/CVE-2024-6409/
6. 릴리스 기능적 회귀: OpenSSH 9.9/9.9p1 발표는 9.8에서 `SSH_CONNECTION_ABANDON` audit call이 빠졌으며 복원했다고 명시. 6387 root RCE 수정이 무효라는 직접 증거는 아니지만 '보안 수정이 정상 기능 모두 무변화'라는 주장에 반례.
   - https://lists.mindrot.org/pipermail/openssh-unix-announce/2024-September/000160.html
7. Debian 12는 상위 9.8p1로 일괄 올리지 않고 `1:9.2p1-2+deb12u3`에서 수정 공지(DSA-5724-1, 2024-07-01). 버전 문자열만으로 평가해서는 안 됨. 이 증거는 W4 선행 확인이며 W4 완료 아님.
   - https://lists.debian.org/debian-security-announce/2024/msg00135.html

## W2 — 악용 실험과 실제 침해 증거 (첫 묶음 부분 완료)

1. Qualys가 재현한 시험체는 Debian 12.5 i386, OpenSSH `9.2p1 Debian-2+deb12u2`, glibc 기반, ASLR 작동, VM 및 약 10 ms 네트워크 지터 환경.
2. 경쟁 상태 승리까지 평균 약 10,000회 시도/3~4시간(동시 연결 최대 100, LoginGraceTime 120초 조건). ASLR 하 glibc 주소 추정 확률 때문에 root shell 확보까지 평균 6~8시간. 이 값은 위 시험 환경의 관측이며 모든 대상 일반 평균이 아님.
   - https://www.openwall.com/lists/oss-security/2024/07/01/3
3. 64-bit amd64 공격은 2024-07-01 공개 시점 연구진이 성공을 실증하지 않았고 가능성만 제시함. 해당 2024년 진술을 2026년까지 영구적 불가능으로 해석하지 않음.
4. 2024-07-02 Palo Alto Networks Unit 42는 야생 악용 활동을 알지 못했고 외부 공개 PoC를 자기 환경에서 테스트해 RCE를 재현하지 못했다고 명시. 이는 Qualys 비공개 성공 실험을 무효화하지 않음.
   - https://unit42.paloaltonetworks.com/threat-brief-cve-2024-6387-openssh/
5. 2024-07-03 Veriti Research는 표제에서 'in the wild' 적극 악용을 주장하지만 제시한 근거는 exploit script 공개 저장소, IP 대상 목록, Shodan 분류. 대상의 상당수로 적힌 OpenSSH 6.4~8.2/주요 7.4는 6387의 8.5~9.7p1 회귀 영향 범위 밖임. 해당 게시물만으로 성공한 CVE-2024-6387 침해·root code execution을 입증하지 못함(게시물의 다른 고전적 CVE 타깃과 혼동 주의).
   - https://securityboulevard.com/2024/07/regresshion-cve-2024-6387-a-targeted-exploit-in-the-wild/
6. 실제 이용 사례 '0건'이라는 전면 부정은 하지 않음: 현재 첫 묶음에 확실한 성공 침해의 공개 증거가 없음. 2024~2026 최신성·기관 telemetry/KEV까지 조사해 W2를 마무리해야 함.
7. 공개 노출 서버 수는 버전 문자열 탐지/백포트 영향/실제 exploitable OS 구분 없이는 실제 취약 서버 수를 뜻하지 않음.

## 한계·반례·다음 관문
- [확실] Qualys 실험에서 root RCE 성립; 상위 9.8p1에서 unsafe 로그 경로가 제거됨.
- [유력] 상위 패치가 CVE-2024-6387의 알려진 기술적 원인을 차단. 타깃별 적용·회귀 테스트/백포트는 미확인.
- [반례] 인터넷 야생 악용 주장은 분류 근거에 문제가 있고, 공개 PoC 독립 재현 실패 보고가 존재. 공격은 간단하지 않으나 영향은 중대.
- [추가 필요] 2025~2026 보고 검증, Linux 배포판 백포트 diff, 자동 회귀 테스트/후속 패치, 객관적 적용·노출 잔존 지표.
- 첫 결과 Research Round Review에서 제안할 서로 다른 경로:
  A. 현실 악용 증거 심화(2024~2026 threat intel, KEV, 기술적 재현의 독립성)
  B. 패치·회귀 코드 심화(특히 Debian/Ubuntu/RHEL 백포트와 테스트)
  C. 현장 적용·잔존 실측(W4 주요 배포판과 공개 데이터).
- 추천: B를 제한적으로 보강한 뒤 C와 W2 최신 실측을 결합하여 A+B+C의 균형을 유지. 이미 제시된 A+B+C 승인 범위는 유지하고 우선순위만 선택받음.
