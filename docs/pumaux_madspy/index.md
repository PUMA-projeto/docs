# Índice Sumário: PUMAUX MADSPY

Este índice sumariza os principais tópicos do sistema PUMAUX MADSPY, com links para os arquivos detalhados de cada seção.

## 1. Objetivos da Aplicação
- Plataforma centralizada para gestão de problemas de usabilidade e acessibilidade.
- Apoio a equipes de produto, design, desenvolvimento e QA.
- Padronização de avaliação e classificação segundo IHC e heurísticas de Nielsen.
- Visualizações analíticas, histórico de ações, integração com ferramentas externas.

[Ver detalhes](objetivos.md)

## 2. Arquitetura
- Monolítica modularizada: apresentação, negócio, persistência.
- Modularidade funcional, baixo acoplamento, abstrações, Docker.
- Tecnologias por camada: Vue 3, Node.js, Prisma, PostgreSQL, JWT, etc.

[Ver detalhes](arquitetura.md)

## 3. Frontend
- SPA em Vue 3 + TypeScript, focada em usabilidade e acessibilidade.
- Estrutura modular, atomic design, composables, testes integrados.
- Padrões de interface e acessibilidade (WCAG, heurísticas de Nielsen).

[Ver detalhes](frontend.md)

## 4. Backend
- Node.js + Express, modular em camadas (controller, service, repository).
- Prisma ORM, contratos abstratos, segurança JWT, middlewares.

[Ver detalhes](backend.md)

## 5. Estrutura de Dados
- Modelagem normalizada, entidades principais (User, Issue, Comment, etc.).
- Relacionamentos, rastreabilidade, indexação para análises.

[Ver detalhes](estrutura_dados.md)

## 6. Funcionalidades Principais
- Dashboard Analytics, catálogo de problemas, Kanban, comentários, gestão de usuários, consulta a materiais de referência.

[Ver detalhes](funcionalidades.md)

## 7. Fluxo de Trabalho
- Fases: Identificação, Triagem, Planejamento, Execução, Conclusão, Auditoria.

[Ver detalhes](fluxo_trabalho.md)

## 8. Diferenciais da Aplicação
- Base teórica estruturada, arquitetura modular, geração automatizada de testes, redundância informacional, interface autoconsciente de UX.

[Ver detalhes](diferenciais.md)

## 9. Hospedagem e Infraestrutura
- Docker, serviços recomendados, backup, CI/CD, segurança.

[Ver detalhes](infraestrutura.md)
