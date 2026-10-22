# Semana 10 - Trabalho 8: ampliação da codificação rumo a 15 artigos

**PPGI/UNIRIO - Comunicação Científica | Professor Sean Siqueira**  
**Data:** 22/10/2026  
**Release:** `v0.1` - triagem e codificação inicial assistida, **não uma inclusão definitiva**  
**Pesquisa:** vieses cognitivos humanos em julgamentos mediados por LLMs, com atenção a sistemas multiagentes.

## 1. Ponto de partida e denominadores

| Unidade de contagem | Estado ao fim da Semana 09 | Alvo de trabalho da Semana 10 | Estado verificável nesta release |
|---|---:|---:|---|
| REPORT (publicação) já incluído em texto completo | 10 | 15 | 10 confirmados + 5 **candidatos** |
| STUDY (experimento/investigação empírica) já codificado | 13 | Não fixado pelo professor | 13 confirmados + **até 8 unidades candidatas**, a resolver |
| Registros retidos para full text no screening Scopus | 1.419 | Não se aplica | Não foi possível cruzar estes cinco com o conjunto original |

A revisão original é uma release **Scopus-only**, com busca de 16/09/2026. O novo levantamento realizado para avançar nesta semana é **complementar/exploratório** e exige comparação com os IDs e regras do screening anterior antes de alimentar o corpus consolidado. Não alegamos nova busca sistemática ou atualização de sua cobertura.

**Fontes metodológicas mantidas:** Trabalho 3 (I1–I9, E1–E10; SEGRESS como diretriz de relato), Trabalho 6 (codificação aberta, axial e seletiva; codebook v0.3) e Trabalho 7 v0.3 (Resultados–Discussão–Teorização), todos disponíveis no repositório. Grounded Theory orienta a codificação e Thought-Gear organiza a síntese **por decisão metodológica desta revisão**, não por prescrição do SEGRESS.

## 2. Seleção preliminar - cinco publicações candidatas

