# Semana 07 - Trabalho 5

> **Disciplina:** Comunicação Científica - PPGI/UNIRIO  
> **Tema:** vieses cognitivos humanos em julgamentos mediados por LLMs, com atenção a sistemas multiagentes  
> **Versão:** v0.2  
> **Escopo:** exploração de teorias comportamentais, confronto com codificação preliminar, revisão das RQs, uso do material de Dorothy Leidner e consolidação para apresentação  
> **Status:** síntese conceitual revisada para aderência ao enunciado da Semana 07

---

## 1. Objetivo da atividade

Este trabalho parte do conjunto já organizado nas semanas anteriores: tema, problema de pesquisa, questões de pesquisa, artigos selecionados e codificação preliminar. O objetivo é verificar quais teorias, modelos e lentes comportamentais podem funcionar como instrumentos analíticos para interpretar o corpus e avaliar se a teoria apenas informa a revisão ou se a revisão começa a sugerir relações, condições ou conceitos ainda não plenamente contemplados pelas teorias existentes.

A atividade foi organizada em sete movimentos alinhados ao enunciado:

1. identificação de teorias comportamentais relacionadas ao tema;
2. seleção de lentes particularmente pertinentes;
3. identificação de construtos, relações, mecanismos e condições de contorno;
4. aplicação dessas lentes a estudos do corpus piloto;
5. comparação entre teoria e codificação preliminar;
6. avaliação de impactos na fundamentação e nas RQs;
7. posicionamento segundo Dorothy Leidner e consolidação em apresentação.

---

## 2. Ponto de partida da revisão

A revisão investiga evidências empíricas sobre como Large Language Models, particularmente sistemas multiagentes, estão associados à manifestação, amplificação ou mitigação de vieses cognitivos humanos em processos de julgamento e tomada de decisão.

A delimitação conceitual permanece:

- o humano é o sujeito cognitivo;
- o LLM é tratado como sistema mediador;
- vieses cognitivos humanos não são automaticamente equivalentes a comportamentos enviesados do modelo;
- `trust`, `reliance`, `overreliance`, `persuasion` e `social influence` são fenômenos relacionados, mas não sinônimos automáticos de viés cognitivo;
- múltiplos agentes são tratados como configuração arquitetural/interacional, não como múltiplos sujeitos humanos.

---

## 3. Teorias, modelos e lentes comportamentais selecionados

A seleção não foi guiada apenas pela presença da palavra “viés”. As lentes foram escolhidas porque ajudam a explicar mecanismos da interação humano–LLM.

| Lente | Construtos principais | Relação/mecanismo central | Condições de contorno relevantes | Como funciona como lente no corpus |
|---|---|---|---|---|
| **Judge–Advisor System (JAS)** | julgamento inicial; advice; julgamento final; advice uptake; weight of advice | uma pessoa revisa ou mantém um julgamento após receber conselho externo | confiança inicial; número de advisors; qualidade percebida do advice; tipo de tarefa; advice opcional ou imposto | ajuda a analisar quando a resposta do LLM atua como conselho incorporado, ignorado ou ponderado |
| **Trust in Automation** | trust; reliance; performance; calibration; appropriate reliance; overreliance; underreliance | informações sobre o sistema influenciam confiança; confiança pode influenciar comportamento de reliance | acurácia real; feedback; incerteza; risco; explicações; fontes; visibilidade de erro | ajuda a separar percepção subjetiva, comportamento observado e desempenho decisório |
| **Normative & Informational Social Influence** | influência normativa; influência informacional; grupo; majority; consensus; opinião | múltiplas fontes podem produzir conformidade social ou ser interpretadas como evidência sobre a realidade | tamanho do grupo; concordância; discordância; posição prévia do usuário; ambiguidade da tarefa | ajuda a interpretar efeitos de múltiplos agentes, consenso e pressão social percebida |
| **CASA - Computers Are Social Actors** | social cues; resposta social a computadores; ator computacional | pessoas podem aplicar respostas sociais a sistemas computacionais | presença de pistas sociais; representação de agência; linguagem; interface | justifica investigar se agentes LLM são processados como fontes sociais, sem assumir que sejam sujeitos humanos |
| **Biased Assimilation / Confirmation Bias** | crença prévia; evidência consonante; evidência dissonante; avaliação enviesada | crenças prévias influenciam busca, avaliação e aceitação da evidência | força da crença inicial; alinhamento da resposta; ambiguidade; polarização prévia | ajuda a separar selective exposure, avaliação de evidência e mudança de crença |
| **Anchoring-and-Adjustment** | âncora; exposição à âncora; ajuste; julgamento final | um valor/posição inicial influencia o julgamento subsequente por ajuste insuficiente | saliência da âncora; incerteza; expertise; ordem de exposição | orienta a busca futura por ancoragem, embora o viés não tenha aparecido no piloto de 5 reports |
| **Automation Bias / Complacency** | automação; scrutiny; workload; erros de omissão/comissão; complacency | dependência indevida da automação pode reduzir verificação e aumentar erros | carga cognitiva; multitarefa; confiabilidade aparente; falhas pouco visíveis; pressão de tempo | impede tratar todo overreliance como automation bias; exige operacionalização específica |

