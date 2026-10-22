import csv, io, pathlib, subprocess, sys, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
SCREEN=ROOT/'data/screening'

def read(name):
    with (SCREEN/name).open(encoding='utf-8',newline='') as f:return list(csv.DictReader(f))

class TestT8A3(unittest.TestCase):
    def test_15_reports_and_suspended_exception(self):
        r=read('t8-a3-inventario-15-report-propostos-mais-suspenso-v0.7.csv')
        self.assertEqual(len(r),16)
        self.assertEqual(sum(x['in_proposed_15']=='YES' for x in r),15)
        self.assertEqual({x['report_id'] for x in r if x['in_proposed_15']=='NO'},{'T8-C03'})
    def test_21_unique_studies_exclude_st017_include_st022(self):
        r=read('t8-a3-indice-21-studies-propostas-v0.7.csv')
        self.assertEqual(len(r),21)
        self.assertEqual(len({x['study_id'] for x in r}),21)
        self.assertNotIn('ST017',{x['study_id'] for x in r})
        self.assertIn('ST022',{x['study_id'] for x in r})
        self.assertEqual(sum(x['source_layer']=='BASELINE_TRABALHO6_NOT_RECODED' for x in r),13)
    def test_quality_dimensions_are_explicit_and_preliminary(self):
        r=read('t8-a3-qa-primary-6-candidatos-v0.7.csv')
        self.assertEqual(len(r),60)
        for group in {x['report_id'] for x in r}:
            self.assertEqual({x['qa_code'] for x in r if x['report_id']==group},{f'QA{i}' for i in range(1,11)})
        self.assertTrue(all(x['rating'] in ('Y','PY','N','U','NA') for x in r))
        self.assertEqual({x['rating'] for x in r if x['report_id']=='T8-C03'},{'U'})
    def test_merge_with_synthetic_baseline(self):
        # Testar algoritmo de fusão, não alegar verificação dos dados originais do usuario.
        wave=SCREEN/'t8-a3-codificacao-wave2-selecionada-8-studies-v0.7.csv'
        with tempfile.TemporaryDirectory() as tmp:
            b=pathlib.Path(tmp)/'baseline.csv'; out=pathlib.Path(tmp)/'output.csv'
            with b.open('w',newline='',encoding='utf-8') as f:
                w=csv.DictWriter(f,fieldnames=['report','study','title','axis']);w.writeheader()
                # 13 unidades históricas, 10 reports distintos
                rep=['FT0070','FT0070','FT0072','FT0072','FT0080','FT0083','FT0310','FT0318','FT0545','FT0772','FT1222','FT1222','FT1233']
                for i,r in enumerate(rep,1):w.writerow({'report':r,'study':f'ST{i:03}','title':'fixture','axis':'AX05'})
            p=subprocess.run([sys.executable,str(ROOT/'scripts/t8_a3_consolidar_v07.py'),'--baseline',str(b),'--wave2',str(wave),'--output',str(out)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,msg=p.stderr+p.stdout)
            with out.open(encoding='utf-8') as f: result=list(csv.DictReader(f))
            self.assertEqual(len(result),21)
            self.assertNotIn('ST017',{x['study'] for x in result})
            p2=subprocess.run([sys.executable,str(ROOT/'scripts/t8_a3_consolidar_v07.py'),'--baseline',str(b),'--wave2',str(wave),'--output',str(out)],capture_output=True,text=True)
            self.assertNotEqual(p2.returncode,0) # safe no-overwrite

if __name__=='__main__':unittest.main()
