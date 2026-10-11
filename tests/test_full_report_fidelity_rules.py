"""Static regressions for Full Report fidelity. NOT a model E2E or semantic PASS."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOT = (ROOT / "PROJECT_BOOTSTRAP.md").read_text(encoding="utf-8")
PIPE = (ROOT / "02_RESEARCH_PIPELINE.md").read_text(encoding="utf-8")
FINAL = (ROOT / "13_FINAL_REPORT.md").read_text(encoding="utf-8")
VALID = (ROOT / "04B_VALIDATION_RULES.md").read_text(encoding="utf-8")
TOOL = (ROOT / "tools/research_validator.py").read_text(encoding="utf-8")


def between(text, start, end):
    return text.split(start, 1)[1].split(end, 1)[0]


class FullReportFidelityRules(unittest.TestCase):
    def test_bootstrap_routes_followup_results_without_short_mode_bloat(self):
        self.assertIn("상세형 최종보고서의 후속 결과 동등 수록", BOOT)
        self.assertIn("Brief·일반 단발 답변", BOOT)
        self.assertIn("추가 승인 관문을 강제하지 않는다", BOOT)

    def test_stage5_discovers_real_files_beyond_parent_wid(self):
        scope = between(PIPE, "## Stage 5 —", "## Stage 6 —")
        for term in ("연구 브랜치 HEAD", "RESEARCH_PLAN.md", "별도 보완·재검증·연결", "파일 목록/트리", "최신 사용자"):
            self.assertIn(term, scope)

    def test_stage5_rejects_presence_equals_approval(self):
        scope = between(PIPE, "## Stage 5 —", "## Stage 6 —")
        for term in ("파일 존재·조건부 완료", "미검증/보류", "열지 못한 중요 파일"):
            self.assertIn(term, scope)

    def test_stage6_connects_semantic_contents_not_just_filename(self):
        scope = between(PIPE, "## Stage 6 —", "## Stage 6.5 —")
        for term in ("상세형 기본 수록과 결과별 연결", "비교 조건·반례·불확실성", "예정/실제 본문", "부록 제목/출처 링크"):
            self.assertIn(term, scope)

    def test_lite_restores_scope_without_full_rereading(self):
        scope = between(PIPE, "### LONG-LITE", "### 할 일")
        for term in ("전체 후보 범위의 경량 재개", "처리/미처리 상태", "반복 재조회하지 않고", "part_assembly=PASS"):
            self.assertIn(term, scope)

    def test_stage7_gate_catches_unseen_followup_sources(self):
        scope = between(PIPE, "## Stage 7 —", "### 목적")
        for term in ("후속 보완을 포함한 전체 입력", "실제 원문을 검토", "Full Report 정보 완전성 PASS", "구조 PASS"):
            self.assertIn(term, scope)

    def test_final_density_preserves_standard_and_user_choice(self):
        self.assertIn("기본값은 **Standard**", FINAL)
        self.assertIn("Full Report 상세형·Expanded의 수록 기본값", FINAL)
        self.assertIn("단순 제목·근거 링크·한 줄", FINAL)
        self.assertIn("사용자가 선택한 상세 부록", FINAL)
        self.assertIn("Brief의 간결성", FINAL)

    def test_validation_requires_real_meaning_and_permits_integration(self):
        scope = between(VALID, "## Stage 5~8 보고서 준비·확정 Gate 검증", "##")
        for term in ("실제 연구 HEAD", "별도 승인 보완", "의미검사", "충실 통합", "미수행 검수"):
            self.assertIn(term, scope)

    def test_validator_still_disclaims_semantic_pass(self):
        self.assertIn('check(out, "semantic_adequacy", "UNKNOWN"', TOOL)
        self.assertIn("No automated proof of fact coverage", TOOL)
        self.assertIn('scope="syntax_and_heading_only"', TOOL)


if __name__ == "__main__":
    unittest.main()
