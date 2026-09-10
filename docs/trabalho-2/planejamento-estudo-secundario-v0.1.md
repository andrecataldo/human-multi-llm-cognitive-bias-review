# Trabalho 2 - Planejamento do Estudo Secundário

> **Versão:** v0.1  
> **Data:** 2026-09-10  
> **Tema:** Vieses cognitivos humanos em julgamentos mediados por LLMs: o papel de sistemas multiagentes  
> **Status:** planejamento preliminar, a ser refinado após a execução completa das buscas e do screening piloto.

## 1. Estudo de mapeamento prévio

### 1.1 Objetivo do mapeamento

Antes da definição do protocolo definitivo, foi realizado um mapeamento exploratório preliminar para compreender as principais ramificações do tema, testar termos de busca, estimar o volume de literatura e identificar dimensões úteis para classificação dos estudos.

O foco conceitual adotado foi a investigação de **vieses cognitivos humanos em processos de julgamento e tomada de decisão mediados por Large Language Models (LLMs)**, com atenção particular a sistemas multiagentes. O humano é tratado como sujeito cognitivo; os LLMs, individuais ou organizados em arquiteturas multiagentes, são considerados mecanismos de mediação capazes de influenciar, amplificar ou mitigar processos de julgamento.

O mapeamento inicial foi executado no **Scopus**, utilizando o campo `TITLE-ABS-KEY` e o período de 2023 a 2026. Foram construídas três famílias exploratórias de busca:

- **M1 - Human–LLM Cognitive Bias:** vieses cognitivos, reliance e julgamento humano;
- **M2 - Human–LLM Interaction / Reliance:** confiança, reliance e mecanismos de interação;
- **M3 - Human–Multi-Agent LLM:** sistemas multiagentes e dimensão humana/decisória.

### 1.2 Resultados das buscas piloto

| Busca | Foco | Resultados |
|---|---|---:|
| M1-v0.1 | Human–LLM + Cognitive Bias | 1.463 |
| M2-v0.1 | Human–LLM + Trust/Reliance/Interaction | 3.380 |
| M3-v0.1 | Human–Multi-Agent / Agentic AI | 6.540 |
| M3-v0.2 | Human–Multi-Agent LLM refinada | 1.477 |

A M3-v0.1 apresentou recall excessivamente amplo. A inspeção dos resultados mostrou recuperação de estudos sobre Agentic AI e colaboração entre agentes sem envolvimento explícito de LLMs ou de julgamento humano. Em resposta, a estratégia foi refinada para exigir simultaneamente três componentes: **LLM/Generative AI + configuração multiagente + dimensão humana ou decisória**. A nova versão reduziu o total de 6.540 para 1.477 documentos, uma redução de aproximadamente 77,4%, confirmando a utilidade do mapping como mecanismo de calibração da estratégia.

A literatura identificada apresentou crescimento fortemente recente:

| Busca | 2023 | 2024 | 2025 | 2026 |
|---|---:|---:|---:|---:|
| M1 | 24 | 163 | 542 | 734 |
| M2 | 65 | 359 | 1.084 | 1.872 |
| M3-v0.2 | 7 | 107 | 528 | 835 |

Os três conjuntos foram comparados por identificador Scopus (`EID`). A união deduplicada de M1, M2 e M3-v0.2 totalizou **5.824 documentos**. Foram observadas as seguintes sobreposições:

| Interseção | Registros |
|---|---:|
| M1 ∩ M2 | 334 |
| M1 ∩ M3-v0.2 | 53 |
| M2 ∩ M3-v0.2 | 120 |
| M1 ∩ M2 ∩ M3-v0.2 | 11 |

A baixa sobreposição entre as três famílias indica que elas acessam regiões conceituais diferentes e complementares da literatura.

### 1.3 Leitura exploratória de estudos-semente

