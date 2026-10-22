# T8-A2 — Revisão de elegibilidade e codificação da Wave 2 (v0.5)

**Data de verificação:** 22/10/2026  
**Disciplina:** Comunicação Científica — PPGI/UNIRIO; professor Sean Siqueira  
**Projeto:** Vieses cognitivos humanos em julgamentos mediados por LLMs, com atenção a sistemas multiagentes.  
**Status:** **T8-A2 — execução parcial auditada, NÃO conclusão da entrega de 15 REPORTS.**

## 1. Objetivo e escopo

Continuar o Trabalho 6, sem reabrir o Trabalho 7, verificando as cinco novas publicações da Wave 2 (`T8-C01..T8-C05`) e as oito unidades empíricas propostas (`ST014..ST021`). A referência para I1–I9 é `docs/trabalho-3/mapeamento-selecao-estudos-primarios-v0.1.md`, seção 7 — **não** `methodology/inclusion-exclusion.md`, que no repositório descreve critérios de estudos *secundários*. As 13 unidades ST001–ST013 do Trabalho 6 e os 10 REPORTS da Wave 1 permanecem intactos.

**Distinções essenciais:** REPORT = publicação; STUDY = experimento/estudo empírico dentro de uma publicação; 15 REPORTS não são 15 STUDIES. SEGRESS orienta o *relato* da revisão; codificação aberta/axial inspirada em Grounded Theory e procedimentos específicos são **decisões próprias do estudo**, não passos prescritos pelo SEGRESS. QAISER só vale para estudos secundários; eventual avaliação de qualidade destes primários requer QA-Primary v0.1 e conferência humana.

## 2. Fontes efetivamente usadas

- Registro histórico e protocolo primário: `docs/trabalho-3/mapeamento-selecao-estudos-primarios-v0.1.md`; o GitHub registra **2.830** reports triados, **1.419** retidos para full text, **10 REPORTS / 13 STUDIES** incluídos na Wave 1.
- Artefatos da Semana 10 já preparados: `semana10-trabalho8-expansao-auditada-v0.2.md`, `semana10-t8-auditoria-proveniencia-v0.3.md`, `codificacao-wave2-8-studies-v0.2.csv`, `evidencias-wave2-v0.2.csv` e candidatos v0.2.
- **T8-C01:** artigo publicado na ACM, DOI `10.1145/3706598.3713133` (`https://doi.org/10.1145/3706598.3713133`) e manuscrito completo dos autores `https://arxiv.org/html/2502.11919`.
- **T8-C02:** manuscrito final open access no PubMed Central `https://pmc.ncbi.nlm.nih.gov/articles/PMC12015287/`, DOI `10.1038/s41598-025-98378-1`; a versão principal foi identificada e seus resultados conferidos.
- **T8-C03:** título, autores, venue/DOI `10.1145/3772318.3790934` confirmados no DBLP (`https://dblp.org/rec/conf/chi/LiPLXZJMC26`); resumo do autor indexado em `https://pgl.jp/papers/69dcad7555a355001e0741de`; **full text indisponível para leitura confiável nesta sessão** (página ACM retornou 403). O resumo analítico de HCI.TOP é secundário e não foi usado como substituto do artigo.
- **T8-C04:** manuscrito dos autores `https://arxiv.org/html/2603.08849`, DOI de publicação CHI `10.1145/3772318.3791796`.
- **T8-C05:** artigo original *Science* DOI `10.1126/science.aec8352`, texto publicado `https://s3.amazonaws.com/media.mediapost.com/uploads/science.aec8352.pdf`; contagens conferidas em páginas 1 e 4 do artigo (páginas 2 e 5 do PDF com folha-resumo inicial).

**Limite de origem:** continuamos sem CSV/TSV/XLSX histórico de 1.419 registros *retidos* ou de 2.830 linhas com status. Logo, nenhum artigo novo pode receber o status "pertencia ao corpus Scopus de 16/09". Não inferir ausência/presença pelo DOI público, Crossref, Google Scholar ou busca Scopus feita hoje.

## 3. Adjudicação preliminar por REPORT (I1–I9)

