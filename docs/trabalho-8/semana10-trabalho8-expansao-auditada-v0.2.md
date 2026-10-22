# Semana 10 - Trabalho 8: expansão auditada da codificação para 15 publicações

**Disciplina:** Comunicação Científica - PPGI/UNIRIO · **Professor:** Sean Siqueira  
**Pesquisa:** vieses cognitivos humanos em julgamentos mediados por LLMs, com atenção a sistemas multiagentes  
**Data:** 22/10/2026 · **Versão:** v0.2 - pacote de trabalho auditado, não submissão final validada  
**Repositório de referência:** https://github.com/andrecataldo/human-multi-llm-cognitive-bias-review

## 1. Continuidade e política de preservação

Não há alteração nem substituição dos resultados já entregues na Semana 09 - Trabalho 7 v0.3 (Resultados, Discussão e Teorização) e na Semana 08 - Trabalho 6. A integração usa os códigos AX01–AX05 e o `codebook-complementar-v0.3.md`, sem reinterpretar retroativamente os treze studies. As novas observações entram como **delta auditável**.

A metodologia de relato segue **SEGRESS**; identificação e seleção respeitam os critérios operacionais I1–I9/E1–E10 explicitados no Trabalho 3; codificação aberta/axial e comparação constante são procedimentos analíticos adotados **pelo presente estudo** e inspirados em Grounded Theory. Thought-Gear auxilia a discussão das proposições, mas nenhuma dessas extensões é atribuída ao SEGRESS. QAISER não foi aplicado a estudos primários.

## 2. Denominadores e proveniência - o que sabemos

| Objeto | Semana 09 validada | Semana 10 auditada | Contagem que podemos declarar |
|---|---:|---:|---|
| Reports da Wave 1, completos | 10 | preservados | **10 incluídos** |
| Study units da Wave 1, codificados | 13 | preservados | **13 unidades** |
| Novos reports | - | 5 candidatos, 4 com fonte primária de corpo completo consultada, 1 somente abstract | **5 candidatos**, não 5 inclusões finais |
| Novas study units humanas | - | 8 unidades mapeadas de forma provisória (ST014–ST021) | **8 linhas de pré-codificação** |
| Total prospectivo | 10 reports/13 studies | +5 reports/+8 studies | **15 reports/21 studies apenas se a elegibilidade for validada** |
| Pool Scopus retido em 16/09/2026 | 1.419 | export não localizado | **sem reconciliação de DOI comprovada** |

**Nota de granulação:** o experimento de prevalência de sycophancy entre **modelos** do report Cheng et al. não é uma unidade de desfecho cognitivo humano. Seus três experimentos *com participantes* são estudos 2a, 2b e 3. Um estudo-piloto de julgamentos independentes citado por Zhuoyan Li et al. é insumo de treinamento/calibração, não uma terceira unidade de intervenção humano–LLM principal; caso a equipe queira contá-lo autonomamente, deve justificar a elegibilidade e rever denominadores.

## 3. Reconciliação bibliográfica com a Wave 1

**Reconciliação executada:** comparação dos **DOIs** dos cinco candidatos com a **lista nominal dos dez reports publicados no Trabalho 3**, sem colisões observadas. Isso demonstra apenas que não são os mesmos dez reports; **não prova** que pertencem aos 1.419 retidos para full text. Para provar essa segunda relação é necessário o export original do screening, com EID/DOI/título e decisão `RETAIN_FOR_FULL_TEXT`. O script entregue `scripts/reconciliar_scopus_wave2.py` executa esse cruzamento estrito quando o arquivo local for fornecido, produzindo CSV de auditoria sem modificar dados brutos.

Os candidatos desta etapa foram identificados por pesquisa **complementar de publicações conhecidas**. Como a busca-base foi Scopus-only em 16/09/2026, os não localizados no pool devem ser documentados em **emenda prospectiva de identificação complementar**, nunca silenciosamente incorporados como se viessem da execução Scopus original. A busca complementar aqui relatada não pretende ser uma segunda busca sistemática completa ou atualização exaustiva.

## 4. Registro de elegibilidade e nível de acesso

