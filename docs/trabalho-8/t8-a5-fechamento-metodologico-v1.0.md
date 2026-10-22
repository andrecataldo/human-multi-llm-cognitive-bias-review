# T8-A5.1 - Fechamento metodológico, decisões e pendências (v1.0)

**Data:** 22/10/2026 · **Disciplina:** Comunicação Científica (PPGI/UNIRIO) · **Professor:** Sean Siqueira  
**Estado:** `MINUTA_DE_DECISAO` - não modifica `protocol/amendments.md` nem `protocol/decision-log.md` automaticamente.

## 1. Deliberação de trabalho e limites

A T8-A5 utiliza, **para fins de síntese provisória**, duas trilhas que não devem ser confundidas:

1. **Busca Scopus original (16/09/2026)**: 3.365 ocorrências → 3.256 reports bibliográficos únicos → 2.830 triados → 1.419 retidos para full text → Wave 1 com **10 reports incluídos / 13 estudos**. Não revisar retrospectivamente essa contagem sem arquivos de origem.
2. **Identificação complementar dirigida (outubro/2026)**: **6 candidatos** C01–C06, sendo C03 suspenso por I9. O conjunto de trabalho considera **5 reports adicionais e 8 estudos adicionais propostos**. **Não** foi demonstrado que pertenciam aos 1.419 e **não** há novo fluxo sistemático de busca em outra base com contagem completa.

Essa segunda trilha é uma **extensão metodológica proposta pelo estudo**. SEGRESS orienta relato e transparência; **não** prescreve a busca complementar nem a codificação inspirada em Grounded Theory, o Thought-Gear ou o instrumento QA-Primary.

A concordância em elaborar a T8-A5 autoriza **preparar a minuta**; não é tratada como assinatura de adjudicação humana do protocolo ou dos reports. A decisão oficial precisa de registro pelo pesquisador responsável.

## 2. Conjunto analítico e escolha do substituto

- **Wave 1**: 10 reports / 13 studies (ST001–ST013), preservados sem recodificação.
- **Expansão proposta**: T8-C01 (ST014/ST015), T8-C02 (ST016), T8-C04 (ST018), T8-C05 (ST019/ST020/ST021), T8-C06 (ST022).
- **Candidato suspenso**: T8-C03 / ST017 - resumo recuperado, texto integral indisponível nesta atividade. Não integrar o denominador, não reaproveitar o identificador.
- **C06**: texto integral disponível e publicação anterior a 16/09/2026; **I5 demanda decisão explícita**. Mede desempenho decisório humano mediado por LLM, **não** medida psicológica direta de viés. C06 usa diferentes LLMs em **braços separados**, não um sistema multi-LLM de consenso.

**Indicador correto da entrega:** `15 REPORTS / 21 STUDIES PROPOSTOS`; a ampliação possui **zero novos reports formalmente homologados** enquanto os gates G01–G08 estiverem abertos.

## 3. Minutas de registro para `protocol/` (NÃO APLICADAS)

### AM-002 - Identificação complementar de estudos primários

| Campo | Minuta |
|---|---|
| Identificador | `AM-002` |
| Data da proposição | 22/10/2026 |
| Situação | `PROPOSED / AWAITING_RESEARCHER_APPROVAL` |
| Objeto | Autorizar, de forma prospectiva, identificação complementar dirigida de estudos primários para uma onda adicional, mantendo separação das contagens da busca Scopus de 16/09/2026. |
| Justificativa | O export linha a linha dos 1.419 retidos não foi recuperado; a atividade docente solicita ampliação do corpus; busca posterior localizou estudos potencialmente pertinentes. |
| Condições | Registrar fontes, datas, termos/estratégias efetivamente executados, DOIs, deduplicação, decisões I1–I9, aquisição de texto completo, verificação humana e fluxo `identificado → avaliado → incluído/excluído`. |
| Efeito | Nenhuma contagem da busca original é alterada; as novas publicações só passam a `data/included/` após adjudicação. |

### SD-021 - C03 suspenso e C06 candidato alternativo

**Proposta:** manter C03 suspenso enquanto seu texto integral não puder ser conferido (I9) e avaliar C06 como alternativa com controle I5. Preservar ST017; usar ST022 para C06. **Status:** `PROPOSED`.

### SD-022 - Denominadores e reporte do corpus

**Proposta:** publicar separadamente números de **REPORTS** e **STUDIES**, distinguir `PROPOSED` de `INCLUDED` e jamais associar retrospectivamente a identificação complementar aos 1.419 registros Scopus sem evidência documental. **Status:** `PROPOSED`.

## 4. Checklist de fechamento

