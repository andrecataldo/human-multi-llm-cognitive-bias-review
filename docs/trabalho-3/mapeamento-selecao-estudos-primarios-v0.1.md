# Trabalho 3 - Mapeamento e seleção de estudos primários

> **Versão:** v0.1  
> **Data:** 2026-09-17  
> **Disciplina:** Comunicação Científica - PPGI/UNIRIO  
> **Tema:** vieses cognitivos humanos em julgamentos mediados por LLMs, com atenção a sistemas multiagentes  
> **Escopo desta entrega:** primeira release, deliberadamente **Scopus-only**  
> **Status:** seleção e síntese descritiva inicial de estudos primários; o estudo secundário completo permanece em evolução.

## 1. Objetivo da atividade

Esta entrega registra a aplicação inicial do planejamento de um **Systematic Mapping Study (SMS)** sobre vieses cognitivos humanos em processos de julgamento e tomada de decisão mediados por Large Language Models (LLMs), com atenção particular a configurações multiagentes.

O objetivo específico desta release é documentar, de forma rastreável:

1. o planejamento do mapeamento à luz do **SEGRESS**;
2. a estratégia de busca executada no **Scopus**;
3. os critérios e o processo de seleção dos estudos;
4. a seleção de pelo menos dez estudos primários empíricos;
5. a distinção entre **REPORT** (publicação) e **STUDY** (unidade empírica);
6. uma síntese descritiva inicial das evidências em relação às questões de pesquisa.

Esta versão não pretende encerrar a revisão. A expansão para outras fontes, novas ondas de recuperação de texto completo, avaliação de qualidade e sínteses posteriores permanecem como evolução do projeto.

---

## 2. Delimitação conceitual

O **humano é tratado como sujeito cognitivo**. Os LLMs são tratados como sistemas mediadores da interação e do julgamento, e não se assume que um modelo de linguagem possua, no mesmo sentido psicológico, os vieses cognitivos humanos.

Durante a classificação das evidências são distinguidos quatro loci possíveis: `HUMAN`, `MODEL`, `INTERACTION` e `UNCLEAR`. O foco principal desta revisão é `HUMAN`, admitindo `INTERACTION` quando o fenômeno emerge da relação entre características do sistema e o julgamento do participante.

Também é mantida uma distinção conceitual entre **vieses cognitivos** e fenômenos associados. *Confirmation bias* e *anchoring bias* constituem o núcleo cognitivo do projeto. *Trust*, *reliance*, *overreliance*, *appropriate reliance*, *persuasion* e *social influence* são tratados como fenômenos relacionados, não como sinônimos de viés cognitivo.

Em sistemas multiagentes, múltiplos agentes são tratados como uma **configuração arquitetural e interacional**, não como múltiplos sujeitos cognitivos humanos. Uma hipótese de pesquisa que emerge do projeto é a distinção entre **pluralidade de agentes** e **independência epistemológica**, mas essa hipótese não é tratada como conclusão prévia.

---

## 3. Questões de pesquisa

### 3.1 Questão principal

> **Que evidências empíricas existem sobre como Large Language Models, particularmente sistemas multiagentes, estão associados à manifestação, amplificação ou mitigação de vieses cognitivos humanos em processos de julgamento e tomada de decisão?**

### 3.2 Questões secundárias

- **RQ1.** Quais vieses cognitivos humanos são investigados?
- **RQ2.** Como esses vieses e fenômenos relacionados são definidos, operacionalizados e medidos?
- **RQ3.** Quais características da interação humano–LLM estão associadas à amplificação ou mitigação de vieses e fenômenos relacionados?
- **RQ4.** Como configurações single-LLM e multi-LLM são empregadas e comparadas?
- **RQ5.** Como consenso, discordância, crítica, debate e verificação se relacionam a julgamento, *trust* e *reliance*?
- **RQ6.** Quais limitações metodológicas, inconsistências e lacunas permanecem?

---

## 4. Referencial metodológico: SEGRESS

Esta etapa utiliza como referência principal **SEGRESS - Software Engineering Guidelines for REporting Secondary Studies**, de Kitchenham, Madeyski e Budgen. O SEGRESS é uma diretriz de **relato e transparência de estudos secundários**, baseada no PRISMA 2020 e estendida para contemplar também mapping studies e revisões qualitativas.

