# Construção do Backlog do Produto

[← Voltar para a Página Principal](../index.md)

# 📌 Backlog - Sistema Puma

## 🎯 Objetivo do Produto

Permitir que stakeholders conheçam o programa Puma, realizem login/cadastro, submetam projetos, organizem disciplinas, turmas e times, e acompanhem o andamento e alocação de projetos.

| **TH-ID** | **Tema**       | **EP-ID** | **Épico**                        | **FE-ID** | **Feature**                         | **US-ID** | **User Story**                                                 |
| --------- | -------------- | --------- | -------------------------------- | --------- | ----------------------------------- | --------- | -------------------------------------------------------------- |
| TH-01     | Página Pública | EP-01     | Gestão da Página Pública         | FE-01     | Gerenciar Conteúdo da Página        | US-01     | Editar textos e imagens da landing page                        |
|           |                |           |                                  | FE-01     |                                     | US-02     | Gerenciar seções da landing page                               |
|           |                |           |                                  | FE-02     | Gerenciar Links e Documentos        | US-03     | Adicionar novos links na landing page                          |
|           |                |           |                                  | FE-02     |                                     | US-04     | Remover links obsoletos da landing page                        |
|           |                | EP-02     | Acompanhamento de Acessos        | FE-03     | Relatórios de Acesso                | US-05     | Gerar relatórios de acesso à landing page                      |
|           |                |           |                                  | FE-03     |                                     | US-06     | Analisar documentos mais acessados na página                   |
|           |                |           |                                  | FE-04     | Monitoramento de Interações         | US-07     | Monitorar seções mais acessadas                                |
|           |                |           |                                  | FE-04     |                                     | US-08     | Entender comportamento dos visitantes                          |
| TH-02     | Autenticação   | EP-03     | Autenticação de Usuário          | FE-05     | Registro de Usuário                 | US-09     | Visitante se cadastrar no sistema                              |
|           |                |           |                                  | FE-05     |                                     | US-10     | Administrador cadastrar usuários manualmente                   |
|           |                |           |                                  | FE-06     | Login de Usuário                    | US-11     | Usuário realizar login                                         |
|           |                |           |                                  | FE-06     |                                     | US-12     | Login seguro para área administrativa                          |
|           |                | EP-04     | Controle de Acesso de Usuário    | FE-07     | Definir Papéis de Usuário           | US-13     | Escolher papel no primeiro acesso                              |
|           |                |           |                                  | FE-07     |                                     | US-14     | Alterar papel de usuários                                      |
|           |                |           |                                  | FE-08     | Gerenciar Permissões                | US-15     | Definir permissões para cada papel                             |
|           |                |           |                                  | FE-08     |                                     | US-16     | Garantir acesso restrito dos alunos às suas atividades         |
| TH-03     | Usuário        | EP-05     | Gerenciamento de Usuários        | FE-09     | Criar Usuário                       | US-17     | Cadastrar novos professores e agentes externos                 |
|           |                |           |                                  | FE-09     |                                     | US-18     | Professor cadastrar agente externo para projetos               |
|           |                |           |                                  | FE-10     | Editar e Remover Usuário            | US-19     | Editar dados de usuários                                       |
|           |                |           |                                  | FE-10     |                                     | US-20     | Remover usuários inativos                                      |
|           |                | EP-06     | Busca e Listagem de Usuários     | FE-11     | Listagem de Usuários                | US-21     | Visualizar lista de usuários                                   |
|           |                |           |                                  | FE-11     |                                     | US-22     | Listar apenas alunos vinculados às turmas                      |
|           |                |           |                                  | FE-12     | Filtro de Usuários                  | US-23     | Filtrar usuários por nome, papel ou status                     |
|           |                |           |                                  | FE-12     |                                     | US-24     | Filtrar alunos nas turmas                                      |
| TH-04     | Projeto        | EP-07     | Gerenciamento de Projetos        | FE-13     | Criar e Editar Projetos             | US-25     | Criar projetos vinculados às turmas                            |
|           |                |           |                                  | FE-13     |                                     | US-26     | Cadastrar projetos gerais                                      |
|           |                |           |                                  | FE-14     | Remover Projetos                    | US-27     | Remover projetos não executados                                |
|           |                |           |                                  | FE-14     |                                     | US-28     | Excluir projetos antigos ou obsoletos                          |
|           |                | EP-08     | Acompanhamento de Projetos       | FE-15     | Listagem de Projetos                | US-29     | Ver projetos coordenados                                       |
|           |                |           |                                  | FE-15     |                                     | US-30     | Ver projetos que participo                                     |
|           |                |           |                                  | FE-16     | Filtro de Projetos                  | US-31     | Buscar projetos por nome ou disciplina                         |
|           |                |           |                                  | FE-16     |                                     | US-32     | Buscar projetos disponíveis                                    |
| TH-05     | Disciplina     | EP-09     | Gerenciamento de Disciplinas     | FE-17     | Criar e Editar Disciplinas          | US-33     | Criar disciplinas                                              |
|           |                |           |                                  | FE-17     |                                     | US-34     | Cadastrar disciplinas gerais                                   |
|           |                |           |                                  | FE-18     | Remover Disciplinas                 | US-35     | Remover disciplinas não ofertadas                              |
|           |                |           |                                  | FE-18     |                                     | US-36     | Excluir disciplinas obsoletas                                  |
|           |                | EP-10     | Busca de Disciplinas             | FE-19     | Listagem de Disciplinas             | US-37     | Ver disciplinas ministradas                                    |
|           |                |           |                                  | FE-19     |                                     | US-38     | Ver disciplinas que estou matriculado                          |
|           |                |           |                                  | FE-20     | Filtro de Disciplinas               | US-39     | Acompanhar progresso dos alunos nas disciplinas                |
|           |                |           |                                  | FE-20     |                                     | US-40     | Acompanhar meu progresso                                       |
| TH-06     | Turmas         | EP-11     | Gerenciamento de Turmas          | FE-21     | Criar e Editar Turmas               | US-41     | Criar novas turmas vinculadas às disciplinas                   |
|           |                |           |                                  | FE-21     |                                     | US-42     | Cadastrar turmas gerais                                        |
|           |                |           |                                  | FE-22     | Remover Turmas                      | US-43     | Remover turmas não realizadas                                  |
|           |                |           |                                  | FE-22     |                                     | US-44     | Excluir turmas inativas                                        |
|           |                | EP-12     | Acompanhamento de Turmas         | FE-23     | Listagem de Turmas                  | US-45     | Listar todas as turmas                                         |
|           |                |           |                                  | FE-23     |                                     | US-46     | Buscar turmas disponíveis                                      |
|           |                |           |                                  | FE-24     | Filtro de Turmas                    | US-47     | Consultar informações sobre turmas                             |
|           |                |           |                                  | FE-24     |                                     | US-48     | Acompanhar distribuição dos alunos nas turmas                  |
| TH-07     | Time           | EP-13     | Gerenciamento de Times           | FE-25     | Criar Times                         | US-49     | Criar times acadêmicos                                         |
|           |                |           |                                  | FE-25     |                                     | US-50     | Criar times de apoio operacionais                              |
|           |                |           |                                  | FE-26     | Gerenciar Times                     | US-51     | Editar, excluir ou reorganizar membros do time                 |
|           |                |           |                                  | FE-26     |                                     | US-52     | Remover times inativos                                         |
|           |                | EP-14     | Acompanhamento dos Times         | FE-27     | Visualizar Meu Time                 | US-53     | Ver informações do meu time                                    |
|           |                |           |                                  | FE-27     |                                     | US-54     | Acompanhar status dos times                                    |
|           |                |           |                                  | FE-28     | Acompanhar Status dos Times         | US-55     | Gerar relatórios sobre status dos times                        |
|           |                |           |                                  | FE-28     |                                     | US-56     | Visualizar status geral dos times                              |
| TH-08     | Entrega        | EP-15     | Gerenciamento de Entregas        | FE-29     | Criar Nova Entrega                  | US-57     | Criar nova entrega parcial ou final                            |
|           |                |           |                                  | FE-29     |                                     | US-58     | Editar uma entrega antes do prazo                              |
|           |                |           |                                  | FE-30     | Acompanhar Entregas                 | US-59     | Consultar histórico de entregas                                |
|           |                |           |                                  | FE-30     |                                     | US-60     | Visualizar todas as entregas feitas pelos times                |
|           |                | EP-16     | Validação e Feedback de Entregas | FE-31     | Validar Entregas                    | US-61     | Validar e avaliar entregas                                     |
|           |                |           |                                  | FE-31     |                                     | US-62     | Solicitar ajustes nas entregas antes da avaliação              |
|           |                |           |                                  | FE-32     | Feedback de Entregas                | US-63     | Fornecer feedback sobre entregas                               |
|           |                |           |                                  | FE-32     |                                     | US-64     | Visualizar feedback recebido                                   |
| TH-09     | Upload         | EP-17     | Upload de Entregas Parciais      | FE-33     | Upload de Entrega Parcial           | US-65     | Fazer upload de arquivos para entregas parciais                |
|           |                |           |                                  | FE-33     |                                     | US-66     | Substituir arquivos da entrega parcial antes do prazo          |
|           |                |           |                                  | FE-34     | Organização e Armazenamento Parcial | US-67     | Visualizar e recuperar arquivos de entregas parciais           |
|           |                |           |                                  | FE-34     |                                     | US-68     | Acessar arquivos das entregas parciais dos times               |
|           |                | EP-18     | Upload de Entregas Finais        | FE-35     | Upload de Entrega Final             | US-69     | Realizar upload da entrega final do projeto                    |
|           |                |           |                                  | FE-35     |                                     | US-70     | Substituir arquivos da entrega final antes do prazo            |
|           |                |           |                                  | FE-36     | Organização e Armazenamento Final   | US-71     | Acessar e visualizar os arquivos da minha entrega final        |
|           |                |           |                                  | FE-36     |                                     | US-72     | Acessar arquivos das entregas finais para realizar a avaliação |


