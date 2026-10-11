#!/usr/bin/env python3
"""Optional read-only W-ID / final report validator.

Machine-checkable structure may PASS, but semantic accuracy, actual chat UI
delivery, and PDF visual quality never PASS merely from file comparisons.
No network, no repository mutations, no mandatory new schemas.
"""
import argparse
import json
import re
import sys
from pathlib import Path

ID = re.compile(r"\b(W\d{1,3}[-_]E\d{1,4})\b", re.I)
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
MARKER = re.compile(r"^\s*<!--\s*item\s*:\s*(W\d{1,3}[-_]E\d{1,4})\s*-->\s*$", re.I)
URL = re.compile(r"https?://[^\s<>\]\)\"']+", re.I)
RANK = {"PASS": 0, "N/A": 0, "UNKNOWN": 1, "HOLD": 2}

def load(path):
    return Path(path).read_text(encoding="utf-8-sig")

def normalize(text):
    return re.sub(r"\s+", " ", text.replace("\ufeff", "")).strip()

def check(out, key, status, reason, **details):
    out["checks"][key] = {"status": status, "reason": reason, **details}

def sections(text):
    """Only explicit Wxx-Eyy headings / item comments count, not prose mentions."""
    lines = text.splitlines()
    result, duplicates = {}, []
    for i, line in enumerate(lines):
        header, comment = HEADING.match(line), MARKER.match(line)
        hit = ID.search(header.group(2)) if header else None
        value = comment.group(1) if comment else hit.group(1) if hit else None
        if not value:
            continue
        key = value.upper().replace("_", "-")
        level = len(header.group(1)) if header else 6
        stop = len(lines)
        for j in range(i + 1, len(lines)):
            next_header = HEADING.match(lines[j])
            if MARKER.match(lines[j]) or (next_header and len(next_header.group(1)) <= level):
                stop = j
                break
        body = "\n".join(lines[i + 1:stop]).strip()
        if key in result:
            duplicates.append(key)
        result[key] = {"body": body, "line": i + 1, "links": set(URL.findall(body))}
    return result, sorted(set(duplicates))

def evidence(args, out):
    before, after = load(args.before), load(args.after)
    old, dup_old = sections(before)
    new, dup_new = sections(after)
    duplicates = sorted(set(dup_old + dup_new))
    check(out, "duplicate_ids", "HOLD" if duplicates else "PASS",
          "Duplicate item headings" if duplicates else "Stable item IDs unique",
          duplicates=duplicates)
    required = set(old) | {x.upper().replace("_", "-") for x in args.required_id}
    if not required:
        check(out, "item_presence", "UNKNOWN", "Baseline has no stable item IDs")
    else:
        missing = sorted(required - set(new))
        check(out, "item_presence", "HOLD" if missing else "PASS",
              "Baseline item headings compared", required=len(required), missing=missing)
        short = sorted(i for i in required & set(new) if len(normalize(new[i]["body"])) < args.min_body_chars)
        check(out, "body_floor", "HOLD" if short else "PASS",
              "Structural floor only; narrative sufficiency needs human/AI review",
              too_short=short, threshold=args.min_body_chars)
        missing_links = {i: sorted(old[i]["links"] - new[i]["links"])
                         for i in old.keys() & new.keys() if old[i]["links"] - new[i]["links"]}
        check(out, "source_links", "HOLD" if missing_links else "PASS",
              "Only detects disappeared URLs, not source validity", missing=missing_links)
    check(out, "content_changes", "PASS" if normalize(before) == normalize(after) else "UNKNOWN",
          "Normalized content unchanged" if normalize(before) == normalize(after)
          else "Changed text may be intentional or may omit meaning: independent review needed")
    check(out, "never_saved", "UNKNOWN",
          "Cannot detect findings never recorded in baseline sources")