### 3.1 Modelo integrador provisório

```text
Human preconditions
prior belief / expertise / initial confidence
        ↓
System configuration
single-LLM / multi-LLM / group size / actual epistemic independence
        ↓
Cues
explanation / source / confidence / agreement / disagreement / consensus / critique
        ↓
Human interpretation
perceived reliability / perceived agent independence / perceived corroboration?
        ↓
Mechanisms
advice weighting / trust calibration / normative influence / informational influence
        ↓
Human action
accept / reject / query / verify / reconsider
        ↓
Outcomes
judgment change / belief change / confidence change / reliance / accuracy
        ↓
Bias manifestation
amplifies / mitigates / null / mixed
```

Este modelo é um **framework analítico provisório**. Ele não é apresentado como teoria validada.

---

## 4. Aplicação das lentes a estudos do corpus piloto

Para evitar que a discussão teórica fique abstrata, três exemplos do corpus piloto mostram como as lentes funcionam na interpretação dos estudos.

| Study | Evidência do piloto | Lente aplicada | Interpretação orientada por teoria |
|---|---|---|---|
| **ST002 - appropriate reliance / explanations / sources / inconsistencies** | explanations aumentaram reliance diante de respostas corretas e incorretas; sources e inconsistencies ajudaram em algumas condições | **Trust in Automation** | explicações podem aumentar confiança/reliance sem necessariamente melhorar calibração; por isso `trust`, `reliance` e `performance` devem permanecer separados |
| **ST007 - multi-agents as social groups** | condições multiagentes aumentaram influência normativa; informational influence não aumentou de modo correspondente; efeitos não foram monotônicos | **Social Influence + CASA** | múltiplos agentes podem produzir efeito social, mas isso não significa que o usuário os interprete como evidência informacional independente |
| **ST010 - sensemaking em interfaces multiagentes** | majority, consensus, critique e debate foram interpretados como pistas de confiabilidade/transparência, mas com dependência da forma de apresentação e custo cognitivo | **JAS + Trust + Social Influence** | consenso e maioria funcionam como cues; não devem ser automaticamente tratados como mecanismos psicológicos nem como evidência epistemicamente independente |

Esses exemplos reforçam três decisões analíticas:

1. **cue não é mecanismo**;
2. **percepção não é comportamento**;
3. **consenso não é automaticamente corroboration independente**.

---

## 5. Comparação entre teoria e codebook preliminar

A comparação com a codificação preliminar mostrou que o codebook v0.2 não deve ser reconstruído. Ele deve ser refinado e reorganizado em camadas.

### 5.1 Decisões principais

| Situação | Decisão |
|---|---|
| Categoria empírica confirmada pela teoria | **manter** |
| Categoria válida, mas ampla ou ambígua | **refinar** |
| Categorias distintas que pertencem a dimensão superior | **agregar hierarquicamente** |
| Conceito previsto pela teoria e potencialmente observável | **acrescentar como candidato** |
| Conceito teórico sem evidência empírica atual | **não codificar como ocorrência** |

### 5.2 Exemplos de refinamento

- `TRUST`, `RELIANCE` e `PERFORMANCE` devem permanecer separados.
- `OVERRELIANCE` não deve ser automaticamente codificado como `AUTOMATION_BIAS`.
- `SOCIAL_INFLUENCE` pode ser refinado em `NORMATIVE_INFLUENCE` e `INFORMATIONAL_INFLUENCE` quando o estudo sustentar essa distinção.
- `CONSENSUS`, `AGREEMENT`, `DISAGREEMENT`, `CRITIQUE` e `DEBATE` devem ser tratados inicialmente como características/cues de interação, não necessariamente como mecanismos psicológicos.
- `PERCEIVED_AGENT_INDEPENDENCE` permanece como código candidato.
- `PERCEIVED_CORROBORATION` surge como candidato, mas não deve ser promovido a construto estabilizado sem apoio do corpus ampliado.

### 5.3 Estrutura em camadas proposta

