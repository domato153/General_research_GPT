"""Structural checks of research trigger, scope and strength contracts.

These tests check rules on disk, NOT that an LLM spontaneously obeys them.
Behavioral tests require an independently replayed actual project session.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def section(filename, start, end):
    text = (ROOT / filename).read_text(encoding="utf-8")
    if text.count(start) != 1:
        raise AssertionError("Missing or repeated section: " + start)
    remainder = text.split(start, 1)[1]
    if end not in remainder:
        raise AssertionError("Missing end of section: " + end)
    return remainder.split(end, 1)[0]

class TriggerStrengthStaticContract(unittest.TestCase):
    def test_bootstrap_trigger_and_choice_separated(self):
        s=section("PROJECT_BOOTSTRAP.md","## 대화형 단계 협업 보존","## 심층조사의 반복 검증")
        for term in ("사용자 질문을 기다리지 않고","필수 근거 오류","개수 제한 없이",
                     "추천만으로 착수하지 않는다","현 근거로 진행","무한 확장"):
            self.assertIn(term,s)
    def test_router_complex_vs_short(self):
        s=section("00_INDEX.md","### 심층조사 반복 검증","### 중간 검증 게이트")
        for term in ("그럴듯해도 Stage 2·3","계획 밖 중요 누락축","다음 승인 W-ID"):
            self.assertIn(term,s)
    def test_stage1_compulsory_but_risk_proportionate(self):
        s=section("02_RESEARCH_PIPELINE.md","## Stage 1 — Initial Research","## Stage 2 — Adversarial Review")
        for term in ("복합·누적 심층조사","실제로 수행","단순·저위험 단발 질문","실질 판단을 생략"):
            self.assertIn(term,s)
    def test_stage2_plan_outside_and_bounded_source_probing(self):
        s=section("02_RESEARCH_PIPELINE.md","## Stage 2 — Adversarial Review","## Stage 3 — Evidence & Freshness Check")
        for term in ("계획 밖 중요 누락축 탐색","비교집단 편향","표적 예비확인",
                     "자동 확장 본조사의 승인인 것은 아니며"):
            self.assertIn(term,s)
    def test_stage3_links_not_equivalent_to_verification(self):
        s=section("02_RESEARCH_PIPELINE.md","## Stage 3 — Evidence & Freshness Check","## Stage 3.5 — Mini Review Gate")
        for term in ("링크 존재만으로","원문·원표","자율 정정/보류","반복 전수조사"):
            self.assertIn(term,s)
    def test_next_work_is_not_outside_plan_scan(self):
        s=section("02_RESEARCH_PIPELINE.md","## 사용자 승인 작업 완료 게이트","## Research Round Review")
        self.assertIn("계획 자체에 빠진 중요 조사축을 탐색하는 별도 판단",s)
    def test_reviewer_disclosure_and_explicit_recommendation_limit(self):
        s=section("02_RESEARCH_PIPELINE.md","## Research Round Review","## Stage 1 — Initial Research")
        for term in ("종합 전환 강한 발동","2~3개로 제한하지 않고","후보 수 상한이 아니다",
                     "개별 후보를 숨기지 않고 선택 가능","현재 근거로 기존 종합검증·조건부 종료"):
            self.assertIn(term,s)
    def test_scope_choice_and_a_vs_d_boundary(self):
        s=section("02_RESEARCH_PIPELINE.md","## Research Round Review","## Stage 1 — Initial Research")
        for term in ("개별 후보 선택·조합·축소","미승인 확장 제안은 새 필수 W-ID 착수 승인이 아니다",
                     "중대한 A 근거 결함","제안/선택/보류/제외"):
            self.assertIn(term,s)
    def test_stage5_finite_closure_and_no_hard_candidate_cap(self):
        s=section("02_RESEARCH_PIPELINE.md","## Stage 5 — Closure Readiness Check","## Stage 6 — Final Report Draft Assembly")
        for term in ("계획 밖 누락 탐색을 실제 수행","무한 확장하지 않는다",
                     "미선택 후보가 있어도 종료 가능","개수 제한 없이"):
            self.assertIn(term,s)
        self.assertNotIn("후보 1~3개와 우선순위",s)
    def test_critique_d_and_validation_congruence(self):
        review=section("03_REVIEW_MODULES.md","## 사용자 선택형 재조사 제안의 품질 검증","## 누락·보완 요청의 분류 원칙")
        d=section("03_REVIEW_MODULES.md","## 누락·보완 요청의 분류 원칙","# 2. Evidence Module")
        checks=section("04B_VALIDATION_RULES.md","## 승인 작업 완료·다음 단계 Gate 검증","## RESEARCH_PLAN.md 정본 검증")
        for term in ("개별 고가치 후보","실제 독립 근거","실행 조합 2~3개"):
            self.assertIn(term,review)
        self.assertIn("고가치 미승인 확장",d)
        for term in ("발동·실검증 강도","원문/원표","후보·조합·권한 및 종료 강도","현 근거로 진행"):
            self.assertIn(term,checks)
    def test_scenario_matrix_and_no_false_live_pass(self):
        s=(ROOT/"tests/TRIGGER_SCOPE_STRENGTH_CASES.md").read_text(encoding="utf-8")
        for i in range(1,21):
            self.assertIn(f"| T{i:02d} |",s)
        for term in ("NOT RUN","E2E UNKNOWN","static","no-write","not a behavioral PASS"):
            self.assertIn(term,s)

if __name__ == "__main__":
    unittest.main()
