#!/usr/bin/env python3
"""Reconciliação bibliográfica da Wave 2 contra export *original* de triagem Scopus.

Nunca presume que encontrar um DOI significa inclusão. Não altera o arquivo de origem.
A saída é bibliográfica (não é avaliação de qualidade ou elegibilidade I1–I9).

Exemplos:
  python scripts/reconciliar_scopus_wave2_v03.py \
    --screening data/screening/original-scopus-2830.csv \
    --candidates data/screening/semana10-candidatos-wave2-v0.2.csv \
    --output data/screening/match-wave2-real.csv

  python scripts/reconciliar_scopus_wave2_v03.py \
    --screening data/screening/original-scopus-1419-retained.csv \
    --retained-only --expected-count 1419 \
    --candidates data/screening/semana10-candidatos-wave2-v0.2.csv \
    --output data/screening/match-wave2-real.csv
"""
import argparse
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

DOI_ALIASES = ('doi', 'digital object identifier', 'digital_object_identifier')
TITLE_ALIASES = ('title', 'document title', 'article title', 'dc.title')
STATUS_ALIASES = ('decision', 'final decision', 'final_decision', 'screening decision', 'screening_decision', 'screening status', 'screening_status', 'status', 'decisao final')
EID_ALIASES = ('eid', 'scopus eid', 'scopus_id', 'record_id')
RETAIN = {'retainforfulltext', 'retainedforfulltext', 'retain', 'retained', 'include', 'included', 'includereport', 'fulltext', 'eligible', 'keep'}
EXCLUDE = {'exclude', 'excluded', 'reject', 'rejected', 'noteligible', 'remove', 'removed'}


def ascii_text(value):
    txt = unicodedata.normalize('NFKD', str(value or ''))
    return ''.join(c for c in txt if not unicodedata.combining(c))


def key(value):
    return re.sub(r'[^a-z0-9]+', '', ascii_text(value).lower())


def norm_doi(value):
    value = str(value or '').strip().lower()
    value = re.sub(r'^https?://(?:dx\.)?doi\.org/', '', value)
    value = re.sub(r'^doi\s*:\s*', '', value)
    value = value.split('?')[0]
    return value.strip(' .;')


def norm_title(value):
    return re.sub(r'[^a-z0-9]+', ' ', ascii_text(value).lower()).strip()


def get_col(headers, aliases):
    by_key = {key(h): h for h in headers if h is not None}
    return next((by_key[key(a)] for a in aliases if key(a) in by_key), None)


def rows_of(path):
    with path.open(encoding='utf-8-sig', newline='') as inp:
        sample = inp.read(65536)
        inp.seek(0)
        if not sample.strip():
            raise ValueError(f'Arquivo vazio: {path}')
        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=',;\t')
        except csv.Error:
            dialect = csv.excel
        reader = csv.DictReader(inp, dialect=dialect)
        heads = reader.fieldnames or []
        if len(heads) < 2:
            raise ValueError(f'CSV inválido ou delimitador não reconhecido: {path}')
        records = list(reader)
    return heads, records


def decision(raw, retained_only):
    if retained_only:
        return 'RETAINED_CONFIRMED_BY_SOURCE_SCOPE'
    if raw is None or not str(raw).strip():
        return 'DECISION_NOT_REPORTED'
    val = key(raw)
    if val in RETAIN:
        return 'RETAINED_EXPLICIT_DECISION'
    if val in EXCLUDE:
        return 'EXCLUDED_EXPLICIT_DECISION'
    return 'UNRECOGNIZED_DECISION'


