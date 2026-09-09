# Raw Data

Arquivos neste diretório representam exportações originais das bases de dados.

## Regra

**Nunca editar ou sobrescrever um arquivo bruto.**

Cada execução deve gerar um novo arquivo com nome contendo, no mínimo:

```text
<database>_<query>_v<version>_<YYYY-MM-DD>.<ext>
```

Exemplo:

```text
scopus_q1_v0.2_2026-09-09.csv
```

Antes de publicar este repositório, revisar condições de redistribuição/licenciamento dos metadados exportados das bases. Se necessário, manter `data/raw/` privado e publicar apenas artefatos derivados permitidos.
