# T8-A2 — Resolução das pendências: identificação complementar e alternativa T8-C06 (v0.6)

> **Disciplina:** Comunicação Científica — PPGI/UNIRIO; professor Sean Siqueira  
> **Data da análise:** 22/10/2026  
> **Status:** **PROPOSTA DOCUMENTADA E PRÉ-EXTRAÇÃO**. Não houve inclusão definitiva, execução sobre o export Scopus histórico ou assinatura da avaliação humana.  
> **Base de comparação:** `docs/trabalho-3/mapeamento-selecao-estudos-primarios-v0.1.md` e T8-A2 v0.5 (arquivos anteriores mantidos).

## 1. Resumo da decisão proposta

Continuar o estudo secundário, cujo objetivo da Semana 10 é alcançar **15 REPORTS** devidamente trabalhados, sem alegar que uma pesquisa feita em 22/10/2026 ocorreu em 16/09/2026. A fonte histórica Scopus (1.419 retidos para texto completo ou 2.830 com decisões) segue indisponível para auditoria. Portanto:

- Os 10 REPORTS originais (13 STUDIES) permanecem a base previamente selecionada.
- Quatro novos candidatos (T8-C01, T8-C02, T8-C04, T8-C05) têm pré-codificação com acesso a textos completos, **mas ainda carecem de proveniência e adjudicação humana**.
- **T8-C03** (*Does Sycophancy Change Decisions?*, DOI `10.1145/3772318.3790934`) permanece como **SUSPENSO_I9**. O registro da CHI 2026 e o resumo bibliográfico estão disponíveis, mas a versão integral não foi recuperada diretamente nesta sessão. Páginas que resumem resultados **não** equivalem à leitura do texto completo primário.
- **T8-C06** (Bean et al., *Nature Medicine*, DOI `10.1038/s41591-025-04074-y`) é uma alternativa ao C03: artigo completo, revisado por pares, publicado antes do cutoff, com decisões humanas em interação com LLMs. **Ainda é candidato e não substituição formalmente aprovada.**

## 2. Registro factual de fontes e operações

| Registro | Busca e resultado | Status |
|---|---|---|
| Fonte histórica | Arquivos do GitHub e documentos anteriores descrevem 1.419 retidos (16/09/2026), mas sem registros bibliográficos linha a linha para cruzamento | `SOURCE_UNAVAILABLE` |
| T8-C03 | Busca web dirigida pelo título exato + DOI + termos `pdf`, `arxiv`, repositório e fontes autorais (22/10/2026). DBLP confirma a publicação CHI 2026; ACM não forneceu acesso integral nesta sessão (403); ResearchGate ofereceu apenas pedido de texto | `ABSTRACT_ONLY_I9_OPEN` |
| T8-C06 | Busca web dirigida em 22/10/2026: `site:pmc.ncbi.nlm.nih.gov LLM AI advice human participants confirmation bias randomized experiment 2025` e pesquisa do título; leitura da página integral *Nature Medicine* e da página de correção | `PRIMARY_FULLTEXT_HTML_REVIEWED` |
| Registro de T8-C06 | DOI `10.1038/s41591-025-04074-y`, publicado **09/02/2026**, *Nature Medicine* 32, pp. 609–615; DOI da correção `10.1038/s41591-026-04404-8` | `METADATA_CONFIRMED` |

**Nota:** a busca web foi **exploratória e dirigida** à resolução do bloqueio; não constitui nova revisão sistemática exaustiva. O artigo T8-C06 **não está comprovadamente dentro ou fora** dos 1.419 registros Scopus originais. Não atribuir `SCOPUS_RETAINED` a qualquer candidato sem export ou evidência equivalente.

### Fontes verificáveis

- Artigo T8-C06, HTML integral: https://www.nature.com/articles/s41591-025-04074-y
- Errata (17/04/2026): https://www.nature.com/articles/s41591-026-04404-8
- Registro bibliográfico: https://pubmed.ncbi.nlm.nih.gov/41663592/
- Projeto de dados/código dos autores: https://github.com/am-bean/HELPMed
- Registro de T8-C03: https://dblp.org/rec/conf/chi/LiPLXZJMC26
- DOI de T8-C03: https://doi.org/10.1145/3772318.3790934

