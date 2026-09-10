# Levantamento sistemático preliminar de estudos secundários - v0.1

> **Status:** versão preliminar para a disciplina de Comunicação Científica.  
> **Data:** 2026-09-09.  
> **Tema:** vieses cognitivos humanos em julgamentos mediados por LLMs, com atenção a sistemas multiagentes.

## 1. Tema de interesse e relevância

Meu tema de interesse é a investigação de **vieses cognitivos humanos em processos de julgamento e tomada de decisão mediados por Large Language Models (LLMs), com atenção especial a sistemas multiagentes**. O interesse decorre da crescente incorporação de LLMs em sistemas de apoio à decisão e da evolução de arquiteturas nas quais múltiplos agentes podem gerar, criticar, verificar ou consolidar recomendações antes de apresentá-las ao usuário. Nesse contexto, características da interação podem influenciar a forma como pessoas avaliam evidências, revisam crenças e confiam nas recomendações recebidas. A pesquisa concentra-se especialmente nos vieses de confirmação e ancoragem e em fenômenos relacionados, como *automation bias*, *overreliance* e *trust calibration*. O tema é relevante para HCI porque o desenho da interação humano–IA pode não apenas melhorar decisões, mas também amplificar ou mitigar limitações cognitivas humanas.

## 2. Procedimento do levantamento

Este documento registra um **levantamento sistemático preliminar**, ainda em execução. O protocolo completo está versionado neste repositório. A estratégia prevê buscas em Scopus, Web of Science, ACM Digital Library, IEEE Xplore e PubMed, organizadas em famílias complementares: vieses cognitivos; confiança/reliance; decisão humano–IA; interação humano–LLM; panorama multiagente; e ponte humano–multiagente.

A primeira pilotagem no Scopus, referente à família **Q1 - Cognitive Bias Core**, foi executada em 09/09/2026 para o período 2018–2026. A consulta retornou **266 registros**, sem erro de sintaxe, e recuperou os dois estudos de calibração esperados para essa família (Bertrand et al., 2022; Romeo & Conti, 2026). Esse resultado é usado apenas para validar preliminarmente a estratégia de busca e **não constitui o corpus final**.

A avaliação de rigor utiliza o **QAISER - Quality Assessment Instrument for Software Engineering systematic literature Reviews**. O instrumento possui 15 itens agrupados em sete dimensões e orienta julgamentos de confiabilidade e relevância; portanto, não é empregado aqui como um escore simples de pontos. A avaliação abaixo é provisória e será revisada após leitura integral e aplicação item a item.

## 3. Estudos secundários preliminarmente identificados

| Estudo | Contribuição principal | Atualidade da evidência | Aderência ao tema |
|---|---|---|---|
| Bertrand et al. (2022) | Revisão sistemática de 37 estudos sobre relações entre vieses cognitivos e XAI; identifica casos em que XAI pode mitigar ou exacerbar vieses | **Baixa para o cenário LLM** | **Alta para vieses**, baixa para LLMs |
| Mehrotra et al. (2024) | Revisão sistemática sobre *appropriate trust*, *trust calibration* e *appropriate reliance* em interação humano–IA | **Baixa para LLMs** - busca final em 15/06/2022 | **Média/alta** |
| Vaccaro et al. (2024) | Revisão sistemática e meta-análise preregistrada de 106 experimentos e 370 efeitos sobre combinações humano–IA | **Média** - estudos até 30/06/2023 | **Média** - forte em decisão, não específica em vieses |
| Gomez et al. (2025) | Revisão sistemática de 105 estudos e taxonomia de padrões de interação em decisão assistida por IA | **Média** - corpus até junho/2023 | **Alta para interação**, viés é indireto |
| Romeo & Conti (2026) | Revisão de 35 estudos sobre *automation bias* e *over-reliance* em colaboração humano–IA | **Alta** - evidência até abril/2025 | **Alta** |
| Li et al. (2024) | Survey sobre sistemas multiagentes baseados em LLMs, cobrindo construção, aplicações, interação e desafios | **Alta para multiagentes** | **Alta para arquitetura multiagente**, baixa para viés humano |
| Moralles et al. (2026) | SLR sobre Agentic AI, definições, arquiteturas, desafios e lacunas | **Alta** - estudos peer-reviewed de 2021–2025 | **Média** |
| Bougault et al. (2026) | Mini-review de 60 estudos sobre Human–LLM Interaction, limitações e diretrizes de design | **Alta** - busca executada em 08/09/2025 | **Alta para Human–LLM**, não específica em vieses |

## 4. Avaliação QAISER preliminar

### 4.1 Legenda

- **✓**: evidência suficiente encontrada até o momento;
- **~**: evidência parcial ou cumprimento incompleto;
- **?**: ainda não verificado em profundidade;
- **-**: não aplicável/não identificado nesta etapa.

Os sete grupos abaixo sintetizam os 15 itens do QAISER:

