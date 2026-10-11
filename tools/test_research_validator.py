"""Offline focused regressions for the optional read-only validator."""
import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("rv", Path(__file__).with_name("research_validator.py"))
rv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rv)

def fixture(tmp_path, name, text):
    file = tmp_path / name
    file.write_text(text, encoding="utf-8")
    return str(file)

def run(capsys, argv):
    code = rv.main(argv)
    return code, json.loads(capsys.readouterr().out)

def test_evidence_preserved_and_not_overclaiming(tmp_path, capsys):
    src = "## W02-E01\n사건 배경과 전개 및 결과를 설명하는 구체적인 자료입니다. https://example.org/a\n## W02-E02\n두 번째 사건에 대한 자세한 기록과 출처가 보존됩니다. https://example.org/b"
    f = fixture(tmp_path, "source.md", src)
    code, r = run(capsys, ["evidence", "--before", f, "--after", f])
    assert code == 0 and r["status"] == "UNKNOWN"
    assert r["checks"]["item_presence"]["status"] == "PASS"
    assert r["checks"]["never_saved"]["status"] == "UNKNOWN"

def test_evidence_deletion_and_link_loss(tmp_path, capsys):
    before = fixture(tmp_path, "old.md", "## W02-E01\n이 중요한 사건의 맥락은 출처에서 확인된 사실입니다. https://example.org/a\n## W02-E02\n다른 사건의 구체적인 원인과 결과도 충분히 기록합니다.")
    after = fixture(tmp_path, "new.md", "## W02-E01\n사건의 맥락은 여전히 남아 있지만 출처는 삭제됐습니다.")
    code, r = run(capsys, ["evidence", "--before", before, "--after", after])
    assert code == 2 and r["checks"]["item_presence"]["missing"] == ["W02-E02"]
    assert r["checks"]["source_links"]["status"] == "HOLD"

def test_title_only_detected(tmp_path, capsys):
    before = fixture(tmp_path, "old.md", "## W02-E01\n배경과 전개가 충분히 기록된 긴 설명이 원래 존재했습니다.")
    after = fixture(tmp_path, "new.md", "## W02-E01\n제목")
    code, r = run(capsys, ["evidence", "--before", before, "--after", after])
    assert code == 2 and r["checks"]["body_floor"]["status"] == "HOLD"

def test_untracked_unknown_exit(tmp_path, capsys):
    f = fixture(tmp_path, "no_ids.md", "# 조사\n개별 ID는 존재하지 않습니다.")
    code, r = run(capsys, ["--fail-on-unknown", "evidence", "--before", f, "--after", f])
    assert code == 3 and r["checks"]["item_presence"]["status"] == "UNKNOWN"

def test_parts_and_delivered_snapshot(tmp_path, capsys):
    a, b = "## 제1장\n첫 번째 내용입니다.", "## 제2장\n측정값 <0.02ms 입니다."
    report = fixture(tmp_path, "FINAL_REPORT.md", a + "\n" + b)
    p1, p2 = fixture(tmp_path, "p1.md", a), fixture(tmp_path, "p2.md", b)
    code, r = run(capsys, ["final", "--report", report, "--part", p1, "--part", p2])
    assert code == 0 and r["checks"]["part_assembly"]["status"] == "PASS"
    wrong = fixture(tmp_path, "wrong.md", b.replace("<0.02ms", "=0.02ms"))
    code, r = run(capsys, ["final", "--report", report, "--part", p1, "--part", wrong])
    assert code == 2 and r["checks"]["part_assembly"]["status"] == "HOLD"
    full = fixture(tmp_path, "full.txt", a + "\n" + b)
    code, r = run(capsys, ["final", "--report", report, "--delivery", full])
    assert r["checks"]["delivery_text"]["status"] == "PASS"
    assert r["checks"]["actual_ui_display"]["status"] == "UNKNOWN"
    new = fixture(tmp_path, "new.txt", a + "\n" + b + "\n새로운 채팅 전용 본문")
    code, r = run(capsys, ["final", "--report", report, "--delivery", new])
    assert code == 2 and r["checks"]["delivery_text"]["status"] == "HOLD"
    code, r = run(capsys, ["final", "--report", report, "--delivery", new, "--delivery-mode", "summary"])
    assert code == 0 and r["checks"]["delivery_text"]["status"] == "UNKNOWN"

def test_source_report_mapping(tmp_path, capsys):
    source = fixture(tmp_path, "W02.md", "## W02-E01\n첫 번째 긴 기록의 맥락과 출처\n## W02-E02\n두 번째 긴 기록의 맥락과 출처")
    report = fixture(tmp_path, "report.md", "## 첫 번째 수록\n구체적인 내용을 소개합니다.")
    mapping = fixture(tmp_path, "mapping.json", json.dumps({"items":[{"id":"W02-E01","section":"## 첫 번째 수록"}]}))
    code, r = run(capsys, ["final", "--report", report, "--source", source, "--mapping", mapping])
    assert code == 0 and r["checks"]["coverage_map_structure"]["status"] == "UNKNOWN"
    mapping = fixture(tmp_path, "mapping.json", json.dumps({"items":[{"id":"W02-E01","section":"## 첫 번째 수록"},{"id":"W02-E02","section":"## 누락된 수록"}]}))
    code, r = run(capsys, ["final", "--report", report, "--source", source, "--mapping", mapping])
    assert code == 2 and r["checks"]["coverage_map_structure"]["status"] == "HOLD"

def test_pdf_probes_without_visual_false_pass(tmp_path, capsys):
    fitz = pytest.importorskip("fitz")
    doc = fitz.open()
    doc.new_page().insert_text((72, 72), "OSLTT <0.02ms, same test conditions.")
    path = tmp_path / "report.pdf"
    doc.save(str(path))
    doc.close()
    code, r = run(capsys, ["pdf", "--pdf", str(path), "--must-contain", "<0.02ms", "--must-not-contain", "=0.02ms"])
    assert code == 0 and r["checks"]["text_probes"]["status"] == "PASS"
    assert r["checks"]["visual_quality"]["status"] == "UNKNOWN"
    code, r = run(capsys, ["pdf", "--pdf", str(path), "--must-contain", "=0.02ms"])
    assert code == 2 and r["checks"]["text_probes"]["status"] == "HOLD"

def test_read_only_and_missing_file(tmp_path, capsys):
    src = "## W02-E01\n조사 내용은 중요한 원문을 충분히 포함합니다."
    p = fixture(tmp_path, "input.md", src)
    original = Path(p).read_bytes()
    run(capsys, ["evidence", "--before", p, "--after", p])
    assert Path(p).read_bytes() == original
    code, r = run(capsys, ["final", "--report", str(tmp_path / "does-not-exist.md")])
    assert code == 0 and r["status"] == "UNKNOWN"
