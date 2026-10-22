import unittest
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec

ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'scripts/t8_a6_validar_v11.py'
spec=spec_from_file_location('t8_a6_validar_v11',S)
m=module_from_spec(spec)
spec.loader.exec_module(m)

class IntegridadeT8A6(unittest.TestCase):
    def test_conjunto(self):
        d=m.validate(ROOT)
        self.assertEqual(d['reports_historicos']+d['reports_adicionais_propostos'],15)
    def test_gates(self):
        a=m.read_csv(ROOT/'data/screening/t8-a6-gates-revisados-v1.1.csv')
        self.assertEqual(len(a),9)
        self.assertNotEqual(next(x for x in a if x['gate']=='G09')['status_t8_a6'],'SUBMETIDO')
    def test_proveniência(self):
        a=m.read_csv(ROOT/'data/screening/t8-a5-registro-adjudicacao-16-reports-v1.0.csv')
        c=[x for x in a if x['report_id'].startswith('T8-C')]
        self.assertEqual(sum(x['in_proposed_15']=='YES' for x in c),5)
        self.assertEqual(sum(x['scopus_original']=='NOT_EVALUATED_SOURCE_UNAVAILABLE' for x in c),6)
    def test_st017_nao_reutilizada(self):
        a=m.read_csv(ROOT/'data/screening/t8-a5-registro-adjudicacao-16-reports-v1.0.csv')
        s=';'.join(x['study_ids'] for x in a if x['in_proposed_15']=='YES')
        self.assertNotIn('ST017',s)
        self.assertIn('ST022',s)

if __name__=='__main__':
    unittest.main()