### 1. Requisitos Funcionais

Define as **funcionalidades centrais do sistema**. O que o sistema deve fazer.

| FR-ID | Descrição                                                                                       |
| ----- | ----------------------------------------------------------------------------------------------- |
| FR-01 | O sistema deve possuir um **Portal de Informações para Visitantes Externos (Página Pública)**.  |
| FR-02 | O sistema deve possuir um **Sistema de Autenticação e Autorização de Usuários**.                |
| FR-03 | O sistema deve possuir um **Sistema de Gerenciamento de Perfis e Papéis de Usuários**.          |
| FR-04 | O sistema deve possuir um **Sistema de Submissão e Gerenciamento de Projetos**.                 |
| FR-05 | O sistema deve possuir um **Sistema de Gerenciamento de Disciplinas**.                          |
| FR-06 | O sistema deve possuir um **Sistema de Gerenciamento de Turmas**.                               |
| FR-07 | O sistema deve possuir um **Sistema de Formação e Gestão de Times**.                            |
| FR-08 | O sistema deve possuir um **Sistema de Entregas e Acompanhamento de Submissões de Atividades**. |
| FR-09 | O sistema deve possuir um **Sistema de Upload e Gerenciamento de Documentos e Arquivos**.       |

### 2. Requisitos Não Funcionais – ISO/IEC 25010 (SQuaRE)