A leitura rápida de títulos, resumos e, quando disponíveis, introduções e conclusões de estudos recuperados ajudou a refinar o escopo e o esquema de classificação. Alguns exemplos informativos são apresentados abaixo.

| Estudo | Desenho/População | Fenômeno principal | Contribuição para o mapping |
|---|---|---|---|
| O’Leary (2026), *Do users anchor on large language model rankings? How do they adjust?* | Experimento com usuários | Anchoring | Evidência direta de ancoragem em rankings numéricos fornecidos por LLM |
| Du, Liu & Xian (2026), *Automation bias in teachers’ evaluation of student writing...* | Experimento 2×2, 214 professores | Automation bias / confirmation / anchoring | Mostra que sinais algorítmicos e visuais podem alterar avaliações humanas mesmo com o texto mantido constante |
| He, Demartini & Gadiraju (2025), *Plan-Then-Execute...* | Estudo empírico, N=248 | Trust / human involvement | Mostra que participação humana e qualidade do planejamento afetam confiança e desempenho com LLM agents |
| Song et al. (2025), *Multi-Agents are Social Groups...* | Estudo com interação single-agent vs multi-agent | Social influence / opinion change | Indica que múltiplos agentes podem aumentar pressão social percebida e mudança de opinião |
| Xie et al. (2024), *WaitGPT...* | Formative study N=8 + user study N=12 | Verification / confidence | Explora monitoramento, verificação e steering humano em interação com agente LLM |

Esses trabalhos não constituem ainda o corpus final da revisão. Eles são utilizados como **estudos-semente** para compreender a terminologia, identificar dimensões relevantes e apoiar a validação das futuras strings de busca.

### 1.4 Esquema de classificação preliminar

O mapeamento levou à construção do seguinte esquema de classificação:

| Dimensão | Categorias preliminares |
|---|---|
| Tipo de pesquisa | empírico com humanos; empírico model-only; teórico; estudo secundário |
| Método | experimento controlado; experimento de campo; user study; survey; qualitativo; observacional; mixed methods; simulação |
| Arquitetura | single-LLM; single-agent; multi-agent; generic AI |
| Configuração dos agentes | mesmo modelo; modelos heterogêneos; não informado |
| População | público geral; estudantes; profissionais; knowledge workers; especialistas; desenvolvedores; gestores |
| Contexto | saúde; educação; software; trabalho; design; hiring; decisão organizacional; outros |
| Viés principal | confirmation; anchoring; automation; outros |
| Fenômeno relacionado | overreliance; appropriate reliance; trust calibration; persuasion; mental models |
| Mecanismo de interação | advice; explanation; agreement; disagreement; debate; critique; verification; consensus |
| Outcome | mudança de julgamento; belief change; decision accuracy; confidence; trust; reliance; verification behavior |
| Locus do viés | HUMAN; MODEL; INTERACTION; UNCLEAR |
| Relação humano–IA | MEDIATED_USE; COLLABORATIVE_USE; COMPARATIVE_ONLY; PERCEPTION_ADOPTION; MODEL_ONLY; UNCLEAR |

### 1.5 Subtópicos consolidados, emergentes e potenciais lacunas

O mapping preliminar sugere três níveis de maturidade.

**Mais explorados:** trust, reliance/overreliance, explanations, recommendations/advice, arquitetura de agentes, coordenação e colaboração multiagente.

**Em crescimento:** Human–LLM interaction, human oversight, verification, mental models, human–agent collaboration e multi-agent debate/consensus.

**Potenciais lacunas:** confirmation bias e anchoring humanos em interação com LLMs; efeitos de consenso e discordância entre múltiplos agentes sobre o julgamento humano; percepção de independência entre agentes; e comparação sistemática entre single-LLM e multi-LLM quanto à amplificação ou mitigação de vieses cognitivos.

Esses pontos são tratados como **hipóteses de lacuna**, não como conclusões definitivas. A confirmação dependerá da revisão sistemática completa.

---

## 2. Questões de pesquisa

