import csv, pathlib, unittest, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from t8_a5_validar_v10 import validate,load

class TestT8A5(unittest.TestCase):
    def test_conjunto_historico_e_proposto(self):
        idx=load('t8-a3-indice-21-studies-propostas-v0.7.csv')
        ids={x['study_id'] for x in idx}
        self.assertEqual(len(ids),21)
        self.assertNotIn('ST017',ids)
        self.assertIn('ST022',ids)
    def test_candidato_suspenso(self):
        inv=load('t8-a5-registro-adjudicacao-16-reports-v1.0.csv')
        self.assertEqual(sum(x['in_proposed_15']=='YES' for x in inv),15)
        self.assertEqual(next(x for x in inv if x['report_id']=='T8-C03')['in_proposed_15'],'NO')
    def test_nao_finge_homologacao(self):
        gates=load('t8-a5-checklist-fechamento-v1.0.csv')
        self.assertEqual(len(gates),9)
        self.assertTrue(all(x['confirmacao_executada']=='NAO' for x in gates))
    def test_integridade_total(self):
        self.assertTrue(validate())

if __name__=='__main__':unittest.main()
