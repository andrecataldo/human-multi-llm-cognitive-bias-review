#!/usr/bin/env python3
"""Confronta cinco candidatos Wave2 com um export Scopus de full-text screening.

Uso:
 python scripts/reconciliar_scopus_wave2.py --screening /caminho/scopus_retidos.csv \
     --candidates data/screening/semana10-candidatos-wave2-v0.2.csv \
     --output data/screening/reconciliacao-scopus-wave2.csv

* Não modifica fonte, não assume que todo registro no export foi retido.
* Match exact DOI; fallback título exato normalizado só quando DOI indisponível.
* Necessário passar export dos RETAIN_FOR_FULL_TEXT, ou screening com coluna decisão.
"""
import argparse
import csv
import re
import unicodedata
from pathlib import Path

DOI_KEYS = ('doi', 'digital object identifier')
TITLE_KEYS = ('title', 'document title', 'article title', 'dc.title')
DECISION_KEYS = ('decision', 'final_decision', 'screening_decision', 'status', 'screening_status')
ID_KEYS = ('eid', 'scopus eid', 'id', 'record_id')

def canon(s):
    s = unicodedata.normalize('NFKD', str(s or ''))
    s = ''.join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r'\s+', ' ', s.strip().lower())

def doi(s):
    s = canon(s)
    s = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', s)
    s = re.sub(r'^doi\s*:\s*', '', s)
    return s.strip(' .;')

def title(s):
    return re.sub(r'[^a-z0-9]+', ' ', canon(s)).strip()

def get(row, aliases):
    keys = {canon(k): k for k in row}
    for alias in aliases:
        if alias in keys:
            return row[keys[alias]]
    return ''

def read_csv(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        sample = f.read(65536)
        f.seek(0)
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=',;\t')
        except csv.Error:
            dialect = csv.excel
        return list(csv.DictReader(f, dialect=dialect))

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--screening', required=True)
    ap.add_argument('--candidates', required=True)
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    base = read_csv(args.screening)
    cand = read_csv(args.candidates)
    if not base: raise SystemExit('Export de screening vazio')
    if not cand: raise SystemExit('Candidatos vazios')
    di, ti = {}, {}
    for idx, row in enumerate(base):
        kdoi = doi(get(row, DOI_KEYS)); kt = title(get(row, TITLE_KEYS))
        if kdoi: di.setdefault(kdoi, []).append(idx)
        if kt: ti.setdefault(kt, []).append(idx)
    out=[]
    for c in cand:
        kdoi = doi(c.get('doi')); kt=title(c.get('title'))
        match = di.get(kdoi,[]) if kdoi else []
        method = 'EXACT_DOI' if match else ''
        if not match and kt:
            match=ti.get(kt,[])
            method='EXACT_NORMALIZED_TITLE' if match else ''
        if len(match)==1:
            b=base[match[0]]
            outcome='MATCH_SINGLE'
            baseid=get(b,ID_KEYS)
            bdecision=get(b,DECISION_KEYS)
        elif len(match)>1:
            outcome='AMBIGUOUS_MULTIPLE'; baseid=''; bdecision=''
        else:
            outcome='NO_MATCH'; baseid=''; bdecision=''
        out.append({'candidate_id':c.get('candidate_id',''), 'doi':c.get('doi',''),
                    'match_status':outcome, 'match_method':method,
                    'scopus_id':baseid,'decision_in_export':bdecision,
                    'note':'Matching is not an eligibility or retained-status decision'})
    p=Path(args.output); p.parent.mkdir(parents=True, exist_ok=True)
    with open(p,'w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f, fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    print(f'{len(out)} candidatos; {sum(x["match_status"]=="MATCH_SINGLE" for x in out)} match único; {sum(x["match_status"]=="NO_MATCH" for x in out)} sem match.')
    print('Confira a decisão de screening do export: match bibliográfico não implica inclusão.')
if __name__ == '__main__': main()