**Legenda:** `S` = sustentado em dados bibliográficos/textuais consultados; `P` = pendente; `N/A` = não se aplica. I1 primário empírico; I2 humanos; I3 mediação/exposição LLM; I4 julgamento/decisão/crença/reliance; I5 viés ou fenômeno relacionado; I6 relação entre LLM e resultado humano; I7 período até 16/09/2026; I8 artigo de periódico ou full conference peer-reviewed; I9 texto completo em EN/PT/ES consultável.

| ID provisório | I1–I8 | I9 / acesso nesta sessão | Não duplicidade dos 10 | Pertence aos 1.419? | Status final |
|---|---|---|---|---|---|
| T8-C01 - Li et al. (2025) | S | **S**, manuscrito completo arXiv HTML / versão CHI verificada | S por DOI | **P** | CANDIDATE - FULLTEXT_REVIEWED |
| T8-C02 - Flamino et al. (2025) | S | **S**, *Scientific Reports* texto integral aberto | S por DOI | **P** | CANDIDATE - FULLTEXT_REVIEWED |
| T8-C03 - Zejian Li et al. (2026) | S por resumo e metadados | **P**, artigo CHI indexado; conteúdo integral não recuperado para conferência | S por DOI | **P** | CANDIDATE - ABSTRACT_ONLY |
| T8-C04 - Zhi et al. (2026) | S | **S**, arXiv HTML completo / publicação CHI verificada | S por DOI | **P** | CANDIDATE - FULLTEXT_REVIEWED |
| T8-C05 - Cheng et al. (2026) | S | **S**, artigo principal completo em PDF da revista *Science*; suplementos não integralmente auditados | S por DOI | **P** | CANDIDATE - FULLTEXT_REVIEWED |

**Atenção:** “FULLTEXT_REVIEWED” significa que o **conteúdo público da fonte primária** foi efetivamente consultado nesta etapa; **não** corresponde a `researcher_check_status=VERIFIED`, nem a juízo formal de qualidade/risco de viés. O report T8-C03 necessita de PDF ou texto completo obtido legitimamente pela biblioteca/ACM/autores; resumos secundários não substituem a fonte original.

## 5. Codificação aberta incremental - cinco reports / oito units

### T8-C01 - From Text to Trust (Zhuoyan Li et al., CHI 2025)

**Fonte publicada:** https://doi.org/10.1145/3706598.3713133; manuscrito de autores com texto completo https://arxiv.org/html/2502.11919. **Atenção editorial:** o cabeçalho da versão arXiv HTML cita DOI de conferência diferente; para referência bibliográfica prevalece a página final da ACM (`10.1145/3706598.3713133`).

**ST014 - experimento de apresentação de análises (seção 3):** decisões humanas sobre renda e recidivismo auxiliadas por recomendações de **random forest**; **GPT-4 produz análise textual de características**, não as recomendações preditivas. A amostra válida após verificações de atenção foi de **134** pessoas (renda) + **150** (recidivismo), total **284**. Manipulação `Control` (sem análise), `Seq` (análises apresentadas sequencialmente) e `All` (todas simultâneas); desfechos acurácia e taxas de overreliance/underreliance. **Resultado dos autores:** não houve diferença estatisticamente significativa nas três medidas entre as três condições, para ambas as tarefas (seções 3.4–3.5). **Interpretação da revisão:** explicação em volume/ordem não garante melhor uso do conselho; não equiparar a mecanismo psicológico demostrado. **Códigos:** `LLM_GENERATED_ANALYSIS`, `EXPLANATION_PRESENTATION`, `OVERRELIANCE`, `UNDERRELIANCE`; AX01, AX05.

**ST015 - experimento de seleção adaptativa (seção 5):** avaliação humana separada, com **447** (renda) + **397** (recidivismo) participantes válidos, total **844**, e tratamentos comparando seleção algorítmica (`Alg`) com Control, Seq, All, Rank (ordem por importância de características) e Human-Solo. **Resultado dos autores:** `Alg` elevou acurácia contra Control/Seq/Rank/Human-Solo em renda, e contra Seq/All/Rank/Human-Solo em recidivismo; **não** se deve afirmar significância em todos os contrastes possíveis. `Alg` reduziu significativamente overreliance contra Control/Seq/All/Rank em ambos os domínios; queda de underreliance **não foi geralmente significativa** entre grupos (seções 5.4.1–5.4.2). **Interpretação:** relevância e temporização da informação podem ser mais decisivas que adicionar explicações; não prova que o GPT-4 explique de fato a lógica da random forest. **Códigos:** `ADAPTIVE_EXPLANATION_SELECTION`, `APPROPRIATE_RELIANCE`, `OVERRELIANCE`, `UNDERRELIANCE`; AX01, AX02, AX05.