| RNF-ID | Categoria               | Subcategoria           | Descrição                                                                                          |
| ------ | ----------------------- | ---------------------- | -------------------------------------------------------------------------------------------------- |
| RNF-01 | Desempenho e Eficiência | Capacidade de resposta | O sistema deve processar requisições em até 2 segundos para 95% das operações.                     |
| RNF-02 | Desempenho e Eficiência | Utilização de recursos | O sistema deve utilizar no máximo 70% de CPU e 75% de memória em cenários de pico.                 |
| RNF-03 | Desempenho e Eficiência | Capacidade             | O sistema deve suportar até 1000 usuários simultâneos sem degradação perceptível.                  |
| RNF-04 | Confiabilidade          | Disponibilidade        | O sistema deve estar disponível 99,5% do tempo durante dias úteis, exceto janelas de manutenção.   |
| RNF-05 | Confiabilidade          | Tolerância a falhas    | O sistema deve garantir que falhas parciais não comprometam o funcionamento geral.                 |
| RNF-06 | Confiabilidade          | Recuperabilidade       | O sistema deve ser capaz de se recuperar de falhas críticas em até 5 minutos.                      |
| RNF-07 | Usabilidade             | Apreensibilidade       | O sistema deve permitir que usuários aprendam as principais funcionalidades em até 1 hora.         |
| RNF-08 | Usabilidade             | Operacionalidade       | O sistema deve ser acessível e funcional tanto em desktop quanto em dispositivos móveis.           |
| RNF-09 | Usabilidade             | Acessibilidade         | O sistema deve atender os critérios WCAG 2.1 nível AA para acessibilidade.                         |
| RNF-10 | Segurança               | Confidencialidade      | Dados sensíveis devem ser criptografados em repouso e em trânsito.                                 |
| RNF-11 | Segurança               | Autenticidade          | O sistema deve possuir autenticação robusta, com suporte a autenticação multifator.                |
| RNF-12 | Segurança               | Integridade            | As informações não podem ser alteradas sem registro em logs de auditoria.                          |
| RNF-13 | Segurança               | Não repúdio            | Todas as ações críticas devem ser registradas para garantir rastreabilidade.                       |
| RNF-14 | Manutenibilidade        | Modularidade           | O sistema deve ser construído de forma modular para facilitar alterações e manutenções.            |
| RNF-15 | Manutenibilidade        | Analisabilidade        | Logs detalhados devem ser gerados para diagnóstico de erros e problemas.                           |
| RNF-16 | Manutenibilidade        | Testabilidade          | O sistema deve permitir a realização de testes automatizados de unidade, integração e sistema.     |
| RNF-17 | Portabilidade           | Adaptabilidade         | O sistema deve ser compatível com navegadores modernos (Chrome, Firefox, Edge, Safari).            |
| RNF-18 | Portabilidade           | Instalação             | O sistema deve ser passível de implantação via contêiner (Docker) em ambientes cloud e on-premise. |
| RNF-19 | Portabilidade           | Substituibilidade      | O backend deve permitir migração entre bancos de dados relacionais (PostgreSQL, MySQL).            |

