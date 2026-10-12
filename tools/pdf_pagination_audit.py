#!/usr/bin/env python3
"""Read-only PDF chapter pagination audit. Whitespace is a review warning."""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
import fitz

RX = re.compile(r'^\s*(\d{1,3})\.\s+(.+)', re.M)

def audit(path: Path, expected: int | None = None, top_limit: float = 180.,
          gap_threshold: float = .30):
    doc = fitz.open(path)
    chapters, pages, problems = [], [], []
    for i, p in enumerate(doc):
        blocks = [b for b in p.get_text('blocks') if b[6] == 0 and b[4].strip()]
        hits = []
        for b in blocks:
            for line in b[4].splitlines():
                m = RX.match(line.strip())
                if m and int(m.group(1)) <= (expected or 999):
                    hits.append({'chapter': int(m.group(1)), 'title': m.group(2).strip(),
                                 'page': i+1, 'y': round(b[1], 1)})
        chapters += hits
        body = [b for b in blocks if b[1] >= 63 and b[3] <= p.rect.height - 57]
        if i >= 2 and not body:
            problems.append({'type': 'contentless_report_page', 'page': i+1})
        bottom = max((b[3] for b in body), default=0.)
        gap = (p.rect.height - 60 - bottom) / max(1., p.rect.height - 130)
        pages.append({'page': i+1, 'last_body_y': round(bottom, 1),
                      'unused_fraction_approx': round(max(0, gap), 3),
                      'chapter_starts': hits})
    for h in chapters:
        if h['y'] > top_limit:
            problems.append({'type': 'chapter_not_at_page_top', **h, 'limit_y': top_limit})
    for i, item in enumerate(pages):
        if i < 2 or item['unused_fraction_approx'] < gap_threshold:
            continue
        next_chapter = i+1 < len(pages) and bool(pages[i+1]['chapter_starts'])
        item['gap_class'] = ('possible_intentional_chapter_end' if next_chapter
                             else 'review_figure_or_table_flow')
    if expected is not None:
        ids = [x['chapter'] for x in chapters]
        if ids != list(range(1, expected+1)):
            problems.append({'type': 'chapter_sequence_incomplete',
                             'actual': ids, 'expected': list(range(1, expected+1))})
    return {'file': str(path), 'page_count': len(doc), 'chapters': chapters,
            'hard_issues': problems,
            'large_gap_pages': [p for p in pages if 'gap_class' in p],
            'verdict': ('FAIL' if problems else
                        'PASS_WITH_REVIEW_WARNINGS' if any('gap_class' in p for p in pages)
                        else 'PASS')}

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('pdf', type=Path)
    ap.add_argument('--expect-chapters', type=int)
    ap.add_argument('--top-limit', type=float, default=180.)
    ap.add_argument('--gap-threshold', type=float, default=.30)
    ap.add_argument('--strict', action='store_true')
    a = ap.parse_args(argv)
    result = audit(a.pdf, a.expect_chapters, a.top_limit, a.gap_threshold)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if a.strict and result['hard_issues'] else 0
if __name__ == '__main__':
    sys.exit(main())