| Gate | Dimensão | Status | Condição para encerrar |
| --- | --- | --- | --- |
| G01 | Proveniência da identificação | ABERTO | Recuperar export histórico 1.419/2.830 OU aprovar emenda prospectiva de identificação complementar com registros fonte/consulta/data |
| G02 | Rastreabilidade da identificação complementar | ABERTO | Registrar quando/onde/como foram encontrados C01 C02 C04 C05 C06; termos, URLs, datas, deduplicação e fluxo de seleção separado |
| G03 | Elegibilidade por texto integral | ABERTO | Aplicar I1–I9 aos 5 candidatos e registrar decisão de cada report, com especial atenção a I5 de C06 |
| G04 | Texto integral candidato suspenso | NAO_BLOQUEIA_CENARIO_15_COM_C06 | C03 fora da contagem; recuperar texto completo apenas se considerado para futura inclusão |
| G05 | Conferência e crítica das evidências | ABERTO | Verificar tamanho das amostras, comparadores, métricas, suplementos, erratas e localizadores dos 8 estudos novos |
| G06 | QA-Primary novos candidatos | ABERTO | Adjudicar QA1–QA10 individualmente com fonte para C01 C02 C04 C05 C06; não somar score |
| G07 | QA-Primary histórico | CONDICIONAL | Aplicar QA1–QA10 aos 10 anteriores somente se afirmar avaliação de qualidade dos 15 reports |
| G08 | Homologação e promoção | ABERTO | Aprovar decisões prospectivamente; confirmar 5 sem duplicatas; mover apenas homologados para data/included/ e atualizar fluxo |
| G09 | Entrega do Classroom | ABERTO | Revisar versão final, link do commit, descrição honesta de 15 propostos vs incluídos e mensagem ao professor |

**Registro de execução:** o arquivo `data/screening/t8-a5-checklist-fechamento-v1.0.csv` é a versão operacional e deverá ser atualizado pelo pesquisador após cada conferência. Nenhuma validação humana é presumida aqui.

## 5. Matriz por publicação

| ID | Estudos | Situação | I5 | I9 | Próxima verificação |
| --- | --- | --- | --- | --- | --- |
| FT0070 | ST001;ST002 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT0072 | ST003;ST004 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT0080 | ST005 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT0083 | ST006 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT0310 | ST007 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT0318 | ST008 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT0545 | ST009 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT0772 | ST010 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT1222 | ST011;ST012 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| FT1233 | ST013 | HISTORICO_WAVE1_INCLUIDO | WAVE1_DOCUMENTADO | CONFERIDO_WAVE1 | Preservar elegibilidade histórica; checar evidencias humanas e QA se declarar qualidade do corpus. |
| T8-C01 | ST014;ST015 | CANDIDATO_ADICIONAL_NAO_HOMOLOGADO | FAVORAVEL_PRELIMINAR | SIM_PRELIMINAR | Conferir DOI, texto/suplementos, criterios I1-I9 e fonte de identificacao; adjudicacao humana. |
| T8-C02 | ST016 | CANDIDATO_ADICIONAL_NAO_HOMOLOGADO | FAVORAVEL_PRELIMINAR | SIM_PRELIMINAR | Conferir DOI, texto/suplementos, criterios I1-I9 e fonte de identificacao; adjudicacao humana. |
| T8-C03 | ST017_SUSPENDED | SUSPENSO_NAO_CONTAR | INDETERMINADO_I9_INDISPONIVEL | NAO_COMPROVADO | Obter texto integral; reavaliar inclusao I1-I9, sem reaproveitar ST017. |
| T8-C04 | ST018 | CANDIDATO_ADICIONAL_NAO_HOMOLOGADO | FAVORAVEL_PRELIMINAR | SIM_PRELIMINAR | Conferir DOI, texto/suplementos, criterios I1-I9 e fonte de identificacao; adjudicacao humana. |
| T8-C05 | ST019;ST020;ST021 | CANDIDATO_ADICIONAL_NAO_HOMOLOGADO | FAVORAVEL_PRELIMINAR | SIM_PRELIMINAR | Conferir DOI, texto/suplementos, criterios I1-I9 e fonte de identificacao; adjudicacao humana. |
| T8-C06 | ST022 | CANDIDATO_ADICIONAL_NAO_HOMOLOGADO | ACEITABILIDADE_PENDENTE_SEM_VIES_DIRETO | SIM_PRELIMINAR | Adjudicar I5; confrontar estudo e correcao; confirmar deduplicacao/proveniencia. |

## 6. Risco de validade e mitigação

**Viés de seleção:** cinco artigos foram escolhidos por identificação dirigida, não por sorteio nem por nova busca sistemática com cobertura completa. Essa forma de identificação pode favorecer artigos conhecidos e resultados específicos; deve ser apresentada como **amostra de expansão dirigida**, e não representativa dos 1.419.

**Viés de confirmação do pesquisador:** a escolha de estudos que parecem reforçar AX01–AX05 pode produzir circularidade. Mitigações recomendadas: registrar por que cada candidato foi selecionado, buscar explicitamente estudos negativos e avaliar se os novos resultados mudam a interpretação original (não apenas a corroboram).

**Instrumento QA:** `QA-Primary` aplicado preliminarmente apenas aos seis candidatos, inclusive o suspenso; dez reports históricos não foram reavaliados. Não relatar pontuação agregada, não afirmar avaliação comparativa de qualidade dos 15.

**Natureza da codificação:** a pré-extração foi `AI-assisted`, com verificação humana pendente. Não alegar segunda revisão independente, saturação teórica, Grounded Theory completa ou teste causal de P5.

## 7. Critério de saída da T8-A5

O arquivo `semana10-trabalho8-final-v1.0.md` é **documento acadêmico integrado e preparado para revisão**, não prova de 15 reports homologados. Uma entrega plenamente conclusiva requer marcações dos gates G01–G08, registros oficiais de emendas/decisões aprovadas, elegibilidade e QA adjudicados e atualização da trilha de evidências. Só depois afirmar no Classroom que “15 artigos foram devidamente trabalhados” sem qualificação.
