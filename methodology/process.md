# Research Process

```mermaid
flowchart TD
    A[Prior exploratory work] --> B[Controlled vocabulary]
    B --> C[Known-set]
    C --> D[Research questions]
    D --> E[Search strategy]
    E --> Q1[Q1 Cognitive Bias]
    E --> Q2[Q2 Trust/Reliance]
    E --> Q3[Q3 Human-AI Decision]
    E --> Q4[Q4 Human-LLM]
    E --> Q5A[Q5a Multi-Agent Landscape]
    E --> Q5B[Q5b Human-Multi-Agent]
    Q1 --> F[Database searches]
    Q2 --> F
    Q3 --> F
    Q4 --> F
    Q5A --> F
    Q5B --> F
    F --> G[Raw exports]
    G --> H[Normalization]
    H --> I[Deduplication]
    I --> J[Title/abstract screening]
    J --> K[Full-text screening]
    K --> L[Included secondary studies]
    L --> M[QAISER]
    L --> N[Currency]
    L --> O[Relevance]
    M --> P[Evidence matrix]
    N --> P
    O --> P
    P --> Q[Research gaps]
    Q --> R[Need for a new systematic review?]
```

## Princípios de processo

1. **Reprodutibilidade:** cada busca deve registrar base, versão da query, data, filtros e número de resultados.
2. **Proveniência:** arquivos brutos não são editados.
3. **Rastreabilidade:** cada estudo deve poder ser rastreado até sua base e query de origem.
4. **Controle de decisões:** mudanças metodológicas são registradas no decision log.
5. **Separação entre descoberta e evidência:** mappers anteriores, OpenAlex e ferramentas de IA servem como fontes exploratórias/auxiliares, não como corpus automaticamente incluído.
6. **Humano como sujeito cognitivo:** não atribuir cognição humana literal ao LLM.
7. **Known-set não é corpus:** estudos conhecidos validam busca; entram no corpus apenas se passarem pelos mesmos critérios de elegibilidade.

