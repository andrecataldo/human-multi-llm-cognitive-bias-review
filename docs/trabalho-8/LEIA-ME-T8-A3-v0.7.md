# Instalação da T8-A3 v0.7 — Trabalho 08

## Antes de tudo

Pacote **provisório** para revisão: não muda `protocol/`, nem `data/included/`, nem versões dos Trabalhos 3, 6 ou 7. Inclui 15 REPORTS/21 STUDIES como *conjunto de trabalho proposto*, e não total definitivamente incluído na seleção Scopus.

## Copiar os arquivos

Na raiz do repositório Ubuntu:

```bash
unzip -n ~/Downloads/t8-a3-consolidacao-v0.7.zip -d .
python -m unittest discover -s tests -p 'test_t8_a3_v07.py' -v
```

## Gerar a matriz real integrada do projeto

O script vai ler o CSV original **já existente no seu repositório** (`data/included/codificacao-semana-08-13-studies-v0.1.csv`) e unir ao CSV de oito unidades propostas. No ambiente de criação do pacote, o merge foi testado com uma fixture simulada, não com a sua cópia local desse CSV histórico.

```bash
python scripts/t8_a3_consolidar_v07.py
```

Saída derivada esperada: `data/screening/t8-a3-codificacao-integrada-21-studies-v0.7.csv`. Por segurança, se a saída já existir, o script **recusará sobrescrita**; use `--force` apenas após conferir o arquivo derivado.

## Conferir antes de commit

```bash
git status
git diff --check
git add docs/trabalho-8/ data/screening/ scripts/t8_a3_consolidar_v07.py tests/test_t8_a3_v07.py
git diff --cached --stat
git diff --cached --check
```

Mensagem sugerida **apenas depois da conferência**:

```bash
git commit -m "docs: consolida codificacao e QA preliminar T8-A3"
git push origin main
```

Não registre `data/screening/` como resultados de inclusão final. A proposta de emenda exige decisão separada antes de modificar os logs oficiais.
