import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "screening"

def rows(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

class TestT8A2(unittest.TestCase):
    def test_five_reports_gated(self):
        vals = rows("t8-a2-elegibilidade-5-reports-v0.5.csv")
        self.assertEqual(len(vals), 5)
        self.assertEqual(len({x['doi'] for x in vals}), 5)
        self.assertTrue(all(x['decisao_final'] == 'PENDENTE' for x in vals))
        self.assertTrue(all(x['pertence_scopus_1419'] == 'NAO_VERIFICAVEL_SEM_EXPORT' for x in vals))
        self.assertEqual(sum(x['i9_texto_integral_conferido']=='SIM' for x in vals), 4)
        self.assertEqual(next(x for x in vals if x['candidate_id']=='T8-C03')['i9_texto_integral_conferido'],'NAO_VERIFICADO')

    def test_eight_studies_not_adjudicated(self):
        vals = rows("codificacao-wave2-8-studies-v0.5.csv")
        self.assertEqual(len(vals), 8)
        self.assertEqual({x['study'] for x in vals}, {f'ST{i:03d}' for i in range(14,22)})
        self.assertTrue(all(x['final_inclusion']=='NOT_DECIDED' for x in vals))
        self.assertEqual(sum(x['report']=='T8-C05' for x in vals),3)
        st016 = next(x for x in vals if x['study']=='ST016')
        self.assertIn('AGENTES QUE MUDAM',st016['result'])

    def test_evidence_traceability(self):
        vals = rows("t8-a2-evidencias-revisadas-v0.5.csv")
        self.assertEqual(len(vals), 16)
        self.assertTrue(all(x['source_locator'] and x['source_url'] for x in vals))
        self.assertTrue(all(x['researcher_check_status'].startswith('PENDING') for x in vals))

if __name__ == '__main__': unittest.main()
