# Semana 10 - Trabalho 08: auditoria de proveniência Scopus (v0.3)

**Data:** 22/10/2026  
**Disciplina:** Comunicação Científica - PPGI/UNIRIO  
**Professor:** Sean Siqueira  
**Projeto:** Vieses cognitivos humanos em julgamentos mediados por LLMs, com atenção a sistemas multiagentes.  
**Status:** AUDITORIA DE PROVENIÊNCIA INCOMPLETA POR AUSÊNCIA DA FONTE ORIGINAL; não equivale à entrega final de 15 reports.

## 1. Propósito

Confrontar os 5 candidatos da Semana 10 (Wave 2) com os **1.419 reports retidos para full-text** na busca Scopus de 16/09/2026, cuja existência e contagens estão documentadas em `docs/trabalho-3/mapeamento-selecao-estudos-primarios-v0.1.md`. Não alterar decisões do Trabalho 3 nem sobrescrever Trabalhos 6 e 7. O relatório v0.2 e a pré-codificação ST014–ST021 continuam sendo o material analítico de referência.

## 2. Fontes consultadas e limitação de acesso

- Arquivos montados da conversa e da Semana 10: **nenhum export de 1.419 reports**, 2.830 reports de screening ou outro CSV estruturado da busca definitiva foi encontrado.
- GitHub `andrecataldo/human-multi-llm-cognitive-bias-review`: consulta à documentação do Trabalho 3, `data/raw/`, `PROJECT_TREE.txt`, buscas por `scopus` e `RETAIN_FOR_FULL_TEXT`. Foram encontradas descrições e contagens, **não o conjunto de linhas retidas**.
- Google Drive conectado: pesquisa de arquivos por `Scopus`, `screening`, `1419`, `BUSCAS SCOPUS`, `triagem` e nomes de pastas possíveis. Foram localizados materiais da disciplina e PDFs de análise Scopus exploratória; **nenhum export identificável dos 1.419**.
- Biblioteca de arquivos do projeto e referência a trabalhos anteriores: documentos de checkpoint e gráficos exploratórios, **sem export de registros**.

**Regra de interpretação:** não encontrar o arquivo não significa que um DOI não tenha sido indexado na Scopus, nem que não tenha sido retido em 16/09/2026. Os cinco candidatos receberam estado **NOT_EVALUATED_SOURCE_UNAVAILABLE** (e não `NO_MATCH`). Não recriar os 1.419 a partir de buscas atuais ou de contagens agregadas.

## 3. Verificação bibliográfica realmente executada

Fonte de comparação disponível: `data/screening/semana10-inventario-15-reports-v0.2.csv` do kit v0.2, com 10 reports da Wave 1 e 5 candidatos da Wave 2; SHA-256 desta cópia: `c8e1604dcb51e9305ae0c1bd8bc078e840bc92663606931ebc2a945011885403`.

**Resultado reproduzível:** os 5 DOIs novos não colidem com os 10 DOIs da Wave 1. Isso prova apenas **não duplicação em relação àqueles dez**. Não há conclusão sobre pertencimento à amostra Scopus de 1.419.

| Candidato | DOI | Relacionamento aos 10 anteriores | Proveniência dos 1.419 | Elegibilidade do full-text |
|---|---|---|---|---|
| T8-C01 | `10.1145/3706598.3713133` | DOI distinto | **Não verificável** | Conferência humana pendente |
| T8-C02 | `10.1038/s41598-025-98378-1` | DOI distinto | **Não verificável** | Conferência humana pendente |
| T8-C03 | `10.1145/3772318.3790934` | DOI distinto | **Não verificável** | Texto integral pendente |
| T8-C04 | `10.1145/3772318.3791796` | DOI distinto | **Não verificável** | Conferência humana pendente |
| T8-C05 | `10.1126/science.aec8352` | DOI distinto | **Não verificável** | Conferência humana pendente |

A matriz CSV `data/screening/semana10-wave2-reconciliacao-status-v0.3.csv` codifica a mesma situação, um candidato por linha. Os resultados anteriores (10 REPORTS, 13 STUDY units) permanecem imutáveis; as 8 ST014–ST021 são uma **pré-codificação**, não um denominador final validado.

## 4. Script auditável preparado e testado

Arquivo: `scripts/reconciliar_scopus_wave2_v03.py`. Este script é mais restritivo que o `v0.2`: normaliza DOI e título, informa EID quando houver, classifica presença e **decisão de triagem separadamente**, gera CSV e manifesto com SHA-256, impede sobrescrita acidental do arquivo fonte e trata duplicações, discrepâncias de DOI e decisões não reconhecidas como eventos de auditoria.

