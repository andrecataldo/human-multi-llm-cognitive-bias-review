# Protocolo de Levantamento de Estudos Secundários — v0.2

## 1. Objetivo

Identificar, caracterizar e avaliar estudos secundários relacionados à influência de sistemas de IA, especialmente Large Language Models e sistemas multiagentes baseados em LLMs, sobre vieses cognitivos humanos em processos de julgamento e tomada de decisão.

## 2. Questão principal

**Quais estudos secundários investigam vieses cognitivos humanos em julgamento ou tomada de decisão mediados por sistemas de IA, LLMs ou sistemas multiagentes baseados em LLMs?**

## 3. Subquestões

- **RQ1.** Quais estudos secundários investigam vieses cognitivos humanos em julgamento ou tomada de decisão mediados por IA, LLMs ou sistemas multiagentes?
- **RQ2.** Quais vieses são abordados, particularmente confirmação e ancoragem?
- **RQ3.** Quais mecanismos de interação humano–IA são associados à amplificação ou mitigação desses vieses?
- **RQ4.** Como os estudos tratam arquiteturas single-agent e multi-agent?
- **RQ5.** Qual é a atualidade das evidências sintetizadas nas revisões existentes?
- **RQ6.** Qual é o rigor metodológico dessas revisões segundo QAISER?
- **RQ7.** Quais lacunas permanecem e em que medida justificam um novo estudo secundário sobre vieses humanos em sistemas multiagentes baseados em LLMs?

## 4. Bases principais

- Scopus
- Web of Science
- ACM Digital Library
- IEEE Xplore
- PubMed

Métodos complementares previstos:

- backward snowballing;
- forward snowballing;
- Google Scholar apenas como apoio;
- OpenAlex/Semantic Scholar como mecanismos complementares de descoberta e auditoria, não substitutos das bases formais.

## 5. Período

Período inicial: **2018–2026**.

A escolha busca preservar literatura de Human–AI/XAI anterior à disseminação dos LLMs e capturar a expansão de LLMs, Agentic AI e sistemas multiagentes.

Mudanças futuras no período deverão ser registradas em `protocol/amendments.md`.

## 6. Tipos elegíveis de estudos secundários

- systematic review;
- systematic literature review;
- systematic mapping;
- scoping review;
- meta-analysis;
- rapid review;
- umbrella/tertiary review;
- critical review apenas quando houver procedimento explícito de busca e seleção.

## 7. Critérios de inclusão — versão inicial

Um estudo é candidato quando apresenta método secundário estruturado e contribui para ao menos uma combinação relevante entre:

- julgamento/tomada de decisão humana;
- IA, LLM ou sistema multiagente baseado em LLM;
- cognitive bias, trust, reliance, overreliance ou interação humano–IA.

## 8. Critérios de exclusão — versão inicial

Excluir:

- estudos primários;
- editoriais, opiniões e tutoriais sem método de revisão;
- estudos exclusivamente sobre fairness, gênero, raça, demografia, discriminação ou viés político sem relação explícita com vieses cognitivos humanos na interação;
- benchmarks de “cognitive bias in LLMs” sem dimensão humana relevante;
- duplicatas;
- estudos fora do período definido, salvo alteração formal do protocolo.

## 9. Screening

O screening será realizado em duas etapas:

1. título/resumo;
2. texto completo.

Como o estudo será conduzido por um pesquisador principal, será usada uma estratégia de mitigação para confiabilidade, por exemplo:

- teste–reteste em uma amostra de aproximadamente 15–20%; e/ou
- verificação de uma amostra por orientador/colega.

A estratégia efetivamente usada será documentada no protocolo final.

## 10. Avaliação metodológica

Será utilizado **QAISER** como instrumento principal de avaliação de qualidade metodológica de estudos secundários.

Não será utilizado um score agregado simplificado. A análise considerará julgamentos por item/grupo e avaliação global de confiabilidade e relevância.

Dimensões complementares:

- **Atualidade:** principalmente a data da última busca/evidence cutoff;
- **Aderência:** proximidade com o objeto Human Cognitive Bias × LLM × Human Judgment × Multi-Agent.

Modelo analítico:

**Rigor × Atualidade × Aderência**

## 11. Síntese

Não há meta-análise planejada para esta fase de mapeamento de estudos secundários.

A síntese será narrativa e tabular, com atenção a:

- vieses investigados;
- locus do viés;
- arquitetura de mediação;
- mecanismos de interação;
- qualidade metodológica;
- atualidade;
- aderência;
- lacunas de pesquisa.

## 12. Controle de mudanças

Qualquer mudança relevante em RQs, período, strings, critérios ou estratégia de avaliação será registrada em:

- `protocol/amendments.md`
- `protocol/decision-log.md`