### 2.1 Estrutura PICOC

| Elemento | Definição |
|---|---|
| **P - Population** | Pessoas envolvidas em tarefas de julgamento ou tomada de decisão mediadas por LLMs |
| **I - Intervention** | Uso de LLMs como apoio à decisão, incluindo single-LLM e sistemas multiagentes |
| **C - Comparison** | sem IA; single-LLM vs multi-LLM; diferentes padrões de interação, como consenso, discordância, crítica ou verificação |
| **O - Outcomes** | confirmation bias, anchoring bias, automation bias, overreliance, trust calibration, mudança de julgamento, confiança e qualidade da decisão |
| **C - Context** | HCI / Human–AI Interaction em tarefas de julgamento e tomada de decisão, em diferentes domínios |

A formulação PICOC resultante é:

> **Em pessoas envolvidas em tarefas de julgamento ou tomada de decisão, como o uso de LLMs - especialmente sistemas multiagentes - comparado a outras formas de apoio ou interação, influencia vieses cognitivos humanos e outcomes associados à confiança, reliance e qualidade da decisão?**

### 2.2 Estrutura GQM

**Goal**

> **Analisar estudos primários empíricos sobre processos humanos de julgamento e tomada de decisão mediados por Large Language Models, com o propósito de compreender como diferentes formas de interação e arquitetura - especialmente single-LLM e sistemas multiagentes - influenciam a manifestação, amplificação ou mitigação de vieses cognitivos humanos, particularmente confirmação e ancoragem, da perspectiva de pesquisadores em HCI e Human–AI Interaction.**

| Goal Question | Dados/Métricas a extrair |
|---|---|
| Que evidências empíricas existem? | ano, venue, domínio, país, tipo de estudo |
| Quais vieses são investigados? | confirmation, anchoring, automation, outros |
| Como são operacionalizados? | mudança de escolha, escalas, erro, confidence, belief change |
| Como ocorre a mediação por LLM? | modelo, arquitetura, número de agentes, sequência e interface |
| Que mecanismos são estudados? | advice, explanation, agreement, disagreement, critique, verification, consensus |
| Qual o efeito observado? | amplificação, mitigação, efeito nulo ou misto |
| Que fatores moderam o efeito? | expertise, trust, task complexity, model accuracy, timing, explanation |
| Qual a qualidade da evidência? | desenho, amostra, controles, validade e transparência |
| Onde estão as lacunas? | populações, mecanismos, comparações e resultados pouco investigados |

### 2.3 Questão principal

> **Que evidências empíricas existem sobre como Large Language Models, particularmente sistemas multiagentes, influenciam a manifestação, amplificação ou mitigação de vieses cognitivos humanos em processos de julgamento e tomada de decisão?**

### 2.4 Questões secundárias

**RQ1.** Quais vieses cognitivos humanos têm sido investigados em processos de julgamento e tomada de decisão mediados por LLMs, e com que frequência aparecem vieses de confirmação e ancoragem?

**RQ2.** Como esses vieses e outcomes relacionados são definidos, operacionalizados e medidos nos estudos empíricos?

**RQ3.** Quais características da interação humano–LLM estão associadas à amplificação ou mitigação de vieses cognitivos humanos?

**RQ4.** Como arquiteturas single-LLM e multi-LLM são empregadas nos estudos e que diferenças são observadas em seus efeitos sobre o julgamento humano?

**RQ5.** Em sistemas multiagentes, como mecanismos como consenso, discordância, crítica, debate e verificação influenciam o julgamento, a confiança e a reliance do usuário?

**RQ6.** Quais limitações metodológicas, inconsistências e lacunas permanecem na evidência disponível sobre vieses cognitivos humanos em interações com LLMs?

### 2.5 Plano conceitual e plano operacional

