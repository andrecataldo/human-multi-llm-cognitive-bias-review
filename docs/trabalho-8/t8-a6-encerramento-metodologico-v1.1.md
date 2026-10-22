# T8-A6.1 - Encerramento metodológico e revisão final da entrega (v1.1)

**Data:** 22/10/2026  
**Curso:** Comunicação Científica - PPGI/UNIRIO - Prof. Sean Siqueira  
**Estado:** `DOCUMENTACAO_DE_ENTREGA_REVISADA / HOMOLOGACAO_CIENTIFICA_PENDENTE`  
**Base rastreada:** T8-A5 v1.0, commit `630400f`, mais a T8-A3 v0.7 e a síntese T8-A4 v0.8.

## 1. Propósito

Conferir os nove gates originalmente registrados no arquivo `data/screening/t8-a5-checklist-fechamento-v1.0.csv`, preservar decisões anteriores e publicar uma **versão de submissão com limitações explícitas**, sem apresentar o número-alvo de 15 reports como resultado metodologicamente homologado. **Nenhum status do protocolo oficial foi alterado.**

## 2. O que foi verificado nesta etapa

1. **Histórico imutável:** a Scopus de 16/09/2026 gerou 3.365 ocorrências, 3.256 reports únicos, 2.830 reports triados e 1.419 retidos para leitura integral; Wave 1 manteve **10 reports/13 estudos**. Fonte: `docs/trabalho-3/mapeamento-selecao-estudos-primarios-v0.1.md`.
2. **Conjunto complementar:** cinco candidatos de análise (C01, C02, C04, C05, C06), com oito unidades (ST014–ST016, ST018–ST022). São **15 reports/21 studies propostos**, não 15 incluídos. Fonte: T8-A3 v0.7 e T8-A5 v1.0.
3. **Suspensão explícita:** C03/ST017 não integra as contagens; o DOI da publicação é verificável em DBLP, mas o texto integral não foi recuperado na etapa. Não inventar o resultado de seu screening de full-text; manter status `SUSPENDED_I9_UNVERIFIED`.
4. **C06:** artigo de Bean et al. publicamente disponível em *Nature Medicine*; correção editorial de 17/04/2026 confirmou retificação de rótulos da Fig. 2a. **Não** há teste diretamente operacionalizado de ancoragem ou confirmação. I5 carece de adjudicação.
5. **C05:** página do artigo de Cheng et al. em *Science* confirma três experimentos com pessoas, N total=2.405; não se deve contar a análise *model-only* como quarto estudo humano nem converter intenção de reparação em comportamento observado.
6. **Qualidade:** a matriz QA-Primary disponível contém 60 avaliações preliminares (6 candidatos × 10 questões, incluindo C03 suspenso), **sem** reavaliação dos dez históricos; uma afirmação geral de QA do corpus seria incorreta.
7. **Registro de decisões:** AM-002, SD-021 e SD-022 continuam `PROPOSED`, pois ainda não houve manifestação específica do pesquisador aprovando a emenda, os critérios e cada inclusão.

### Fontes complementares consultadas nesta checagem

- C03 - DBLP: <https://dblp.dagstuhl.de/rec/conf/chi/LiPLXZJMC26.html>; ResearchGate: <https://www.researchgate.net/publication/403752328_Does_Sycophancy_Change_Decisions_Effect_of_LLM_Sycophancy_on_AI-Assisted_Decision-Making> (indica necessidade de solicitar PDF integral).
- C06 - artigo original: <https://doi.org/10.1038/s41591-025-04074-y>; correção editorial: <https://doi.org/10.1038/s41591-026-04404-8>; texto completo: <https://pmc.ncbi.nlm.nih.gov/articles/PMC12920132/>.
- C05 - artigo editorial: <https://doi.org/10.1126/science.aec8352>; registro bibliográfico e abstract: <https://pubmed.ncbi.nlm.nih.gov/41886588/>.

**Nota de origem:** conferências bibliográficas realizadas agora **não reconstruíram a estratégia de busca complementar do início de outubro** e **não** comprovam presença dos cinco artigos entre os 1.419 do Scopus. Datas/termos originais desconhecidos foram marcados `NOT_DOCUMENTED`, sem preencher lacunas por inferência.

## 3. Revisão dos nove gates (sem substituição do checklist v1.0)

