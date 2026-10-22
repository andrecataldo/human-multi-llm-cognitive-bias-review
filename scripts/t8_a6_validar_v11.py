#!/usr/bin/env python3
"""Valida a integridade estrutural da entrega T8-A6 v1.1; NÃO valida evidências científicas."""
from pathlib import Path
import csv

def read_csv(p):
    with Path(p).open(encoding='utf-8-sig',newline='') as h:
        return list(csv.DictReader(h))

def validate(root=Path('.')):
    root=Path(root)
    assert (root/'docs/trabalho-8/semana10-trabalho8-final-v1.1.md').is_file()
    text=(root/'docs/trabalho-8/semana10-trabalho8-final-v1.1.md').read_text(encoding='utf-8')
    assert '15 publicações' in text or '15 REPORTS' in text
    assert 'não' in text.lower() and 'ST017' in text
    assert (root/'docs/trabalho-8/t8-a6-mensagem-classroom-v1.1.md').is_file()
    assert (root/'docs/trabalho-8/t8-a6-encerramento-metodologico-v1.1.md').is_file()
    ledger=read_csv(root/'data/screening/t8-a5-registro-adjudicacao-16-reports-v1.0.csv')
    assert len(ledger)==16, f'Ledger deve ter 16 reports, teve {len(ledger)}'
    hist=[x for x in ledger if x['review_track'].startswith('WAVE1')]
    props=[x for x in ledger if x['in_proposed_15']=='YES' and x['review_track'].startswith('WAVE2')]
    suspended=[x for x in ledger if x['in_proposed_15']=='NO']
    assert len(hist)==10 and len(props)==5 and len(suspended)==1, (len(hist),len(props),len(suspended))
    assert {r['report_id'] for r in props} == {'T8-C01','T8-C02','T8-C04','T8-C05','T8-C06'}
    assert suspended[0]['report_id']=='T8-C03'
    u=[]
    for x in hist+props:
        u.extend(x['study_ids'].split(';'))
    assert len(u)==21 and len(set(u))==21, (len(u),len(set(u)))
    assert 'ST017' not in u and 'ST022' in u
    gates=read_csv(root/'data/screening/t8-a6-gates-revisados-v1.1.csv')
    assert {x['gate'] for x in gates}=={f'G{i:02d}' for i in range(1,10)}
    states={x['gate']:x['status_t8_a6'] for x in gates}
    assert states['G01']=='ABERTO' and states['G08']=='ABERTO'
    assert states['G09']=='PREPARADO_NAO_SUBMETIDO'
    sources=read_csv(root/'data/screening/t8-a6-verificacoes-fonte-v1.1.csv')
    assert len(sources)>=5
    check=read_csv(root/'data/screening/t8-a5-checklist-fechamento-v1.0.csv')
    assert len(check)==9
    print('T8-A6 v1.1 — validação estrutural OK')
    print('Históricos: 10 REPORTS | Candidatos principais: 5 REPORTS | Suspenso: 1 REPORT')
    print('STUDIES no conjunto proposto: 21 | ST017 não incluída')
    print('G01 e G08 ainda abertos; G09 preparado/não submetido')
    return {'reports_historicos':10,'reports_adicionais_propostos':5,'estudos_propostos':21,'suspensos':1}

if __name__=='__main__':
    validate()