### 3. Temas

**Temas** categorizam as **principais áreas do sistema**, agrupando funcionalidades sob tópicos amplos.

| FR-ID | TH-ID | Tema           | Descrição                                                                                 |
| ----- | ----- | -------------- | ----------------------------------------------------------------------------------------- |
| FR-01 | TH-01 | Página Pública | Gerenciar funcionalidades de acesso a informações públicas (landing page, pré-login).     |
| FR-02 | TH-02 | Autenticação   | Gerenciar funcionalidades relacionadas ao acesso e segurança do sistema.                  |
| FR-03 | TH-03 | Usuário        | Gerenciar funcionalidades relacionadas a perfis de usuários e controle de papéis.         |
| FR-04 | TH-04 | Projeto        | Gerenciar funcionalidades de submissão, acompanhamento, avaliação e alocação de projetos. |
| FR-05 | TH-05 | Disciplina     | Gerenciar funcionalidades de gestão de disciplinas.                                       |
| FR-06 | TH-06 | Turmas         | Gerenciar funcionalidades de gestão de turmas.                                            |
| FR-07 | TH-07 | Time           | Gerenciar funcionalidades de formação e organização de times de alunos.                   |
| FR-08 | TH-08 | Entrega        | Gerenciar funcionalidades de entrega, submissão e acompanhamento de atividades.           |
| FR-09 | TH-09 | Upload         | Gerenciar funcionalidades de upload, armazenamento e recuperação de arquivos.             |

### 4. Épicos

Cada épico é dividido em, no mínimo, duas capacidades, representando subfuncionalidades.

| TH-ID     | EP-ID | Épico                            | Descrição                                                                                    |
| --------- | ----- | -------------------------------- | -------------------------------------------------------------------------------------------- |
| **TH-01** | EP-01 | Gestão da Página Pública         | Gerenciar conteúdo, links, seções e atualizações da página pública (Landing Page).           |
| **TH-01** | EP-02 | Acompanhamento de Acessos        | Monitorar acessos, interações e métricas da página pública para otimização de conteúdo.      |
| **TH-02** | EP-03 | Autenticação de Usuário          | Gerenciar registro e login dos usuários.                                                     |
| **TH-02** | EP-04 | Controle de Acesso de Usuário    | Gerenciar permissões e papéis dos usuários.                                                  |
| **TH-03** | EP-05 | Gerenciamento de Usuários        | Gerenciar cadastro, consulta, edição, remoção e atribuição de papéis dos usuários.           |
| **TH-03** | EP-06 | Busca e Listagem de Usuários     | Gerenciar listagem de usuários e aplicação de filtros.                                       |
| **TH-04** | EP-07 | Gerenciamento de Projetos        | Gerenciar submissão, acompanhamento, avaliação e alocação de projetos.                       |
| **TH-04** | EP-08 | Acompanhamento de Projetos       | Monitorar status, progresso e avaliação de projetos no sistema.                              |
| **TH-05** | EP-09 | Gerenciamento de Disciplinas     | Gerenciar criação, edição, remoção e consulta de disciplinas.                                |
| **TH-05** | EP-10 | Busca de Disciplinas             | Gerenciar listagem e filtros de disciplinas.                                                 |
| **TH-06** | EP-11 | Gerenciamento de Turmas          | Gerenciar criação, edição, remoção e consulta de turmas.                                     |
| **TH-06** | EP-12 | Acompanhamento de Turmas         | Visualizar, monitorar e atualizar dados das turmas vinculadas às disciplinas.                |
| **TH-07** | EP-13 | Gerenciamento de Times           | Gerenciar criação, organização, alocação e acompanhamento dos times vinculados aos projetos. |
| **TH-07** | EP-14 | Acompanhamento dos Times         | Visualizar, monitorar e atualizar dados dos times e seus respectivos projetos.               |
| **TH-08** | EP-15 | Gerenciamento de Entregas        | Gerenciar submissão, acompanhamento e histórico de entregas de atividades pelos times.       |
| **TH-08** | EP-16 | Validação e Feedback de Entregas | Gerenciar validação, feedback e acompanhamento das entregas realizadas.                      |
| **TH-09** | EP-17 | Upload de Entregas Parciais      | Gerenciar funcionalidades de upload, armazenamento e recuperação de entregas parciais.       |
| **TH-09** | EP-18 | Upload de Entregas Finais        | Gerenciar funcionalidades de upload, armazenamento e recuperação de entregas finais.         |

