# Construção do Backlog do Produto

[← Voltar para a Página Principal](../index.md)

# 📌 Backlog USM - Sistema Puma

## 🎯 Objetivo do Produto

Permitir que stakeholders conheçam o programa Puma, realizem login/cadastro, submetam projetos, organizem disciplinas, turmas e times, e acompanhem o andamento e alocação de projetos.

## ✅ Funcionalidades Mapeadas

### 1. Explorar o Puma (Landing Page Pré-login)

| Atividade                 | User Story                                          | Tarefa Técnica                                                              |
| ------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------- |
| Navegar pelas informações | ...usuário visitante, quero conhecer o que é o Puma | Implementar landing page com seções como “O que é”, “Edital”, “Metodologia” |
| Acessar o edital          | ...usuário visitante, quero acessar o edital        | Botão com link para edital                                                  |
| Ver benefícios            | ...candidato, quero entender os benefícios          | Sessão com lista de benefícios                                              |

### 2. Cadastro e Login

| Atividade                | User Story                                                                    | Tarefa Técnica                                                            |
| ------------------------ | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Realizar cadastro        | ...usuário novo, quero me cadastrar para acessar o sistema                    | Fluxo em 3 etapas com upload de foto (opcional), formulário e confirmação |
| Fazer login              | ...usuário, quero acessar minha conta                                         | Formulário com campos de email e senha                                    |
| Escolher tipo de usuário | ...novo usuário, quero escolher se sou estudante, professor ou agente externo | Dropdown de seleção de perfil                                             |

### 3. Submissão de Projetos

| Atividade              | User Story                                          | Tarefa Técnica                                |
| ---------------------- | --------------------------------------------------- | --------------------------------------------- |
| Submeter projeto       | ...stakeholder logado, quero cadastrar uma proposta | Formulário em 4 etapas com validações         |
| Escolher identificação | ...usuário, quero me identificar com CPF ou CNPJ    | Componente para seleção e entrada de CPF/CNPJ |
| Anexar documentos      | ...stakeholder, quero enviar arquivos de apoio      | Upload de documentos no final do formulário   |

### 4. Disciplinas

| Atividade                   | User Story                                                            | Tarefa Técnica                                                       |
| --------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Acessar disciplinas         | ...usuário professor, quero visualizar e gerenciar minhas disciplinas | Tela “Minhas Disciplinas” com listagem filtrada por professor logado |
| Gerenciar disciplinas       | ...professor, quero adicionar, modificar ou excluir disciplinas       | Interface com funcionalidades para gerenciamento de disciplinas      |
| Ver projetos por disciplina | ...professor, quero acessar os projetos vinculados                    | Página de detalhe da disciplina com listagem de projetos             |

### 5. Turma

| Atividade              | User Story                                            | Tarefa Técnica                                       |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------- |
| Acompanhar turmas      | ...professor, quero visualizar as turmas que coordeno | Tela com listagem de turmas vinculadas               |
| Gerenciar turmas       | ...professor, quero criar, editar ou excluir turmas   | Interface com opções de gerenciamento                |
| Ver projetos por turma | ...professor, quero visualizar os projetos alocados   | Página de detalhes da turma com listagem de projetos |

### 6. Projetos

| Atividade                             | User Story                                                            | Tarefa Técnica                                              |
| ------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------- |
| Acompanhar projetos                   | ...usuário, quero acompanhar o status dos projetos                    | Tela de listagem com status e filtros                       |
| Avaliar propostas de projeto          | ...professor, quero analisar propostas recebidas                      | Interface de avaliação com formulário de parecer            |
| Alocar/Realocar projeto em disciplina | ...professor, quero vincular projetos a disciplinas                   | Interface de seleção de disciplina e atribuição de projetos |
| Alocar/Realocar projeto em turma      | ...professor, quero vincular projetos a turmas                        | Interface com opção de vincular projeto a turma específica  |
| Levantar preferência dos alunos       | ...professor, quero coletar preferências dos alunos para formar times | Formulário de preferência e visualização agrupada           |

### 7. Times

| Atividade                         | User Story                                                        | Tarefa Técnica                                             |
| --------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| Formar times                      | ...professor ou admin, quero formar os times de discentes         | Interface de criação de times                              |
| Gerenciar times                   | ...professor ou admin, quero organizar os times                   | Interface de gerenciamento de times                        |
| Alocar/Realocar times por projeto | ...professor, quero vincular ou mover times entre projetos        | Interface para selecionar projeto e alocar/remanejar times |
| Meu time                          | ...aluno, quero consultar informações sobre o meu time de projeto | Interface de meu time para aluno                           |


### 8. Entregas

| Atividade                    | User Story                                                                                  | Tarefa Técnica                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Realizar nova entrega        | ... aluno, quero realizar uma nova entrega de atividade do time                             | Interface de nova entrega parcial ou final                    |
| Realizar upload de arquivos  | ... aluno, quero realizar upload de arquivos para compor uma nova entrega de atividade      | Campo de upload de arquivos na realização de uma nova entrega |
| Visualizar entregas do time  | ... professor ou aluno, quero consultar informações sobre entregas realizadas pelo meu time | Lista de entregas realizadas pelo time                        |
| Gerenciar entregas do time   | ... professor ou aluno, quero gerenciar informações sobre entregas realizadas pelo meu time | Detalhes de entregas realizadas e Editar entregas realizadas  |
| Acompanhar entregas da turma | ... professor, quero acompanhar as entregas da turma por time                               | Interface de entregas da turma por time                       |


## Histórico de Revisões

| Data       | Versão | Alterações             | Autores                                                                                         |
| ---------- | ------ | ---------------------- | ----------------------------------------------------------------------------------------------- |
| 25/04/2025 | 0.1    | Criação do documento   | [Mateus Vieira](https://github.com/matix0) e [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 20/05/2025 | 0.2    | Atualização para USM   | [Mateus Vieira](https://github.com/matix0) e [Lucas Antunes](https://github.com/LucasGSAntunes) |
| 21/05/2025 | 0.3    | Atividades de entregas | [Mateus Vieira](https://github.com/matix0) e [Lucas Antunes](https://github.com/LucasGSAntunes) |

[← Voltar para a Página Principal](../index.md)