**Contraevidência / limitação:** estudos envolvendo decisão assistida por recomendação de algoritmo preditivo + análise textual de LLM; portanto não classificar como múltiplos agentes LLM, nem como decisão inicialmente gerada por LLM. Fontes: seções 3.1–3.5, 5.3–5.4, 6.3 da fonte primária.

### T8-C02 - Testing the limits of large language models in debating humans (Flamino et al., *Scientific Reports* 2025)

**Fonte integral:** https://www.nature.com/articles/s41598-025-98378-1. **ST016 - protocolo de jogos de debate e opinião:** 37 jogos concluídos, com composições `HH` (humanos; 10 jogos), `AH` (3 humanos + 3 agentes; 17) e `AA` (seis agentes; 10); **111 humanos entraram em jogos, 97 efetivamente conversaram**. Agentes geravam mensagens com GPT-4 e Llama 2, usavam personas e memória restrita ao jogo. Jogos inteiramente AA funcionam como comparação de dinâmica, **não como novo estudo cognitivo humano**. Os resultados incluem alterações de opinião e confiança percebida, com modelagem multinível; os autores concluem que agentes foram **menos convincentes aos humanos que outros humanos**, apesar de se manterem mais centrados no tema. O modelo relatou odds de mudança de opinião de 0,047 entre humanos versus 0,288 entre agentes ao agregar parceiros, uma diferença de **comportamento de quem muda opinião**, e não prova de que o humano é seis vezes mais persuadido por um LLM.

**Codificação:** `HUMAN_LLM_DEBATE`, `GROUP_COMPOSITION`, `AGENT_PERSONA`, `OPINION_SWITCH`, `PERCEIVED_CONFIDENCE`; AX03, AX04, AX05. **Limites:** universidade específica, condições de debate sobre dietas, agentes com identidade não transparente durante o jogo; não testou independência percebida versus real entre agentes. **Rastreamento:** introdução, desenho experimental, Results / *Opinion changing* / *Personal and perceived confidence*.

### T8-C03 - Does Sycophancy Change Decisions? (Zejian Li et al., CHI 2026)

**DOI e publicação verificados:** https://doi.org/10.1145/3772318.3790934. **ST017 - registro preliminar por resumo**, ainda sem codificação full text: experimento *mixed-design* `4 × 2` com **106 participantes**, confrontando `non-sycophantic`, `opinion agreement`, `direct praise` e `self-deprecation` em tarefas de previsão de encontros e investimento ETF. **Resultado afirmado no resumo dos autores:** concordância com opiniões prévias reforçou decisões iniciais; autodepreciação elevou confiança; entrevistas revelaram tensão entre suporte e objetividade quando os elogios se tornam excessivos. **Não registrar coeficientes, p-valores, inferências causais detalhadas ou medidas específicas a partir de sites de resumo de terceiros sem conferir a publicação original.**

**Codificação provisória:** `SYCOPHANCY_OPINION_AGREEMENT`, `DIRECT_PRAISE`, `SELF_DEPRECATION`, `DECISION_CHANGE`, `CONFIDENCE`; AX01, AX03, AX05. **Pendência impeditiva:** acesso integral, seção de medidas e análises, efeito por tarefa, intervalos e correções múltiplas. **Estado:** ABSTRACT_ONLY - *não elegível para alegação de full-text screening concluído*. Resumo do programa CHI: https://pgl.jp/papers/69dcad7555a355001e0741de.

### T8-C04 - Investigating the Effects of LLM Use on Critical Thinking Under Time Constraints (Zhi, Kumar e Lee, CHI 2026)

**Fontes:** https://doi.org/10.1145/3772318.3791796; https://arxiv.org/html/2603.08849. **ST018 - experimento único** `4 × 2` entre sujeitos, **N=393**, em tarefa de argumentação e decisão a partir de documentos. Fatores: acesso a LLM (`Early`, `Continuous`, `Late`, `No`) e tempo (`Insufficient`, `Sufficient`). Medidas distintas: pontuação do texto (*Essay*), número de argumentos, *Myside Bias score* (diferença absoluta entre número de argumentos pró e contra), recall e avaliação da fonte.