### 5. Features

| TH-ID     | EP-ID | FE-ID | Feature                             | Descrição                                                                                |
| --------- | ----- | ----- | ----------------------------------- | ---------------------------------------------------------------------------------------- |
| **TH-01** | EP-01 | FE-01 | Gerenciar Conteúdo da Página        | Editar texto, links, imagens e seções da landing page pública.                           |
| **TH-01** | EP-01 | FE-02 | Gerenciar Links e Documentos        | Adicionar ou remover links para edital, regulamento, benefícios e outros.                |
| **TH-01** | EP-02 | FE-03 | Relatórios de Acesso                | Gerar relatórios de acesso à página pública (visitantes, cliques, tempo de navegação).   |
| **TH-01** | EP-02 | FE-04 | Monitoramento de Interações         | Acompanhar comportamento dos visitantes na página pública para otimizar o conteúdo.      |
| **TH-02** | EP-03 | FE-05 | Registro de Usuário                 | Permitir que novos usuários se cadastrem no sistema.                                     |
| **TH-02** | EP-03 | FE-06 | Login de Usuário                    | Permitir que usuários façam login com email e senha.                                     |
| **TH-02** | EP-04 | FE-07 | Definir Papéis de Usuário           | Permitir que usuários escolham ou sejam atribuídos a papéis (Aluno, Professor, Externo). |
| **TH-02** | EP-04 | FE-08 | Gerenciar Permissões                | Permitir controle de acesso baseado nos papéis definidos.                                |
| **TH-03** | EP-05 | FE-09 | Criar Usuário                       | Permitir cadastro manual de novos usuários.                                              |
| **TH-03** | EP-05 | FE-10 | Editar e Remover Usuário            | Permitir editar informações ou remover usuários do sistema.                              |
| **TH-03** | EP-06 | FE-11 | Listagem de Usuários                | Permitir visualizar todos os usuários cadastrados.                                       |
| **TH-03** | EP-06 | FE-12 | Filtro de Usuários                  | Permitir aplicar filtros por nome, email, papel, status, etc.                            |
| **TH-04** | EP-07 | FE-13 | Criar e Editar Projetos             | Permitir criar e modificar projetos.                                                     |
| **TH-04** | EP-07 | FE-14 | Remover Projetos                    | Permitir excluir projetos quando necessário.                                             |
| **TH-04** | EP-08 | FE-15 | Listagem de Projetos                | Exibir lista de projetos cadastrados.                                                    |
| **TH-04** | EP-08 | FE-16 | Filtro de Projetos                  | Permitir filtrar projetos por nome, disciplina, turma, status, etc.                      |
| **TH-05** | EP-09 | FE-17 | Criar e Editar Disciplinas          | Permitir criar e modificar disciplinas.                                                  |
| **TH-05** | EP-09 | FE-18 | Remover Disciplinas                 | Permitir excluir disciplinas quando necessário.                                          |
| **TH-05** | EP-10 | FE-19 | Listagem de Disciplinas             | Exibir lista de disciplinas cadastradas.                                                 |
| **TH-05** | EP-10 | FE-20 | Filtro de Disciplinas               | Permitir filtrar disciplinas por nome, período, professor, etc.                          |
| **TH-06** | EP-11 | FE-21 | Criar e Editar Turmas               | Permitir criar e modificar turmas.                                                       |
| **TH-06** | EP-11 | FE-22 | Remover Turmas                      | Permitir excluir turmas quando necessário.                                               |
| **TH-06** | EP-12 | FE-23 | Listagem de Turmas                  | Exibir lista de turmas cadastradas.                                                      |
| **TH-06** | EP-12 | FE-24 | Filtro de Turmas                    | Permitir filtrar turmas por nome, período, disciplina, etc.                              |
| **TH-07** | EP-13 | FE-25 | Criar Times                         | Permitir criação de times de alunos vinculados a projetos.                               |
| **TH-07** | EP-13 | FE-26 | Gerenciar Times                     | Permitir editar, excluir ou reorganizar os times.                                        |
| **TH-07** | EP-14 | FE-27 | Visualizar Meu Time                 | Permitir que alunos visualizem informações sobre seus próprios times.                    |
| **TH-07** | EP-14 | FE-28 | Acompanhar Status dos Times         | Permitir que professores e administradores monitorem o status e andamento dos times.     |
| **TH-08** | EP-15 | FE-29 | Criar Nova Entrega                  | Permitir que usuários realizem submissões de entregas parciais ou finais.                |
| **TH-08** | EP-15 | FE-30 | Acompanhar Entregas                 | Permitir visualizar o histórico de entregas realizadas pelos times.                      |
| **TH-08** | EP-16 | FE-31 | Validar Entregas                    | Permitir que professores avaliem e validem as entregas realizadas pelos times.           |
| **TH-08** | EP-16 | FE-32 | Feedback de Entregas                | Permitir que professores ou orientadores forneçam feedback sobre as entregas.            |
| **TH-09** | EP-17 | FE-33 | Upload de Entrega Parcial           | Permitir que alunos realizem upload de arquivos para submissões parciais.                |
| **TH-09** | EP-17 | FE-34 | Organização e Armazenamento Parcial | Organizar e armazenar as entregas parciais vinculadas aos projetos e times.              |
| **TH-09** | EP-17 | FE-35 | Visualizar e Recuperar Entregas     | Permitir que alunos e professores visualizem e recuperem arquivos das entregas parciais. |
| **TH-09** | EP-18 | FE-36 | Upload de Entrega Final             | Permitir que alunos realizem upload de arquivos para submissões finais do projeto.       |
| **TH-09** | EP-18 | FE-37 | Organização e Armazenamento Final   | Organizar e armazenar as entregas finais vinculadas aos projetos e times.                |
| **TH-09** | EP-18 | FE-38 | Visualizar e Recuperar Entregas     | Permitir que alunos e professores visualizem e recuperem arquivos das entregas finais.   |

