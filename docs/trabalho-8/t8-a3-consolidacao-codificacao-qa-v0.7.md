# Semana 10 — Trabalho 08 | T8-A3: consolidação da codificação e QA-Primary (v0.7)

> **PPGI/UNIRIO · Comunicação Científica · Prof. Sean Siqueira · 22/10/2026**  
> **Estado:** `WORKING_SET_PROVISIONAL / AI_ASSISTED / RESEARCHER_CHECK_PENDING`.  
> **Referências internas:** Trabalho 3 (seleção Scopus), Trabalho 6 (codebook v0.3 e 13 STUDIES), Trabalho 7 v0.3 (AX01–AX05), T8-A2 v0.5 e v0.6.  
> **Escopo:** consolidar análises **sem declarar cinco novos REPORTS como definitivamente incluídos**.

## 1. Objetivo e unidade de análise

Consolidar o Trabalho 08 com um conjunto de trabalho de **15 REPORTS e 21 STUDY units**, mantendo distinguíveis publicação e unidade empírica. Os 10 REPORTS/13 STUDIES originais são preservados tal como versionados no Trabalho 6. A expansão proposta inclui **C01 (ST014, ST015), C02 (ST016), C04 (ST018), C05 (ST019–ST021) e C06 (ST022)**. O C03/ST017 está **suspenso por texto integral indisponível**; o identificador ST017 não é reaproveitado.

Esse conjunto 15/21 **não** representa resultado homologado de um screening Scopus. O export com os 1.419 registros de setembro continua indisponível; o protocolo registra uma alternativa de identificação complementar apenas como **proposta**. A seleção final requer adjudicação humana e decisão metodológica documentada.

## 2. Critérios de elegibilidade e proposta de decisão

| REPORT | DOI | I1–I9 | Evidência disponível | Decisão nesta etapa | STUDY(s) |
|---|---|---|---|---|---|
| C01 — Li et al. (2025) | `10.1145/3706598.3713133` | Favoráveis preliminarmente | Texto completo de autores e metadados ACM | `PROPOSED_NOT_INCLUDED` | ST014–ST015 |
| C02 — Flamino et al. (2025) | `10.1038/s41598-025-98378-1` | Favoráveis preliminarmente | Artigo aberto PMC / periódico | `PROPOSED_NOT_INCLUDED` | ST016 |
| C03 — Li et al. (2026) | `10.1145/3772318.3790934` | **I9 não confirmado** | Resumo apenas | `SUSPENDED_NOT_IN_WORKING_SET` | ST017 (histórico) |
| C04 — Zhi et al. (2026) | `10.1145/3772318.3791796` | Favoráveis preliminarmente | Artigo CHI e texto de autores | `PROPOSED_NOT_INCLUDED` | ST018 |
| C05 — Cheng et al. (2026) | `10.1126/science.aec8352` | Favoráveis preliminarmente | Artigo Science; suplementos não integralmente auditados | `PROPOSED_NOT_INCLUDED` | ST019–ST021 |
| C06 — Bean et al. (2026) | `10.1038/s41591-025-04074-y` | Favoráveis preliminarmente, **ressalva I5** | Texto integral Nature Medicine e correção 17/04/2026 | `PROPOSED_NOT_INCLUDED` | ST022 |

**Ressalva I5/C06:** há julgamento e decisão com mediação LLM, mas não teste direto de anchoring, confirmation ou automation bias. O estudo pode compor a síntese de *qualidade da decisão* e *interação*, não a contagem de vieses diretamente operacionalizados.

## 3. QA-Primary — avaliação inicial (não adjudicada)

O instrumento QA-Primary do projeto avalia `QA1` objetivo; `QA2` participantes; `QA3` desenho; `QA4` documentação do LLM; `QA5` operacionalização; `QA6` comparador; `QA7` análise; `QA8` ameaças; `QA9` rastreabilidade; `QA10` transparência. Escala **Y, PY, N, U, NA** sem escore numérico ou limiar agregado. A matriz longa em CSV justifica **cada uma das 60 células** e fornece links/localizadores. `PY` não é uma declaração de falha: sinaliza evidência parcial ou aspecto ainda não verificado. `U` em C03 reflete a impossibilidade de avaliar o texto integral nesta execução.

