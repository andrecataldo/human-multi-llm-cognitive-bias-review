# Codebook complementar - Semana 08, v0.3 (provisório)

> Alterações em relação ao piloto v0.2: inclusão de códigos observáveis nas cinco units complementares. `ACCEPTED_FOR_CODING` **não** equivale a construto psicológico validado. 

| Código | Definição operacional / regra de aplicação | Origem / evidência | Estatuto |
|---|---|---|---|
| `CONFIRMATION_BIAS` | Viés humano explicitamente operacionalizado por procura seletiva por concordância | FT1222; planejamento | EXISTENTE / DIRETO |
| `OVERRELIANCE` | Uso de recomendação errada do LLM em oposição a informação/correção disponível; não é automaticamente automation bias | FT0070, FT0072, FT0080, FT1233 | EXISTENTE |
| `APPROPRIATE_RELIANCE` | Discriminação entre aderir à recomendação correta e rejeitar incorreta; registrar a métrica usada | FT0080, FT0070 | EXISTENTE |
| `RELIANCE_DISCLAIMER` | Aviso usado como intervenção para calibrar reliance | FT0080 | EMERGENTE, CUE |
| `UNCERTAINTY_HIGHLIGHTING` | Destaque de trechos inseguros do conselho LLM; diferente de frase explícita | FT0080 | REFINAMENTO DE CUE |
| `IMPLICIT_ANSWER` | Representação indireta que exige inferência/cálculo da resposta | FT0080 | EMERGENTE, INTERVENÇÃO |
| `OPPONENT_TYPE` | Interlocutor é humano ou GPT-4; distingue agente real de fonte percebida | FT0083 | EMERGENTE, CONTEXTO |
| `PERSONALIZATION` | Argumentos usam informações pessoais do debatedor; não inferir significância incremental após errata | FT0083 | EMERGENTE, MANIPULAÇÃO |
| `SOURCE_IDENTITY_LABEL` | Etiqueta AI versus expert; verificar o que participante efetivamente percebeu | FT0318 | EMERGENTE, CUE |
| `HUMAN_LIKE_TONE` | Manipulação da linguagem para parecer humana versus neutra | FT0318 | EMERGENTE, CUE |
| `FACT_BASED_ARGUMENTS` | Contestação de crença com dados e evidências | FT0318 | EMERGENTE, CONTEÚDO; mecanismo só se isolado |
| `DEFAULT_LLM_FRAMING` | Enquadramento da narrativa do modelo em configuração default | FT0545 | EMERGENTE, CONTEÚDO DO MODELO |
| `PROMPTED_LIBERAL_FRAMING` | Enquadramento liberal induzido por prompt | FT0545 | EMERGENTE, MANIPULAÇÃO |
| `PROMPTED_CONSERVATIVE_FRAMING` | Enquadramento conservador induzido por prompt | FT0545 | EMERGENTE, MANIPULAÇÃO |
| `FIRST_PERSON_UNCERTAINTY` | Expressão de incerteza de primeira pessoa, separada de medida comportamental | FT1233 | EMERGENTE, CUE |
| `GENERAL_UNCERTAINTY` | Expressão impessoal de incerteza em linguagem natural | FT1233 | EMERGENTE, CUE |
| `PERCEIVED_AGENT_INDEPENDENCE` | Impressão de fontes independentes, quando participante a expressar; não inferir por quantidade de agentes | FT0772 | CANDIDATO / NÃO CONFIRMADO |
| `ANCHORING_BIAS` | Julgamento humano influenciado por âncora inicial com operacionalização adequada | Nenhum dos 10 operacionaliza diretamente na extração disponível | A PRIORI / NÃO OBSERVADO |
| `AUTOMATION_BIAS` | Construto definido e mensurado especificamente pelos autores; não sinônimo de overreliance | Nenhum dos 10 operacionaliza diretamente na extração disponível | A PRIORI / NÃO OBSERVADO |

## Regras de adjudicação

1. Registrar `cue` e `mecanismo` em campos diferentes; não codificar como mecanismo uma mera decoração de interface.
2. Para `OPINION_CHANGE`, registrar medição e comparador. Para `CONFIRMATION_BIAS`, exigir operacionalização compatível (por exemplo, comportamento confirmatório) ou marcar apenas evidência indireta.
3. Registrar variáveis contextuais e condições de contorno que mudam comparação (LSAT versus estimativa visual, rótulo AI versus expert, 1 versus 3 versus 5 agentes etc.).
4. Quando houver correção editorial, a versão corrigida prevalece na interpretação e no log; nunca copiar alegação antiga de significância.
5. `NOT_REPORTED`, `NOT_TESTED`, `NOT_SUPPORTED` e `NULL_EFFECT` representam situações diferentes e devem ser preservadas.
6. Cada excerto deve conter link do report, seção/página, trecho ou paráfrase curta e identificação AUTHOR versus REVIEW.