## 3. Ficha preliminar de elegibilidade do T8-C06 — I1–I9

| Critério | Resultado da leitura | Decisão pendente |
|---|---|---|
| I1 Primário empírico | Experimento randomizado pré-registrado com humanos; complementado por benchmarks/model-only que **não** entram como STUDY humana | Favorável |
| I2 Participantes humanos | 1.298 adultos no Reino Unido | Favorável |
| I3 Uso de LLM | Grupos GPT-4o, Llama 3 e Command R+; controle com recursos habituais, inclusive busca na Internet | Favorável |
| I4 Julgamento/decisão | Condição médica provável e escolha de conduta (disposition) em dez cenários | Favorável |
| I5 Viés ou fenômeno relacionado | Decisão, reliance comportamental exploratória e qualidade de julgamento; **nenhum cognitive bias específico é inferido como operacionalizado** | Favorável com ressalva de escopo |
| I6 Relação LLM–outcome | Comparação entre braços experimentais e respostas finais de participantes | Favorável |
| I7 Período até 16/09/2026 | Publicado 09/02/2026; correção 17/04/2026 | Favorável |
| I8 Peer-reviewed, artigo completo | Periódico *Nature Medicine*; seção editorial de revisão por pares | Favorável |
| I9 Texto integral em EN/PT/ES | HTML integral disponível e consultado, com resultados, método e limitações | Favorável |

**Pré-decisão:** `PRE_ELIGIBLE_WITH_SCOPE_CAVEAT`, sujeita à verificação humana, à pesquisa de duplicatas no conjunto completo e à emenda de identificação complementar. Não marcar `INCLUDE_REPORT` ainda.

## 4. Extração e codificação preliminar — T8-C06 / ST022

**Identificador proposto:** `ST022` (novo ID, para **não reaproveitar ST017**, já atribuído à pré-codificação do T8-C03). O número é identificador estável, não contagem de unidades incluídas. Se o C03 for excluído, ST017 permanece histórico/suspenso; o denominador deve ser contado por `INCLUDE_STUDY`, não pelo maior ID.

- **Desenho:** estudo randomizado pré-registrado com 1.298 participantes e quatro condições (três LLMs ou controle). Até duas respostas por participante; 600 respostas por condição. **Não equiparar participantes a respostas**.
- **Ator humano:** adulto leigo. **Arquitetura:** uso de **um** modelo por braço, não debate multiagente. Comparar três modelos em grupos separados não é multi-LLM colaborativo.
- **Domínio:** identificação de possíveis condições e decisão sobre procura de atendimento em cenário simulado, sem decisão clínica real acompanhada.
- **Medidas:** (a) proporção de respostas que identificam condição relevante e (b) proporção de escolhas corretas de conduta; referência médica construída por profissionais. A análise de uma amostra de 30 conversas observa intercâmbio de informação e aproveitamento de recomendações, mas **não mede diretamente** um construto psicométrico de automation bias ou anchoring bias.
- **Resultados autores:** modelos, quando receberam os cenários completos, identificaram ao menos uma condição relevante em aproximadamente 94,9% das respostas; participantes com LLM acertaram condições em menos de 34,5% das respostas e condutas em menos de 44,2%, sem superar o controle; a análise estatística mostrou **controle superior para identificar condições**, e **diferenças de acerto de conduta não significativas**. Respostas em condição LLM não reproduziram consistentemente os acertos dos modelos isolados.
- **Interpretação da revisão (não dos autores):** o estudo ilustra que a disponibilidade de conselho competente não garante transferência de desempenho à interação humano–LLM, consistente com **AX02 (escrutínio/processamento da informação)** e **AX05 (descompasso entre capacidade isolada do modelo e desempenho observado na interação)**. **Não** usar como evidência causal de `OVERRELIANCE`, `AUTOMATION_BIAS`, `CONFIRMATION_BIAS` ou `ANCHORING_BIAS`.
- **Limites:** cenários fictícios; domínio médico de alto risco; controle permite busca usual; dificuldade de atribuir falha a mecanismo causal isolado; achado sobre seguir recomendações deriva parcialmente de pequena amostra qualitativa (30 conversas).