### 6. User Stories

Cada feature possui no mínimo duas user stories, considerando a perspectiva dos diferentes papéis no sistema.

| TH-ID | EP-ID | FE-ID | US-ID | User Story                                                                                                  | Role           |
| :---- | :---- | :---- | :---- | ----------------------------------------------------------------------------------------------------------- | -------------- |
| TH-01 | EP-01 | FE-01 | US-01 | Como administrador, quero editar textos e imagens da landing page para manter as informações atualizadas.   | Administrador  |
| TH-01 | EP-01 | FE-01 | US-02 | Como administrador, quero gerenciar as seções da landing page para destacar informações importantes.        | Administrador  |
| TH-01 | EP-01 | FE-02 | US-03 | Como administrador, quero adicionar novos links para documentos importantes na landing page.                | Administrador  |
| TH-01 | EP-01 | FE-02 | US-04 | Como administrador, quero remover links obsoletos da landing page para manter o conteúdo relevante.         | Administrador  |
| TH-01 | EP-02 | FE-03 | US-05 | Como administrador, quero gerar relatórios de acesso à landing page para entender o volume de visitantes.   | Administrador  |
| TH-01 | EP-02 | FE-03 | US-06 | Como gestor, quero analisar quais documentos são mais acessados na página para melhorar sua organização.    | Administrador  |
| TH-01 | EP-02 | FE-04 | US-07 | Como administrador, quero monitorar quais seções da página recebem mais acessos para otimizar seu conteúdo. | Administrador  |
| TH-01 | EP-02 | FE-04 | US-08 | Como gestor, quero entender o comportamento dos visitantes na página para aprimorar a comunicação pública.  | Administrador  |
| TH-02 | EP-03 | FE-05 | US-09 | Como visitante, quero me cadastrar no sistema para submeter projetos ou participar de turmas.               | Visitante      |
| TH-02 | EP-03 | FE-05 | US-10 | Como administrador, quero cadastrar usuários manualmente quando necessário.                                 | Administrador  |
| TH-02 | EP-03 | FE-06 | US-11 | Como usuário, quero fazer login para acessar minhas funcionalidades no sistema.                             | Todos          |
| TH-02 | EP-03 | FE-06 | US-12 | Como administrador, quero acessar a área administrativa com login seguro.                                   | Administrador  |
| TH-02 | EP-04 | FE-07 | US-13 | Como usuário, quero escolher meu papel (Aluno, Professor, Agente Externo) no primeiro acesso.               | Todos          |
| TH-02 | EP-04 | FE-07 | US-14 | Como administrador, quero alterar o papel de um usuário quando necessário.                                  | Administrador  |
| TH-02 | EP-04 | FE-08 | US-15 | Como administrador, quero definir as permissões para cada papel no sistema.                                 | Administrador  |
| TH-02 | EP-04 | FE-08 | US-16 | Como professor, quero garantir que alunos tenham acesso restrito apenas às suas atividades e turmas.        | Professor      |
| TH-03 | EP-05 | FE-09 | US-17 | Como administrador, quero cadastrar novos professores e agentes externos no sistema.                        | Administrador  |
| TH-03 | EP-05 | FE-09 | US-18 | Como professor, quero cadastrar um agente externo para apoiar meus projetos.                                | Professor      |
| TH-03 | EP-05 | FE-10 | US-19 | Como administrador, quero editar dados de usuários que estejam incorretos.                                  | Administrador  |
| TH-03 | EP-05 | FE-10 | US-20 | Como administrador, quero excluir usuários inativos ou com registros incorretos.                            | Administrador  |
| TH-03 | EP-06 | FE-11 | US-21 | Como administrador, quero visualizar a lista completa de usuários cadastrados no sistema.                   | Administrador  |
| TH-03 | EP-06 | FE-11 | US-22 | Como professor, quero listar apenas os alunos vinculados às minhas turmas.                                  | Professor      |
| TH-03 | EP-06 | FE-12 | US-23 | Como administrador, quero aplicar filtros para encontrar usuários por nome, papel ou status.                | Administrador  |
| TH-03 | EP-06 | FE-12 | US-24 | Como professor, quero filtrar alunos nas minhas turmas por nome, matrícula ou status.                       | Professor      |
| TH-04 | EP-07 | FE-13 | US-25 | Como professor, quero criar novos projetos para minhas turmas.                                               | Professor      |
| TH-04 | EP-07 | FE-13 | US-26 | Como administrador, quero cadastrar projetos gerais no sistema.                                              | Administrador  |
| TH-04 | EP-07 | FE-14 | US-27 | Como professor, quero remover projetos que não serão mais executados.                                        | Professor      |
| TH-04 | EP-07 | FE-14 | US-28 | Como administrador, quero excluir projetos antigos ou obsoletos.                                             | Administrador  |
| TH-04 | EP-08 | FE-15 | US-29 | Como professor, quero visualizar todos os projetos que estou coordenando.                                    | Professor      |
| TH-04 | EP-08 | FE-15 | US-30 | Como aluno, quero visualizar os projetos em que estou participando.                                          | Aluno          |
| TH-04 | EP-08 | FE-16 | US-31 | Como professor, quero buscar projetos por nome ou disciplina.                                                | Professor      |
| TH-04 | EP-08 | FE-16 | US-32 | Como aluno, quero buscar projetos disponíveis usando filtros de nome e professor.                            | Aluno          |
| TH-05 | EP-09 | FE-17 | US-33 | Como professor, quero criar novas disciplinas para minhas turmas.                                            | Professor      |
| TH-05 | EP-09 | FE-17 | US-34 | Como administrador, quero cadastrar disciplinas gerais no sistema.                                           | Administrador  |
| TH-05 | EP-09 | FE-18 | US-35 | Como professor, quero remover disciplinas que não serão mais ofertadas.                                      | Professor      |
| TH-05 | EP-09 | FE-18 | US-36 | Como administrador, quero excluir disciplinas antigas ou obsoletas.                                          | Administrador  |
| TH-05 | EP-10 | FE-19 | US-37 | Como professor, quero visualizar todas as disciplinas que estou ministrando.                                 | Professor      |
| TH-05 | EP-10 | FE-19 | US-38 | Como aluno, quero visualizar as disciplinas em que estou matriculado.                                        | Aluno          |
| TH-05 | EP-10 | FE-20 | US-39 | Como professor, quero acompanhar o progresso dos alunos nas disciplinas e atividades.                        | Professor      |
| TH-05 | EP-10 | FE-20 | US-40 | Como aluno, quero acompanhar meu próprio progresso nas atividades, disciplinas e projetos.                   | Aluno          |
| TH-06 | EP-11 | FE-21 | US-41 | Como professor, quero criar novas turmas vinculadas às disciplinas.                                          | Professor      |
| TH-06 | EP-11 | FE-21 | US-42 | Como administrador, quero cadastrar turmas gerais no sistema.                                                | Administrador  |
| TH-06 | EP-11 | FE-22 | US-43 | Como professor, quero remover turmas que não serão mais realizadas.                                          | Professor      |
| TH-06 | EP-11 | FE-22 | US-44 | Como administrador, quero excluir turmas antigas ou inativas.                                                | Administrador  |
| TH-06 | EP-12 | FE-23 | US-45 | Como professor, quero listar todas as turmas sob minha responsabilidade.                                     | Professor      |
| TH-06 | EP-12 | FE-23 | US-46 | Como aluno, quero buscar turmas disponíveis usando filtros.                                                  | Aluno          |
| TH-06 | EP-12 | FE-24 | US-47 | Como professor, quero consultar rapidamente informações sobre as turmas que acompanho.                       | Professor      |
| TH-06 | EP-12 | FE-24 | US-48 | Como administrador, quero acompanhar a distribuição de alunos nas turmas.                                    | Administrador  |
| TH-07 | EP-13 | FE-25 | US-49 | Como professor, quero criar times de alunos para projetos.                                                   | Professor      |
| TH-07 | EP-13 | FE-25 | US-50 | Como administrador, quero criar times operacionais ou de apoio no sistema.                                  | Administrador  |
| TH-07 | EP-13 | FE-26 | US-51 | Como professor, quero editar, excluir ou reorganizar os membros dos times.                                  | Professor      |
| TH-07 | EP-13 | FE-26 | US-52 | Como administrador, quero remover times inativos do sistema.                                                | Administrador  |
| TH-07 | EP-14 | FE-27 | US-53 | Como aluno, quero acessar informações do meu time, membros e projetos.                                      | Aluno          |
| TH-07 | EP-14 | FE-27 | US-54 | Como professor, quero acompanhar o status dos times que estou coordenando.                                  | Professor      |
| TH-07 | EP-14 | FE-28 | US-55 | Como professor, quero gerar relatórios sobre o status dos times.                                            | Professor      |
| TH-07 | EP-14 | FE-28 | US-56 | Como administrador, quero visualizar o status geral dos times no sistema.                                   | Administrador  |
| TH-08 | EP-15 | FE-29 | US-57 | Como aluno, quero criar uma nova entrega parcial ou final do meu projeto.                                   | Aluno          |
| TH-08 | EP-15 | FE-29 | US-58 | Como aluno, quero editar uma entrega antes do prazo final.                                                  | Aluno          |
| TH-08 | EP-15 | FE-30 | US-59 | Como aluno, quero consultar o histórico de entregas do meu time.                                            | Aluno          |
| TH-08 | EP-15 | FE-30 | US-60 | Como professor, quero visualizar todas as entregas feitas pelos meus times.                                 | Professor      |
| TH-08 | EP-16 | FE-31 | US-61 | Como professor, quero validar e avaliar as entregas realizadas pelos alunos.                                | Professor      |
| TH-08 | EP-16 | FE-31 | US-62 | Como professor, quero solicitar ajustes nas entregas antes de finalizar a avaliação.                        | Professor      |
| TH-08 | EP-16 | FE-32 | US-63 | Como professor, quero fornecer feedback sobre as entregas para auxiliar no desenvolvimento dos alunos.      | Professor      |
| TH-08 | EP-16 | FE-32 | US-64 | Como aluno, quero visualizar os feedbacks recebidos sobre minhas entregas.                                  | Aluno          |
| TH-09 | EP-17 | FE-33 | US-65 | Como aluno, quero fazer upload de arquivos para submissões parciais do meu projeto.                         | Aluno          |
| TH-09 | EP-17 | FE-33 | US-66 | Como aluno, quero substituir arquivos de uma entrega parcial antes do prazo.                                | Aluno          |
| TH-09 | EP-17 | FE-34 | US-67 | Como aluno, quero visualizar e recuperar meus arquivos de entregas parciais.                                | Aluno          |
| TH-09 | EP-17 | FE-34 | US-68 | Como professor, quero acessar os arquivos das entregas parciais dos times que acompanho.                    | Professor      |
| TH-09 | EP-18 | FE-35 | US-69 | Como aluno, quero realizar upload da minha entrega final do projeto.                                        | Aluno          |
| TH-09 | EP-18 | FE-35 | US-70 | Como aluno, quero substituir arquivos da entrega final enquanto o prazo estiver aberto.                     | Aluno          |
| TH-09 | EP-18 | FE-36 | US-71 | Como aluno, quero acessar e visualizar os arquivos da minha entrega final.                                  | Aluno          |
| TH-09 | EP-18 | FE-36 | US-72 | Como professor, quero acessar os arquivos das entregas finais para realizar a avaliação.                    | Professor      |

## Histórico de Revisões

| Data       | Versão | Alterações                                            | Autores                                                                                         |
| ---------- | ------ | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 25/04/2025 | 0.1    | Criação do documento                                  | [Mateus Vieira](https://github.com/matix0) e [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 20/05/2025 | 0.2    | Atualização para USM                                  | [Mateus Vieira](https://github.com/matix0) e [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 21/05/2025 | 0.3    | Atividades de entregas                                | [Mateus Vieira](https://github.com/matix0) e [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 18/06/2025 | 0.4    | Atualização do mapeamento de funcionalidade e backlog | [Mateus Vieira](https://github.com/matix0) e [Lucas Antunes](https://github.com/LucasGSAntunes) |


[← Voltar para a Página Principal](../index.md)