**Plano conceitual.** O estudo busca contribuir para a compreensão de LLMs como mediadores sociotécnicos do julgamento humano, distinguindo vieses cognitivos do usuário, comportamentos produzidos pelo modelo e efeitos emergentes da interação. A revisão pretende organizar a literatura segundo mecanismos de mediação - como aconselhamento, explicação, consenso, discordância, crítica e verificação - e investigar como esses mecanismos se relacionam com a amplificação ou mitigação de vieses de confirmação e ancoragem.

**Plano operacional.** Serão identificados e sintetizados estudos primários empíricos envolvendo participantes humanos em tarefas de julgamento ou tomada de decisão com LLMs. Para cada estudo serão extraídos desenho experimental, população, contexto, modelo utilizado, configuração single ou multiagente, mecanismos de interação, viés investigado, forma de mensuração, outcomes, moderadores, resultados e qualidade metodológica.

---

## 3. Estratégia de busca

### 3.1 Princípios

A estratégia definitiva foi refinada a partir do mapping e organizada em três famílias complementares. O objetivo é preservar recall sem recorrer a uma única string excessivamente ampla.

- **S1 - Cognitive Bias Core:** busca vieses cognitivos explicitamente relacionados a LLMs e participantes humanos;
- **S2 - Reliance / Belief-Change Bridge:** busca reliance, trust calibration, persuasão e mudança de crença ligados a julgamento ou mecanismos de interação;
- **S3 - Human–Multi-Agent LLM:** busca especificamente o recorte multiagente.

Termos muito amplos, como `trust`, `confidence` e `recommendation`, não serão utilizados isoladamente.

### 3.2 S1 - Cognitive Bias Core

```text
TITLE-ABS-KEY(
  "large language model"
  OR "large language models"
  OR LLM
  OR LLMs
  OR "generative AI"
  OR "generative artificial intelligence"
  OR ChatGPT
)
AND
TITLE-ABS-KEY(
  human
  OR humans
  OR user
  OR users
  OR participant
  OR participants
  OR people
)
AND
TITLE-ABS-KEY(
  "cognitive bias"
  OR "cognitive biases"
  OR "confirmation bias"
  OR "anchoring bias"
  OR "automation bias"
  OR debiasing
)
```

### 3.3 S2 - Reliance / Belief-Change Bridge

```text
TITLE-ABS-KEY(
  "large language model"
  OR "large language models"
  OR LLM
  OR LLMs
  OR "generative AI"
  OR "generative artificial intelligence"
  OR ChatGPT
)
AND
TITLE-ABS-KEY(
  human
  OR humans
  OR user
  OR users
  OR participant
  OR participants
  OR people
)
AND
TITLE-ABS-KEY(
  overreliance
  OR "over reliance"
  OR "appropriate reliance"
  OR reliance
  OR "trust calibration"
  OR "calibrated trust"
  OR "appropriate trust"
  OR "algorithm aversion"
  OR "algorithm appreciation"
  OR persuasion
  OR persuasive
  OR "belief change"
  OR "opinion change"
  OR "social influence"
)
AND
TITLE-ABS-KEY(
  judgment
  OR judgement
  OR "decision making"
  OR "decision-making"
  OR choice
  OR choices
  OR belief
  OR beliefs
  OR opinion
  OR opinions
  OR advice
  OR recommendation
  OR recommendations
  OR explanation
  OR explanations
  OR verification
)
```

### 3.4 S3 - Human–Multi-Agent LLM

```text
TITLE-ABS-KEY(
  "large language model"
  OR "large language models"
  OR LLM
  OR LLMs
  OR "generative AI"
  OR "generative artificial intelligence"
  OR ChatGPT
)
AND
TITLE-ABS-KEY(
  "multi agent"
  OR "multi-agent"
  OR multiagent
  OR "LLM agent"
  OR "LLM agents"
  OR "agentic AI"
  OR "agent debate"
  OR "multi agent debate"
  OR "multi-agent debate"
  OR "agent collaboration"
  OR "multi agent collaboration"
  OR "multi-agent collaboration"
)
AND
TITLE-ABS-KEY(
  human
  OR humans
  OR user
  OR users
  OR participant
  OR participants
  OR people
)
AND
TITLE-ABS-KEY(
  judgment
  OR judgement
  OR "decision making"
  OR "decision-making"
  OR belief
  OR beliefs
  OR opinion
  OR opinions
  OR "cognitive bias"
  OR "confirmation bias"
  OR "anchoring bias"
  OR "automation bias"
  OR overreliance
  OR reliance
  OR "trust calibration"
  OR persuasion
  OR "social influence"
)
```