| Candidato | REPORT/DOI | Fonte integral | I1–I8 | I9 | Origem nos 1.419 | Pré-decisão | STUDIES propostos |
|---|---|---|---|---|---|---|---|
| T8-C01 | Li et al. 2025 — `10.1145/3706598.3713133` | ACM + manuscrito | Indícios favoráveis | Sim | Não verificável | Pré-elegível, revisão humana pendente | ST014, ST015 |
| T8-C02 | Flamino et al. 2025 — `10.1038/s41598-025-98378-1` | PMC | Indícios favoráveis | Sim | Não verificável | Pré-elegível, revisão humana pendente | ST016 |
| T8-C03 | Zejian Li et al. 2026 — `10.1145/3772318.3790934` | **Não**: resumo apenas | Indícios favoráveis no resumo/metadados | **Pendente** | Não verificável | **Suspenso por I9** | ST017 somente pré-codificado |
| T8-C04 | Zhi et al. 2026 — `10.1145/3772318.3791796` | Manuscrito autoral | Indícios favoráveis | Sim | Não verificável | Pré-elegível, revisão humana pendente | ST018 |
| T8-C05 | Cheng et al. 2026 — `10.1126/science.aec8352` | Artigo publicado | Indícios favoráveis | Sim | Não verificável | Pré-elegível, revisão humana pendente | ST019–ST021 |

**Interpretação:** quatro publicações têm texto integral acessível e pré-avaliação favorável, não homologada; uma permanece sem comprovação de I9. Todas aguardam identificação na amostra histórica ou uma emenda prospectiva de busca complementar. `I1–I8 favoráveis` não substitui formulário de avaliação humana completo nem avaliação QA-Primary.

## 4. Revisão das oito unidades empíricas e respectivos construtos

| STUDY | Eixo | Variável/intervenção | Outcome humano e interpretação admissível |
|---|---|---|---|
| ST014 | AX01, AX05 | Análise de atributos por GPT-4 em recomendações de random forest: controle vs sequencial vs todas | Maior volume de análise não gerou diferenças significativas nas medidas principais nos contextos testados; NÃO concluir inexistência de efeito geral de explicações. |
| ST015 | AX01, AX02, AX05 | Seleção dinâmica de análises LLM versus condições alternativas | Melhor discriminação do uso de conselho e acurácia em comparações específicas; ressalvar que a análise LLM não é necessariamente explicação fiel do modelo preditivo. |
| ST016 | AX03, AX04, AX05 | Debates HH/AH/AA com agentes GPT-4 e Llama 2 | Agentes foram **menos eficazes em persuadir humanos** que outros humanos; odds 0,288 versus 0,047 são de **agentes versus humanos alterarem sua própria opinião**, não a chance de persuasão exercida por agentes. Grupos AA são contraste sem outcome humano e NÃO viram outra STUDY incluída. |
| ST017 | AX01, AX03, AX05 | Concordância; elogio; autodepreciação; controle, dois tipos de tarefa | **Resumo do autor apenas:** concordância reforça decisão inicial; autodepreciação afeta confiança; não importar betas ou p-valores encontrados em resumos de terceiros. |
| ST018 | AX02, AX03, AX05 | Momento do acesso Early/Continuous/Late/No e tempo insuficiente/suficiente | Sob tempo suficiente, Late reduziu *myside bias* medido (3,42 vs 4,41; p<0,05) sem reduzir número de argumentos (5,25 vs 5,12). `MYSIDE_BIAS` é **proxy operacional definido pelos autores**, não `ANCHORING_BIAS` nem automaticamente `CONFIRMATION_BIAS`. |
| ST019 | AX01, AX03, AX05 | Social sycophancy × estilo antropomórfico; Study 2a, N=804 | Convicção de estar certo e intenções de reparação; não equiparar respostas autorrelatadas a ações reais de reparação. |
| ST020 | AX01, AX03, AX05 | Social sycophancy × rótulo percebido AI/humano; Study 2b, N=801 | Mesma família de outcomes; manipulação da **origem percebida**, não respostas redigidas por humanos; não reportar moderação significativa onde artigo não a sustenta. |
| ST021 | AX01, AX03, AX05 | Conversa em oito turnos sobre conflito real; Study 3, N=800 | Convicção de estar certo, disposição a reparar, confiança/preferência; cartas abertas são proxy exploratório, não observação longitudinal de reconciliação real. |

O artigo Cheng et al. inclui Study 1 sobre **saídas de 11 modelos**: metodologicamente importante para contextualizar a intervenção, mas **fora do denominador de STUDIES humanas**. As unidades válidas para este objeto são 2a, 2b e 3: `804 + 801 + 800 = 2.405` pessoas, não quatro experimentos humanos.

## 5. Correções de auditoria em relação à v0.2

