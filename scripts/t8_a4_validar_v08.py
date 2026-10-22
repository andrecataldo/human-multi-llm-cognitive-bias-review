#!/usr/bin/env python3
"""Validacao estrutural de T8-A4 v0.8; nao valida achados cientificos."""
from pathlib import Path
import csv

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'/'screening'
FILES={
    'axial':'t8-a4-matriz-axial-v0.8.csv',
    'comparison':'t8-a4-comparacao-constante-v0.8.csv',
    'props':'t8-a4-proposicoes-p1-p5-v0.8.csv',
    'rq':'t8-a4-matriz-rq-v0.8.csv',
    'trace':'t8-a4-rastreabilidade-afirmacoes-v0.8.csv',
    'index':'t8-a3-indice-21-studies-propostas-v0.7.csv',
    'inventory':'t8-a3-inventario-15-report-propostos-mais-suspenso-v0.7.csv',
    'a3evidence':'t8-a3-trilha-evidencias-provisoria-v0.7.csv',
}

def read(k):
    with (DATA/FILES[k]).open(encoding='utf-8-sig',newline='') as f:
        return list(csv.DictReader(f))

def tokens(value):
    return {v.strip() for v in value.replace('/', ';').split(';') if v.strip()}

def validate():
    d={k:read(k) for k in FILES}
    assert {r['axis'] for r in d['axial']} == {f'AX{i:02d}' for i in range(1,6)}
    assert {r['proposition'] for r in d['props']} == {f'P{i}' for i in range(1,6)}
    assert {r['rq'] for r in d['rq']} == {f'RQ{i}' for i in range(1,7)}
    assert len(d['comparison'])==9 and len({r['contrast_id'] for r in d['comparison']})==9
    assert len(d['trace'])==15 and len({r['claim_id'] for r in d['trace']})==15
    idx={r['study_id'] for r in d['index']}
    expected={f'ST{i:03d}' for i in list(range(1,17))+list(range(18,23))}
    assert idx==expected and 'ST017' not in idx
    proposed=[r for r in d['inventory'] if r['in_proposed_15']=='YES']
    assert len(proposed)==15 and len(d['inventory'])==16
    evidence_ids={r['evidence_id'] for r in d['a3evidence']}
    axes={r['axis'] for r in d['axial']}
    for domain in ['axial','comparison','props','rq','trace']:
        for row in d[domain]:
            for col in ('baseline','expansion','study_ids','wave1_study_ids','wave2_study_ids'):
                if col in row:
                    missing=tokens(row[col])-idx
                    assert not missing,(domain,col,missing)
            for col in ('axes','axis'):
                if col in row:
                    missing=tokens(row[col])-axes
                    assert not missing,(domain,col,missing)
            for col in ('evidence_refs','a3_evidence_ids'):
                if col in row:
                    missing=tokens(row[col])-evidence_ids
                    assert not missing,(domain,col,missing)
    assert 'NOT_DIRECTLY_TESTED' in next(x for x in d['props'] if x['proposition']=='P5')['evidence_status']
    assert all(r['researcher_validation']=='PENDING_HUMAN_SOURCE_CHECK' for r in d['trace'])
    print('T8-A4: validacao estrutural OK; 5 AX, 9 comparacoes, 5 P, 6 RQ, 15 afirmacoes; base 15 REPORTS/21 STUDIES PROPOSTOS.')
    return True

if __name__=='__main__':validate()