| Gate | Situação da entrega em 22/10 | Entendimento | Próximo responsável |
| --- | --- | --- | --- |
| G01 - proveniência | **ABERTO** | Export Scopus indisponível; AM-002 ainda proposta. | Pesquisador |
| G02 - trilha complementar | **PARCIAL** | DOIs e fontes bibliográficas conhecidos; faltam strings, data da identificação e fluxo auditável completo. | Pesquisador |
| G03 - elegibilidade I1–I9 | **ABERTO** | Cinco reports avaliados preliminarmente; nenhum novo homologado; I5 de C06 requer fundamento. | Pesquisador |
| G04 - C03 | **RESOLVIDO APENAS PARA O CONJUNTO DE TRABALHO** | C03 fora dos 15 propostos e ST017 reservado; I9 continua não verificado. | Pesquisa futura, se C03 retornar |
| G05 - evidência | **ABERTO** | Localizadores e matrizes existentes; conferência humana dos oito novos estudos pendente. | Pesquisador |
| G06 - QA-Primary dos candidatos | **ABERTO** | 60 avaliações preliminares, sem adjudicação humana. | Pesquisador |
| G07 - QA dos históricos | **CONDICIONAL / NÃO APLICÁVEL À AFIRMAÇÃO ATUAL** | Esta entrega NÃO afirma avaliação QA completa dos 15; executar se essa alegação for introduzida. | Pesquisador |
| G08 - inclusão/promover dados | **ABERTO** | Ninguém promoveu os cinco a `data/included/` por ausência de homologação. | Pesquisador |
| G09 - submissão | **PREPARADO, NÃO SUBMETIDO** | Há mensagem do Classroom e documento v1.1, mas falta validar push e optar pela entrega transparente. | Aluno |

A situação de G04 não representa acesso ao texto integral de C03. A situação condicional de G07 não prova qualidade dos históricos. O estado G09 não registra envio ao Classroom.

## 4. Proposta AM-002 e decisões SD-021/022: ainda NÃO aprovadas

**AM-002 (PROPOSED):** permitir identificação complementar dirigida como **trilha separada** da seleção Scopus de setembro, com fluxo, datas, fontes, registros e razões de inclusão próprios; a ausência do export não autoriza informar que os cinco já pertenciam aos 1.419. Se a estratégia de identificação inicial não puder ser recuperada retrospectivamente, registrar esta limitação e, se necessário, executar nova busca documentada prospectivamente.

**SD-021 (PROPOSED):** manter C03/ST017 suspenso e avaliar C06/ST022 como substituto, sem reaproveitar IDs; aceitar C06 só após decisão justificada sobre I5.

**SD-022 (PROPOSED):** relatar contagens históricas e complementares separadamente; distinguir `REPORT`, `STUDY`, `CANDIDATE`, `INCLUDED`, `AI_ASSISTED` e `RESEARCHER_VALIDATED`.

**Condição de aprovação:** decisão inequívoca do pesquisador, lançamento prospectivo em `protocol/amendments.md` e `protocol/decision-log.md`, conferência I1–I9 por report, checagem de duplicação e promoção controlada dos registros. Esta T8-A6 **não** faz isso automaticamente.

## 5. Verificações possíveis sem o export

- Deduplicação **parcial**: DOIs dos cinco propostos diferentes dos dez históricos, conforme inventário. Não implica deduplicação completa contra os 1.419.
- Localizadores: DOI e texto integral acessível em fontes de quatro candidatos e de C06; QA inicial e trilhas já descritas; falta checagem humana sistemática.
- C06: retificação de Fig. 2a verificada diretamente na página da editora; não alterar artificialmente estimativas de efeito.
- Número de unidades: 13 históricas + 8 adicionais = 21; ST017 não integra esse conjunto.
- Limite epistêmico: P5, a hipótese de *corroboração aparente*, não é diretamente testada nos 21 estudos propostos.

**Não foi possível executar:** correspondência linha a linha com 1.419; adjudicação independente; QA-Primary definitivo; inclusão formal de C06; reconstrução verificável da história de busca dirigida; submissão real no Classroom.

## 6. Arquivos que devem permanecer intocados

- `docs/trabalho-3/mapeamento-selecao-estudos-primarios-v0.1.md`
- `docs/trabalho-6/` e `data/included/codificacao-semana-08-13-studies-v0.1.csv`
- `docs/trabalho-7/`
- `protocol/amendments.md` e `protocol/decision-log.md` enquanto AM-002 / SD-021 / SD-022 não forem explicitamente aprovadas

**Status final T8-A6.1:** documentação de fechamento metodológico conferida; decisões de inclusão científica permanecem abertas.