def final(args, out):
    report = load(args.report)
    check(out, "report_present", "PASS" if normalize(report) else "HOLD",
          "Report file nonempty" if normalize(report) else "Empty final report")
    if args.part:
        actual = "\n".join(load(p) for p in args.part)
        equal = normalize(report) == normalize(actual)
        check(out, "part_assembly", "PASS" if equal else "HOLD",
              "Actual supplied Part contents compared to report", count=len(args.part), equal=equal)
    else:
        check(out, "part_assembly", "N/A", "No Part snapshots supplied")
    if args.delivery:
        if args.delivery_mode == "full":
            equal = normalize(report) == normalize(load(args.delivery))
            check(out, "delivery_text", "PASS" if equal else "HOLD",
                  "Supplied text snapshot comparison only, not UI display", equal=equal)
        else:
            check(out, "delivery_text", "UNKNOWN",
                  "Summary/visual edition needs a separate meaning audit, not literal equality")
        check(out, "actual_ui_display", "UNKNOWN",
              "Local transcript/snapshot is not proof of actual rendered chat UI")
    else:
        check(out, "delivery_text", "UNKNOWN", "Delivered text not supplied")
    if args.source:
        sources = set()
        for f in args.source:
            items, _ = sections(load(f))
            sources.update(items)
        if args.mapping:
            try:
                entries = json.loads(load(args.mapping))["items"]
                if not isinstance(entries, list):
                    raise ValueError("items must be an array")
                invalid, missing, mapped = [], [], set()
                for e in entries:
                    key = str(e["id"]).upper().replace("_", "-")
                    section = str(e.get("section", "")).strip()
                    disposition = e.get("disposition", "full")
                    if not ID.fullmatch(key) or disposition not in ("full", "brief", "appendix", "excluded") or (disposition != "excluded" and not section):
                        invalid.append(key)
                        continue
                    mapped.add(key)
                    if key not in sources or (disposition != "excluded" and section not in report.splitlines()):
                        missing.append(key)
                unmapped = sorted(sources - mapped)
                state = "HOLD" if invalid or missing else "UNKNOWN" if unmapped else "PASS"
                check(out, "coverage_map_structure", state,
                      "Section presence only; depth, valid exclusion, and counterevidence require Stage 7",
                      invalid=invalid, missing=missing, unmapped=unmapped)
            except (ValueError, TypeError, KeyError) as exc:
                check(out, "coverage_map_structure", "HOLD", f"Invalid map: {exc}")
        else:
            check(out, "coverage_map_structure", "UNKNOWN",
                  "Source W-ID findings exist but no explicit coverage/selection map supplied",
                  stable_source_items=len(sources))
    else:
        check(out, "coverage_map_structure", "UNKNOWN",
              "No source W-ID file supplied: inclusion cannot be confirmed")
    check(out, "semantic_adequacy", "UNKNOWN",
          "No automated proof of fact coverage, detailed narratives, counterarguments, or authorization")

def pdf(args, out):
    try:
        import fitz
    except ImportError:
        check(out, "reader", "UNKNOWN", "Optional PyMuPDF unavailable")
        return
    try:
        with fitz.open(args.pdf) as doc:
            check(out, "pages", "PASS" if doc.page_count else "HOLD",
                  "PDF opened; page count is not quality proof", count=doc.page_count)
            contents = normalize("\n".join(p.get_text() for p in doc))
            if args.must_contain or args.must_not_contain:
                missing = [v for v in args.must_contain if normalize(v) not in contents]
                bad = [v for v in args.must_not_contain if normalize(v) in contents]
                check(out, "text_probes", "HOLD" if missing or bad else "PASS",
                      "Only user-supplied information probes, not full content comparison",
                      missing=missing, unexpected=bad)
            else:
                check(out, "text_probes", "UNKNOWN", "No text probes supplied")
            outside = []
            for i, page in enumerate(doc, 1):
                for block in page.get_text("blocks"):
                    rect = fitz.Rect(block[:4])
                    if rect.is_empty or rect.is_infinite or not page.rect.contains(rect):
                        outside.append(i)
            check(out, "block_bounds", "HOLD" if outside else "PASS",
                  "Extracted block bounds only; does not prove full visual quality",
                  outside_pages=sorted(set(outside)))
        check(out, "visual_quality", "UNKNOWN",
              "Render and inspect actual PDF pages, captions, fonts, figures and pagination")
        check(out, "semantic_fidelity", "UNKNOWN",
              "Text probes do not prove all chart/table meaning preserved")
    except Exception as exc:
        check(out, "reader", "HOLD", f"PDF unavailable or unreadable: {type(exc).__name__}: {exc}")

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fail-on-unknown", action="store_true",
                        help="Optional exit code 3 on UNKNOWN; default does not block on unknown")
    sub = parser.add_subparsers(dest="mode", required=True)
    ev = sub.add_parser("evidence")
    ev.add_argument("--before", required=True)
    ev.add_argument("--after", required=True)
    ev.add_argument("--required-id", action="append", default=[])
    ev.add_argument("--min-body-chars", type=int, default=20)
    fi = sub.add_parser("final")
    fi.add_argument("--report", required=True)
    fi.add_argument("--part", action="append", default=[])
    fi.add_argument("--source", action="append", default=[])
    fi.add_argument("--mapping", help='Optional JSON with items [{"id","section","disposition"}]')
    fi.add_argument("--delivery", help="Available text snapshot only, not UI proof")
    fi.add_argument("--delivery-mode", choices=["full", "summary", "visual"], default="full")
    pd = sub.add_parser("pdf")
    pd.add_argument("--pdf", required=True)
    pd.add_argument("--must-contain", action="append", default=[])
    pd.add_argument("--must-not-contain", action="append", default=[])
    args = parser.parse_args(argv)
    out = {"mode": args.mode, "checks": {},
           "note": "Read-only preflight; not a semantic audit or live chat E2E."}
    try:
        {"evidence": evidence, "final": final, "pdf": pdf}[args.mode](args, out)
    except (OSError, UnicodeError) as exc:
        check(out, "file_access", "UNKNOWN", f"Input unavailable: {type(exc).__name__}: {exc}")
    highest = max((RANK[c["status"]] for c in out["checks"].values()), default=1)
    out["status"] = "HOLD" if highest == 2 else "UNKNOWN" if highest == 1 else "PASS"
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 2 if highest == 2 else 3 if highest == 1 and args.fail_on_unknown else 0

if __name__ == "__main__":
    sys.exit(main())