### Correção editorial

Em 17/04/2026, a editora corrigiu os rótulos do eixo y em **Figura 2a** (havia repetição de `80` no lugar de `40`). O aviso de correção relata ajuste gráfico de escala; **não registra alteração dos valores ou inferências**. Para extrair a Figura 2a, utilizar a versão atualizada.

## 5. Efeito sobre o inventário e noção de 15 artigos

**Sem emenda aprovada:** corpus histórico = **10 REPORTS / 13 STUDIES**; expansão ainda não homologada.  
**Se** uma identificação complementar for formalmente adotada e quatro candidatos existentes + T8-C06 forem adjudicados: **15 REPORTS e, conforme pré-identificação, 21 STUDIES humanas** (novas unidades ST014–ST016, ST018–ST022; ST017 **suspensa**, não computada).  
Isso é um **cenário**, não um resultado ocorrido.

O inventário v0.6 mantém os seis registros (cinco anteriores + um alternativo) para transparência, **não** diz que seis novos reports serão incluídos. Preservar `docs/trabalho-8/*v0.1..v0.5*` e arquivos antigos em `data/screening/`.

## 6. Deliberação metodológica proposta — AM-002 e SD-021

Registrar em `protocol/amendments.md` e `protocol/decision-log.md` **somente após aprovação** da seguinte decisão de método própria do projeto:

> **AM-002 (PROPOSTA):** Em vista da indisponibilidade, até 22/10/2026, do export linha a linha da busca Scopus de 16/09/2026, admitir uma identificação complementar **prospectivamente registrada em 22/10/2026** por busca web dirigida e consulta às fontes editoriais. Preservar integralmente os números da busca Scopus histórica; não atribuir à amostra original os candidatos desta expansão sem reconciliação documental; aplicar mesmos critérios I1–I9 e E1–E10, avaliar qualidade de estudos primários, apresentar o processo e os registros de fontes/datas separadamente no fluxo final de seleção. Não apresentar a busca dirigida como exaustiva. Manter I9 como exigência. Caso apareça o export original, reconciliar as fontes e resolver duplicatas antes do fluxo final.

**SD-021 (PROPOSTA):** Manter T8-C03 suspenso por falta de texto completo e considerar T8-C06 como **substituto candidato**, com ID próprio; não migrar automaticamente ST017 para novo report.

**SEGRESS:** a emenda é decisão da pesquisa, **não procedimento prescrito pelo SEGRESS**; o SEGRESS orienta a transparência do relato das fontes, datas e seleção.

## 7. Gates restantes para finalizar o Trabalho 08

1. Verificar, se possível, export histórico (1.419 retidos ou 2.830 com decisões); **não** inferir proveniência sem dados.
2. Aprovar explicitamente ou rejeitar a identificação complementar e registrar as decisões em `protocol/`.
3. Adjudicar humanamente as evidências e os critérios I1–I9 dos quatro candidatos mantidos e do T8-C06; realizar QA-Primary; testar o codebook atualizado sem confundir *cue* com mecanismo.
4. Somente então promover registros para `data/included/`, consolidar 15 REPORTS com número efetivo de STUDIES, atualizar discussão axial/seletiva e redigir o Trabalho 08 final para o Classroom.

**Auditabilidade:** `data/screening/t8-a2-candidatos-e-alternativa-v0.6.csv`, `data/screening/t8-a2-evidencias-c06-v0.6.csv` e `data/screening/t8-a2-codificacao-c06-v0.6.csv` são **dados derivados novos**, sem sobrescrever os v0.5.
