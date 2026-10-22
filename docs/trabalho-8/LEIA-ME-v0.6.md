# T8-A2 — Complemento v0.6 (22/10/2026)

Pacote ADITIVO para a raiz do repositório `human-multi-llm-cognitive-bias-review/`. Não altera versões anteriores e **não representa inclusão final**.

## Instalação

```bash
cd ~/projects/human-multi-llm-cognitive-bias-review
unzip -n ~/Downloads/t8-a2-pendencias-e-alternativa-v0.6.zip -d .
python -m unittest discover -s tests -p 'test_t8_a2_v06.py' -v
git status
git diff --check
```

## Arquivos

- `docs/trabalho-8/t8-a2-pendencias-e-alternativa-v0.6.md` — decisão proposta, origem, gates e análise científica preliminar.
- `data/screening/t8-a2-candidatos-e-alternativa-v0.6.csv` — seis candidatos em paralelo, **não seis incluídos**.
- `data/screening/t8-a2-evidencias-c06-v0.6.csv` — evidências primárias e interpretação da revisão separadas.
- `data/screening/t8-a2-codificacao-c06-v0.6.csv` — estudo ST022 proposto, sem reuso do código ST017.
- `tests/test_t8_a2_v06.py` — teste de integridade estrutural das matrizes.

Não versionar texto integral protegido de editora. O artigo T8-C06 é open access, mas os artefatos versionados se limitam a metadados e paráfrases.

## Nota metodológica

`protocol/amendments.md` e `protocol/decision-log.md` **não foram editados**: AM-002/SD-021 permanecem *propostas* até deliberação. Não publicar os 15 artigos como incluídos, nem dizer que os seis estão comprovados no screening da Scopus.
