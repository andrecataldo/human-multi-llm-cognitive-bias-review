# T8-A2 — v0.5 — Conteúdo do pacote

Extrair **na raiz do repositório** `~/projects/human-multi-llm-cognitive-bias-review/`, preservando caminhos internos. Adiciona somente arquivos novos `.md`, `.csv` e teste `.py`; não sobrescreve versões anteriores.

```bash
unzip -n ~/Downloads/t8-a2-revisao-v0.5.zip -d ~/projects/human-multi-llm-cognitive-bias-review
cd ~/projects/human-multi-llm-cognitive-bias-review
python -m unittest discover -s tests -p 'test_t8_a2_v05.py' -v
git status
git add docs/trabalho-8/t8-a2-revisao-elegibilidade-codificacao-v0.5.md data/screening/*v0.5.csv tests/test_t8_a2_v05.py
git diff --cached --check
git diff --cached --stat
```

O commit só deve ser realizado **após** conferir testes e o relatório. Com a fonte original Scopus ausente, isso é um **checkpoint preliminar**, não a entrega final do Classroom.
