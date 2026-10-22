"""Testes de consistencia de T8-A4 (sem validacao de fontes cientificas)."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from t8_a4_validar_v08 import read,validate,tokens

class TestT8A4(unittest.TestCase):
    def test_all_integrity(self): self.assertTrue(validate())
    def test_5_axes(self): self.assertEqual({x['axis'] for x in read('axial')},{f'AX{i:02d}' for i in range(1,6)})
    def test_5_propositions_preserved(self):
        p=read('props');self.assertEqual({x['proposition'] for x in p}, {f'P{i}' for i in range(1,6)})
        self.assertIn('NOT_DIRECTLY_TESTED', next(x for x in p if x['proposition']=='P5')['evidence_status'])
    def test_proposed_21_no_st017(self):
        ids={x['study_id'] for x in read('index')};self.assertEqual(len(ids),21);self.assertNotIn('ST017',ids);self.assertIn('ST022',ids)
    def test_15_reports_plus_suspended(self):
        inv=read('inventory');self.assertEqual(len(inv),16);self.assertEqual(sum(x['in_proposed_15']=='YES' for x in inv),15)
    def test_trace_claims_a3_sources(self):
        evid={x['evidence_id'] for x in read('a3evidence')};claims=read('trace')
        self.assertEqual(len(claims),15)
        self.assertTrue(all(tokens(x['a3_evidence_ids'])<=evid for x in claims))

if __name__=='__main__':unittest.main()
