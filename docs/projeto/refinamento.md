# 📄 Documento de Refinamento Técnico – Formação de Times e Gestão de Entregas

## 🔗 Contexto

O sistema permite a gestão de formação de times acadêmicos vinculados a projetos, bem como o acompanhamento e a entrega de atividades parciais e finais dos alunos.

---

## 🎯 Funcionalidades do Módulo de Times

| Funcionalidade                     | Descrição Técnica                                                                 |
| ---------------------------------- | --------------------------------------------------------------------------------- |
| Levantamento de Preferências       | Tela que exibe o status dos formulários preenchidos pelos alunos.                 |
| Geração Automática de Times        | Algoritmo que aloca alunos nos projetos, baseado nas preferências coletadas.      |
| Edição Manual de Alocação          | Permite que professores alterem a alocação dos alunos entre os projetos (Trocar). |
| Confirmação de Times               | Confirma a formação dos times e bloqueia alterações posteriores.                  |
| Visualização do Meu Time (Aluno)   | Cada aluno visualiza seu time, membros, projeto e stakeholder.                    |
| Visualização dos Times (Professor) | O professor acessa todos os times, projetos, stakeholders e seus membros.         |
| Relatórios dos Times               | Geração de relatórios sobre status e composição dos times.                        |

---

## 🎯 Funcionalidades do Módulo de Entregas

| Funcionalidade                   | Descrição Técnica                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------- |
| Criar Nova Entrega               | Formulário para envio de entrega parcial ou final, com campos de título, descrição e categoria.     |
| Seleção de Tipo de Envio         | Upload de arquivo ou envio de link externo (ex.: site, drive, repositório).                         |
| Categorização                    | Permite selecionar a categoria da entrega (ex.: Apresentação, Relatório, Produto, Documentação).    |
| Relacionamento com Etapas        | Define se a entrega corresponde a uma etapa parcial específica ou à entrega final.                  |
| Visualização de Entregas         | Alunos e professores podem visualizar todas as entregas realizadas, organizadas por time e projeto. |
| Histórico e Controle de Entregas | Mantém histórico com datas, versões, tipos e arquivos entregues.                                    |
| Feedback e Avaliação             | Professores podem avaliar, solicitar ajustes e fornecer feedback sobre as entregas.                 |

---

## 🏗️ Arquitetura Funcional do Módulo

```plaintext
                        +-----------------------------+
                        |          Usuário            |
                        +-----------------------------+
                                   ↓
                 +-------------------------------------------+
                 |               Interface Web              |
                 | - Página de Preferências                 |
                 | - Formação de Times                      |
                 | - Meu Time                               |
                 | - Realizar Entrega                       |
                 | - Acompanhar Entregas                    |
                 +-------------------------------------------+
                                   ↓
                +--------------------------------------------------+
                |                 API Gateway                      |
                | - Gerenciamento de Autenticação                  |
                | - Gerenciamento de Permissões e Perfis           |
                +--------------------------------------------------+
                                   ↓
        +---------------------------------------------------------------+
        |                         Serviços Backend                      |
        |                                                               |
        | +----------------------+   +-------------------------------+ |
        | | Serviço de Times      |   | Serviço de Entregas           | |
        | | - Preferências        |   | - Upload                      | |
        | | - Geração de Times    |   | - Histórico de Entregas       | |
        | | - Edição e Troca      |   | - Avaliação e Feedback        | |
        | | - Relatórios          |   | - Visualização e Download     | |
        | +----------------------+   +-------------------------------+ |
        +---------------------------------------------------------------+
                                   ↓
                  +---------------------------------------------+
                  |              Banco de Dados                 |
                  | - Users                                     |
                  | - Times                                     |
                  | - Projetos                                  |
                  | - Entregas                                  |
                  | - Preferências                              |
                  +---------------------------------------------+
```

---

## 🗄️ Entidades Principais

| Entidade        | Atributos                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------ |
| **Time**        | id, projeto_id, membros[], status                                                                |
| **Projeto**     | id, título, stakeholder, categoria                                                               |
| **Entrega**     | id, time_id, tipo (parcial/final), categoria, título, descrição, link_ou_arquivo, data_envio     |
| **Usuário**     | id, nome, matrícula, papel (Aluno, Professor, Admin), email                                      |
| **Preferência** | id, usuario_id, respostas[], status (pendente/concluído)                                         |

---

## 🔐 Permissões

| Papel         | Ações Permitidas                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------ |
| **Aluno**     | Preencher preferências, visualizar time, realizar entregas, visualizar feedback                        |
| **Professor** | Gerenciar times, trocar membros, validar entregas, fornecer feedback, gerar relatórios de time/entrega |
| **Admin**     | Visualizar e editar qualquer informação para suporte e auditoria                                       |