def process(screening_path, candidate_path, retained_only=False, expected_count=None):
    sh, base = rows_of(screening_path)
    ch, cand = rows_of(candidate_path)
    if not base or not cand:
        raise ValueError('Arquivo de screening ou candidatos sem linhas')
    if expected_count is not None and len(base) != expected_count:
        raise ValueError(f'Contagem incompatível: esperado {expected_count}; encontrado {len(base)}. Corrija a origem, sem ajustar o número artificialmente.')
    sd, st, ss, se = (get_col(sh, aliases) for aliases in (DOI_ALIASES, TITLE_ALIASES, STATUS_ALIASES, EID_ALIASES))
    cd, ct = get_col(ch, DOI_ALIASES), get_col(ch, TITLE_ALIASES)
    ci = get_col(ch, ('candidate_id', 'id', 'report_id'))
    if not (sd or st) or not (cd or ct):
        raise ValueError('Títulos/DOIs não identificados nos dois arquivos; confira cabeçalhos.')
    if not ss and not retained_only:
        raise ValueError('O screening não informa decisão. Se o CSV contém APENAS os 1419 retidos, execute com --retained-only --expected-count 1419; caso contrário, forneça coluna de decisão.')
    if not ci:
        raise ValueError('Arquivo de candidatos sem candidate_id/report_id')
    by_doi = defaultdict(list)
    by_title = defaultdict(list)
    for i, row in enumerate(base):
        if sd and norm_doi(row.get(sd)):
            by_doi[norm_doi(row[sd])].append(i)
        if st and norm_title(row.get(st)):
            by_title[norm_title(row[st])].append(i)
    out=[]
    for c in cand:
        doi, title = norm_doi(c.get(cd) if cd else ''), norm_title(c.get(ct) if ct else '')
        matches = by_doi.get(doi, []) if doi else []
        method = 'EXACT_DOI' if matches else ''
        if not matches and title:
            matches = by_title.get(title, [])
            method = 'EXACT_NORMALIZED_TITLE' if matches else ''
        result = {'candidate_id':c.get(ci, ''),'doi':c.get(cd, '') if cd else '',
                  'title':c.get(ct,'') if ct else '', 'match_method':method,
                  'match_status':'', 'decision_interpretation':'',
                  'scopus_eid':'', 'decision_raw':'', 'note':''}
        if len(matches) > 1:
            result['match_status'] = 'AMBIGUOUS_MULTIPLE_RECORDS'
            result['note'] = 'Examinar colisões/duplicatas Scopus manualmente'
        elif not matches:
            result['match_status'] = 'NOT_PRESENT_IN_SUPPLIED_EXPORT'
            result['note'] = 'Não demonstra ausência do artigo na Scopus ou na literatura'
        else:
            b=base[matches[0]]
            base_doi = norm_doi(b.get(sd)) if sd else ''
            result['scopus_eid'] = b.get(se,'') if se else ''
            result['decision_raw'] = b.get(ss,'') if ss else ''
            if method == 'EXACT_NORMALIZED_TITLE' and doi and base_doi and doi != base_doi:
                result['match_status'] = 'TITLE_MATCH_DOI_CONFLICT'
                result['decision_interpretation'] = 'MANUAL_CHECK_REQUIRED'
                result['note'] = f'DOI de origem diferente: {base_doi}'
            else:
                status = decision(result['decision_raw'], retained_only)
                result['decision_interpretation'] = status
                result['match_status'] = ('MATCH_RETAINED' if status.startswith('RETAINED_')
                                           else 'MATCH_EXCLUDED' if status == 'EXCLUDED_EXPLICIT_DECISION'
                                           else 'MATCH_DECISION_UNCLEAR')
                if method == 'EXACT_NORMALIZED_TITLE':
                    result['note']='Match por título requer conferência humana (DOI faltante em uma das fontes)'
        out.append(result)
    sha = hashlib.sha256(screening_path.read_bytes()).hexdigest()
    metadata = {'input_file':str(screening_path), 'screening_sha256':sha,
                'input_records':len(base), 'candidate_records':len(cand),
                'assumption_retained_only':retained_only, 'decision_column':ss,
                'doi_column':sd,'title_column':st,'eid_column':se,
                'counts':dict(Counter(x['match_status'] for x in out)),
                'interpretation':'Bibliographic matching only. Not a full-text inclusion or independent quality appraisal.'}
    return out, metadata


def main():
    ap=argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--screening',type=Path,required=True)
    ap.add_argument('--candidates',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--retained-only',action='store_true',help='Declaração explícita: entrada contém APENAS itens retidos')
    ap.add_argument('--expected-count',type=int,help='Falha se número de linhas da fonte for diferente')
    ap.add_argument('--force',action='store_true',help='Permite sobrescrever apenas as saídas, nunca inputs')
    args=ap.parse_args()
    if args.screening.resolve()==args.output.resolve() or args.candidates.resolve()==args.output.resolve():
        ap.error('Não é permitido sobrescrever arquivo de origem')
    manifest=args.output.with_suffix('.audit.json')
    if not args.force and (args.output.exists() or manifest.exists()):
        ap.error('Saída já existe. Escolha outro caminho ou use --force')
    try:
        out, meta=process(args.screening,args.candidates,args.retained_only,args.expected_count)
    except (OSError,ValueError) as exc:
        ap.error(str(exc))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(out[0].keys()))
        writer.writeheader();writer.writerows(out)
    manifest.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'records':meta['input_records'], 'candidate_matches':meta['counts'], 'audit_json':str(manifest)},ensure_ascii=False))

if __name__=='__main__':
    main()