| REPORT | QA1 | QA2 | QA3 | QA4 | QA5 | QA6 | QA7 | QA8 | QA9 | QA10 |
|---|---|---|---|---|---|---|---|---|---|---|
| C01 | Y | Y | Y | PY | Y | Y | Y | Y | PY | PY |
| C02 | Y | Y | Y | PY | Y | Y | Y | PY | PY | PY |
| C03 (suspenso) | U | U | U | U | U | U | U | U | U | U |
| C04 | Y | Y | Y | PY | Y | Y | Y | Y | Y | PY |
| C05 | Y | Y | Y | PY | Y | Y | PY | PY | PY | PY |
| C06 | Y | Y | Y | Y | Y | Y | Y | PY | Y | Y |

**Critical flags interpretativas:** C06 não mede viés psicológico diretamente (`CRITICAL_BIAS_MEASURE` como lembrete de escopo, **não defeito definitivo**); C01 mistura preditor random forest com análises GPT-4; C02 inclui grupos sem humanos; C04 usa proxy *myside*; C05 utiliza intenções autorrelatadas. Os **10 reports originais não foram reavaliados com QA-Primary** nesta etapa e não é metodologicamente correto apresentar uma tabela completa 15/15 de qualidade sem essa análise.

## 4. Codificação aberta — oito unidades propostas, com evidências e contrapontos

| STUDY | Condição / intervenção | Outcome efetivamente medido | Resultado dos autores conforme fontes já auditadas | Limite / memo crítico | Categorias |
|---|---|---|---|---|---|
| **ST014 — C01** | Apresentação sequencial ou simultânea de análises GPT-4 sobre recomendações random forest. | Acurácia, *overreliance*, *underreliance*. | Sem melhoria estatisticamente significativa nessas comparações principais. | Mais explicação ≠ qualidade automaticamente; o texto do LLM não é explicação fiel garantida do preditor. | AX01, AX05 |
| **ST015 — C01** | Seleção adaptativa de análises conforme modelo do comportamento humano. | Acurácia e indicadores de reliance apropriada. | Melhora em comparações específicas relativamente a controles/apresentações não adaptativas. | Não afirmar superioridade universal ou mediação psicológica isolada. | AX01, AX02, AX05 |
| **ST016 — C02** | Debates em jogos HH/AH/AA; apenas os contextos com humanos contribuem para outcomes humanos. | Mudança de opinião e avaliações sociais. | Agentes foram menos persuasivos para humanos que outros humanos nas condições testadas. | Odds 0,288 e 0,047 referem-se a **agentes/humanos mudarem sua própria opinião**, não à capacidade de convencer outros; AA é contraste model-only. | AX03, AX04, AX05 |
| **ST018 — C04** | Momento Early/Continuous/Late/No LLM × tempo suficiente/insuficiente. | Desempenho em texto/argumentação e proxy *myside*. | Efeito de timing dependente do tempo: ajuda inicial sob pressão, impacto contrário quando há tempo. | *Myside* é diferença absoluta pró/contra; medir conjuntamente total de argumentos. Não equivale a ancoragem. | AX02, AX03, AX05 |
| **ST019 — C05** | Respostas sycophantic × estilo antropomórfico; Study 2a, N=804. | Convicção de estar certo e intenção de reparar. | Respostas concordantes elevam convicção e reduzem intenção reparadora. | Não converter intenção autorrelatada em reparação observada. | AX01, AX03, AX05 |
| **ST020 — C05** | Sycophancy × identidade da fonte percebida; Study 2b, N=801. | Convicção, intenção reparadora. | Efeito de sycophancy; rotulagem não eliminou o padrão principal reportado. | Resposta rotulada como humana não foi necessariamente escrita por humano. | AX01, AX03, AX05 |
| **ST021 — C05** | Chat ao vivo sobre conflito interpessoal; Study 3, N=800. | Convicção, confiança/preferência e intenção de reparar. | Padrão adverso nas intenções coexistiu com preferência/confiança maiores. | Ausência de observação de reconciliação de longo prazo. | AX01, AX03, AX05 |
| **ST022 — C06** | GPT-4o/Llama 3/Command R+ em braços separados versus recursos habituais; N=1.298. | Identificação de condições médicas e decisão de conduta simulada. | Participantes com LLM não tiveram ganhos de decisão vs controle; habilidade do modelo isolado não se traduziu em benefício humano. | Modelo sozinho é **benchmark distinto**, não braço humano controlado; sem cognitive bias diretamente medido. Correção de Fig. 2a só nos rótulos do eixo. | AX02, AX05 |