- **G1 - Motivação:** justificativa para a revisão;
- **G2 - Protocolo:** protocolo prévio, pilotagem e validação;
- **G3 - Identificação e seleção:** critérios, busca, seleção e exclusões;
- **G4 - Coleta e appraisal:** extração, caracterização e avaliação da qualidade dos estudos primários;
- **G5 - Síntese:** método de síntese e consideração da qualidade/características dos estudos;
- **G6 - Conclusões:** rastreabilidade e adequação das recomendações/conclusões;
- **G7 - Conflitos:** financiamento e conflitos de interesse.

| Estudo | G1 | G2 | G3 | G4 | G5 | G6 | G7 | Confiabilidade preliminar |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Bertrand et al. (2022) | ✓ | ? | ✓ | ? | ✓ | ✓ | ? | **Moderada** |
| Mehrotra et al. (2024) | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ? | **Moderada** |
| Vaccaro et al. (2024) | ✓ | ✓ | ✓ | ~ | ✓ | ✓ | ✓ | **Alta** |
| Gomez et al. (2025) | ✓ | ? | ✓ | ~ | ✓ | ✓ | ? | **Moderada** |
| Romeo & Conti (2026) | ✓ | ~ | ✓ | ~ | ✓ | ✓ | ? | **Moderada** |
| Li et al. (2024) | ✓ | ? | ~ | ? | ✓ | ✓ | ✓ | **Baixa/moderada** |
| Moralles et al. (2026) | ✓ | ~ | ~ | ? | ✓ | ✓ | ? | **Moderada** |
| Bougault et al. (2026) | ✓ | ~ | ~ | ~ | ✓ | ✓ | ✓ | **Baixa** |

### 4.2 Nota metodológica

A classificação de confiabilidade acima é **provisória**. O QAISER não deve ser reduzido a um somatório do tipo “11/15”. A versão final deverá registrar a justificativa de cada item e consolidar os julgamentos nos níveis item, grupo e revisão.

## 5. Por que um novo estudo secundário é necessário?

Embora existam revisões sistemáticas sobre vieses cognitivos em XAI, *automation bias*, confiança, *reliance* e colaboração humano–IA, o conhecimento disponível permanece fragmentado. Parte das revisões metodologicamente mais robustas utiliza conjuntos de evidências encerrados antes ou no início da rápida disseminação dos LLMs conversacionais. Em contrapartida, revisões mais recentes sobre LLMs, Agentic AI e sistemas multiagentes concentram-se predominantemente em arquitetura, autonomia, desempenho, coordenação e segurança, e não nos vieses cognitivos do decisor humano. Além disso, a literatura nem sempre distingue claramente vieses cognitivos humanos, comportamentos enviesados produzidos pelo modelo e efeitos que emergem da própria interação humano–IA.

**No levantamento realizado até o momento, não foi identificada uma síntese sistemática especificamente dedicada a compreender como LLMs - particularmente arquiteturas multiagentes - podem amplificar, manter ou mitigar vieses de confirmação e ancoragem durante o julgamento humano.** Essa formulação é deliberadamente conservadora: o levantamento ainda está em execução e, portanto, não se afirma que tais revisões “não existem”. A combinação preliminar de desatualização temporal, fragmentação conceitual e ausência de foco nas novas formas de mediação constitui a principal justificativa para uma nova revisão.

## 6. Síntese de uma página

### Vieses cognitivos humanos em julgamentos mediados por LLMs: estudos secundários e lacunas

Este levantamento examina estudos secundários sobre vieses cognitivos humanos em processos de julgamento e tomada de decisão mediados por Inteligência Artificial, com ênfase em Large Language Models (LLMs) e sistemas multiagentes. O interesse decorre da expansão dos LLMs de ferramentas de geração de texto para componentes de apoio à decisão, nos quais respostas, recomendações e debates entre agentes podem alterar a forma como usuários avaliam evidências e revisam crenças. O foco recai especialmente sobre vieses de confirmação e ancoragem, relacionados a automação, confiança e dependência excessiva. Esse recorte é relevante para HCI porque mudanças no desenho da interação podem alterar diretamente o comportamento decisório do usuário.

Os estudos secundários identificados mostram um campo relevante, porém fragmentado. Bertrand et al. (2022) revisaram 37 estudos sobre vieses cognitivos em decisões assistidas por XAI e mostraram que explicações podem mitigar ou exacerbar vieses. Mehrotra et al. (2024) sintetizaram a literatura sobre confiança apropriada em interação humano–IA, destacando *trust calibration* e *appropriate reliance*, mas sua busca terminou em junho de 2022, antes da adoção massiva de LLMs conversacionais. Vaccaro et al. (2024), em revisão sistemática e meta-análise de 106 experimentos, concluíram que combinações humano–IA não superam necessariamente o melhor agente isolado e observaram perdas em tarefas decisórias. Gomez et al. (2025) analisaram 105 estudos e identificaram que a interação humano–IA ainda é dominada por padrões simples. Romeo e Conti (2026) atualizaram a discussão sobre *automation bias* até abril de 2025, mostrando que explicações, confiança, expertise e características da tarefa influenciam a dependência de recomendações automatizadas.