### 3.5 Período

O mapping utilizou 2023–2026 para caracterizar a literatura contemporânea. Para a busca definitiva, o período proposto é **2020 a setembro de 2026**, a fim de reduzir o risco de exclusão de estudos pioneiros envolvendo GPT-3 e LLMs anteriores à popularização do ChatGPT.

### 3.6 Bases de dados

As seguintes bases são propostas:

| Base | Papel esperado |
|---|---|
| Scopus | cobertura multidisciplinar e baseline do mapping |
| Web of Science Core Collection | cobertura multidisciplinar complementar |
| ACM Digital Library | HCI, Human–AI Interaction e Computação |
| IEEE Xplore | sistemas inteligentes, agentes e Human–AI |
| PubMed/MEDLINE | saúde, decisão clínica e interação humano–IA |
| APA PsycINFO | psicologia cognitiva, julgamento, decisão e persuasão, mediante disponibilidade institucional |

Até esta versão do protocolo, apenas **Scopus foi pilotada empiricamente**. A utilidade relativa das demais bases será avaliada na execução da busca definitiva; portanto, ainda não se afirma que todas apresentem o mesmo desempenho ou cobertura.

### 3.7 Métodos complementares

Após a seleção inicial, serão utilizados:

- backward snowballing;
- forward snowballing;
- busca por referências de estudos altamente aderentes;
- Google Scholar como mecanismo auxiliar de descoberta e citação, não como base principal do corpus.

### 3.8 Validação da estratégia

A estratégia será validada com um **known-set de estudos primários**, dividido em:

- **Calibration set:** estudos usados para verificar se os termos recuperam evidências conhecidas;
- **Holdout set:** estudos não usados para ajustar a string e utilizados posteriormente para verificar generalização da estratégia.

---

## 4. Critérios de inclusão e exclusão

### 4.1 Inclusão

**I1 - Estudo primário empírico.** Deve reportar dados empíricos originais, quantitativos, qualitativos ou mistos.

**I2 - Participantes humanos.** Deve envolver seres humanos como participantes, usuários, decisores ou avaliadores.

**I3 - Uso de LLMs.** A intervenção ou sistema deve utilizar Large Language Models, Generative AI baseada em LLMs ou agentes cuja capacidade principal dependa de LLMs.

**I4 - Processo de julgamento ou tomada de decisão.** Os participantes devem realizar julgamento, escolha, avaliação, formação/revisão de crença, recomendação, priorização ou decisão.

**I5 - Fenômeno cognitivo ou mecanismo relacionado.** O estudo deve investigar confirmation bias, anchoring bias, automation bias, overreliance, appropriate reliance, trust calibration, belief/opinion change, persuasion ou mecanismo diretamente ligado ao julgamento humano.

**I6 - Relação entre LLM e outcome humano.** Deve ser possível relacionar alguma característica da mediação por LLM ao comportamento, julgamento, confiança, reliance ou decisão do participante.

**I7 - Período.** Publicações entre 2020 e setembro de 2026.

**I8 - Tipo de publicação.** Artigos de periódicos e trabalhos completos em conferências científicas peer-reviewed.

**I9 - Texto integral disponível.** O texto completo deve permitir avaliação metodológica e extração.

### 4.2 Exclusão

**E1 - Model-only.** Estudos exclusivamente sobre vieses, raciocínio ou comportamento do LLM sem participantes humanos.

