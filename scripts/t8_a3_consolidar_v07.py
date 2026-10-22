#!/usr/bin/env python3
"""T8-A3 v0.7: une as 13 linhas históricas do Trabalho 6 às 8 linhas propostas, sem editar as fontes.

Não substitui adjudicação e não modifica data/included/.
"""
import argparse, csv, pathlib, sys

def read_csv(p):
    with p.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def main(argv=None):
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('--baseline',default='data/included/codificacao-semana-08-13-studies-v0.1.csv')
    a.add_argument('--wave2',default='data/screening/t8-a3-codificacao-wave2-selecionada-8-studies-v0.7.csv')
    a.add_argument('--output',default='data/screening/t8-a3-codificacao-integrada-21-studies-v0.7.csv')
    a.add_argument('--force',action='store_true',help='Sobrescrever somente arquivo DERIVADO indicado por --output')
    args=a.parse_args(argv)
    baseline,wave2,output=map(pathlib.Path,(args.baseline,args.wave2,args.output))
    if output.resolve() in (baseline.resolve(),wave2.resolve()):
        raise SystemExit('ERROR: --output aponta para arquivo de origem; recusado')
    if output.exists() and not args.force:raise SystemExit(f'ERROR: {output} ja existe; use --force apos conferir')
    b,w=read_csv(baseline),read_csv(wave2)
    if len(b)!=13 or len(w)!=8:raise SystemExit(f'ERROR: Esperado baseline 13 e wave2 8, recebido {len(b)} e {len(w)}')
    for name,part in (('baseline',b),('wave2',w)):
        if not {'report','study','title','axis'}.issubset(part[0]): raise SystemExit(f'ERROR: faltam colunas em {name}')
    if {'ST017'} & {r['study'] for r in w}:raise SystemExit('ERROR: ST017 suspenso nao pode integrar proposta')
    ids=[r['study'] for r in b+w]
    if len(set(ids))!=21 or set(ids)!={f'ST{i:03}' for i in range(1,17)}|{f'ST{i:03}' for i in range(18,23)}:
        raise SystemExit('ERROR: IDs duplicados ou diferente do registro 21 sem ST017')
    reports={r['report'] for r in b+w}
    if len(reports)!=15: raise SystemExit(f'ERROR: reports propostos: {len(reports)} (esperado 15)')
    fields=list(dict.fromkeys(k for r in b+w for k in r.keys()))
    fields+=['cohort','publication_status','researcher_check_status_t8a3']
    out=[]
    for r in b:
        out.append({**r,'cohort':'WAVE1_HISTORICAL','publication_status':'INCLUDED_WAVE1_DOCUMENTED','researcher_check_status_t8a3':'HISTORICAL_CHECK_PENDING'})
    for r in w:
        out.append({**r,'cohort':'WAVE2_PROPOSED','publication_status':'NOT_INCLUDED_FINAL','researcher_check_status_t8a3':'PENDING'})
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('w',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(out)
    print(f'OK: {len(out)} study units em {len(reports)} reports PROPOSTOS; {output}')
    return 0
if __name__=='__main__':sys.exit(main())