A literatura recente já aborda diretamente LLMs e sistemas multiagentes, mas com outro foco. Li et al. (2024) sintetizam arquiteturas, interação entre agentes e aplicações de LLM-based multi-agent systems, enquanto Moralles et al. (2026) revisam definições, arquiteturas e desafios de Agentic AI. Esses levantamentos concentram-se principalmente em arquitetura, autonomia, desempenho, segurança e coordenação, e não em vieses cognitivos do usuário humano. Bougault et al. (2026) aproxima-se da interação humano–LLM, mas apresenta limitações metodológicas e não focaliza especificamente vieses humanos.

A avaliação preliminar pelo QAISER evidencia um descompasso entre rigor, atualidade e aderência. Revisões metodologicamente mais robustas possuem evidências encerradas antes ou no início da era dos LLMs, enquanto revisões recentes sobre LLMs ou agentes frequentemente não investigam vieses humanos ou apresentam métodos menos rigorosos. Assim, justifica-se um novo estudo secundário que integre HCI, vieses cognitivos, confiança, *reliance* e arquiteturas single- e multi-LLM, distinguindo vieses humanos, comportamentos do modelo e efeitos emergentes da interação.

**Extensão da síntese:** 404 palavras; aproximadamente 2.958 caracteres com espaços.

## 7. Referências dos estudos secundários

1. Bertrand, A., Belloum, R., Eagan, J. R., & Maxwell, W. (2022). *How Cognitive Biases Affect XAI-assisted Decision-making: A Systematic Review*. Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society (AIES '22), 78–91. https://doi.org/10.1145/3514094.3534164
2. Mehrotra, S., Degachi, C., Vereschak, O., Jonker, C. M., & Tielman, M. L. (2024). *A Systematic Review on Fostering Appropriate Trust in Human-AI Interaction: Trends, Opportunities and Challenges*. ACM Journal on Responsible Computing, 1(4), Article 26, 1–45. https://doi.org/10.1145/3696449
3. Vaccaro, M., Almaatouq, A., & Malone, T. (2024). *When combinations of humans and AI are useful: A systematic review and meta-analysis*. Nature Human Behaviour, 8, 2293–2303. https://doi.org/10.1038/s41562-024-02024-1
4. Gomez, C., Cho, S. M., Ke, S., Huang, C.-M., & Unberath, M. (2025). *Human-AI collaboration is not very collaborative yet: a taxonomy of interaction patterns in AI-assisted decision making from a systematic review*. Frontiers in Computer Science, 6, 1521066. https://doi.org/10.3389/fcomp.2024.1521066
5. Romeo, G., & Conti, D. (2026). *Exploring automation bias in human–AI collaboration: a review and implications for explainable AI*. AI & Society, 41, 259–278. https://doi.org/10.1007/s00146-025-02422-7
6. Li, X., Wang, S., Zeng, S., Wu, Y., & Yang, Y. (2024). *A survey on LLM-based multi-agent systems: workflow, infrastructure, and challenges*. Vicinagearth, 1, Article 9. https://doi.org/10.1007/s44336-024-00009-2
7. Moralles, C., Da Costa, L. A. L. F., Rigo, S. J., Kunst, R., De Souza, V. C., Silva, E. P., Prado, G. L. E., Schardosim, T. C., & Roehrs, A. (2026). *A Systematic Literature Review of Agentic AI: Definitions, Architectures, and Challenges*. IEEE Access, 14, 36176–36190. https://doi.org/10.1109/ACCESS.2026.3668138
8. Bougault, P., Ma, L., & Guey, W. (2026). *Designing Human-LLM Systems: A Review of Current State, Limitations, and Guidelines to Better Interaction*. In V. G. Duffy (Ed.), Digital Human Modeling and Applications in Health, Safety, Ergonomics and Risk Management (pp. 303–321). Springer. https://doi.org/10.1007/978-3-032-29842-3_20

## 8. Referências metodológicas

- Kitchenham, B., & Charters, S. (2007). *Guidelines for performing Systematic Literature Reviews in Software Engineering*. EBSE Technical Report EBSE-2007-01, Version 2.3.
- Usman, M., Ali, N. B., & Wohlin, C. (2023). *A Quality Assessment Instrument for Systematic Literature Reviews in Software Engineering*. e-Informatica Software Engineering Journal, 17(1), 230105. https://doi.org/10.37190/e-Inf230105

## 9. Limitações desta versão

1. As buscas nas cinco bases ainda não foram concluídas; apenas a Q1 foi pilotada no Scopus.
2. O conjunto de estudos acima é um *known-set* e conjunto preliminar de candidatos, não o corpus final.
3. A avaliação QAISER ainda precisa ser refeita item a item a partir do texto integral de cada revisão.
4. As categorias de atualidade e aderência são analíticas e não fazem parte do QAISER.
5. A conclusão sobre a necessidade de uma nova revisão deve ser atualizada após deduplicação, screening e snowballing.

## 10. Uso de Inteligência Artificial Generativa

Ferramentas de Inteligência Artificial Generativa foram utilizadas como apoio à revisão textual, organização de ideias, estruturação do material e refinamento de trechos. A seleção das fontes, a definição dos critérios metodológicos, a interpretação acadêmica dos estudos, a análise crítica dos resultados e a redação final são de responsabilidade exclusiva do autor.