**Resultados dos autores:** interação significativa entre disponibilidade temporal e momento do LLM para **Essay score**, `F(3,381)=6,39`, `p<0,001`. Sob tempo **insuficiente**, `Early` e `Continuous` ajudaram em comparações específicas com `Late`; com tempo **suficiente**, houve **tendência descritiva** de pontuações maiores em `Late` e `No`, sem anunciar significância indiscriminada entre todas as condições. Sob tempo **suficiente**, `Late` reduziu Myside Bias em relação a `No` (médias **3,42 vs 4,41**, `p<0,05`) mantendo número semelhante de argumentos. `Early` e `Continuous` também mostraram menores diferenças pró/contra, mas geraram menos argumentos; não interpretá-las automaticamente como análise mais equilibrada. **Interpretação:** temporização do apoio pode alterar a amplitude do raciocínio; `Myside Bias` é operacionalização explícita no artigo e **não** demonstra por si só um mecanismo psicológico de *anchoring bias*. **Códigos:** `ACCESS_TIMING`, `TIME_AVAILABILITY`, `MYSIDE_BIAS`, `ARGUMENT_BALANCE`, `ESSAY_PERFORMANCE`; AX02, AX03, AX05. **Rastreamento:** seções 3.2, 4.1–4.3, Tabelas 3–4 e §6.

### T8-C05 - Sycophantic AI decreases prosocial intentions and promotes dependence (Cheng et al., *Science* 2026)

**Fonte publicada:** https://doi.org/10.1126/science.aec8352; cópia textual do artigo principal consultada: https://s3.amazonaws.com/media.mediapost.com/uploads/science.aec8352.pdf. **Importante:** autores distinguem *Study 1* (11 modelos, prevalência de sycophancy em dados de avaliação, **não** unidade de julgamento humano) dos três experimentos com participantes **Studies 2a, 2b e 3**, total **N=2.405**.

**ST019 - Study 2a, N=804:** experimento de vinhetas com respostas de IA concordantes vs não-concordantes e **manipulação adicional de estilo** (antropomórfico versus neutro). Participantes imaginavam conflitos interpessoais baseados em casos em que o narrador foi julgado culpado por consenso humano, mas desconheciam essa classificação. **Medidas**: crença de estar certo, disposição para reparar, e percepção da resposta. **Achados do artigo:** sycophancy elevou convicção de estar certo e reduziu disposição de reparação; não foram observados efeitos principais ou de interação significativos de estilo para esses dois desfechos. **Códigos:** `SOCIAL_SYCOPHANCY`, `ANTHROPOMORPHIC_STYLE`, `RIGHTNESS_JUDGMENT`, `REPAIR_INTENTION`; AX01, AX03, AX05.

**ST020 - Study 2b, N=801:** experimento de vinhetas com **origem percebida da resposta (humano vs IA)** manipulada, mantendo o conteúdo produzido por IA. **Achados:** sycophancy elevou convicção e reduziu intenção reparadora; rótulo de fonte não exibiu efeito principal/interação significativo nos dois desfechos principais; moderação exploratória por percepção de objetividade discutida separadamente. **Códigos:** `SOURCE_IDENTITY_LABEL`, `SOCIAL_SYCOPHANCY`, `PERCEIVED_OBJECTIVITY`, `REPAIR_INTENTION`; AX01, AX03, AX05.

**ST021 - Study 3, N=800:** interação **real** por chat de oito turnos sobre conflito interpessoal passado do participante, sob resposta sycophantic vs não sycophantic. **Achados:** direção geral replicada - maior convicção de estar certo, menor intenção reparadora, preferência/confiança na resposta favorável -, mas **intenção declarada não equivale a comportamento reparador no mundo real**. **Códigos:** `LIVE_CHAT`, `SOCIAL_SYCOPHANCY`, `RIGHTNESS_JUDGMENT`, `REPAIR_INTENTION`, `TRUST_PREFERENCE`; AX01, AX03, AX05.