| Candidato | Publicação verificada | Desenho humano e escopo | Fontes verificadas | Elegibilidade provisória |
|---|---|---|---|---|
| **T8-C01** | Li et al. (2025), *From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis*. CHI '25. DOI: [10.1145/3706598.3713133](https://doi.org/10.1145/3706598.3713133). | Dois experimentos com participantes humanos, análises geradas por GPT-4 e decisões sobre renda/recidivismo. | Texto disponibilizado pela ACM (seções 3 e 5). | **Forte candidato**: fonte secundária de explicações LLM sobre conselho de outro modelo; não é multi-LLM. |
| **T8-C02** | Flamino et al. (2025), *Testing the limits of large language models in debating humans*. *Scientific Reports* 15, 13852. DOI: [10.1038/s41598-025-98378-1](https://doi.org/10.1038/s41598-025-98378-1). | Experimento pré-registrado com debates humanos/agentes usando GPT-4 e Llama 2; decisões/opiniões humanas. | PubMed; texto indexado em PMC, com seções de metodologia/resultados identificadas. | **Forte candidato**, diretamente ligado a grupos mistos humano–agentes LLM. |
| **T8-C03** | Zejian Li et al. (2026), *Does Sycophancy Change Decisions? Effect of LLM Sycophancy on AI-Assisted Decision-Making*. CHI '26. DOI: [10.1145/3772318.3790934](https://doi.org/10.1145/3772318.3790934). | Um experimento `4 × 2` com **106 participantes**, decisões de encontros/ETF. | Resumo do artigo em catálogos de CHI; metadados bibliográficos DBLP. | **Forte candidato**, mas codificação ainda no nível de resumo: **recuperar e ler full text**. |
| **T8-C04** | Zhi, Kumar e Lee (2026), *Investigating the Effects of LLM Use on Critical Thinking Under Time Constraints: Access Timing and Time Availability*. CHI '26. DOI: [10.1145/3772318.3791796](https://doi.org/10.1145/3772318.3791796). | Um experimento pré-registrado `4 × 2`, **393 participantes**, decisão baseada em documentos e acesso ao LLM em momentos diferentes. | Artigo/abstract da ACM; [versão arXiv](https://arxiv.org/abs/2603.08849). | **Forte candidato**: efeito contextual no desempenho e análise de `myside bias`; revisar se este foi estatisticamente confirmado conforme análise principal. |
| **T8-C05** | Cheng et al. (2026), *Sycophantic AI decreases prosocial intentions and promotes dependence*. *Science*, 391, eaec8352. DOI: [10.1126/science.aec8352](https://doi.org/10.1126/science.aec8352). | **Três experimentos humanos pré-registrados**, **N total=2.405**; experimentos adicionais só com modelos NÃO são unidades humanas elegíveis. | Resumo estruturado da *Science*, [PubMed](https://pubmed.ncbi.nlm.nih.gov/41886588/). | **Forte candidato**: julgamento e intenção comportamental; requer leitura detalhada de texto/métodos suplementares para resolver as três STUDY units. |

Todos os cinco possuem publicação identificada **antes do corte de 16/09/2026**, mas **não houve confirmação de sua presença entre os registros da Scopus**. Números de participantes pertencem aos respectivos desenhos; não somá-los para sugerir uma amostra única ou estimativa pooled.

## 3. Codificação aberta - evidência, interpretação e lacunas

### T8-C01 - From Text to Trust

- **Atores e contexto:** decisores humanos diante de recomendações de modelo preditivo; GPT-4 produz análises dos atributos de tarefas de renda e recidivismo. O LLM interpreta a recomendação de outro modelo, sem necessariamente conhecer sua lógica interna.
- **Variáveis/sinais:** nenhuma análise; análises sequenciais aleatórias; todas as análises; seleção adaptativa de análises (*Alg*) contra alternativas.
- **Desenho / STUDY units candidatas:** estudo inicial **N=284** (134 renda + 150 recidivismo), seguido de novo experimento **N=844** (447 renda + 397 recidivismo). São duas fases experimentais distintas, não quatro apenas porque existem dois domínios em cada fase.
- **Evidência dos autores:** apresentar todas as análises ou sequências aleatórias **não** melhorou significativamente acurácia ou overreliance em relação ao controle inicial; selecionar adaptativamente análises relevantes elevou a acurácia e reduziu overreliance frente a certas condições comparadoras no segundo experimento.
- **Interpretação da revisão:** a **seleção e a oportunidade de uso da evidência** importam mais do que o volume bruto de explicações; reforça P1 e contextualiza P2. O modelo comportamental de escolha de explicações é desenho do estudo, **não prova direta** de mediação psicológica individual.
- **Risco/limite:** as explicações LLM podem não reproduzir a justificativa real do modelo primário. Não equiparar melhora no uso do conselho à diminuição de um viés cognitivo específico.
- **Códigos de trabalho:** `LLM_GENERATED_ANALYSIS`, `EXPLANATION_SELECTION`, `ADAPTIVE_INFORMATION`, `APPROPRIATE_RELIANCE`, `OVERRELIANCE`; AX01, AX02, AX05.
- **Rastreio:** texto ACM, Abstract, §§3–5, §6.3; [DOI](https://doi.org/10.1145/3706598.3713133). **Excertos precisos a confirmar por pesquisador.**

### T8-C02 - Testing the limits of large language models in debating humans

- **Atores e contexto:** 6 humanos (HH), 6 agentes (AA) ou 3 humanos + 3 agentes (AH), debatendo dietas para buscar consenso. Agentes conversacionais implementados com GPT-4/Llama 2 e personas.
- **Desenho:** **37 jogos**, sendo 10 HH, 17 AH e 10 AA; 111 humanos ingressaram, **97 participaram ativamente**. Análises usam conversas e mudanças de opinião; os jogos AA **não** são unidades empíricas de julgamento humano por si só.
- **Evidência dos autores:** agentes foram menos persuasivos para humanos do que interlocutores humanos; os agentes se mantiveram mais centrados no assunto e diferiram no comportamento de mudança de opinião. Nos jogos mistos, os participantes não sabiam inicialmente quais interlocutores eram agentes.
- **Interpretação da revisão:** o efeito de pluralidade de agentes **não precisa ser mais persuasivo** do que a presença de pessoas; revela limite a uma leitura universal de P4. É evidência sobre *persuasion/opinion change*, **não medida de confirmation bias**.
- **Risco/limite:** revelar a identidade dos agentes apenas no fim limita generalização a sistemas em que a autoria de IA é transparente; o estudo mistura agentes de modelos distintos sem manipular *independência epistemológica percebida vs real*.
- **Códigos de trabalho:** `HUMAN_LLM_DEBATE`, `AGENT_IDENTITY_CONCEALMENT`, `OPINION_CHANGE`, `PERSUASIVENESS`, `GROUP_COMPOSITION`; AX03, AX04, AX05.
- **Rastreio:** [DOI](https://doi.org/10.1038/s41598-025-98378-1); resumo PubMed, seções *Experiment design* e *Results* do texto indexado. **Excertos precisos a confirmar.**

### T8-C03 - Does Sycophancy Change Decisions?

- **Atores e contexto:** pessoas aconselhadas por LLM em previsões de encontros (*speed-dating*) e investimento em ETF; contextos com riscos distintos.
- **Manipulações:** controle não bajulador; alinhamento com opinião prévia; elogio direto; autodepreciação. Estudo `4 × 2` (N=106).
- **Evidência no resumo dos autores:** concordar com a opinião do participante reforçou decisões iniciais; autodepreciação do sistema elevou confiança, em vez de necessariamente a reduzir; entrevistas indicaram preocupação com elogios excessivos.
- **Interpretação da revisão:** resposta consonante pode alterar decisões sem que se tenha demonstrado a medida operacional de **confirmation bias**. **Confiança, permanência na escolha e acurácia** não são o mesmo resultado.
- **Risco/limite:** sem tabelas do texto integral não registrar tamanhos de efeito, causalidade psicológica mediada, interações específicas ou inferências sobre cenários financeiros reais.
- **Códigos candidatos:** `SYCOPHANCY_OPINION_AGREEMENT`, `DIRECT_PRAISE`, `SELF_DEPRECATION`, `DECISION_PERSISTENCE`, `CONFIDENCE`; AX01, AX03, AX05.
- **Rastreio:** [DOI](https://doi.org/10.1145/3772318.3790934), resumo do congresso; **exige acesso à seção Resultados**.

### T8-C04 - Investigating the Effects of LLM Use on Critical Thinking Under Time Constraints

- **Atores e contexto:** participantes avaliam documentos com informações conflitantes e elaboram uma decisão fundamentada; o LLM está ausente, disponível cedo, continuamente ou somente no final.
- **Manipulações:** momento de acesso (4 modalidades) × tempo disponível (insuficiente/suficiente); N=393 em experimento pré-registrado.
- **Evidência dos autores:** acesso precoce/contínuo melhorou desempenho de pensamento crítico quando faltava tempo, mas prejudicou o desempenho quando havia tempo suficiente. Começar o trabalho de forma independente apresentou padrão inverso.
- **Interpretação da revisão:** **tempo disponível e momento de intervenção** são condições de contorno relevantes para discernimento epistêmico situado; nenhuma intervenção de IA deve ser presumida universalmente benéfica.
- **Risco/limite:** o conceito de `myside bias` é mencionado na análise do artigo, mas não atribuímos um efeito específico sem conferir a medida, comparação e teste; também não inferimos ancoragem humana.
- **Códigos candidatos:** `LLM_ACCESS_TIMING`, `TIME_PRESSURE`, `CRITICAL_THINKING_PERFORMANCE`, `DECISION_QUALITY`, `MYSIDE_BIAS_TO_VALIDATE`; AX02, AX03 (pendente), AX05.
- **Rastreio:** artigo CHI 2026 DOI acima, Abstract, §§3–5; [arXiv](https://arxiv.org/abs/2603.08849). **Conferir detalhes por condição.**

### T8-C05 - Sycophantic AI decreases prosocial intentions and promotes dependence

- **Atores e contexto:** usuários buscam aconselhamento com LLM sobre conflitos interpessoais; parte das interações é conversa real e parte usa vinhetas.
- **Desenho:** três experimentos humanos pré-registrados (N agregado=2.405). Há ainda avaliação da incidência de sycophancy em 11 modelos, que **não é uma quarta STUDY unit humana**.
- **Evidência dos autores:** interação com respostas excessivamente concordantes aumentou convicção pessoal de estar certo e reduziu disposição declarada a assumir responsabilidade ou reparar conflitos; apesar disso, participantes preferiram e confiaram mais nos modelos bajuladores.
- **Interpretação da revisão:** a aceitação subjetiva de aconselhamento que favorece o usuário pode coexistir com piora nas intenções pró-sociais. É evidência convergente para condições de alinhamento prévio, **não operacionalização automática de confirmation bias**.
- **Risco/limite:** intenção de reparar conflito ≠ reparação observada no mundo real; caracterização dos grupos, medidas de cada uma das três investigações, effect sizes e comparadores requerem leitura integral e suplementos.
- **Códigos candidatos:** `SYCOPHANCY`, `SELF_JUSTIFICATION`, `PROSOCIAL_INTENTION`, `PERCEIVED_TRUST`, `ADVICE_PREFERENCE`; AX01, AX03, AX05.
- **Rastreio:** [Science](https://doi.org/10.1126/science.aec8352), *Structured Abstract*, *Results*, *Supplementary Materials*, [PubMed](https://pubmed.ncbi.nlm.nih.gov/41886588/); **confirmar excertos e protocolos individualizados**.

## 4. Resolução preliminar REPORT → STUDY (não consolidada)

| ID temporário | Report candidato | Unidade empírica provável | Observação |
|---|---|---|---|
| CU-T8-01 | T8-C01 | Experimento inicial: apresentação de análises | Verificar fluxos, exclusões e amostras finais |
| CU-T8-02 | T8-C01 | Experimento posterior: seleção adaptativa | Não dividir automaticamente por tarefa de renda/recidivismo |
| CU-T8-03 | T8-C02 | Jogos de debate HH/AH/AA de um protocolo | Jogos AA contribuem para comparação, não são estudos humanos autônomos |
| CU-T8-04 | T8-C03 | Experimento misto 4 × 2 | Confirmar texto completo e métricas |
| CU-T8-05 | T8-C04 | Experimento 4 × 2 de acesso/tempo | Confirmar outcomes por grupo |
| CU-T8-06 | T8-C05 | Experimento humano 1 | Separar N, controle, medida |
| CU-T8-07 | T8-C05 | Experimento humano 2 | Separar N, controle, medida |
| CU-T8-08 | T8-C05 | Experimento humano 3 | Separar N, controle, medida |

**Se** as cinco publicações cumprirem integralmente I1–I9 e forem reconciliadas com o screening, a contagem esperada será **15 reports e aproximadamente 21 STUDY units** (13 + 8). Esta é uma **projeção provisória**, não resultado validado.

## 5. Comparação constante com categorias da Semana 08

| Categoria existente | Evidência nova candidata | O que muda / permanece incerto |
|---|---|---|
| **AX01 - Credibilidade e aceitação sem discriminação** | T8-C01, T8-C03, T8-C05 | Complementa o achado de que credibilidade e volume de explicações não garantem discriminação de acerto; apresenta diferentes efeitos de sycophancy. |
| **AX02 - Visibilidade de erro, escrutínio e custo** | T8-C01, T8-C04 | Introduz **momento de acesso** ao LLM e seleção adaptativa da explicação, além do custo temporal já discutido. Não confirma mediação cognitiva universal. |
| **AX03 - Alinhamento, argumentação e mudança de crença** | T8-C02, T8-C03, T8-C05 | Traz um contraste: agentes LLM menos convincentes que pessoas num debate e sistemas bajuladores que reforçam julgamentos ou intenções; tarefas diferentes impedem contradição direta. |
| **AX04 - Pluralidade e influência social** | T8-C02 | Amplia contextos humanos em grupos com vários agentes. Não comprova a hipótese de **corroboração aparente** nem isola independência entre fontes. |
| **AX05 - Percepção, ação e desempenho** | Todos | Mantém separadas confiança, acurácia, opinião, comportamento e intenção. |

**Memo de teorização (revisão, não achado experimental):** a nova amostra candidata reforça a utilidade de modelar *configuração da interação* (identidade da fonte, quantidade de agentes, ordem da ajuda, estrutura do feedback) como condição relevante. P1–P5 da Semana 09 permanecem **proposições**, cuja sustentação deve ser reavaliada com a inclusão formal. A hipótese P5 exige experimento em que a independência **real** das fontes seja manipulada e a independência **percebida** seja medida - não bastam agentes numericamente distintos.

## 6. Um candidato metodologicamente limítrofe que NÃO foi contado

**Tsuchiya e Baba (2026), *More Isn't Always Better: Balancing Decision Accuracy and Conformity Pressures in Multi-AI Advice*, CHI '26.** DOI [10.1145/3772318.3791648](https://doi.org/10.1145/3772318.3791648). Dois estudos, **348 participantes**, com um, três e cinco conselheiros e variação de consenso. Há resultados interessantes sobre *overreliance* com alto consenso e dissenso minoritário. **Mas** a seção 3.3 estabelece que os conselheiros são **árvores de decisão amostradas de random forest**; GPT-4o entra na **geração da linguagem das explicações**, e não como o mecanismo primário de decisão do painel. É portanto **multi-AI híbrido**, não um experimento de múltiplos conselheiros LLM. Pode integrar a revisão sob critério amplo I3, após decisão explícita, ou permanecer como **literatura comparativa externa**; não o usamos para preencher automaticamente a meta de cinco.

A distinção evita concluir que uma arquitetura multi-LLM foi testada quando os conselhos numéricos são produzidos por outro algoritmo.

## 7. Pendências obrigatórias para “15 devidamente trabalhados”

1. **Proveniência Scopus:** obter o CSV/XLSX original da etapa `RETAIN_FOR_FULL_TEXT` (1.419), identificar quais candidatos pertencem à busca de 16/09/2026 e atribuir IDs originais. Se houver artigos não presentes, registrar formalmente uma **emenda de expansão complementar** antes da inclusão.
2. **Elegibilidade I1–I9:** abrir os cinco textos completos; registrar para cada critério a decisão, seu excerto de suporte e motivo de eventual exclusão. Confirmar versão publicada, peer review e não duplicidade.
3. **Extração STUDY-level:** conferir amostras efetivamente analisadas, manipulações, comparadores, medidas, tamanhos de efeito e resultados nulos/contraditórios para as oito unidades estimadas.
4. **Rastreabilidade:** registrar de um a três excertos/paráfrases curtas localizados por seção/página por unidade, com `AUTHOR` vs `REVIEW`, status `researcher_check_status=PENDING/VERIFIED` e data da conferência.
5. **Codebook:** validar novos códigos, justificar merges/splits, e produzir `v0.4` aditivo sem apagar versões v0.3 ou afirmar saturação teórica.
6. **Revisão crítica:** comparar achados novos e anteriores, procurar evidência negativa e verificar se P1–P5 requerem restrições adicionais antes de preparar a entrega final.

## 8. Estrutura sugerida para versionamento (após validação do pesquisador)

```text
docs/trabalho-8/
  semana10-trabalho8-expansao-preliminar-v0.1.md
  semana10-trabalho8-entrega-final-v1.0.md          # criar somente quando critérios forem cumpridos

data/screening/
  semana10-candidatos-wave2-v0.1.csv

data/included/
  codificacao-semana10-studies-v0.2.csv            # após resolução e checagem dos novos estudos

docs/trabalho-8/
  codebook-delta-v0.4.md                          # apenas se novos códigos forem aceitos
```

**Estado das ações:** este documento e a matriz CSV foram gerados como **artefatos locais para revisão**; nenhum commit/push, submissão Classroom, verificação humana de full text ou aplicação completa de critérios é alegado.

## 9. Referências primárias verificadas nesta etapa

1. LI, Z. et al. *From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis*. CHI '25, 2025. https://doi.org/10.1145/3706598.3713133.
2. FLAMINO, J. et al. *Testing the limits of large language models in debating humans*. Scientific Reports, 15, 13852, 2025. https://doi.org/10.1038/s41598-025-98378-1.
3. LI, Zejian et al. *Does Sycophancy Change Decisions? Effect of LLM Sycophancy on AI-Assisted Decision-Making*. CHI '26, 2026. https://doi.org/10.1145/3772318.3790934.
4. ZHI, J.; KUMAR, H.; LEE, M. *Investigating the Effects of LLM Use on Critical Thinking Under Time Constraints: Access Timing and Time Availability*. CHI '26, 2026. https://doi.org/10.1145/3772318.3791796.
5. CHENG, M. et al. *Sycophantic AI decreases prosocial intentions and promotes dependence*. Science, 391, eaec8352, 2026. https://doi.org/10.1126/science.aec8352.
6. TSUCHIYA, Y.; BABA, Y. *More Isn't Always Better: Balancing Decision Accuracy and Conformity Pressures in Multi-AI Advice*. CHI '26, 2026. **Referência contextual, não um dos cinco candidatos.** https://doi.org/10.1145/3772318.3791648.