**Delimitação de participantes:** C05 possui 2.405 pessoas **nos três estudos humanos** (804 + 801 + 800). Seu Study 1 avalia respostas de modelos e não gera unidade humana adicional. C06 possui 1.298 participantes, mas cerca de 2.400 respostas em tarefas: participantes e respostas não são unidades intercambiáveis. C01 possui dois experimentos humanos independentes. Não somar tamanhos amostrais como meta-análise.

## 5. Codificação axial — comparação com os cinco eixos do Trabalho 7

| Eixo original | Evidência nova e diálogo com a Wave 1 | Tensão / limite |
|---|---|---|
| **AX01 — Credibilidade/aceitação sem discriminar acurácia** | C01 distingue volume de explicações de apresentação adaptativa; C05 evidencia preferência por respostas concordantes mesmo com intenções sociais potencialmente piores. | Preferência ≠ decisão factual correta; tarefa social não usa o mesmo *ground truth* de uma tarefa classificatória. |
| **AX02 — Visibilidade do erro, escrutínio e custo** | C01 enfatiza seleção útil de análises; C04 mostra que temporização da assistência é condição de contorno; C06 evidencia falhas de transferência de informação na interação. | Não chamar tempo ou falha de comunicação de *mecanismo mediador causal* quando não isolado no desenho. |
| **AX03 — Alinhamento, argumentação e revisão de crenças** | C02 introduz contraste experimental em debates; C04, assimetria argumentativa contextual; C05, sycophancy e convicção. | Persuasão, conformidade, confirmação e convicção **não são o mesmo construto**. |
| **AX04 — Pluralidade de agentes e influência social** | C02 informa diferenças de debate humano-agente, junto a ST007/ST010 anteriores. | Não é teste de fontes epistemicamente independentes nem da hipótese de corroboração aparente; AA é condição sem humanos. |
| **AX05 — Confiança percebida versus ação/desempenho** | C05 mostra possível divergência confiança/preferência × intenção de reparar; C06 evidencia distância entre competência model-only e decisão do humano assistido. | Outcomes sociais e precisão médica não compartilham escala; sintetizar *mecanismos candidatos*, não efeitos agregados comparáveis. |

### Comparação constante e casos negativos

1. Explicações **nem sempre** ajudam (ST014), mas seleção adaptativa **pode** ajudar (ST015); condições de apresentação importam.
2. LLMs **não são necessariamente melhores debatedores/persuadores** do que humanos (ST016), apesar de mensagens tematicamente focadas.
3. Apoio inicial pode **melhorar ou piorar** desempenho conforme tempo disponível (ST018).
4. Usuários podem preferir respostas sycophantic mesmo com **efeitos indesejáveis sobre intenções** (ST019–ST021).
5. **Capacidade de um modelo isolado** não garante **melhoria de decisões humanas** em interação (ST022).

## 6. Codificação seletiva — integração prudente

**Categoria integradora provisória:** _o efeito da assistência por LLM sobre o julgamento humano depende da combinação de credibilidade percebida, desenho interacional, qualidade da informação, condições temporais e capacidade de escrutínio; confiança ou competência do modelo, isoladamente, não determinam qualidade do desfecho humano._

Esta é **síntese interpretativa** da revisão, não uma teoria validada. Preservamos as proposições P1–P5 do Trabalho 7, incluindo P5 (*corroboração aparente*) apenas como **hipótese não testada diretamente**. Os novos estudos fortalecem hipóteses relativas a (a) condições de apresentação de informação, (b) moderação temporal e (c) dissociação entre percepção de confiabilidade e consequências, sem estabelecer mecanismo universal ou saturação teórica.

### Limites substantivos das RQs

- **RQ1 / RQ2:** novos construtos/proxies incluem *myside*, *social sycophancy* e qualidade da decisão; não declarar que medem ancoragem ou confirmação sem operacionalização.
- **RQ3:** há variação observada segundo timing, formato de análises e enquadramento interacional.
- **RQ4 / RQ5:** comparações mono/multi-LLM **ainda são escassas no conjunto**, e C06 contém modelos em braços separados, não cooperação de múltiplos LLMs.
- **RQ6:** proveniência Scopus ainda não validada; modalidades, domínios e métricas heterogêneos; conferência humana pendente.

## 7. Fluxo de seleção e integridade metodológica