Para esta entrega foram priorizados especialmente os itens do checklist relacionados a:

- definição dos objetivos e RQs;
- critérios de elegibilidade;
- fonte de informação e data da busca;
- estratégia de busca reproduzível;
- processo de seleção e transparência sobre automação;
- fluxo de records/reports/studies;
- características dos estudos incluídos;
- métodos de análise das características dos estudos;
- limitações do processo e disponibilidade dos materiais.

### 4.1 Escopo metodológico desta release

Para a entrega de 17/09/2026 foi adotada, deliberadamente, uma **release Scopus-only**. Portanto, os itens de *Information Sources* e *Search Strategy* são considerados atendidos no escopo desta versão por meio da documentação completa da busca Scopus. Uma expansão futura para outras bases deve ser apresentada como ampliação posterior de escopo, e não como algo já realizado.

### 4.2 Extensões metodológicas próprias

Além das orientações de transparência do SEGRESS, foram utilizados procedimentos próprios do estudo: *known-set* para calibração da busca, piloto estratificado de 100 reports, `screening-codebook v1.0`, screening assistido por IA, adjudicação de casos incertos, checagem amostral de exclusões e uma passagem sistemática de resgate de potenciais falsos negativos.

Essas práticas são **extensões metodológicas deste estudo** e não são atribuídas ao SEGRESS.

---

## 5. Fonte de informação e período

| Elemento | Definição nesta release |
|---|---|
| Base executada | **Scopus** |
| Campo principal | `TITLE-ABS-KEY` |
| Período | 2020–2026 |
| Restrição Scopus | `PUBYEAR > 2019 AND PUBYEAR < 2027` |
| Data da busca definitiva | **16/09/2026** |
| Idioma na busca | Sem filtro de idioma |
| Tipos mantidos na pré-seleção estrutural | Article; Conference paper |
| Preprints | Fora do corpus principal; podem ser mantidos como *emerging-evidence watchlist* |

---

## 6. Estratégia definitiva de busca no Scopus

A estratégia foi dividida em quatro consultas complementares. S2 foi separada em duas regiões - *reliance* e *belief/social influence* - para reduzir ruído sem perder fenômenos relacionados ao julgamento humano.

| Estratégia | Foco | Resultados |
|---|---|---:|
| S1 | Cognitive Bias Core | **346** |
| S2a | Reliance / Calibration | **1.475** |
| S2b | Belief / Persuasion / Social Influence | **633** |
| S3 | Human–Multi-Agent LLM | **911** |
| **Total bruto de ocorrências** |  | **3.365** |

### 6.1 S1 - Cognitive Bias Core

