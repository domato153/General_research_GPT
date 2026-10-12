"""Targeted positive/negative cases for adaptive report-chart validation."""
import tempfile
import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from visual_layout_audit import inspect_svg


def svg(body, w=600, h=300):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>'


class ChartLayoutTests(unittest.TestCase):
    def run_case(self, src):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / 'chart.svg'
            p.write_text(src, encoding='utf-8')
            return inspect_svg(p)

    def test_footer_crosses_tick_is_flagged(self):
        s = svg('<text x="200" y="245" font-size="16">25%</text>'
                '<text x="70" y="248" font-size="14">Source: a long citation under chart</text>')
        self.assertTrue(self.run_case(s)['text_collisions_estimated'])

    def test_dense_date_ticks_are_flagged(self):
        s = svg('<text x="220" y="240" font-size="15" text-anchor="middle">2026-02</text>'
                '<text x="245" y="240" font-size="15" text-anchor="middle">2026-03</text>')
        self.assertTrue(self.run_case(s)['text_collisions_estimated'])

    def test_one_row_stretched_plot_is_flagged(self):
        s = svg('<line x1="200" y1="80" x2="200" y2="265" />'
                '<rect x="200" y="95" width="80" height="15" data-group="g1" data-value="40" />'
                '<rect x="200" y="120" width="90" height="15" data-group="g1" data-value="45" />')
        self.assertTrue(self.run_case(s)['sparse_single_group'])

    def test_well_spaced_multi_row_not_flagged(self):
        s = svg('<text x="200" y="245" font-size="16">25%</text>'
                '<text x="70" y="282" font-size="14">Source: study</text>'
                '<line x1="200" y1="80" x2="200" y2="220" />'
                '<rect x="200" y="95" width="80" height="15" data-group="g1" data-value="40" />'
                '<rect x="200" y="185" width="90" height="15" data-group="g2" data-value="45" />')
        self.assertFalse(self.run_case(s)['needs_review'])

    def test_compact_one_row_not_flagged(self):
        s = svg('<line x1="200" y1="80" x2="200" y2="165" />'
                '<rect x="200" y="95" width="80" height="15" data-group="g1" data-value="40" />'
                '<rect x="200" y="120" width="90" height="15" data-group="g1" data-value="45" />')
        self.assertFalse(self.run_case(s)['needs_review'])


if __name__ == '__main__':
    unittest.main()