**Opção A: CSV original dos 2.830 triados, com coluna de decisão (`RETAIN_FOR_FULL_TEXT` / `EXCLUDE` ou equivalente):**

```bash
python scripts/reconciliar_scopus_wave2_v03.py \
  --screening /CAMINHO/DO/ARQUIVO_ORIGINAL_2830.csv \
  --expected-count 2830 \
  --candidates data/screening/semana10-candidatos-wave2-v0.2.csv \
  --output data/screening/resultado-reconciliacao-scopus-wave2.csv
```

**Opção B: CSV original já filtrado EXCLUSIVAMENTE com os 1.419 retidos:**

```bash
python scripts/reconciliar_scopus_wave2_v03.py \
  --screening /CAMINHO/DO/ARQUIVO_ORIGINAL_1419.csv \
  --retained-only --expected-count 1419 \
  --candidates data/screening/semana10-candidatos-wave2-v0.2.csv \
  --output data/screening/resultado-reconciliacao-scopus-wave2.csv
```

**Não usar** `--retained-only` sobre o conjunto de 2.830 ou sobre um export bruto sem decisão de triagem: isso transformaria presenças bibliográficas em retenções fictícias.

A rotina grava `resultado-reconciliacao-scopus-wave2.csv` e `resultado-reconciliacao-scopus-wave2.audit.json`, que registra contagens, colunas lidas, hipótese `retained-only` e checksum SHA-256 do screening consultado. Ambos podem ser versionados como artefatos derivados, mas a fonte original permanece intacta. Este relatório **não contém resultado real de execução sobre os 1.419**.

### Interpretação dos resultados previstos

| Saída | Interpretação | Ação |
|---|---|---|
| `MATCH_RETAINED` com `EXACT_DOI` | Report encontrado com decisão de retenção documentada (ou arquivo verificado de retidos) | Prosseguir para full-text screening I1–I9 e conferência humana |
| `MATCH_RETAINED` com título | Há coincidência textual, mas DOI ausente na fonte | Checar EID e metadados antes de confirmar |
| `MATCH_EXCLUDED` | DOI/título encontrado, mas triagem original o excluiu | Registrar razão; não inverter decisão sem nova adjudicação documentada |
| `MATCH_DECISION_UNCLEAR` | Presença bibliográfica sem confirmação de retenção | Verificar código de decisão e linha original |
| `TITLE_MATCH_DOI_CONFLICT` | Título semelhante e DOI divergente | Corrigir metadados/versões manualmente |
| `AMBIGUOUS_MULTIPLE_RECORDS` | Mais de uma linha candidata na origem | Adjudicar duplicatas |
| `NOT_PRESENT_IN_SUPPLIED_EXPORT` | Não identificado no **arquivo fornecido** | Considerar emenda formal de busca complementar ou substituição por candidato comprovadamente retido; não inferir ausência global |

## 5. Checagens realizadas sem acesso aos 1.419

- Diferença de DOIs Wave 1 × Wave 2: **5 de 5 sem colisão** no inventário versionado v0.2.
- Código: **3 testes automatizados passaram** (retenção, exclusão, conflito de DOI, ausência, múltiplos registros, arquivo sem decisão e contagem errada). Eles utilizam **dados de teste**, não uma base real da Scopus.
- Base histórica: **10 REPORTS / 13 STUDY units**, preservados.
- Expansão: **5 REPORTS / 8 STUDY units propostos**, não homologados.
- Validação I9: o report T8-C03 ainda requer texto completo; os outros quatro têm pré-leitura documentada no v0.2, mas conferência humana ainda pendente.

## 6. Critério de fechamento acadêmico

1. Recuperar o **CSV/TSV Scopus original** dos 1.419 (ou 2.830 com decisões), guardar seu checksum e executar o script acima. Se a exportação original estiver em XLSX, exportar uma cópia CSV preservando o original.
2. Adjudicar matches ambíguos e candidatos não retidos. Quando vierem de canal complementar, registrar **emenda prospectiva** ao protocolo com fonte e data, nunca atribuir retroativamente à busca de 16/09.
3. Obter o texto integral de T8-C03 (ST017), aplicar I1–I9 e confirmar as unidades ST014–ST021, medidas e citações humanas. QAISER permanece apenas para **revisões secundárias**, não para esses studies primários.
4. Somente após a elegibilidade formal e auditoria dos cinco novos reports, atualizar `data/included/`, declarar o total `15 reports` (e contar estudos separadamente), editar a versão final do Trabalho 8 e preparar submissão ao Classroom.

**Conclusão:** o material v0.3 registra o bloqueio com precisão, entrega um procedimento replicável e evita alegar reconciliação onde só há inventário bibliográfico. Não foi feito commit, push ou alteração de artefatos anteriores.