**E2 - Comparação humano versus LLM sem mediação.** Estudos que apenas comparem desempenho de humanos e modelos sem que o LLM participe do processo decisório humano.

**E3 - Bias social/fairness sem componente cognitivo humano.** Estudos centrados exclusivamente em gênero, raça, política, demografia, fairness, discriminação ou estereótipos sem relação com julgamento humano mediado.

**E4 - Estudos puramente técnicos.** Trabalhos sobre fine-tuning, prompting, alignment, hallucination, safety ou debiasing do modelo sem avaliação de impacto humano.

**E5 - Trust/adoption sem julgamento ou decisão.** Surveys de percepção, intenção de uso, satisfação ou aceitação sem tarefa decisória relevante.

**E6 - Multi-agent sem componente humano relevante.** Estudos de debate, coordenação ou consenso exclusivamente entre agentes.

**E7 - IA não baseada em LLM.** Estudos exclusivamente sobre sistemas de IA não baseados em LLMs.

**E8 - Estudos secundários ou não empíricos.** Revisões, mappings, surveys de literatura, editoriais, position papers e trabalhos conceituais sem dados empíricos originais.

**E9 - Informação metodológica insuficiente.** Posters, abstracts estendidos ou publicações que não permitam avaliar método e resultados.

**E10 - Duplicatas.** Quando múltiplas publicações utilizarem os mesmos dados, será preservada a versão mais completa e as demais serão registradas como relacionadas.

### 4.3 Preprints

Preprints não comporão o corpus principal peer-reviewed, mas poderão ser registrados em uma **emerging-evidence watchlist**, especialmente por se tratar de um tema recente.

### 4.4 Processo de screening

O screening será realizado em duas etapas:

1. **Título e resumo:** em casos de dúvida, o estudo será mantido para reduzir falsos negativos.
2. **Texto integral:** aplicação completa dos critérios I1–I9 e E1–E10.

Para exclusões em texto integral, será registrada uma razão principal padronizada.

---

## 5. Avaliação de qualidade e extração de dados

### 5.1 Princípios de qualidade

QAISER não será utilizado para os estudos primários, pois foi concebido para avaliar revisões sistemáticas. A qualidade metodológica dos estudos primários será avaliada com um instrumento compatível com os diferentes desenhos empíricos encontrados.

A qualidade **não será utilizada como filtro automático de inclusão**. Ela será empregada para:

- caracterizar a força da evidência;
- interpretar resultados;
- estratificar estudos;
- realizar análises de sensibilidade.

A versão inicial do instrumento será pilotada e poderá ser substituída ou complementada por instrumentos validados específicos para os desenhos encontrados antes da execução definitiva.

### 5.2 QA-Primary v0.1

| ID | Critério | Pergunta operacional |
|---|---|---|
| QA1 | Objetivo | Objetivo, hipótese ou questão estão claramente definidos? |
| QA2 | População | Participantes, recrutamento e amostra estão adequadamente descritos? |
| QA3 | Desenho | O desenho empírico é apropriado para responder à questão? |
| QA4 | Intervenção LLM | Modelo, versão, prompts/configuração e interação são suficientemente documentados? |
| QA5 | Operacionalização | O viés ou outcome está claramente definido e adequadamente medido? |
| QA6 | Comparação/controle | Há baseline ou condição de comparação apropriada quando necessária? |
| QA7 | Análise | Os métodos quantitativos ou qualitativos são adequados? |
| QA8 | Validade | Confundidores, ameaças à validade e limitações são tratados? |
| QA9 | Rastreabilidade | As conclusões são sustentadas pelos resultados? |
| QA10 | Transparência | Materiais, dados, código, preregistration, financiamento e conflitos são adequadamente reportados? |

Escala:

- **Y** - atendido;
- **PY** - parcialmente atendido;
- **N** - não atendido;
- **U** - não informado / informação insuficiente;
- **NA** - não aplicável.

