# Delta de codebook — Trabalho 08 / T8-A3 v0.5 (PROPOSTO)

**Referências de base:** `docs/trabalho-6/codebook-complementar-v0.3.md` e `docs/trabalho-8/codebook-delta-semana10-v0.4.md`.
A numeração v0.5 identifica a revisão proposta do *delta*; não substitui nem aprova automaticamente o codebook anterior.

| Código | Definição e aplicação | Proibido inferir | Estudo / eixo | Tipo |
|---|---|---|---|---|
| `HUMAN_LLM_INFORMATION_TRANSFER` | Dificuldade observada na transferência de dados clínicos para o chatbot e na incorporação de suas respostas, conforme análises qualitativas dos autores. | Viés de automação causal ou ancoragem sem teste específico. | ST022 / AX02 | PROCESSO OBSERVADO, EXPLORATÓRIO |
| `MODEL_VS_ASSISTED_PERFORMANCE_GAP` | Diferença descritiva entre desempenho do LLM sozinho em um benchmark e de pessoas usando LLM em experimento. | Efeito causal puro ou comparação pareada equivalente entre braços randomizados; não é uma STUDY humana extra. | ST022 / AX05 | CONTRASTE ANALÍTICO |
| `CONDITION_IDENTIFICATION_ACCURACY` | Identificar uma condição médica relevante segundo padrão de especialistas. | Diagnóstico clínico real. | ST022 / AX05 | OUTCOME |
| `DISPOSITION_ACCURACY` | Acerto da escolha de conduta em cenário médico simulado. | Ação de cuidado real ou saúde posterior. | ST022 / AX05 | OUTCOME |
| `CONTROL_USUAL_RESOURCES` | Condição controle com recursos habituais, incluindo busca, em vez de privação total de informação. | Grupo 'sem qualquer auxílio'. | ST022 / AX05 | COMPARADOR |
| `AGENT_COUNT_NOT_EPISTEMIC_INDEPENDENCE` | Marcador interpretativo: número de agentes não determina diversidade ou independência de suas evidências. | Inferir corroboração aparente observada apenas porque há múltiplos agentes. | ST007, ST010, ST016 / AX04 | MEMO, NÃO OUTCOME |

**Permanecem vigentes:** `MYSIDE_BIAS` (proxy operacional dos autores em ST018), `SOCIAL_SYCOPHANCY`, `RIGHTNESS_JUDGMENT`, `REPAIR_INTENTION`, `ADAPTIVE_EXPLANATION_SELECTION`, `HUMAN_LLM_DEBATE`, etc. (v0.4). `CONFIRMATION_BIAS` continua com evidência direta principalmente em ST011–ST012; `ANCHORING_BIAS` continua sem demonstração direta no corpus atual; `AUTOMATION_BIAS` não deve ser equiparado automaticamente a overreliance.

**Regras:** sempre separar `AUTHOR`, `REVIEW` e `EDITOR`; cue ≠ mecanismo; confiança ≠ reliance ≠ qualidade; intenção ≠ comportamento; condição controle ≠ benchmark model-only; resultado não significativo ≠ ausência universal de efeito; nenhum código candidato significa construto validado. A avaliação científica humana continua pendente.
