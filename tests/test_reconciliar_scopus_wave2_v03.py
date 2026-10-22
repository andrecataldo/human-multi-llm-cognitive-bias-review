"""Testes de regressão locais sem acesso aos 1.419 registros originais."""
import csv
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'reconciliar_scopus_wave2_v03.py'
spec = importlib.util.spec_from_file_location('reconcile', SCRIPT)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def write(p, header, rows):
    with p.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.writer(f);w.writerow(header);w.writerows(rows)


class ReconcileTests(unittest.TestCase):
    def test_explicit_decisions_and_conflict(self):
        with tempfile.TemporaryDirectory() as temp:
            folder=Path(temp)
            s,c=folder/'s.csv',folder/'c.csv'
            write(s,['DOI','Title','EID','final_decision'],[
                ['10.1000/one','A title','2-s2.0-1','RETAIN_FOR_FULL_TEXT'],
                ['10.1000/two','Second title','2-s2.0-2','EXCLUDE'],
                ['10.1000/other','Third title','2-s2.0-3','RETAIN_FOR_FULL_TEXT'],
                ['10.1000/doubled','Doubled','2-s2.0-4','RETAIN_FOR_FULL_TEXT'],
                ['10.1000/doubled','Doubled','2-s2.0-5','RETAIN_FOR_FULL_TEXT'],
            ])
            write(c,['candidate_id','doi','title'],[
                ['C01','https://doi.org/10.1000/one','A title'],
                ['C02','10.1000/two','Second title'],
                ['C03','10.1000/mismatch','Third title'],
                ['C04','10.1000/missing','Absent'],
                ['C05','10.1000/doubled','Doubled'],
            ])
            out,meta=module.process(s,c)
            self.assertEqual([x['match_status'] for x in out],['MATCH_RETAINED','MATCH_EXCLUDED','TITLE_MATCH_DOI_CONFLICT','NOT_PRESENT_IN_SUPPLIED_EXPORT','AMBIGUOUS_MULTIPLE_RECORDS'])
            self.assertEqual(meta['input_records'],5)
            with self.assertRaises(ValueError): module.process(s,c,expected_count=1419)

    def test_retained_only_requires_flag(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp);s,c=p/'s.csv',p/'c.csv'
            write(s,['DOI','Title'],[['10.1000/one','Title']])
            write(c,['candidate_id','doi','title'],[['C01','10.1000/one','Title']])
            with self.assertRaisesRegex(ValueError,'decisão'): module.process(s,c)
            out,_=module.process(s,c,retained_only=True,expected_count=1)
            self.assertEqual(out[0]['match_status'],'MATCH_RETAINED')

    def test_title_match_without_doi_is_weaker(self):
        with tempfile.TemporaryDirectory() as temp:
            p=Path(temp);s,c=p/'s.tsv',p/'c.csv'
            write(s,['DOI','Title','decision'],[['','A: Study of Decisions','RETAIN_FOR_FULL_TEXT']])
            write(c,['candidate_id','doi','title'],[['C01','10.1000/one','A Study of Decisions']])
            out,_=module.process(s,c)
            self.assertEqual(out[0]['match_status'],'MATCH_RETAINED')
            self.assertEqual(out[0]['match_method'],'EXACT_NORMALIZED_TITLE')
            self.assertIn('conferência humana',out[0]['note'])

if __name__ == '__main__':
    unittest.main()
