# Herança Negra Musicalidade — MVP acadêmico

Projeto acadêmico de apoio ao ensino da musicalidade e dos fundamentos históricos da capoeira do grupo Herança Negra, vinculado ao ODS 4 (Educação de Qualidade).

## Escopo mínimo
- RF01: organizar e listar o acervo por categoria (áudio e texto).
- RF02: reproduzir arquivos MP3 locais (funcionalidade planejada; interface ainda não implementada).
- RF03: exibir textos históricos (interface ainda não implementada).
- RF04: administração de conteúdos com autenticação (funcionalidade futura).

## Implementação atual
O módulo `src/main.py` implementa a **camada de dados**, com SQLite, cadastro, consulta e filtragem de metadados. Não há aplicativo Android, player ou interface Kivy prontos nesta versão. Os testes automatizados validam somente as operações implementadas; não comprovam reprodução de áudio, acessibilidade ou testes com usuários.

## Como testar
Requer Python 3.10+.

```bash
python -m pip install pytest pytest-cov
python -m pytest tests/ -v
python -m pytest tests/ --cov=src --cov-report=term-missing
```

O GitHub Actions executa os testes a cada push e pull request. A cobertura deve ser informada com base no relatório efetivamente gerado, nunca estimada.

## Estrutura
- `src/main.py`: núcleo de dados do acervo.
- `tests/test_main.py`: testes do núcleo.
- `.github/workflows/ci.yml`: integração contínua.
- `docs/requisitos.md`: requisitos e limites do MVP.

Projeto de Software — Experiência Prática 3.
