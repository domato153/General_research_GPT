"""Five unit regressions: bad/good chapter pagination and expected whitespace."""
import sys, tempfile, unittest
from pathlib import Path
import fitz
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from pdf_pagination_audit import audit
class PageTests(unittest.TestCase):
    def check(self, body_pages):
        with tempfile.TemporaryDirectory() as d:
            f=Path(d)/'test.pdf'; pdf=fitz.open()
            for items in [[(95,'COVER')],[(95,'CONTENTS')],*body_pages]:
                p=pdf.new_page(width=595,height=842)
                for y,t in items:
                    p.insert_text((65,y),t,fontsize=12)
            pdf.save(f)
            return audit(f,2)
    def test_midpage_fails(self):
        a=self.check([[(95,'1. First')],[(400,'2. Second')]])
        self.assertTrue(any(x['type']=='chapter_not_at_page_top' for x in a['hard_issues']))
    def test_page_top_pass(self):
        self.assertFalse(self.check([[(95,'1. First')],[(95,'2. Second')]])['hard_issues'])
    def test_missing_chapter_fails(self):
        a=self.check([[(95,'1. First')]])
        self.assertTrue(any(x['type']=='chapter_sequence_incomplete' for x in a['hard_issues']))
    def test_intentional_gap_is_only_warning(self):
        a=self.check([[(95,'1. First'),(190,'Short ending')],[(95,'2. Second')]])
        self.assertFalse(a['hard_issues'])
        self.assertEqual(a['large_gap_pages'][0]['gap_class'],'possible_intentional_chapter_end')
    def test_non_chapter_gap_requires_review(self):
        a=self.check([[(95,'1. First'),(190,'Text')],[(95,'Continued chart')],[(95,'2. Second')]])
        self.assertTrue(any(x['gap_class']=='review_figure_or_table_flow' for x in a['large_gap_pages']))
if __name__=='__main__':
    unittest.main()
