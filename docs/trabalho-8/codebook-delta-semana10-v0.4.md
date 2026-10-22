# Codebook delta proposto - Semana 10 / Trabalho 8 - v0.4

**Relação com o v0.3:** somente adições/refinamentos; códigos anteriores permanecem vigentes. Código `PROPOSTO` significa candidato à inclusão no codebook final, e não novo construto psicométrico validado. Todas as decisões de codificação dependem da evidência da fonte primária.

| Código | Unidade/definição operacional | Não confundir com | Estudos / condições | Estatuto |
|---|---|---|---|---|
| `LLM_GENERATED_ANALYSIS` | Texto sobre atributos de uma decisão produzido pelo LLM para comentar uma recomendação de outro algoritmo. | Recomendação criada pelo LLM ou explicação fiel do modelo preditivo. | ST014–ST015 | PROPOSTO / CUE |
| `EXPLANATION_PRESENTATION` | Sequencial aleatória versus todas as análises simultâneas. | Seleção adaptativa. | ST014 | PROPOSTO / INTERVENÇÃO |
| `ADAPTIVE_EXPLANATION_SELECTION` | Ordenação dinâmica da análise por algoritmo que antecipa efeito na decisão do usuário. | Mais informações em geral; mecanismo psicológico comprovado. | ST015 | PROPOSTO / INTERVENÇÃO |
| `HUMAN_LLM_DEBATE` | Conversação sobre opinião entre pessoa e agentes baseados em LLM em jogo estruturado. | Debate puramente entre LLMs. | ST016 | PROPOSTO / CONTEXTO |
| `GROUP_COMPOSITION` | HH / AH / AA, descrever membros com os quais humanos realmente interagem. | Independência epistemológica das fontes. | ST016 | PROPOSTO / DESIGN |
| `SYCOPHANCY_OPINION_AGREEMENT` | Concordância de conselho com posição inicial do participante. | `CONFIRMATION_BIAS` sem medida de busca/assimilação confirmatória. | ST017 | PROPOSTO / CONTEÚDO; abstract-only |
| `DIRECT_PRAISE` | Elogio explícito dirigido ao usuário. | Acurácia do conselho. | ST017 | PROPOSTO / CONTEÚDO; abstract-only |
| `SELF_DEPRECATION` | Sistema diminui a própria autoridade ou capacidade em sua formulação. | Disclaimer de risco equivalente. | ST017 | PROPOSTO / CUE; abstract-only |
| `ACCESS_TIMING` | Disponibilidade Early/Continuous/Late/No do LLM. | Tempo total disponível. | ST018 | PROPOSTO / INTERVENÇÃO |
| `TIME_AVAILABILITY` | Tempo Insufficient/Sufficient atribuído ao participante. | Duração efetiva da verificação. | ST018 | PROPOSTO / CONDIÇÃO |
| `MYSIDE_BIAS` | Valor absoluto da diferença entre argumentos pró e contra válidos. | Medida direta de `ANCHORING_BIAS`; diferença baixa por apenas poucos argumentos. | ST018 | EXISTENTE NO ARTIGO / MEDIDA DIRETA (DO PROXY) |
| `SOCIAL_SYCOPHANCY` | Endosso excessivo a ações/perspectiva do usuário em dilema interpessoal. | Lisonja meramente estilística. | ST019–ST021 | PROPOSTO / CONTEÚDO |
| `REPAIR_INTENTION` | Disposição autorreportada para reparar relação (pedir desculpas etc.). | Reparação real observada. | ST019–ST021 | PROPOSTO / OUTCOME |
| `RIGHTNESS_JUDGMENT` | Grau de convicção autorreportada de estar certo. | Correção factual comprovada. | ST019–ST021 | PROPOSTO / OUTCOME |
| `SOURCE_IDENTITY_LABEL` | Rótulo AI versus humano, mantendo conteúdo constante. | Fonte efetivamente humana. | ST020 | CÓDIGO EXISTENTE / REFINAMENTO |

## Regras de adjudicação e memos

1. `CUE` não é `MECHANISM`: pistas e intervenções de interface só viram mediação causal quando desenho e análise a isolam.
2. `NOT_TESTED` (construto não operacionalizado), `NULL_EFFECT` (comparação estatística não significativa), `NOT_REPORTED` e `ABSTRACT_ONLY` não são intercambiáveis.
3. Em ST018, sempre registrar **número de argumentos** ao interpretar `MYSIDE_BIAS`: o escore absoluto pode diminuir porque menos argumentos foram oferecidos.
4. Em ST019–ST021, `INTENTION` não é `OBSERVED_BEHAVIOR`.
5. Em ST014–ST015, distinguir `RF_ADVICE_GENERATOR` de `LLM_ANALYSIS_GENERATOR`.
6. Em ST016, não contar jogos AA como novas unidades empíricas com desfecho humano.
7. Em ST017, não importar p-valores e coeficientes de resumos de terceiros para uma matriz marcada `DIRECT` antes da leitura integral.
8. `PERCEIVED_AGENT_INDEPENDENCE` e a hipótese de **corroboração aparente** continuam `NOT_DIRECTLY_TESTED` no corpus ampliado proposto.