```text
A. Context
B. System / interaction configuration
C. Cues
D. Cognitive and social mechanisms
E. Human behavior
F. Human outcomes
G. Bias interpretation
H. Evidence and provenance
```

Essa reorganização permite distinguir melhor condições, sinais, mecanismos, ações humanas, outcomes e interpretação de vieses.

---

## 6. Impactos na fundamentação e nas RQs

A leitura teórica não altera o problema central da revisão. O principal impacto ocorre na fundamentação e no refinamento das RQs intermediárias.

### 6.1 Questão principal mantida

> **Que evidências empíricas existem sobre como Large Language Models, particularmente sistemas multiagentes, estão associados à manifestação, amplificação ou mitigação de vieses cognitivos humanos em processos de julgamento e tomada de decisão?**

A formulação permanece adequada porque não pressupõe causalidade forte nem direção única do efeito.

### 6.2 RQs propostas para versão v0.3

**RQ1.** Quais vieses cognitivos humanos são investigados?

**RQ2.** Como esses vieses e fenômenos relacionados são definidos, operacionalizados e medidos?

**RQ3.** Quais características da interação humano–LLM e quais mecanismos cognitivos, comportamentais ou sociais são associados à amplificação ou mitigação de vieses e fenômenos relacionados?

**RQ4.** Como configurações single-LLM e multi-LLM são implementadas, caracterizadas e comparadas, incluindo número de agentes e, quando reportadas, relações de dependência ou independência entre eles?

**RQ5.** Como dinâmicas de interação como consenso, discordância, crítica, debate e verificação se relacionam aos processos de *advice-taking*, *trust*, *reliance*, influência social e julgamento humano?

**RQ6.** Quais limitações metodológicas, inconsistências e lacunas permanecem?

### 6.3 Cuidado metodológico

Não foram criadas RQs específicas sobre `PERCEIVED_CORROBORATION` ou independência epistemológica, porque isso transformaria hipóteses analíticas emergentes em pressupostos da revisão.

---

## 7. Dorothy Leidner e o posicionamento da revisão

O material de Dorothy Leidner utilizado nesta etapa inclui:

- o artigo **Review and Theory Symbiosis: An Introspective Retrospective**;
- o vídeo/aula disponibilizado no Classroom, apresentado como **Theorizing from Literature Reviews**;
- a lista pública da AIS SIGDITE PhD Research Academy, que associa essa sessão a leituras sobre revisão, teorização, modelo de *thought-gear* e teoria baseada em literatura.

Como não foi realizada transcrição literal do vídeo, ele foi usado como orientação interpretativa para a pergunta: **quando uma revisão apenas aplica teoria existente e quando começa a teorizar a partir da literatura?** As formulações específicas abaixo são fundamentadas principalmente no artigo de Leidner e nos artefatos do nosso processo de revisão.

### 7.1 Framework RTD

Leidner propõe um framework para trabalhos de **Review and Theory Development (RTD)**. O framework distingue quatro tipos de revisão conforme duas dimensões: foco da revisão, variando de descrição a identificação de tendências/lacunas; e objetivo da revisão, variando de síntese a teorização.

| Tipo RTD | Foco | Objetivo | Relação com nosso estudo |
|---|---|---|---|
| Organizing Review | descrição | síntese | não é o foco principal; nosso estudo vai além da descrição |
| Assessing Review | tendências/lacunas | síntese | é o posicionamento principal atual |
| Specific-Theorizing Review | lacuna específica | teoria para preencher lacuna | possível trajetória futura, mas ainda prematura |
| Broad-Theorizing Review | fenômeno amplo | teoria do fenômeno | possível trajetória futura, mas não reivindicada agora |

### 7.2 Posicionamento formal

Metodologicamente, o estudo é conduzido como um **Systematic Mapping Study**. No framework de Leidner, porém, ele se posiciona predominantemente como uma **Assessing Review**, pois busca sintetizar tendências, relações, inconsistências e lacunas em um domínio delimitado.

Formulação curta:

> **Predominantly Assessing, with emerging theorizing potential.**

Essa formulação não significa que o estudo já produza uma nova teoria. Significa apenas que a revisão está localizada no quadrante de identificação de tendências/lacunas, com alguns sinais iniciais de teorização emergente.

---

## 8. Theory → Review e Review → Theory

### 8.1 Theory → Review

No estágio atual, a teoria informa fortemente a revisão:

- JAS ajuda a organizar julgamento inicial, advice e julgamento final;
- Trust in Automation separa trust, reliance e performance;
- Social Influence distingue mecanismos normativos e informacionais;
- Biased Assimilation ajuda a decompor confirmation bias;
- Automation Bias evita equiparar qualquer overreliance a automation bias.

