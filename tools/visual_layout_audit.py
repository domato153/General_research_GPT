#!/usr/bin/env python3
"""Conservative SVG text-collision and sparse-plot preflight for research charts.

Outputs review targets, not proof of PDF visual quality. Read-only; --strict exits
nonzero for review findings. Final verdict requires inspection of rendered pages.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from pathlib import Path


def _length(value, default=0.):
    try:
        return float(re.match(r'[-+]?\d+(?:\.\d+)?', str(value)).group())
    except (AttributeError, ValueError):
        return default


def _width(text, font_size):
    units = 0.
    for ch in text:
        if ch.isspace():
            units += .34
        elif unicodedata.east_asian_width(ch) in 'FW' or 'HANGUL' in unicodedata.name(ch, ''):
            units += 1.
        elif ch in 'ilI1.,:;|!':
            units += .28
        elif ch in 'mwMW@%':
            units += .82
        else:
            units += .57
    return units * font_size


def inspect_svg(svg: Path) -> dict:
    root = ET.parse(svg).getroot()
    vb = list(map(float, root.attrib.get('viewBox', '0 0 0 0').split()))
    if len(vb) != 4 or vb[2] <= 0 or vb[3] <= 0:
        raise ValueError(f'Invalid viewBox: {svg}')
    _, _, canvas_w, canvas_h = vb
    labels, bars, grid_bottom = [], [], []
    for el in root.iter():
        tag = el.tag.rsplit('}', 1)[-1]
        if tag == 'text':
            text = ''.join(el.itertext()).strip()
            if not text:
                continue
            size = _length(el.get('font-size'), 16)
            x, y = _length(el.get('x')), _length(el.get('y'))
            w = _width(text, size)
            anchor = el.get('text-anchor', 'start')
            left = x - w / 2 if anchor == 'middle' else x - w if anchor == 'end' else x
            labels.append({'text': text[:100], 'box': (left, y - .9 * size, left + w, y + .17 * size)})
        elif tag == 'rect' and el.get('data-value') is not None:
            bars.append({'y': _length(el.get('y')),
                         'bottom': _length(el.get('y')) + _length(el.get('height')),
                         'group': el.get('data-group') or el.get('data-date') or el.get('data-category')})
        elif tag == 'line' and abs(_length(el.get('x1')) - _length(el.get('x2'))) < .1:
            if _length(el.get('y2')) > _length(el.get('y1')):
                grid_bottom.append((_length(el.get('y1')), _length(el.get('y2'))))
    collisions = []
    for i, p in enumerate(labels):
        for q in labels[i + 1:]:
            a, b = p['box'], q['box']
            iw = min(a[2], b[2]) - max(a[0], b[0])
            ih = min(a[3], b[3]) - max(a[1], b[1])
            if iw >= 8 and ih >= 3:
                collisions.append({'a': p['text'], 'b': q['text'],
                                   'overlap_estimate': [round(iw, 1), round(ih, 1)]})
    sparse = []
    groups = {b['group'] for b in bars if b['group'] is not None}
    if bars and len(groups) == 1 and grid_bottom:
        top = min(y1 for y1, _ in grid_bottom)
        bottom = max(y2 for _, y2 in grid_bottom)
        maxbar = max(b['bottom'] for b in bars)
        gap = (bottom - maxbar) / max(1, bottom - top)
        if gap > .43 and (bottom - maxbar) > 70:
            sparse.append({'group': next(iter(groups)),
                           'empty_plot_fraction': round(gap, 3)})
    out_of_bounds = [v['text'] for v in labels
                     if v['box'][0] < -3 or v['box'][2] > canvas_w + 3
                     or v['box'][1] < -3 or v['box'][3] > canvas_h + 3]
    return {'path': str(svg), 'viewBox': vb, 'text_collisions_estimated': collisions,
            'sparse_single_group': sparse, 'out_of_bounds_estimated': out_of_bounds,
            'needs_review': bool(collisions or sparse or out_of_bounds)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('svg', nargs='+', type=Path)
    ap.add_argument('--strict', action='store_true',
                    help='Nonzero exit for review targets; requires rendered confirmation')
    args = ap.parse_args(argv)
    results = [inspect_svg(p) for p in args.svg]
    print(json.dumps({'results': results,
                      'needs_review': sum(x['needs_review'] for x in results)},
                     ensure_ascii=False, indent=2))
    return 2 if args.strict and any(x['needs_review'] for x in results) else 0


if __name__ == '__main__':
    sys.exit(main())
