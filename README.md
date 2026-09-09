# Human Multi-LLM Cognitive Bias Review

Repositório de trabalho para o levantamento e planejamento de estudos secundários sobre **vieses cognitivos humanos em julgamentos mediados por Large Language Models (LLMs), com atenção especial a sistemas multiagentes**.

## Título de trabalho

**Vieses cognitivos humanos em julgamentos mediados por LLMs: o papel de sistemas multiagentes**

## Problema de pesquisa

**Como a mediação por Large Language Models, particularmente por sistemas multiagentes, influencia a manifestação, amplificação ou mitigação de vieses cognitivos humanos em processos de julgamento e tomada de decisão?**

Questão específica orientadora:

**Como concordância, discordância, crítica e verificação entre agentes LLM influenciam os vieses de confirmação e ancoragem no julgamento humano?**

## Objetivo geral

Investigar como diferentes formas de mediação por Large Language Models, especialmente sistemas multiagentes, influenciam vieses cognitivos humanos em processos de julgamento e tomada de decisão.

## Escopo conceitual

O humano é tratado como o **sujeito cognitivo**. LLMs - individuais ou organizados em arquiteturas multiagentes - são tratados como mecanismos de mediação capazes de influenciar, amplificar ou mitigar processos de julgamento humano.

A pesquisa distingue explicitamente:

- vieses cognitivos humanos;
- comportamentos enviesados ou *bias-like* produzidos por modelos;
- efeitos emergentes da interação humano-LLM;
- dinâmicas específicas de sistemas multiagentes, como consenso, discordância, crítica, debate e verificação.

Interfaces cérebro-máquina (BMI/BCI) permanecem como **contexto de aplicação e possível extensão futura**, não como critério de inclusão da revisão atual.

## Pipeline metodológico

```text
Exploratory prior work
        ↓
Controlled vocabulary
        ↓
Known-set
        ↓
Research questions
        ↓
Search strategy
        ↓
┌──────┬──────┬──────┬──────┬───────┬───────┐
│ Q1   │ Q2   │ Q3   │ Q4   │ Q5a   │ Q5b   │
│ Bias │Trust │H-AI  │H-LLM │MA-Land│H-MA   │
└──────┴──────┴──────┴──────┴───────┴───────┘
        ↓
Scopus / Web of Science / ACM DL / IEEE Xplore / PubMed
        ↓
Raw exports
        ↓
Normalization
        ↓
Deduplication
        ↓
Title/abstract screening
        ↓
Full-text screening
        ↓
Secondary studies
        ↓
QAISER + Currency + Relevance
        ↓
Evidence matrix
        ↓
Research gaps
        ↓
Need for a new systematic review?
```

## Estrutura do repositório

```text
protocol/          protocolo, emendas e decisões metodológicas
methodology/       RQs, vocabulário, known-set, critérios e processo
searches/          estratégia conceitual e strings por base
  conceptual/
  scopus/
data/              resultados brutos e derivados
  raw/
  normalized/
  deduplicated/
  screening/
  included/
  excluded/
quality/qaiser/     avaliação metodológica das revisões
synthesis/          matrizes, sínteses e gaps
docs/               entregas da disciplina
scripts/            automações mecânicas e reprodutíveis
references/         referências metodológicas
```

## Regra de proveniência

Arquivos em `data/raw/` **não devem ser alterados**. Processamentos sempre geram novos artefatos em diretórios derivados.

Fluxo de dados:

```text
RAW → NORMALIZED → DEDUPLICATED → SCREENED → INCLUDED
```

## Papel do código

Código será usado apenas para tarefas mecânicas e auditáveis, como:

- normalização de metadados;
- união de exportações;
- deduplicação por DOI/título;
- validação do known-set;
- métricas de busca;
- contagens para PRISMA.

Decisões científicas de inclusão/exclusão e julgamento QAISER permanecem sob responsabilidade do pesquisador.

## Status

- A1 - Tema, problema e objetivo: concluído
- A2 - Modelo conceitual: concluído
- A3 - Research Questions: concluído
- A4 - Delimitação conceitual: concluído
- A5 v0.2 - Vocabulário controlado + known-set: concluído
- A6 v0.2 - Estratégia de busca + versão Scopus: pronta para pilotagem
- Próximo passo: **pilotagem Scopus Q1 → Q2 → Q3 → Q4 → Q5a → Q5b**
