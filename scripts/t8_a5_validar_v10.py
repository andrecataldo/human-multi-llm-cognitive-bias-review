#!/usr/bin/env python3
"""Valida apenas consistência estrutural da minuta T8-A5; não é revisão por pares."""
import csv, pathlib, sys, json
ROOT=pathlib.Path(__file__).resolve().parents[1]
D=ROOT/'data'/'screening'

def load(n):
    with (D/n).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def validate():
    inv=load('t8-a5-registro-adjudicacao-16-reports-v1.0.csv')
    assert len(inv)==16, f'inventário tem {len(inv)} linhas, esperado 16'
    assert len({x['report_id'] for x in inv})==16
    assert sum(x['in_proposed_15']=='YES' for x in inv)==15
    susp=[x for x in inv if x['report_id']=='T8-C03']
    assert len(susp)==1 and susp[0]['in_proposed_15']=='NO'
    assert not any(x['status_decisao']=='FORMALMENTE_HOMOLOGADO' and x['report_id'].startswith('T8-C') for x in inv)
    idx=load('t8-a3-indice-21-studies-propostas-v0.7.csv')
    st=[x['study_id'] for x in idx]
    expected={f'ST{i:03d}' for i in list(range(1,17))+list(range(18,23))}
    assert len(st)==21 and len(set(st))==21 and set(st)==expected
    qa=load('t8-a3-qa-primary-6-candidatos-v0.7.csv')
    assert len(qa)==60 and len({x['report_id'] for x in qa})==6
    assert all(x['assessment_status']=='PRELIMINARY_NOT_HUMAN_ADJUDICATED' for x in qa)
    gates=load('t8-a5-checklist-fechamento-v1.0.csv')
    assert len(gates)==9 and all(x['confirmacao_executada']=='NAO' for x in gates)
    states=json.loads((D/'t8-a5-manifesto-estado-v1.0.json').read_text(encoding='utf-8'))
    assert states['analytical_working_set']['proposed_reports']==15
    assert states['supplementary_identification']['approved_new_reports']==0
    for fn in ('docs/trabalho-8/semana10-trabalho8-final-v1.0.md','docs/trabalho-8/t8-a5-fechamento-metodologico-v1.0.md'):
        assert (ROOT/fn).is_file(), f'ausente: {fn}'
    # Check referential integrity of studies in 15 report inventory.
    reportids={x['report_id'] for x in inv if x['in_proposed_15']=='YES'}
    assert {x['report_id'] for x in idx}==reportids
    print('T8-A5 v1.0: OK | 15 REPORTS propostos / 21 STUDIES propostos; C03 suspenso; 9 gates não homologados.')
    print('Atenção: testes de estrutura não aprovam AM-002, QA, elegibilidade nem conferência humana.')
    return True

if __name__=='__main__':
    try: validate()
    except (AssertionError, FileNotFoundError, KeyError, ValueError) as e:
        print(f'ERRO T8-A5: {e}',file=sys.stderr);sys.exit(1)
