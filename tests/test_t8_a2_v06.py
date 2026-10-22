from pathlib import Path
import unittest, csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'screening'

class TestT8A2v06(unittest.TestCase):
    def read(self, filename):
        with (DATA / filename).open(encoding='utf-8-sig', newline='') as fh:
            return list(csv.DictReader(fh))

    def test_six_candidates_and_c03_pending(self):
        rows = self.read('t8-a2-candidatos-e-alternativa-v0.6.csv')
        self.assertEqual(len(rows), 6)
        self.assertEqual({r['candidate_id'] for r in rows}, {f'T8-C{i:02d}' for i in range(1,7)})
        c03, c06 = rows[2], rows[5]
        self.assertEqual(c03['fulltext_status'], 'ABSTRACT_ONLY')
        self.assertEqual(c06['candidate_role'], 'ALTERNATE_PROPOSED_FOR_C03')
        self.assertEqual(c06['scopus_1419_membership'], 'UNRESOLVED')
        self.assertEqual(c06['study_ids_reserved'], 'ST022')

    def test_c06_evidence_separates_sources(self):
        rows = self.read('t8-a2-evidencias-c06-v0.6.csv')
        self.assertEqual(len(rows), 7)
        self.assertEqual({r['study_id'] for r in rows}, {'ST022'})
        self.assertEqual({r['evidence_owner'] for r in rows}, {'AUTHOR','EDITOR','REVIEW'})

    def test_c06_not_included_or_quality_scored(self):
        rows = self.read('t8-a2-codificacao-c06-v0.6.csv')
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['study'], 'ST022')
        self.assertEqual(rows[0]['final_inclusion'], 'NOT_DECIDED')
        self.assertEqual(rows[0]['qa_primary_status'], 'NOT_PERFORMED')
        self.assertEqual(rows[0]['researcher_check_status'], 'PENDING')

if __name__ == '__main__': unittest.main()