```text
Busca Scopus de 16/09/2026 (histórico imutável)
    1.419 retidos -> Wave 1: 10 REPORTS -> 13 STUDIES

Identificação dirigida posterior (outubro/2026, fora do fluxo histórico comprovado)
    6 candidatos avaliados: C01...C06
    1 suspenso (C03, I9 pendente)
    5 REPORTS em conjunto analítico proposto
       C01(2), C02(1), C04(1), C05(3), C06(1) = 8 STUDIES

Conjunto analítico proposto = 15 REPORTS / 21 STUDIES
Conjunto novo formalmente incluído = 0 enquanto gates em aberto
```

Não atribuir aos 1.419 qualquer candidato não reconciliado. Este registro segue o espírito de transparência de **SEGRESS**. A codificação inspirada em Grounded Theory, a comparação constante, os memos, o QA-Primary e a seleção complementar são **decisões metodológicas do nosso estudo**, não regras inventadas como parte do SEGRESS. QAISER é instrumento para revisões, não para os artigos primários.

## 8. Artefatos e rastreabilidade

- `data/screening/t8-a3-inventario-15-report-propostos-mais-suspenso-v0.7.csv` — 16 registros auditáveis: 10 anteriores + 5 propostos + 1 suspenso, com `in_proposed_15`.
- `data/screening/t8-a3-indice-21-studies-propostas-v0.7.csv` — 21 unidades e suas origens; **não** reescreve as linhas históricas da Semana 08.
- `data/screening/t8-a3-codificacao-wave2-selecionada-8-studies-v0.7.csv` — pré-codificação de oito unidades novas (sem ST017, com ST022).
- `data/screening/t8-a3-qa-primary-6-candidatos-v0.7.csv` — QA por dimensão e report, com fundamento e lacunas, não adjudicada.
- `data/screening/t8-a3-trilha-evidencias-provisoria-v0.7.csv` — origem AUTHOR/EDITOR/REVIEW e localizadores, conferência humana pendente.
- `docs/trabalho-8/t8-a3-codebook-delta-v0.5-proposto.md` — refinamento incremental de códigos; **não substitui** o v0.3.
- `docs/trabalho-8/t8-a3-nota-metodologica-decisao-v0.7.md` — decisões submetidas à adjudicação, sem editar `protocol/`.
- `scripts/t8_a3_consolidar_v07.py` — comando para gerar matriz integrada a partir das 13 linhas históricas do seu GitHub mais as 8 novas; mantém original intacto.
- `tests/test_t8_a3_v07.py` — testes de contagem, unicidade, ID suspenso e merge a partir de fixture simulada.

## 9. Pendências e próximo gate de publicação

**Antes de v1.0 e Classroom:** (G1) validar o caminho complementar ou reconciliar o export; (G2) adjudicar cinco reports e confirmar que não são duplicatas no pool; (G3) revisar QA-Primary/trechos pelos pesquisadores, incluindo suplementos quando necessário; (G4) fazer QA dos 10 históricos se o relatório final pretender avaliação de qualidade do corpus todo; (G5) transferir arquivos homologados para `data/included/` e atualizar fluxos.

**Resultado da T8-A3 v0.7:** consolidação qualitativa **provisória, auditável e pronta para conferência**, não homologação de 15 REPORTS. Nenhum arquivo anterior foi sobrescrito ou commit efetuado por este pacote.

## 10. Fontes principais e correções

1. Li et al. (2025), CHI. https://doi.org/10.1145/3706598.3713133 ; manuscrito: https://arxiv.org/html/2502.11919 . **DOI ACM prevalece** sobre DOI que aparece em cabeçalho da versão arXiv.
2. Flamino et al. (2025), *Scientific Reports*. https://pmc.ncbi.nlm.nih.gov/articles/PMC12015287/ . Distinguir odds da mudança do próprio ator e persuasão de terceiros.
3. Zhi et al. (2026), CHI. https://doi.org/10.1145/3772318.3791796 ; manuscrito: https://arxiv.org/html/2603.08849 .
4. Cheng et al. (2026), *Science*. https://doi.org/10.1126/science.aec8352 .
5. Bean et al. (2026), *Nature Medicine*. https://www.nature.com/articles/s41591-025-04074-y ; correção: https://www.nature.com/articles/s41591-026-04404-8 .
6. Li et al. (2026), CHI, **suspenso**. https://doi.org/10.1145/3772318.3790934 .