```text
TITLE-ABS-KEY(
    (
        "large language model*"
        OR LLM
        OR LLMs
        OR ChatGPT
        OR "GPT-3"
        OR "GPT-4"
        OR "GPT-4o"
        OR "GPT-5"
    )
    AND
    (
        human*
        OR user*
        OR participant*
        OR people
    )
    AND
    (
        "cognitive bias*"
        OR "confirmation bias"
        OR "confirmatory bias"
        OR "anchoring bias"
        OR "anchoring effect*"
        OR "automation bias"
        OR "cognitive debias*"
    )
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

### 6.2 S2a - Reliance / Calibration

```text
TITLE-ABS-KEY(
    (
        "large language model*"
        OR LLM
        OR LLMs
        OR ChatGPT
        OR "GPT-3"
        OR "GPT-4"
        OR "GPT-4o"
        OR "GPT-5"
    )
    AND
    (
        (human* W/5 reliance)
        OR (user* W/5 reliance)
        OR (participant* W/5 reliance)
        OR overreliance
        OR "over-reliance"
        OR underreliance
        OR "under-reliance"
        OR "appropriate reliance"
        OR "calibrated reliance"
        OR "reliance calibration"
        OR "trust calibration"
        OR "calibrated trust"
    )
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

### 6.3 S2b - Belief / Persuasion / Social Influence

```text
TITLE-ABS-KEY(
    (
        "large language model*"
        OR LLM
        OR LLMs
        OR ChatGPT
        OR "GPT-3"
        OR "GPT-4"
        OR "GPT-4o"
        OR "GPT-5"
    )
    AND
    (
        human*
        OR user*
        OR participant*
    )
    AND
    (
        persuasion
        OR persuasive
        OR "belief change"
        OR "belief revision"
        OR "belief update*"
        OR "opinion change"
        OR "opinion shift*"
        OR "attitude change"
        OR "social influence"
        OR "advice taking"
        OR "advice-taking"
    )
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

### 6.4 S3 - Human–Multi-Agent LLM

```text
TITLE-ABS-KEY(
    (
        "large language model*"
        OR LLM
        OR LLMs
        OR ChatGPT
        OR "GPT-3"
        OR "GPT-4"
        OR "GPT-4o"
        OR "GPT-5"
    )
    AND
    (
        multi W/1 agent*
        OR multiagent*
        OR "multiple agent*"
        OR multi W/1 LLM*
        OR "multiple LLM*"
        OR "multi-agent debate"
        OR "agent debate"
        OR "agent collaboration"
        OR "agent consensus"
    )
    AND
    (
        human*
        OR user*
        OR participant*
        OR people
    )
    AND
    (
        judg*
        OR decision*
        OR bias*
        OR reliance
        OR overreliance
        OR trust
        OR persuasion
        OR "belief change"
        OR "opinion change"
        OR "social influence"
        OR agreement
        OR disagreement
        OR consensus
        OR critique
        OR debate
        OR verification
    )
)
AND PUBYEAR > 2019
AND PUBYEAR < 2027
```

### 6.5 Validação por known-set

Antes da busca definitiva, as strings foram testadas contra um conjunto de estudos previamente conhecidos e claramente relevantes. O objetivo do *known-set* foi testar a capacidade das regiões de busca de recuperar estudos-semente; ele **não foi utilizado como corpus final nem como garantia de inclusão**.

---

## 7. Critérios de elegibilidade

### 7.1 Inclusão

| Código | Critério |
|---|---|
| I1 | Estudo primário empírico |
| I2 | Participantes humanos |
| I3 | Uso, exposição ou interação com LLM |
| I4 | Julgamento, decisão, avaliação, mudança de crença/opinião ou comportamento de reliance |
| I5 | Viés cognitivo ou fenômeno humano relacionado definido no protocolo |
| I6 | Relação observável entre a mediação por LLM e um outcome humano |
| I7 | Publicação entre janeiro/2020 e 16/09/2026 |
| I8 | Artigo peer-reviewed de periódico ou full conference paper |
| I9 | Texto completo disponível em inglês, português ou espanhol |

### 7.2 Exclusão

| Código | Critério |
|---|---|
| E1 | Comportamento/bias apenas do modelo, sem outcome humano elegível |
| E2 | Comparação humano versus LLM sem mediação/interação relevante |
| E3 | Fairness/demographic/social bias sem julgamento cognitivo humano no escopo |
| E4 | Estudo puramente técnico |
| E5 | Trust/acceptance/adoption sem outcome de julgamento, decisão, crença ou reliance |
| E6 | Multi-agent sem participante ou outcome humano |
| E7 | IA não baseada em LLM |
| E8 | Estudo secundário, conceitual, editorial ou não empírico |
| E9 | Informação metodológica insuficiente após leitura do texto completo |
| E10 | Report redundante referente ao mesmo estudo |

No screening de título/resumo, a regra adotada foi **“na dúvida, reter”**. `UNCERTAIN` não foi utilizado como sinônimo de exclusão.

---

## 8. Processo de seleção

### 8.1 Consolidação e deduplicação

A execução das quatro buscas gerou **3.365 ocorrências brutas**. Após consolidação por EID foram obtidos **3.259 registros únicos**. Uma adjudicação adicional de colisões bibliográficas removeu três duplicatas de indexação, resultando em **3.256 reports bibliográficos únicos**.

### 8.2 Pré-seleção estrutural

Foram mantidos `Article` e `Conference paper`, incluindo `Final` e `Article in press`. O idioma não foi usado para exclusão automática nessa fase.

Resultado:

- entrada: **3.256 reports**;
- exclusões estruturais: **426**;
- reports encaminhados ao screening de título/resumo: **2.830**.

### 8.3 Screening de título e resumo

O procedimento foi inicialmente calibrado em um piloto estratificado de **100 reports**. O piloto produziu um `screening-codebook v1.0`, com decisões `INCLUDE`, `EXCLUDE` e `UNCERTAIN`, além de códigos explícitos para o primeiro motivo decisivo de exclusão.

Na sequência foi executado um screening **AI-assisted** sobre os 2.830 reports. A automação foi utilizada como apoio de classificação e priorização, e **não é tratada como um segundo revisor humano**. O procedimento incluiu modelo auxiliar baseado em TF-IDF + regressão logística, regras conservadoras, adjudicação dos `UNCERTAIN`, checagem amostral de 320 exclusões e uma passagem de resgate sobre todas as exclusões.

A passagem de resgate recuperou **153 reports** para full text. Ao final do screening de título/resumo desta release:

- `RETAIN_FOR_FULL_TEXT`: **1.419 reports**;
- `EXCLUDE`: **1.411 reports**.

Os **1.419** constituem o pool Scopus para futuras ondas de texto completo; não representam estudos definitivamente incluídos.

### 8.4 Recuperação e full-text screening da Wave 1

Para cumprir a primeira entrega e validar o procedimento de full text, foi realizada uma onda controlada de recuperação de textos completos. Dez reports tiveram o texto completo verificavelmente recuperado e foram avaliados com I1–I9.

Resultado da Wave 1:

- reports recuperados e avaliados em full text: **10**;
- `INCLUDE_REPORT`: **10**;
- exclusões no full text desta Wave 1: **0**.

A decisão `INCLUDE_REPORT` ocorre no nível da publicação. Em seguida foi realizada a resolução `REPORT → STUDY`, identificando **13 unidades empíricas** nos 10 reports.

### 8.5 Fluxo resumido desta release

```text
Scopus S1 + S2a + S2b + S3
        |
        v
3.365 ocorrências brutas
        | consolidação/deduplicação
        v
3.256 reports bibliográficos únicos
        | pré-seleção estrutural
        v
2.830 reports para title/abstract screening
        | screening + adjudicação + QC + rescue
        v
1.419 reports retidos para full text
        | Wave 1 de recuperação
        v
10 reports com full text verificado
        | aplicação I1–I9
        v
10 INCLUDE_REPORT
        | resolução REPORT → STUDY
        v
13 STUDY units
```

---

## 9. Transparência sobre uso de Inteligência Artificial

A seleção e extração desta release utilizaram IA como apoio metodológico. Foram empregados procedimentos assistidos para triagem, organização de casos, recuperação de potenciais falsos negativos e pré-extração de dados.

Para evitar uma descrição metodologicamente incorreta:

- a IA **não é apresentada como segundo revisor humano independente**;
- decisões assistidas mantêm trilha de auditoria;
- casos incertos foram retidos de forma conservadora;
- full-text screening só foi realizado quando o texto completo havia sido efetivamente recuperado;
- informações não sustentadas pelas fontes permaneceram `NOT_REPORTED` ou pendentes;
- resultados dos autores e interpretação da revisão foram mantidos em campos separados.

A extração consolidada permanece marcada como `AI-assisted/source-grounded`, com `researcher_check_status=PENDING` para as 13 unidades.

---

## 10. Reports primários selecionados na Wave 1

| ID | Ano | Report | Venue | DOI | Foco principal no mapping |
|---|---:|---|---|---|---|
| FT0070 | 2025 | Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies | Conference on Human Factors in Computing Systems - Proceedings | `10.1145/3706598.3714020` | Appropriate reliance, overreliance, explanations, sources e inconsistencies |
| FT0072 | 2025 | Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance | Conference on Human Factors in Computing Systems - Proceedings | `10.1145/3706598.3714082` | Overreliance, decision accuracy e uncertainty/confidence cues |
| FT0080 | 2025 | To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models | Conference on Human Factors in Computing Systems - Proceedings | `10.1145/3706598.3714097` | Appropriate reliance, overreliance, underreliance e calibration |
| FT0083 | 2025 | On the conversational persuasiveness of GPT-4 | Nature Human Behaviour | `10.1038/s41562-025-02194-6` | Persuasion e opinion change em debate com GPT-4 |
| FT0310 | 2025 | Multi-Agents are Social Groups: Investigating Social Influence of Multiple Agents in Human-Agent Interactions | Proceedings of the ACM on Human-Computer Interaction | `10.1145/3757633` | Multi-agent social influence, opinion change e polarization |
| FT0318 | 2025 | Dialogues with large language models reduce conspiracy beliefs even when the AI is perceived as human | PNAS Nexus | `10.1093/pnasnexus/pgaf325` | Belief change e correção de conspiracy beliefs por diálogo |
| FT0545 | 2026 | How latent and prompting biases in AI-generated historical narratives influence opinions | PNAS Nexus | `10.1093/pnasnexus/pgag022` | Opinion change após narrativas ideologicamente enquadradas por LLM |
| FT0772 | 2026 | Sensemaking in Multi-Agent LLM Interfaces: How Users Interpret Transparency and Trustworthiness Cues | Conference on Human Factors in Computing Systems - Proceedings | `10.1145/3772318.3791157` | Multi-agent sensemaking, trustworthiness cues e reliance intention |
| FT1222 | 2024 | Generative Echo Chamber? Efects of LLM-Powered Search Systems on Diverse Information Seeking | Conference on Human Factors in Computing Systems - Proceedings | `10.1145/3613904.3642459` | Confirmation bias, selective exposure e generative echo chamber |
| FT1233 | 2024 | "I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust | 2024 ACM Conference on Fairness, Accountability, and Transparency, FAccT 2024 | `10.1145/3630106.3658941` | Uncertainty expression, reliance, trust e overreliance |

---

## 11. Resolução REPORT → STUDY

Um **REPORT** corresponde à publicação bibliográfica; um **STUDY** corresponde a uma investigação empírica distinta. Um mesmo report pode conter múltiplos experimentos com amostras independentes.

Nesta Wave 1:

- FT0070 contém **2 STUDY units**;
- FT0072 contém **2 STUDY units**;
- FT1222 contém **2 STUDY units**;
- os outros sete reports contêm **1 STUDY unit** cada;
- total: **13 STUDY units**.

| Study | Report | Unidade empírica | N analisado | Desenho | Construto/fenômeno principal | RQs |
|---|---|---|---:|---|---|---|
| ST001 | FT0070 | Study 1 - Think-Aloud Study | 16 | Think-aloud + behavioral/qualitative study | Fenômeno relacionado: reliance; overreliance; underreliance; verification behavior | RQ2, RQ3, RQ5, RQ6 |
| ST002 | FT0070 | Study 2 - Controlled Experiment | 308 | Large-scale preregistered controlled experiment | Fenômeno relacionado: appropriate reliance; overreliance; confidence; verification | RQ2, RQ3, RQ5, RQ6 |
| ST003 | FT0072 | Experiment 1 | 90 | Between-subjects online experiment: traditional vs LLM-based search | Fenômeno relacionado: overreliance; decision accuracy; error detection | RQ2, RQ3, RQ5, RQ6 |
| ST004 | FT0072 | Experiment 2 | 120 | Three-condition online experiment: confidence highlighting | Fenômeno relacionado: overreliance; verification; uncertainty communication | RQ2, RQ3, RQ5, RQ6 |
| ST005 | FT0080 | Main randomized online experiment | 400 (report-level N; exclusion details not re-extracted) | Preregistered randomized online experiment | Fenômeno relacionado: appropriate reliance; overreliance; underreliance; confidence calibration | RQ2, RQ3, RQ5, RQ6 |
| ST006 | FT0083 | Main preregistered debate study | 900 | Preregistered controlled multiround debate experiment | Fenômeno relacionado: persuasion; opinion change | RQ2, RQ3, RQ5, RQ6 |
| ST007 | FT0310 | Main human–multi-agent study | 93 | Human experiment with 1-, 3-, and 5-agent conditions | Fenômeno relacionado: social influence; normative influence; opinion change; polarization; pressure to conform | RQ2, RQ3, RQ4, RQ5, RQ6 |
| ST008 | FT0318 | Main preregistered experiment | 955 | Preregistered human–LLM dialogue experiment | Fenômeno relacionado: belief change; persuasion; conspiracy-belief correction | RQ2, RQ3, RQ6 |
| ST009 | FT0545 | Main preregistered survey experiment | 1,912 | Preregistered survey experiment | Fenômeno relacionado: opinion change; persuasion from latent/prompted framing | RQ2, RQ3, RQ6 |
| ST010 | FT0772 | Main qualitative comparative user study | 12 | Design-led qualitative comparative structured-observation study | Fenômeno relacionado: trust calibration; reliance intention; epistemic heuristics; verification/sensemaking | RQ2, RQ3, RQ4, RQ5, RQ6 |
| ST011 | FT1222 | Study 1 | 115 | Online between-subject experiment: conversational vs web search | Viés direto: confirmation bias; selective exposure | RQ1, RQ2, RQ3, RQ6 |
| ST012 | FT1222 | Study 2 | 223 | Online factorial experiment: consonant/neutral/dissonant LLM bias | Viés direto: confirmation bias; selective exposure | RQ1, RQ2, RQ3, RQ6 |
| ST013 | FT1233 | Main preregistered human-subject experiment | 404 | Large-scale preregistered human-subject experiment | Fenômeno relacionado: overreliance; reliance; trust; uncertainty communication | RQ2, RQ3, RQ5, RQ6 |

---

## 12. Síntese descritiva por questão de pesquisa

### 12.1 RQ1 - Quais vieses cognitivos humanos são investigados?

Nesta Wave 1, **confirmation bias/selective exposure** é o único viés cognitivo humano explicitamente nomeado e operacionalizado como tal. Isso ocorre em ST011 e ST012, ambos do report *Generative Echo Chamber?*. As medidas incluem *confirmatory querying*, exposição seletiva e indicadores de polarização.

Nenhuma das 13 STUDY units selecionadas oferece evidência direta sobre **anchoring bias**. Essa ausência caracteriza apenas o corpus desta release e não permite afirmar que ancoragem esteja ausente da literatura.

### 12.2 RQ2 - Como são definidos, operacionalizados e medidos?

A operacionalização é heterogênea. *Reliance* e *overreliance* aparecem como concordância com resposta LLM correta/incorreta, mudança de resposta, Relative LLM Reliance, Relative Self-Reliance e Appropriate Reliance Ratio. *Confirmation/selective exposure* é medida por *confirmatory queries*, mudanças de atitude, argumentos, *agreement*, *trust* e *extremeness*. Persuasion e belief change utilizam medidas pré/pós de opinião ou confiança. Estudos multiagentes também empregam *think-aloud*, entrevistas e *card sorting*.

Assim, `bias`, `trust` e `reliance` não podem ser agregados como se fossem um único outcome.

### 12.3 RQ3 - Quais características da interação amplificam ou mitigam os fenômenos?

O corpus contém evidências relacionadas a *explanations*, *sources*, *inconsistencies*, *uncertainty wording*, *confidence highlighting*, personalização, enquadramento ideológico, busca conversacional, número de agentes, discordância, crítica, consenso e transparência.

Os resultados são dependentes do contexto. Explicações podem aumentar reliance inclusive quando a resposta está incorreta; fontes, inconsistências e alguns sinais de incerteza podem reduzir overreliance. Personalização e framing podem aumentar persuasion/opinion shift. Busca conversacional pode aumentar *confirmatory querying*.

Não emerge uma característica de interface universalmente benéfica ou prejudicial.

### 12.4 RQ4 - Como single-LLM e multi-LLM são empregados e comparados?

Apenas ST007 e ST010 são diretamente multiagentes nesta Wave 1.

ST007 compara 1, 3 e 5 agentes e encontra maior **normative influence** em condições multiagentes, além de alguns efeitos de mudança de opinião e polarização que não crescem monotonicamente com o número de agentes. Os agentes possuem identidades distintas, mas utilizam o mesmo backend GPT-4 e conteúdo argumentativo controlado.

ST010 investiga interfaces multiagentes simuladas e mostra que usuários interpretam número de agentes, discordância, crítica e consenso como sinais de confiabilidade. O estudo não testa um backend multiagente live.

A distinção entre **pluralidade percebida/social** e **independência epistemológica real** emerge, portanto, como uma questão de pesquisa promissora, mas não como conclusão causal estabelecida.

### 12.5 RQ5 - Como consenso, discordância, crítica, debate e verificação se relacionam a judgment, trust e reliance?

Nove STUDY units contribuem diretamente para esta questão. *Source checking* e verificação podem reduzir erros em alguns estudos de reliance; inconsistências e confidence cues podem estimular revisão. Debate aparece em ST006 e ST007. ST010 explora diretamente disagreement, critique e consensus como sinais usados pelos participantes para interpretar a confiabilidade.

O padrão transversal é que cues do processo alteram a forma como usuários avaliam e utilizam respostas LLM, mas a direção não é fixa. Consenso e número de agentes podem funcionar como heurísticas de confiabilidade sem garantir independência ou correção.

### 12.6 RQ6 - Quais limitações e lacunas permanecem?

As limitações autorreportadas incluem amostras pequenas em estudos qualitativos, tarefas curtas ou fechadas, populações online específicas, respostas pré-geradas, interfaces experimentais/mock, generalização limitada para outros modelos/domínios e efeitos dependentes da tarefa ou wording.

Para o corpus desta Wave 1, destacam-se quatro lacunas descritivas:

1. baixa cobertura direta de vieses cognitivos humanos em comparação com fenômenos associados;
2. ausência de anchoring bias entre as unidades incluídas;
3. pouca evidência comparativa direta entre single- e multi-LLM;
4. ausência de manipulação explícita da diferença entre independência **real** e **percebida** entre agentes.

Essas lacunas são restritas ao corpus analisado e não constituem afirmações de ausência na literatura global.

---

## 13. Síntese transversal da evidência

| Tema | STUDY units | Síntese descritiva |
|---|---|---|
| Confirmation bias / selective exposure | ST011; ST012 | Busca conversacional e LLM consonante com atitudes prévias podem aumentar *confirmatory querying*; efeitos posteriores sobre atitudes e argumentos são mistos. |
| Overreliance / appropriate reliance | ST001–ST005; ST013 | LLMs incorretos podem induzir overreliance; fontes, inconsistências, wording de incerteza e confidence cues podem mitigar parte dos erros, mas também produzir underreliance ou efeitos dependentes da formulação. |
| Persuasion / belief-opinion change | ST006; ST008; ST009 | Personalização e framing podem deslocar opiniões; diálogo baseado em evidência pode reduzir confiança em crenças não sustentadas. |
| Multi-agent social influence / sensemaking | ST007; ST010 | Pluralidade de agentes pode aumentar normative influence e atuar como cue de confiabilidade; independência epistemológica real não foi estabelecida como mecanismo causal. |

---

## 14. Principais limitações desta entrega

Esta release possui limitações explícitas:

- a busca definitiva foi realizada apenas no **Scopus**;
- apenas uma primeira Wave de 10 reports passou por full-text screening, embora o pool Scopus contenha 1.419 candidatos;
- screening e extração foram **AI-assisted**, sem segundo revisor humano independente;
- as 13 unidades permanecem com `researcher_check_status=PENDING`;
- a síntese é descritiva e não combina estatisticamente resultados heterogêneos;
- a avaliação formal de qualidade/risk of bias dos estudos primários ainda não foi aplicada;
- resultados desta Wave 1 não devem ser generalizados como retrato definitivo de toda a literatura.

---

## 15. Conclusão

A primeira release do mapeamento identificou e validou em texto completo **10 reports primários**, correspondentes a **13 unidades empíricas**. A maior parte da evidência selecionada investiga fenômenos associados ao julgamento humano - especialmente reliance, overreliance, trust calibration, persuasion e social influence - enquanto evidência direta de cognitive bias apareceu, nesta Wave 1, principalmente em confirmation bias/selective exposure.

Os resultados mostram que LLMs podem estar associados tanto à **amplificação** quanto à **mitigação** de padrões problemáticos de julgamento humano, dependendo da arquitetura da interação, da correção da resposta, das pistas fornecidas pela interface e da tarefa. Os dados não sustentam uma interpretação simples segundo a qual mais explicação, mais transparência ou mais agentes sejam necessariamente benéficos.

No recorte multiagente, a diferença entre **quantidade de agentes apresentada ao usuário** e **independência epistemológica real das fontes** surge como uma direção promissora para investigação futura. Nesta etapa, porém, ela permanece uma hipótese derivada da síntese, não uma conclusão causal.

---

## 16. Referências dos 10 reports primários

1. Kim S.S.Y., Liao Q.V., Vorvoreanu M., Ballard S., Vaughan J.W. (2024). *"I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust*. 2024 ACM Conference on Fairness, Accountability, and Transparency, FAccT 2024. https://doi.org/10.1145/3630106.3658941
2. Sharma N., Liao Q.V., Xiao Z. (2024). *Generative Echo Chamber? Efects of LLM-Powered Search Systems on Diverse Information Seeking*. Conference on Human Factors in Computing Systems - Proceedings. https://doi.org/10.1145/3613904.3642459
3. Bo J.Y., Wan S., Anderson A. (2025). *To Rely or Not to Rely? Evaluating Interventions for Appropriate Reliance on Large Language Models*. Conference on Human Factors in Computing Systems - Proceedings . https://doi.org/10.1145/3706598.3714097
4. Boissin E., Costello T.H., Spinoza-Martín D., Rand D.G., Pennycook G. (2025). *Dialogues with large language models reduce conspiracy beliefs even when the AI is perceived as human*. PNAS Nexus. https://doi.org/10.1093/pnasnexus/pgaf325
5. Kim S.S.Y., Vaughan J.W., Liao Q.V., Lombrozo T., Russakovsky O. (2025). *Fostering Appropriate Reliance on Large Language Models: The Role of Explanations, Sources, and Inconsistencies*. Conference on Human Factors in Computing Systems - Proceedings . https://doi.org/10.1145/3706598.3714020
6. Salvi F., Horta Ribeiro M., Gallotti R., West R. (2025). *On the conversational persuasiveness of GPT-4*. Nature Human Behaviour. https://doi.org/10.1038/s41562-025-02194-6
7. Song T., Tan Y., Zhu Z., Feng Y., Lee Y.-C. (2025). *Multi-Agents are Social Groups: Investigating Social Influence of Multiple Agents in Human-Agent Interactions*. Proceedings of the ACM on Human-Computer Interaction. https://doi.org/10.1145/3757633
8. Spatharioti S.E., Rothschild D., Goldstein D.G., Hofman J.M. (2025). *Effects of LLM-based Search on Decision Making: Speed, Accuracy, and Overreliance*. Conference on Human Factors in Computing Systems - Proceedings . https://doi.org/10.1145/3706598.3714082
9. Pareek S., Govers J., Kollerup N.K., Wong E., Velloso E., Goncalves J. (2026). *Sensemaking in Multi-Agent LLM Interfaces: How Users Interpret Transparency and Trustworthiness Cues*. Conference on Human Factors in Computing Systems - Proceedings . https://doi.org/10.1145/3772318.3791157
10. Shu M., Karell D., Okura K., Davidson T.R. (2026). *How latent and prompting biases in AI-generated historical narratives influence opinions*. PNAS Nexus. https://doi.org/10.1093/pnasnexus/pgag022

## 17. Referências metodológicas

1. Kitchenham, B., Madeyski, L., & Budgen, D. (2023). *SEGRESS: Software Engineering Guidelines for REporting Secondary Studies*. IEEE Transactions on Software Engineering, 49(3), 1273–1292. https://doi.org/10.1109/TSE.2022.3174092
2. Kitchenham, B., & Charters, S. (2007). *Guidelines for performing Systematic Literature Reviews in Software Engineering*. EBSE Technical Report EBSE-2007-01.

---

## 18. Observação sobre reprodutibilidade

Os artefatos intermediários desta execução - strings, exports, consolidação, deduplicação, screening, codebook, full-text manifest, resolução REPORT→STUDY, template de extração, logs de adjudicação e matrizes de evidência - estão sendo preservados no repositório do projeto para permitir auditoria e evolução das próximas releases.