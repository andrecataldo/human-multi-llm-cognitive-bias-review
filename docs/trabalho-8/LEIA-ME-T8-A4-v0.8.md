# T8-A4 — Instruções de aplicação (v0.8)

**Instalar:** extrair o ZIP na raiz de `~/projects/human-multi-llm-cognitive-bias-review` com `unzip -n`; arquivos anteriores não são alterados. Este pacote adiciona apenas caminhos `docs/trabalho-8/`, `data/screening/`, `scripts/` e `tests/`.

**Verificação:**

```bash
python -m unittest discover -s tests -p 'test_t8_a4_v08.py' -v
python scripts/t8_a4_validar_v08.py

git status
git diff --check
```

O verificador consulta também os arquivos de inventário/índice/evidência do T8-A3 já presentes no repositório. Testes são **estruturais**; não ratificam veracidade das fontes primárias ou inclusão de novos reports.

**Versionamento depois da conferência:**

```bash
git add docs/trabalho-8/t8-a4-*.md data/screening/t8-a4-*.csv scripts/t8_a4_validar_v08.py tests/test_t8_a4_v08.py
git diff --cached --check
git diff --cached --stat
git commit -m 'docs: registra sintese ampliada e discussao preliminar T8-A4'
git push origin main
```

Não versionar a T8-A4 como resultado definitivo de 15 artigos. Não promover candidatos a `data/included/` sem adjudicação.