---

## 🔄 Fluxo de Formação de Times

```plaintext
1. Professor inicia levantamento de preferências.
2. Alunos preenchem o formulário de preferência de projetos.
3. O sistema verifica o status:
   - Se todos preencheram → habilita "Formar Times".
   - Se não → permite "Formar Times" mesmo assim (com aviso).
4. Algoritmo gera os times baseado nas preferências.
5. Professor pode:
   - Aceitar.
   - Trocar membros manualmente.
6. Professor confirma a formação → Times ficam fixos.
7. Alunos acessam "Meu Time" para visualizar.
```

---

## 📦 Fluxo de Gestão de Entregas

```plaintext
1. Aluno seleciona se é entrega parcial ou final.
2. Preenche título, descrição, categoria e tipo (upload ou link).
3. Submete a entrega.
4. Entrega fica disponível para professores e para o próprio aluno.
5. Professor acessa, avalia e fornece feedback.
6. Aluno visualiza feedbacks nas entregas realizadas.
```

---

# 🔗 Diagrama de Sequência – Formação de Times

```plaintext
Ator Professor → Interface → Backend → Banco de Dados

1. Professor acessa a tela de levantamento de preferências.
2. Interface solicita status de preenchimento → Backend → Banco → Retorna status.
3. Professor clica em "Formar Times".
4. Backend executa algoritmo de formação baseado nas preferências → Consulta Banco.
5. Banco retorna dados dos alunos e preferências.
6. Backend grava os times gerados → Banco.
7. Backend retorna times para a Interface.
8. Interface exibe lista dos times formados.
9. Professor pode ajustar (trocar alunos) → Backend → Atualiza Banco.
10. Professor confirma formação dos times → Backend → Atualiza status para "Confirmado" no Banco.
```

---

# 🔗 Diagrama de Sequência – Gestão de Entregas

```plaintext
Ator Aluno/Professor → Interface → Backend → Banco de Dados

1. Aluno acessa "Realizar Entrega".
2. Preenche formulário (parcial ou final).
3. Envia dados e arquivos/link → Backend.
4. Backend valida e grava no Banco.
5. Entrega aparece na listagem do aluno e do professor.
6. Professor acessa a entrega → Consulta Backend → Banco → Retorna dados e arquivos.
7. Professor avalia:
   a. Aprovar.
   b. Solicitar ajustes.
   c. Enviar feedback.
8. Backend atualiza status, comentários e feedback → Banco.
9. Aluno visualiza feedback na interface → Consulta Banco via Backend.
```

---

# 🗺️ Diagrama Entidade-Relacionamento (ER)

![er_diagram_times_entregas](https://hackmd.io/_uploads/S10AcIgNxe.png)

| Entidade        | Relacionamento                                                    |
| --------------- | ----------------------------------------------------------------- |
| **Usuário**     | 1:N com **Preferência**, 1:N com **Entrega**, N:M com **Time**    |
| **Time**        | N:M com **Usuário**, N:1 com **Projeto**                          |
| **Projeto**     | 1:N com **Time**, 1:N com **Entrega**                             |
| **Preferência** | N:1 com **Usuário**, N:1 com **Projeto**                          |
| **Entrega**     | N:1 com **Time**, N:1 com **Projeto**, N:1 com **Usuário**        |

---

## 🗄️ Atributos principais por entidade

- **Usuário**: id, nome, matrícula, email, role
- **Projeto**: id, título, stakeholder, categoria
- **Time**: id, projeto_id, status, membros[]
- **Preferência**: id, usuario_id, projeto_id, respostas[], status
- **Entrega**: id, time_id, projeto_id, usuario_id, tipo (parcial/final), categoria, título, descrição, arquivo_ou_link, data_envio, status, feedback

---

# 🔄 Fluxo BPMN – Formação de Times + Entregas

```plaintext
[Início]
  ↓
[Coletar Preferências dos Alunos]
  ↓
[Formar Times Automaticamente]
  → [Trocar membros manualmente?] → Sim → [Reorganizar membros]
                                       ↓ Não
  ↓
[Confirmar Formação dos Times]
  ↓
[Início das Entregas]
  ↓
[Aluno Preenche Formulário de Entrega]
  ↓
[Submeter Entrega]
  ↓
[Professor Avalia e Dá Feedback]
  → [Solicitar Ajustes?] → Sim → [Aluno Refaz e Envia Novamente]
                              ↓ Não
  ↓
[Fim]
```