Não será utilizado um escore agregado simples.

### 5.3 Critical flags

Algumas fragilidades serão registradas separadamente por sua relevância direta para as RQs:

```text
CRITICAL_BIAS_MEASURE
CRITICAL_COMPARATOR
CRITICAL_LLM_DOCUMENTATION
CRITICAL_HUMAN_SAMPLE
CRITICAL_ANALYSIS
```

### 5.4 Formulário de extração

#### A. Proveniência

```text
study_id
title
authors
year
venue
doi
database_source
query_source
extractor
extraction_date
study_family_id
```

#### B. Desenho e população

```text
study_type
research_design
domain
country
sample_size
population
expertise
recruitment
```

#### C. Tecnologia e arquitetura

```text
model_provider
model_name
model_version
model_access_date
architecture
n_agents
agent_models
agent_roles
interface_type
interaction_turns
prompt_available
```

#### D. Variáveis cognitivas

```text
bias_locus
bias_type
bias_explicit
bias_definition
bias_operationalization
initial_judgment
final_judgment
belief_change
decision_accuracy
```

#### E. Interação humano–LLM

```text
human_ai_relation
advice
explanation
verification
agreement
disagreement
critique
debate
consensus
persuasion
human_final_decision
```

#### F. Trust e reliance

```text
trust_measure
trust_calibration
reliance_measure
appropriate_reliance
overreliance
confidence
perceived_accuracy
perceived_independence
actual_agent_independence
```

#### G. Resultados

```text
outcome_name
direction
effect_measure
effect_value
confidence_interval
p_value
authors_interpretation
reviewer_interpretation
```

#### H. Qualidade

```text
qa1_objective
qa2_population
qa3_design
qa4_llm
qa5_outcome
qa6_comparison
qa7_analysis
qa8_validity
qa9_traceability
qa10_transparency
critical_flags
quality_notes
```

Estados de dados ausentes:

- `NR` - Not Reported;
- `NA` - Not Applicable;
- `UNCLEAR` - informação ambígua.

### 5.5 Procedimento de extração

O formulário será inicialmente pilotado em aproximadamente 5 a 10 estudos heterogêneos, incluindo single-LLM, multi-agent, confirmation/anchoring, trust/reliance, experimento controlado e user study.

Após o piloto serão avaliados:

- clareza das categorias;
- campos ausentes;
- redundâncias;
- dificuldades de codificação;
- capacidade de os dados extraídos responderem às RQs.

Na execução individual, será empregado procedimento de **test–retest** em uma amostra aleatória de aproximadamente 20% dos estudos. Quando possível, uma parcela também será conferida por outro pesquisador.

Publicações que reportem o mesmo experimento ou conjunto de dados serão vinculadas por `study_family_id` para evitar dupla contagem.

### 5.6 Uso da qualidade na síntese

A síntese será realizada em três níveis:

1. **Síntese principal:** todos os estudos elegíveis;
2. **Síntese estratificada:** comparação segundo características metodológicas relevantes;
3. **Análise de sensibilidade:** verificação de mudanças nas conclusões quando estudos com critical flags forem separados.

---

## 6. Modelo conceitual preliminar

```text
               HUMAN INITIAL STATE
        beliefs / prior judgment / expertise
                       │
                       ▼
              LLM MEDIATION
                       │
          ┌────────────┴────────────┐
          │                         │
      Single LLM                Multi-LLM
                                    │
                         ┌──────────┼──────────┐
                         │          │          │
                     consensus  disagreement critique
                         │          │          │
                         └────── verification ─┘
                                    │
                                    ▼
                         HUMAN–AI INTERACTION
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                   trust         reliance       confidence
                    │               │               │
                    └───────────────┼───────────────┘
                                    ▼
                           HUMAN JUDGMENT
                                    │
                       ┌────────────┴────────────┐
                       │                         │
                 amplification              mitigation
                       │                         │
                confirmation bias         confirmation bias
                anchoring bias            anchoring bias
```

