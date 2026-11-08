# Requisitos — Herança Negra Musicalidade

Origem: planejamento da Experiência Prática 2.

- **RF01 (obrigatório):** listar categorias e títulos do acervo cultural. A camada de dados está implementada; interface pendente.
- **RF02 (obrigatório):** reproduzir MP3 local selecionado, com um áudio por vez. Pendente.
- **RF03 (obrigatório):** apresentar texto histórico legível em dispositivo móvel. Pendente.
- **RF04 (desejável):** inserir conteúdos por interface administrativa com autenticação do Mestre. Pendente.

**Arquitetura planejada:** MVC, Python, Kivy/KivyMD e SQLite local.

**Implementação atual:** protótipo técnico da camada de dados com SQLite, consultas parametrizadas e testes automatizados. Não equivale ao MVP Android completo.

**Validação:** testes unitários da camada de dados no CI. Testes com usuários, execução em Android, player, interface e métricas de desempenho permanecem a realizar.