1. **DOI em T8-C01:** a ACM confirma a publicação `10.1145/3706598.3713133`; o cabeçalho da versão HTML arXiv traz `10.1145/3613904.3642625` e não é autoridade bibliográfica para esta edição. Usar o DOI ACM no relatório e na busca de deduplicação.
2. **Interpretação dos odds em T8-C02:** `0.288 (agentes mudando)` contra `0.047 (humanos mudando)` mede **suscetibilidade à mudança dos atores**, não probabilidade de eles convencerem outras pessoas. A publicação também relata separadamente que agentes foram menos convincentes para humanos.
3. **Mensuração em T8-C04:** o índice de myside depende da diferença pró/contra e pode ser menor quando menos argumentos são escritos. Valor menor só deve ser interpretado como menor assimetria argumentativa no contraste com volume semelhante de argumentos.
4. **ST019–ST021:** rótulo AI/humano, estilo antropomórfico e preferência por respostas sycophantic são fatores distintos; não pressupor mecanismo cognitivo causal não isolado.
5. **ST017:** a pesquisa externa encontrou referência bibliográfica e resumo, mas **não conseguiu texto completo verificável**. Estatísticas em página HCI.TOP não são tratadas como confirmação primária.

## 6. Resultado da T8-A2, contagem e limites

- Histórico preservado: **10 REPORTS / 13 STUDIES**.
- Wave 2 auditada: **5 candidaturas a REPORT**, com **8 STUDIES pré-codificadas** (2+1+1+1+3).
- Total **projetado e ainda não validado**: **15 REPORTS / 21 STUDIES**.
- **4/5** candidaturas têm texto integral consultável e evidência suficiente para **pré-elegibilidade**; **1/5** em `ABSTRACT_ONLY`, sem I9 confirmado.
- **0/5** têm pertencimento aos 1.419 registros confirmado (estado `NOT_EVALUATED_SOURCE_UNAVAILABLE`, e não `NO_MATCH`).
- **0/5** têm decisão formal `INCLUDE_REPORT` concluída ou avaliação humana registrada. Não usar 15/21 como denominador efetivo na síntese final.

Esta é uma ampliação **pré-analítica** e não uma prova de lacuna global nem teste direto da hipótese P5/`corroboração aparente`. Estudos single-LLM, multi-LLM ou combinações random forest + LLM não devem ser agrupados como se estivessem testando o mesmo mecanismo.

## 7. Matriz, controle de qualidade e próximos gates

Artefatos:

- `data/screening/t8-a2-elegibilidade-5-reports-v0.5.csv`: checklist I1–I9, nível de evidência, status de origem e decisão para 5 publicações.
- `data/screening/codificacao-wave2-8-studies-v0.5.csv`: nova cópia com oito STUDIES, correções ST016 e ressalvas por unidade; **não substitui a v0.2**, para preservar a trilha de alterações.
- `data/screening/t8-a2-evidencias-revisadas-v0.5.csv`: as 12 evidências da v0.2 auditadas e quatro evidências adicionais, separando autor, metadados e interpretação da revisão.
- `tests/test_t8_a2_v05.py`: integridade estrutural das contagens e dos estados; não valida resultados experimentais nem substitui leitura crítica.

**Gates para fechamento acadêmico:**

- **G1 — Fonte de screening:** executar o script já versionado `scripts/reconciliar_scopus_wave2_v03.py` contra export histórico dos 1.419 retidos (ou 2.830 com decisões). Se a fonte original for irrecuperável, decidir e aprovar emenda prospectiva, registrando data, fontes e consulta, *sem mudar retrospectivamente o screening de setembro*.
- **G2 — Texto integral T8-C03:** obter artigo ACM via acesso institucional/autores, aplicar I1–I9; se não for viável, substituir por REPORT elegível **sem criar retroativamente sua presença no corpus original**.
- **G3 — Adjudicação:** conferir evidências, resultados, QA-Primary e ST014–ST021 por pesquisador humano, registrando decisão e eventuais correções.
- **G4 — Release:** só então mover versões adjudicadas para `data/included/`, atualizar síntese axial/seletiva e produzir `docs/trabalho-8/semana10-trabalho8-final-v1.0.md` com 15 reports de fato incluídos.

**Ação para esta entrega:** versionar os arquivos v0.5 como **T8-A2 (verificação preliminar)**. Não substituí-los por arquivo "final" e não alegar que o artigo T8-C03 foi integralmente lido.