---

## 7. Principais decisões decorrentes do mapping

1. **Confirmation bias e anchoring bias permanecem os fenômenos cognitivos centrais.**
2. **Trust, reliance e overreliance são tratados como fenômenos relacionados, moderadores ou outcomes, não como sinônimos de cognitive bias.**
3. **Sistemas multiagentes são tratados como dimensão arquitetural e interacional, e não como sujeitos cognitivos.**
4. **LLM passa a ser requisito explícito da busca definitiva.**
5. **A estratégia será organizada em famílias complementares de busca, e não em uma mega-query.**
6. **Bias do modelo e bias humano serão separados por `bias_locus`.**
7. **Estudos model-only e comparações humano-vs-LLM sem mediação serão separados do corpus principal.**
8. **A percepção de independência entre múltiplos agentes passa a ser uma variável de interesse potencial.**
9. **O período definitivo será ampliado para 2020–2026 para reduzir risco de perda de estudos pioneiros.**
10. **O protocolo será atualizado após a validação do known-set e pilotagem das bases adicionais.**

---

## 8. Limitações da versão v0.1

- O mapping quantitativo foi pilotado apenas no Scopus.
- As demais bases ainda não tiveram desempenho empiricamente comparado.
- O screening sistemático dos 5.824 registros deduplicados ainda não foi executado.
- As lacunas identificadas são preliminares.
- O instrumento QA-Primary v0.1 ainda precisa ser pilotado e refinado.
- O known-set definitivo de estudos primários ainda será formalizado em calibration e holdout sets.
- A estratégia S1/S2/S3 ainda deverá ser executada e validada em cada base antes de ser considerada congelada.

---

## 9. Uso de Inteligência Artificial Generativa

Ferramentas de Inteligência Artificial Generativa foram utilizadas como apoio à **revisão textual, organização de ideias, estruturação do material e refinamento de trechos**. A seleção das fontes, a definição dos critérios metodológicos, a interpretação acadêmica dos estudos, a análise crítica dos resultados e a redação final são de responsabilidade exclusiva do autor.

---

## 10. Referências metodológicas

- Kitchenham, B., & Charters, S. (2007). *Guidelines for performing Systematic Literature Reviews in Software Engineering*. EBSE Technical Report EBSE-2007-01, Version 2.3.
- Usman, M., Ali, N. B., & Wohlin, C. (2023). *A Quality Assessment Instrument for Systematic Literature Reviews in Software Engineering*. e-Informatica Software Engineering Journal, 17(1), 230105. https://doi.org/10.37190/e-Inf230105

## 11. Estudos-semente citados no mapping

- O’Leary, D. E. (2026). *Do users anchor on large language model rankings? How do they adjust?* Journal of Decision Systems, 35(1). https://doi.org/10.1080/12460125.2026.2688523
- Du, P., Liu, T., & Xian, X. (2026). *Automation bias in teachers’ evaluation of student writing: effects of algorithmic warnings and visual risk cues in AI detection reports*. Frontiers in Psychology, 17. https://doi.org/10.3389/fpsyg.2026.1889402
- He, G., Demartini, G., & Gadiraju, U. (2025). *Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant*. CHI 2025. https://doi.org/10.1145/3706598.3713218
- Song, T., Tan, Y., Zhu, Z., Feng, Y., & Lee, Y.-C. (2025). *Multi-Agents are Social Groups: Investigating Social Influence of Multiple Agents in Human-Agent Interactions*. Proceedings of the ACM on Human-Computer Interaction, 9(7), 1–33. https://doi.org/10.1145/3757633
- Xie, L., Zheng, C., Xia, H., Qu, H., & Zhu-Tian, C. (2024). *WaitGPT: Monitoring and Steering Conversational LLM Agent in Data Analysis with On-the-Fly Code Visualization*. UIST 2024.