**Efeito reportado sobre os três estudos:** o artigo relata aumentos aproximados de 62%/43%/25% em julgamento de estar certo e reduções aproximadas de 28%/21%/10% em disposição reparadora para 2a/2b/3 respectivamente, com testes reportados como `q<0,001` no resumo agregado da seção de resultados. **Não agregar esses percentuais em um efeito combinado**, nem atribuir os 49% de maior afirmação nas avaliações dos **modelos** aos experimentos humanos. Fonte: artigo principal, §§*Method and results*, RQ2/RQ3, figuras 3–4, Box 1 (página impressa 4 de 9); suplementos de métodos/tabelas ainda não foram auditados integralmente.

## 6. Atualização axial - comparação constante

| Eixo herdado | Novos candidatos | Resultado, confronto ou moderação |
|---|---|---|
| **AX01** - Credibilidade e aceitação sem discriminação | ST014, ST015, ST017*, ST019–ST021 | Mais análise textual não melhora automaticamente desempenho (ST014), mas seleção adaptativa melhora discriminação contra comparadores específicos (ST015); sycophancy eleva confiança/preferência sem evidenciar benefício para o julgamento social (ST019–ST021). |
| **AX02** - Sinais de erro, escrutínio e custo | ST015, ST018 | A **seleção** de informação e o **momento** do apoio integram as condições de contorno, sem alegar que o custo moderou causalmente os fenômenos em todas as tarefas. |
| **AX03** - Alinhamento, argumentação e crença | ST016, ST017*, ST018, ST019–ST021 | Participantes humanos percebem agentes menos convincentes em debate (ST016), enquanto respostas que validam conflitos podem reforçar convicções (ST019–ST021). Contextos e comparadores diferentes; não são contradições diretas. `MYSIDE_BIAS` de ST018 foi **mensurado**, diferentemente de ancoragem inferida na discussão. |
| **AX04** - Pluralidade e influência social | ST016 | Em grupos mistos, agentes conversacionais não se comportaram como humanos nem produziram vantagem persuasiva universal; **sem teste direto** de independência epistêmica percebida. |
| **AX05** - Percepção, ação e desempenho | Todas, respeitando * | Acurácia, overreliance, opinião, intenção pró-social e confiança são constructos e métricas diferentes. |

`*` ST017 permanece suportado por abstract, não pelo full text.

**Tensão central nova:** “LLM mais cedo” pode auxiliar a produzir argumentos sob pressão temporal, mas antecipar o apoio com tempo suficiente pode limitar deliberação e recall; isto exige revisar explicações simplistas de que mais assistência é sempre melhor. **Não reduzir** uma diferença entre argumentos pró/contra a confirmação causal de viés de ancoragem.

## 7. Teorização do Trabalho 7: teste de sensibilidade conceitual, NÃO reescrita

- **P1 - Explicação e aceitação:** ST014/ST015 introduzem uma distinção forte entre quantidade de explicações e seleção contextual. Não alteram o achado prévio em FT0070.
- **P2 - Avisos e verificação:** ST018 acrescenta o tempo disponível e o momento de acesso como condições possivelmente moderadoras, **sem provar** o moderador custo de checagem postulado em P2.
- **P3 - Crença anterior e busca:** ST017 e ST019–ST021 examinam concordância/validação; **não replicam** a medida de *confirmatory querying* de FT1222.
- **P4 - Pluralidade:** ST016 reforça que a influência depende de quem participa e do desenho experimental; “múltiplos agentes” não implica persuasão mais intensa.
- **P5 - Corroboração aparente:** **permanece SEM TESTE DIRETO**. Nem ST016 nem os demais manipulam a independência real das fontes e medem a independência percebida.

Os resultados do Trabalho 7 ficam como marco imutável; acima há apenas memos da nova onda que poderão orientar uma futura versão consolidada **depois** da inclusão formal dos reports.

## 8. Limitações e ameaças à validade (transparência)