### 8.2 Review → Theory

A revisão também começa a sugerir relações e conceitos candidatos:

- pluralidade percebida versus independência epistemológica real;
- consenso versus corroboration percebida;
- cue disponível → cue percebido → cue utilizado → outcome;
- mecanismos concorrentes e efeitos não monotônicos;
- divergência entre percepção subjetiva, comportamento observado e performance.

Esses elementos ainda são tratados como hipóteses analíticas, não como teoria estabelecida.

---

## 9. Resposta ao item 6 do trabalho

No estágio atual, as teorias selecionadas informam predominantemente a revisão. Elas fornecem construtos e mecanismos que ajudam a reinterpretar e organizar a codificação preliminar, permitindo distinguir advice-taking, trust, reliance, influência normativa, influência informacional, cues, mecanismos e outcomes.

Entretanto, a análise piloto também começou a revelar relações que não são plenamente explicadas por nenhuma dessas lentes isoladamente. Destacam-se a distinção entre pluralidade percebida e independência epistemológica real em sistemas multiagentes, a possível percepção de corroboration produzida pelo consenso entre agentes e a separação entre cue disponível, cue percebido, cue utilizado e seus efeitos comportamentais.

Assim, o estudo encontra-se predominantemente no movimento:

```text
Theory → Review
```

mas apresenta sinais iniciais de:

```text
Review → Theory
```

A sustentação desse segundo movimento dependerá da expansão e síntese do corpus.

---

## 10. Resultados da etapa

Os principais resultados desta etapa são:

1. **Matriz teórica construída:** foram selecionadas lentes que explicam mecanismos de advice-taking, trust/reliance, influência social e vieses específicos.
2. **Aplicação concreta ao corpus piloto:** ST002, ST007 e ST010 mostram como as lentes requalificam interpretações sobre explanations, consensus, majority, social influence e perceived reliability.
3. **Codebook reinterpretado:** o codebook v0.2 permanece válido, mas deve ser reorganizado em camadas analíticas.
4. **RQs refinadas:** RQ3, RQ4 e RQ5 ficam mais explicativas, sem transformar hipóteses emergentes em pressupostos.
5. **Posicionamento RTD definido:** o estudo é um SMS metodologicamente, mas se posiciona como **Assessing Review** no framework de Leidner.
6. **Relações candidatas identificadas:** perceived plurality, actual epistemic independence, perceived corroboration e cue perceived/used tornam-se pontos de atenção para o corpus ampliado.
7. **Cuidado epistemológico:** a revisão ainda não reivindica nova teoria; trabalha com framework analítico provisório.

---

## 11. Síntese final

A principal contribuição desta etapa é transformar a revisão de uma organização descritiva de códigos em uma estrutura analítica orientada por mecanismos. As teorias selecionadas ajudam a explicar como características da interação humano–LLM podem atuar sobre julgamento, confiança, dependência, verificação, influência social e manifestação de vieses.

Ao mesmo tempo, o corpus preliminar sugere que sistemas multiagentes baseados em LLMs introduzem problemas ainda pouco capturados pelas teorias existentes, especialmente a diferença entre pluralidade percebida e independência epistemológica real. Esse ponto permanece como lacuna candidata e deverá ser testado na expansão do corpus.

---

## 12. Referências principais

- Bonaccio, S.; Dalal, R. S. (2006). *Advice taking and decision-making: An integrative literature review, and implications for the organizational sciences*.
- Deutsch, M.; Gerard, H. B. (1955). *A study of normative and informational social influences upon individual judgment*.
- Lee, J. D.; See, K. A. (2004). *Trust in automation: Designing for appropriate reliance*.
- Leidner, D. E. (2018). *Review and Theory Symbiosis: An Introspective Retrospective*.
- Leidner, D. E.; Tona, O. (2021). *A thought-gear model of theorizing from literature*.
- Lord, C. G.; Ross, L.; Lepper, M. R. (1979). *Biased assimilation and attitude polarization*.
- Nass, C.; Steuer, J.; Tauber, E. R. (1994). *Computers are social actors*.
- Parasuraman, R.; Manzey, D. H. (2010). *Complacency and bias in human use of automation*.
- Shepherd, D. A.; Sutcliffe, K. M. (2011). *Inductive top-down theorizing: A source of new theories of organization*.
- Tversky, A.; Kahneman, D. (1974). *Judgment under uncertainty: heuristics and biases*.
- AIS SIGDITE PhD Research Academy. *March 2025 - Dorothy Leidner: Theorizing from Literature Reviews*.