1. **Origem da seleção:** não há match comprovado aos 1.419 registros Scopus; não afirmar que os cinco são amostragem originada da busca de 16/09/2026.
2. **Acesso incompleto:** ST017 é codificação de **abstract**; suas hipóteses detalhadas, amostra analítica final e testes requerem texto integral.
3. **Conferência humana:** registro construído com assistência de IA e leitura de fontes primárias públicas; `researcher_check_status=PENDING` para todas as unidades novas.
4. **Granulação:** um report pode conter mais estudos; estudo auxiliar do algoritmo e experimentos de modelos não entram automaticamente em outcomes humanos.
5. **Algoritmo preditivo ≠ LLM:** em ST014–ST015, random forest gera o conselho, enquanto o LLM acrescenta análise textual. Não catalogar como `LLM_ADVICE_GENERATOR`.
6. **Viés cognitivo vs medidas próximas:** não usar persuasão, preferência, confiança ou opinião como confirmação de confirmation/anchoring/automation bias; exceção operacional delimitada: *Myside Bias score* em ST018.
7. **Inferência causal:** não transformar diferenças entre estudos em mediação causal transversal, nem efeito nulo sem testar equivalência.
8. **Outcomes autorreportados:** intenção de agir no estudo de Cheng não comprova ação no cotidiano.
9. **Correção anterior:** FT0083 deve continuar interpretado conforme errata de setembro/2026: comparação GPT-4 personalizado vs não personalizado `p=0,0678`, não significativa.

## 9. Artefatos da Semana 10 e fechamento necessário

| Artefato | Finalidade | Situação |
|---|---|---|
| `semana10-trabalho8-expansao-auditada-v0.2.md` | leitura, rastreabilidade e discussão | **produzido** |
| `semana10-candidatos-wave2-v0.2.csv` | relatório de elegibilidade, profundidade de acesso, proveniência | **produzido** |
| `codificacao-wave2-8-studies-v0.2.csv` | delta ST014–ST021 compatível com CSV da Semana 08 | **produzido (pré-codificação)** |
| `evidencias-wave2-v0.2.csv` | medidas-chave e localizadores por study | **produzido** |
| `codebook-delta-semana10-v0.4.md` | novas definições/cautelas sem apagar codebook v0.3 | **produzido (proposto)** |
| `reconciliar_scopus_wave2.py` | cruzamento local de DOI/título exato com export da Scopus | **produzido; ainda não executado no pool 1.419** |

**Critério de conclusão definitiva da atividade:** (a) obter o CSV/XLSX Scopus ou registrar emenda explícita para novos canais de identificação; (b) texto completo de ST017 com full-text screening; (c) auditoria humana de pelo menos medidas/excertos decisivos e confirmação das oito unidades; (d) somente então mover a matriz delta de `data/screening` para `data/included`, declarar o novo total, versionar e submeter. O script aceita CSV/TSV exportado; para XLSX exportar uma cópia CSV sem alterar o original.

## 10. Referências primárias dos novos reports

1. LI, Zhuoyan; ZHU, Hangxiao; LU, Zhuoran; XIAO, Ziang; YIN, Ming. *From Text to Trust: Empowering AI-assisted Decision Making with Adaptive LLM-powered Analysis*. CHI '25, 2025. https://doi.org/10.1145/3706598.3713133. Texto: https://arxiv.org/html/2502.11919.
2. FLAMINO, James; MODI, Mohammed Shahid; SZYMANSKI, Boleslaw K.; CROSS, Brendan; MIKOLAJCZYK, Colton. *Testing the limits of large language models in debating humans*. Scientific Reports, 15, 13852, 2025. https://doi.org/10.1038/s41598-025-98378-1. Texto: https://www.nature.com/articles/s41598-025-98378-1.
3. LI, Zejian et al. *Does Sycophancy Change Decisions? Effect of LLM Sycophancy on AI-Assisted Decision-Making*. CHI '26, 2026. https://doi.org/10.1145/3772318.3790934. **Abstract acessado; texto integral pendente.**
4. ZHI, Jiayin; KUMAR, Harsh; LEE, Mina. *Investigating the Effects of LLM Use on Critical Thinking Under Time Constraints: Access Timing and Time Availability*. CHI '26, 2026. https://doi.org/10.1145/3772318.3791796. Texto: https://arxiv.org/html/2603.08849.
5. CHENG, Myra; LEE, Cinoo; KHADPE, Pranav; YU, Sunny; HAN, Dyllan; JURAFSKY, Dan. *Sycophantic AI decreases prosocial intentions and promotes dependence*. Science, 391(6792), eaec8352, 2026. https://doi.org/10.1126/science.aec8352. PDF do artigo: https://s3.amazonaws.com/media.mediapost.com/uploads/science.aec8352.pdf.