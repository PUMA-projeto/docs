# :material-api: ProjectService API

!!! info "Visão Geral"
A **ProjectService API** é o serviço central para gerenciamento de projetos acadêmicos, turmas, disciplinas e avaliações por pares no sistema PUMA. Esta API oferece endpoints completos para criação, edição, exclusão e consulta de recursos relacionados ao ambiente educacional.

## :material-chart-timeline: Sumário de Endpoints

| Grupo                                           | Endpoints    | Descrição                                  |
| ----------------------------------------------- | ------------ | ------------------------------------------ |
| [🎯 Avaliação por Pares](#avaliacao-por-pares)  | 2 endpoints  | Solicitações e gerenciamento de avaliações |
| [🧠 Competências](#competencias)                | 3 endpoints  | Macro e microcompetências do sistema       |
| [📂 Categorias](#categorias)                    | 4 endpoints  | Gerenciamento de categorias de projetos    |
| [🎓 Turmas](#turmas)                            | 5 endpoints  | Criação e administração de turmas          |
| [🔑 Palavras-chave](#palavras-chave)            | 8 endpoints  | Sistema de tags e palavras-chave           |
| [📚 Áreas de Conhecimento](#areas-conhecimento) | 2 endpoints  | Subáreas e áreas de conhecimento           |
| [👨‍🏫 Professores](#professores)                  | 1 endpoint   | Listagem de professores                    |
| [📋 Projetos](#projetos)                        | 12 endpoints | CRUD completo de projetos                  |
| [📖 Disciplinas](#disciplinas)                  | 6 endpoints  | Gerenciamento de disciplinas               |
| [👥 Usuários](#usuarios)                        | 2 endpoints  | Dados de usuários e estudantes             |
| [🔗 Associações](#associacoes)                  | 4 endpoints  | Vínculos entre projetos e turmas           |

---

## 🎯 Avaliação por Pares {#avaliacao-por-pares}

### :material-plus-circle: Criar Solicitação de Avaliação

!!! abstract "Visão Geral"
Cria uma nova solicitação de avaliação por pares para turmas específicas com microcompetências definidas.

=== "Requisição"

    **`POST`** `/solicitation/create`

    **Tags:** `Avaliação por pares`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `name` | `string` | ❌ | Nome da solicitação | `"Avaliação Final - Semestre 2024.1"` |
    | `classIds` | `array` | ❌ | IDs das turmas participantes | `["uuid1", "uuid2"]` |
    | `startDate` | `string` | ❌ | Data de início (ISO 8601) | `"2024-03-15T08:00:00Z"` |
    | `endDate` | `string` | ❌ | Data de término (ISO 8601) | `"2024-03-25T23:59:59Z"` |
    | `microCompetenceIds` | `array` | ❌ | IDs das microcompetências | `[1, 2, 3]` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "name": "Avaliação Final - Semestre 2024.1",
          "classIds": ["550e8400-e29b-41d4-a716-446655440000"],
          "startDate": "2024-03-15T08:00:00Z",
          "endDate": "2024-03-25T23:59:59Z",
          "microCompetenceIds": [1, 2, 3]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Solicitação criada com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos na requisição |
    | <span style="color: red">**401**</span> | 🔒 Não autorizado | Token de acesso inválido |

    !!! success "Resposta de Sucesso (200)"
        ```json
        {
          "id": 1,
          "name": "Avaliação Final - Semestre 2024.1",
          "status": "active",
          "createdAt": "2024-03-01T10:00:00Z"
        }
        ```

---

### :material-format-list-bulleted: Listar Solicitações

!!! abstract "Visão Geral"
Retorna uma lista filtrada de solicitações de avaliação por pares existentes no sistema.

=== "Requisição"

    **`GET`** `/solicitations`

    **Tags:** `Avaliação por pares`

    #### 🔍 Parâmetros de Query

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `creatorId` | `integer` | ❌ | ID do criador da solicitação | `123` |
    | `classId` | `uuid` | ❌ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |
    | `competence` | `string` | ❌ | Nome da competência | `"Trabalho em Equipe"` |
    | `class` | `string` | ❌ | Nome da turma | `"Engenharia de Software - 2024.1"` |
    | `creator` | `string` | ❌ | Nome do criador | `"Prof. João Silva"` |

    !!! example "Exemplo de Requisição"
        ```
        GET /solicitations?creatorId=123&classId=550e8400-e29b-41d4-a716-446655440000
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de solicitações retornada |
    | <span style="color: red">**400**</span> | ❌ Erro | Parâmetros de busca inválidos |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Avaliação Final - Semestre 2024.1",
            "creatorId": 123,
            "creatorName": "Prof. João Silva",
            "classIds": ["550e8400-e29b-41d4-a716-446655440000"],
            "startDate": "2024-03-15T08:00:00Z",
            "endDate": "2024-03-25T23:59:59Z",
            "status": "active"
          }
        ]
        ```

---

## 🧠 Competências {#competencias}

### :material-delete: Excluir Macrocompetência

!!! abstract "Visão Geral"
Remove uma macrocompetência específica do sistema usando seu identificador único.

=== "Requisição"

    **`DELETE`** `/competence/macro/{macroComptenceId}`

    **Tags:** `Competences`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `macroComptenceId` | `integer` | ✅ | ID da macrocompetência a ser excluída | `15` |

    !!! warning "Atenção"
        Esta operação é irreversível. Certifique-se de que a macrocompetência não está sendo utilizada em outras partes do sistema.

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Macrocompetência excluída com sucesso |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Macrocompetência não existe |
    | <span style="color: red">**409**</span> | ⚠️ Conflito | Macrocompetência em uso, não pode ser excluída |

---

### :material-eye: Listar Competências por Criador

!!! abstract "Visão Geral"
Retorna todas as competências cadastradas no sistema, opcionalmente filtradas pelo ID do criador.

=== "Requisição"

    **`GET`** `/competences/{creatorId}`

    **Tags:** `Competences`

    #### 🔍 Parâmetros de Query

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `creatorId` | `integer` | ❌ | ID do usuário criador das competências | `456` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de competências retornada |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Criador não encontrado |

    !!! success "Resposta de Sucesso (200)"
        ```json
        {
          "macroCompetences": [
            {
              "id": 1,
              "name": "Comunicação",
              "description": "Habilidades de comunicação oral e escrita",
              "creatorId": 456,
              "microCompetences": [
                {
                  "id": 101,
                  "name": "Apresentação Oral",
                  "description": "Capacidade de apresentar ideias de forma clara"
                },
                {
                  "id": 102,
                  "name": "Redação Técnica",
                  "description": "Habilidade de escrever documentos técnicos"
                }
              ]
            }
          ]
        }
        ```

---

### :material-plus: Cadastrar Competências

!!! abstract "Visão Geral"
Cadastra uma lista de macrocompetências e suas respectivas microcompetências no sistema.

=== "Requisição"

    **`POST`** `/competences`

    **Tags:** `Competences`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição |
    |-------|------|:-----------:|-----------|
    | `macros` | `array` | ✅ | Lista de macrocompetências |
    | `macros[].name` | `string` | ✅ | Nome da macrocompetência |
    | `macros[].description` | `string` | ✅ | Descrição da macrocompetência |
    | `macros[].micros` | `array` | ✅ | Lista de microcompetências |
    | `macros[].micros[].name` | `string` | ✅ | Nome da microcompetência |
    | `macros[].micros[].description` | `string` | ✅ | Descrição da microcompetência |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "macros": [
            {
              "name": "Trabalho em Equipe",
              "description": "Capacidade de trabalhar colaborativamente",
              "micros": [
                {
                  "name": "Colaboração",
                  "description": "Habilidade de colaborar efetivamente"
                },
                {
                  "name": "Liderança",
                  "description": "Capacidade de liderar grupos"
                }
              ]
            },
            {
              "name": "Pensamento Crítico",
              "description": "Habilidade de análise e solução de problemas",
              "micros": [
                {
                  "name": "Análise de Problemas",
                  "description": "Capacidade de identificar e analisar problemas"
                },
                {
                  "name": "Tomada de Decisões",
                  "description": "Habilidade de tomar decisões fundamentadas"
                }
              ]
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**201**</span> | ✅ Criado | Competências cadastradas com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos na requisição |
    | <span style="color: red">**409**</span> | ⚠️ Conflito | Competência já existe |

---

## 📂 Categorias {#categorias}

### :material-format-list-bulleted: Listar Categorias

!!! abstract "Visão Geral"
Retorna todas as categorias de projetos cadastradas no sistema.

=== "Requisição"

    **`GET`** `/categoria`

    **Tags:** `Categorias`

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de categorias retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Empresa Pública",
            "projectCount": 15
          },
          {
            "id": 2,
            "name": "Startup",
            "projectCount": 8
          }
        ]
        ```

---

### :material-plus-circle: Criar Nova Categoria

!!! abstract "Visão Geral"
Cria uma nova categoria para classificação de projetos no sistema.

=== "Requisição"

    **`POST`** `/categoria`

    **Tags:** `Categorias`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `categoria` | `string` | ✅ | Nome da categoria | `"Empresa Pública"` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "categoria": "Empresa Pública"
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**201**</span> | ✅ Criado | Categoria criada com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos |
    | <span style="color: red">**409**</span> | ⚠️ Conflito | Categoria já existe |

---

### :material-delete: Excluir Categoria

!!! abstract "Visão Geral"
Remove uma categoria existente do sistema.

=== "Requisição"

    **`DELETE`** `/categoria/{categoriaId}`

    **Tags:** `Categorias`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `categoriaId` | `integer` | ✅ | ID da categoria a ser excluída | `1` |

    !!! warning "Atenção"
        Certifique-se de que a categoria não está sendo utilizada em projetos ativos.

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Categoria excluída com sucesso |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Categoria não existe |
    | <span style="color: red">**409**</span> | ⚠️ Conflito | Categoria em uso, não pode ser excluída |

---

### :material-link-variant: Adicionar Categoria ao Projeto

!!! abstract "Visão Geral"
Associa uma categoria existente a um projeto específico.

=== "Requisição"

    **`POST`** `/categoria/{projectId}`

    **Tags:** `Categorias`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `projectId` | `integer` | ✅ | ID do projeto | `2` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `categoriaId` | `integer` | ✅ | ID da categoria | `1` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Categoria associada ao projeto |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Projeto ou categoria não existe |

---

## 🎓 Turmas {#turmas}

### :material-plus-circle: Criar Turma

!!! abstract "Visão Geral"
Cria uma nova turma para uma disciplina específica, definindo horários, professores e monitores.

=== "Requisição"

    **`POST`** `/class`

    **Tags:** `Class`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `subjectId` | `string` | ✅ | ID da disciplina | `"1"` |
    | `semester` | `string` | ✅ | Semestre da turma | `"1"` |
    | `year` | `string` | ✅ | Ano da turma | `"2024"` |
    | `periods` | `array` | ✅ | Períodos de aula | Ver detalhes abaixo |
    | `teachers` | `array` | ❌ | IDs dos professores | `[101, 102]` |
    | `monitors` | `array` | ❌ | IDs dos monitores | `[201, 202]` |

    #### 📅 Estrutura de Períodos (`periods`)

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `day` | `string` | ✅ | Dia da semana | `"segunda"` |
    | `timeStart` | `string` | ✅ | Horário de início (HH:MM) | `"08:00"` |
    | `timeFinish` | `string` | ✅ | Horário de término (HH:MM) | `"10:00"` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "subjectId": "1",
          "semester": "1",
          "year": "2024",
          "periods": [
            {
              "day": "segunda",
              "timeStart": "08:00",
              "timeFinish": "10:00"
            },
            {
              "day": "quarta",
              "timeStart": "08:00",
              "timeFinish": "10:00"
            }
          ],
          "teachers": [101, 102],
          "monitors": [201]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**201**</span> | ✅ Criado | Turma criada com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos na requisição |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Disciplina não encontrada |

---

### :material-format-list-bulleted: Listar Turmas

!!! abstract "Visão Geral"
Retorna uma lista de todas as turmas cadastradas no sistema.

=== "Requisição"

    **`GET`** `/class`

    **Tags:** `Class`

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de turmas retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "subjectId": 1,
            "subjectName": "Engenharia de Software",
            "semester": "1",
            "year": "2024",
            "classNumber": 1,
            "active": true,
            "studentCount": 35,
            "periods": [
              {
                "day": "segunda",
                "timeStart": "08:00",
                "timeFinish": "10:00"
              }
            ]
          }
        ]
        ```

---

### :material-eye-plus: Listar Turmas com Detalhes

!!! abstract "Visão Geral"
Lista todas as turmas com informações detalhadas, filtradas por tipo de usuário.

=== "Requisição"

    **`GET`** `/class-extra-attributes`

    **Tags:** `Class`

    #### 🔍 Parâmetros de Query

    | Parâmetro | Tipo | Obrigatório | Descrição | Valores Aceitos |
    |-----------|------|:-----------:|-----------|-----------------|
    | `userType` | `string` | ✅ | Tipo de usuário | `Professor`, `Aluno` |

    !!! example "Exemplo de Requisição"
        ```
        GET /class-extra-attributes?userType=Professor
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista detalhada de turmas retornada |
    | <span style="color: red">**400**</span> | ❌ Erro | Tipo de usuário inválido |

---

### :material-account-school: Minhas Turmas (Professor)

!!! abstract "Visão Geral"
Lista as turmas nas quais um professor específico está lecionando, com informações detalhadas.

=== "Requisição"

    **`GET`** `/my-classes-extra-attributes/{userId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do professor | `2` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Turmas do professor retornadas |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Professor não encontrado |

---

### :material-account-student: Minhas Turmas (Estudante)

!!! abstract "Visão Geral"
Lista as turmas nas quais um estudante específico está matriculado.

=== "Requisição"

    **`GET`** `/class/{userId}/student`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do estudante | `2` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Turmas do estudante retornadas |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Estudante não encontrado |

---

### :material-folder-open: Listar Projetos de uma Turma

!!! abstract "Visão Geral"
Retorna todos os projetos associados a uma turma específica.

=== "Requisição"

    **`GET`** `/{classId}/projetos`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `string` | ✅ | ID da turma | `"12345"` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de projetos retornada |
    | <span style="color: red">**400**</span> | ❌ Erro | Requisição inválida |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |
    | <span style="color: red">**500**</span> | ⚠️ Erro interno | Erro interno do servidor |

---

### :material-account-plus: Turmas Disponíveis para Ingresso

!!! abstract "Visão Geral"
Lista todas as turmas nas quais um estudante pode se inscrever, excluindo disciplinas onde já possui matrícula ativa.

=== "Requisição"

    **`GET`** `/joinable-classes`

    **Tags:** `Class`

    #### 🔍 Parâmetros de Query

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `string` | ✅ | ID do usuário | `"123"` |
    | `limit` | `integer` | ✅ | Limite de resultados | `10` |
    | `offset` | `integer` | ✅ | Offset para paginação | `0` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de turmas disponíveis |
    | <span style="color: red">**400**</span> | ❌ Erro | Parâmetros inválidos |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "classId": 1,
            "subjectId": 1,
            "subjectName": "Engenharia de Software",
            "teachers": ["Prof. João Silva", "Prof. Maria Santos"],
            "classNumber": 1,
            "studentJoinMethod": "codigo",
            "accessCode": "ABCD1234",
            "semester": "1",
            "year": 2024,
            "active": true,
            "periods": [
              {
                "day": "segunda",
                "timeStart": "08:00",
                "timeFinish": "09:30"
              }
            ]
          }
        ]
        ```

---

### :material-account-group: Listar Alunos de uma Turma

!!! abstract "Visão Geral"
Retorna todos os estudantes matriculados em uma turma específica.

=== "Requisição"

    **`GET`** `/class/{classId}/students`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de estudantes retornada |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |

---

### :material-key: Ingressar via Código de Acesso

!!! abstract "Visão Geral"
Permite que um estudante ingresse em uma turma utilizando o código de acesso fornecido pelo professor.

=== "Requisição"

    **`POST`** `/class/join`

    **Tags:** `Class`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do estudante | `123` |
    | `accessCode` | `string` | ✅ | Código de acesso da turma | `"ABCD1234"` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "userId": 123,
          "accessCode": "ABCD1234"
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Estudante adicionado à turma |
    | <span style="color: red">**400**</span> | ❌ Erro | Código inválido ou estudante já matriculado |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma ou estudante não encontrado |

---

### :material-account-plus-outline: Adicionar Estudante Manualmente

!!! abstract "Visão Geral"
Adiciona um estudante a uma turma de forma manual, sem necessidade de código de acesso.

=== "Requisição"

    **`POST`** `/class/{classId}/student`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do estudante | `123` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Estudante adicionado à turma |
    | <span style="color: red">**400**</span> | ❌ Erro | Estudante já matriculado |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma ou estudante não encontrado |

---

### :material-information: Exibir Detalhes da Turma

!!! abstract "Visão Geral"
Retorna informações detalhadas de uma turma específica.

=== "Requisição"

    **`GET`** `/class/{classId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Detalhes da turma retornados |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |

---

### :material-pencil: Editar Turma

!!! abstract "Visão Geral"
Edita as informações de uma turma existente.

=== "Requisição"

    **`PUT`** `/class/{classId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    !!! info "Campos Editáveis"
        Envie apenas os campos que deseja alterar. Campos não informados manterão seus valores atuais.

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Turma atualizada com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |

---

### :material-delete: Excluir Turma

!!! abstract "Visão Geral"
Remove uma turma do sistema permanentemente.

=== "Requisição"

    **`DELETE`** `/class/{classId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `integer` | ✅ | ID da turma | `1` |

    !!! danger "Atenção"
        Esta operação é irreversível e removerá todos os dados relacionados à turma.

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Turma excluída com sucesso |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |
    | <span style="color: red">**409**</span> | ⚠️ Conflito | Turma possui vínculos ativos |

---

### :material-key-change: Alterar Código de Acesso

!!! abstract "Visão Geral"
Atualiza o código de acesso de uma turma para permitir novos ingressos de estudantes.

=== "Requisição"

    **`PATCH`** `/class/{classId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `accessCode` | `string` | ❌ | Novo código de acesso | `"XYZ789"` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Código atualizado com sucesso |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |

---

### :material-account-minus: Remover Estudante da Turma

!!! abstract "Visão Geral"
Remove um estudante específico de uma turma.

=== "Requisição"

    **`DELETE`** `/class/{classId}/student`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do estudante | `123` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Estudante removido da turma |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma ou estudante não encontrado |

---

### :material-account-group: Listar Alunos de uma Turma

!!! abstract "Visão Geral"
Lista todos os estudantes matriculados em uma turma específica com suas informações básicas.

=== "Requisição"

    **`GET`** `/class/{classId}/students`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de estudantes retornada |
    | <span style="color: red">**400**</span> | ❌ Erro | Requisição inválida |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "fullName": "Alice Smith",
            "userId": 1,
            "userProfileImage": "https://picsum.photos/200",
            "Student": {
              "regNumber": "190115564"
            }
          },
          {
            "fullName": "João Silva",
            "userId": 2,
            "userProfileImage": "https://picsum.photos/201",
            "Student": {
              "regNumber": "190115565"
            }
          }
        ]
        ```

---

### :material-key: Ingressar via Código de Acesso

!!! abstract "Visão Geral"
Permite que um estudante ingresse em uma turma utilizando o código de acesso fornecido pelo professor.

=== "Requisição"

    **`POST`** `/class/{classId}/join`

    **Tags:** `Class - Ingresso na Turma`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `string` | ✅ | ID da turma | `"ABC123"` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `userId` | `string` | ✅ | ID do estudante | `"abc123"` |
    | `accessCode` | `string` | ✅ | Código de acesso da turma | `"12345"` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "userId": "abc123",
          "accessCode": "12345"
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Estudante adicionado à turma |
    | <span style="color: red">**400**</span> | ❌ Erro | Requisição inválida |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma ou usuário não encontrado |
    | <span style="color: red">**500**</span> | ⚠️ Erro interno | Erro interno do servidor |

---

### :material-account-plus-outline: Adicionar Estudante Manualmente

!!! abstract "Visão Geral"
Adiciona um estudante a uma turma de forma manual, sem necessidade de código de acesso.

=== "Requisição"

    **`POST`** `/class/{classId}/join/manual`

    **Tags:** `Class - Ingresso na Turma`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `integer` | ✅ | ID da turma | `2` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `userId` | `string` | ✅ | ID do estudante | `"1"` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "userId": "1"
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**201**</span> | ✅ Criado | Estudante adicionado à turma |
    | <span style="color: red">**400**</span> | ❌ Erro | Estudante já matriculado |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma ou estudante não encontrado |

---

### :material-information: Exibir Detalhes da Turma

!!! abstract "Visão Geral"
Retorna informações detalhadas de uma turma específica, incluindo dados contextuais do usuário.

=== "Requisição"

    **`GET`** `/class/{classId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `integer` | ✅ | ID da turma | `4` |

    #### 🔍 Parâmetros de Query

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do usuário logado | `2` |

    !!! example "Exemplo de Requisição"
        ```
        GET /class/4?userId=2
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Detalhes da turma retornados |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |

---

### :material-pencil: Editar Turma

!!! abstract "Visão Geral"
Edita as informações de uma turma existente, incluindo métodos de ingresso, horários e professores.

=== "Requisição"

    **`PUT`** `/class/{classId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `string` | ✅ | ID da turma | `"ABC123"` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `studentJoinMethod` | `string` | ❌ | Método de inserção de alunos | `"codigo"` |
    | `accessCode` | `string` | ❌ | Código de acesso (se método for código) | `"12345"` |
    | `semester` | `string` | ❌ | Semestre da turma | `"1"` |
    | `year` | `string` | ❌ | Ano da turma | `"2024"` |
    | `periods` | `array` | ❌ | Períodos de aula | Ver estrutura abaixo |
    | `teachers` | `array` | ❌ | IDs dos professores | `[101, 102]` |
    | `monitors` | `array` | ❌ | IDs dos monitores | `[201, 202]` |

    #### 📅 Estrutura de Períodos (`periods`)

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `day` | `string` | ✅ | Dia da semana | `"segunda"` |
    | `timeStart` | `string` | ✅ | Horário de início | `"08:00"` |
    | `timeFinish` | `string` | ✅ | Horário de término | `"10:00"` |

    !!! info "Campos Editáveis"
        Envie apenas os campos que deseja alterar. Campos não informados manterão seus valores atuais.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "studentJoinMethod": "codigo",
          "accessCode": "12345",
          "semester": "1",
          "year": "2024",
          "periods": [
            {
              "day": "segunda",
              "timeStart": "08:00",
              "timeFinish": "10:00"
            }
          ],
          "teachers": [101, 102],
          "monitors": [201]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Turma atualizada com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Requisição inválida |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |
    | <span style="color: red">**500**</span> | ⚠️ Erro interno | Erro interno do servidor |

---

### :material-delete: Excluir Turma

!!! abstract "Visão Geral"
Remove uma turma do sistema permanentemente.

=== "Requisição"

    **`DELETE`** `/class/{classId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `integer` | ✅ | ID da turma | `1` |

    !!! danger "Atenção"
        Esta operação é irreversível e removerá todos os dados relacionados à turma.

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Turma excluída com sucesso |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |
    | <span style="color: red">**409**</span> | ⚠️ Conflito | Turma possui vínculos ativos |

---

### :material-key-change: Alterar Código de Acesso

!!! abstract "Visão Geral"
Atualiza o código de acesso de uma turma para permitir novos ingressos de estudantes.

=== "Requisição"

    **`PATCH`** `/class/{classId}`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `accessCode` | `string` | ❌ | Novo código de acesso | `"ABC123"` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "accessCode": "ABC123"
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Código atualizado com sucesso |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma não encontrada |

---

### :material-account-minus: Remover Estudante da Turma

!!! abstract "Visão Geral"
Remove um estudante específico de uma turma.

=== "Requisição"

    **`DELETE`** `/class/{classId}/student`

    **Tags:** `Class`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `classId` | `uuid` | ✅ | ID da turma | `"550e8400-e29b-41d4-a716-446655440000"` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do estudante | `1` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "userId": 1
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Estudante removido da turma |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Turma ou estudante não encontrado |

---

## 🔑 Palavras-chave {#palavras-chave}

### :material-format-list-bulleted: Listar Palavras-chave

!!! abstract "Visão Geral"
Retorna todas as palavras-chave cadastradas no sistema, com opção de filtro por nome.

=== "Requisição"

    **`GET`** `/keyword`

    **Tags:** `Keywords`

    #### 🔍 Parâmetros de Query

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `keyword` | `string` | ❌ | Nome da palavra-chave para filtro | `"pjbl"` |

    !!! example "Exemplo de Requisição"
        ```
        GET /keyword?keyword=pjbl
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de palavras-chave retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "keyword": "pjbl",
            "psp": "PSP1",
            "createdAt": "2024-01-15T10:00:00Z"
          },
          {
            "id": 2,
            "keyword": "agile",
            "psp": "PSP2",
            "createdAt": "2024-01-16T14:30:00Z"
          }
        ]
        ```

---

### :material-plus-circle: Criar Palavra-chave

!!! abstract "Visão Geral"
Cadastra uma nova palavra-chave para utilização em projetos.

=== "Requisição"

    **`POST`** `/keyword`

    **Tags:** `Keywords`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `keyword` | `string` | ✅ | Nome da palavra-chave | `"pjbl"` |
    | `psp` | `string` | ❌ | Processo de Software Pessoal | `"PSP1"` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "keyword": "pjbl",
          "psp": "PSP1"
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**201**</span> | ✅ Criado | Palavra-chave criada com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos |
    | <span style="color: red">**409**</span> | ⚠️ Conflito | Palavra-chave já existe |

---

### :material-text-search: Palavras-chave em Abstract

!!! abstract "Visão Geral"
Lista palavras-chave que estão relacionadas a projetos (presentes em abstracts).

=== "Requisição"

    **`GET`** `/keyword/abstract`

    **Tags:** `Keywords`

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Palavras-chave relacionadas retornadas |

---

### :material-tag-outline: Palavras-chave Disponíveis

!!! abstract "Visão Geral"
Lista palavras-chave que não estão associadas a nenhuma disciplina específica.

=== "Requisição"

    **`GET`** `/keyword/available`

    **Tags:** `Keywords`

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Palavras-chave disponíveis retornadas |

---

### :material-pencil: Editar Palavra-chave

!!! abstract "Visão Geral"
Modifica o valor de uma palavra-chave já cadastrada.

=== "Requisição"

    **`PUT`** `/keyword/available`

    **Tags:** `Keywords`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `keywordid` | `integer` | ✅ | ID da palavra-chave | `1` |
    | `newKeyword` | `string` | ✅ | Novo valor da palavra-chave | `"newKeyword"` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "keywordid": 1,
          "newKeyword": "newKeyword"
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Palavra-chave atualizada |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Palavra-chave não existe |

---

### :material-link: Associar Disciplina à Palavra-chave

!!! abstract "Visão Geral"
Cria uma associação entre uma palavra-chave e uma disciplina.

=== "Requisição"

    **`POST`** `/keyword/subject`

    **Tags:** `Keywords`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `keywordid` | `integer` | ✅ | ID da palavra-chave | `1` |
    | `subjectid` | `integer` | ✅ | ID da disciplina | `2` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "keywordid": 1,
          "subjectid": 2
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Associação criada com sucesso |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Palavra-chave ou disciplina não existe |

---

### :material-link-variant: Editar Associação Palavra-chave/Disciplina

!!! abstract "Visão Geral"
Modifica a associação existente entre uma palavra-chave e uma disciplina.

=== "Requisição"

    **`PUT`** `/keyword/subject`

    **Tags:** `Keywords`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `keywordid` | `integer` | ✅ | ID da palavra-chave | `1` |
    | `subjectid` | `integer` | ✅ | ID da nova disciplina | `2` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Associação atualizada |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Palavra-chave ou disciplina não existe |

---

### :material-eye: Exibir Disciplina por Palavra-chave

!!! abstract "Visão Geral"
Retorna a disciplina associada a uma palavra-chave específica.

=== "Requisição"

    **`GET`** `/keyword/subject/{keywordId}`

    **Tags:** `Keywords`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `keywordId` | `integer` | ✅ | ID da palavra-chave | `1` |

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Disciplina relacionada retornada |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Palavra-chave não possui disciplina associada |

---

### :material-delete: Excluir Palavra-chave

!!! abstract "Visão Geral"
Remove uma palavra-chave do sistema permanentemente.

=== "Requisição"

    **`DELETE`** `/keyword/{keywordId}`

    **Tags:** `Keywords`

    #### 🎯 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `keywordId` | `integer` | ✅ | ID da palavra-chave | `1` |

    !!! warning "Atenção"
        Esta operação remove permanentemente a palavra-chave e todas suas associações.

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Palavra-chave excluída |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Palavra-chave não existe |
    | <span style="color: red">**409**</span> | ⚠️ Conflito | Palavra-chave em uso, não pode ser excluída |

---

## 📚 Áreas de Conhecimento {#areas-conhecimento}

### :material-format-list-bulleted: Listar Subáreas

!!! abstract "Visão Geral"
Retorna todas as subáreas de conhecimento cadastradas na plataforma.

=== "Requisição"

    **`GET`** `/knowledgeareas`

    **Tags:** `Areas`

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de subáreas retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Engenharia de Software",
            "description": "Área focada no desenvolvimento sistemático de software"
          },
          {
            "id": 2,
            "name": "Inteligência Artificial",
            "description": "Área de sistemas inteligentes e aprendizado de máquina"
          }
        ]
        ```

---

### :material-image: Obter Imagem de Disciplina

!!! abstract "Visão Geral"
Retorna uma imagem específica do diretório de imagens de disciplinas.

=== "Requisição"

    **`GET`** `/getImage`

    **Tags:** `Subject`

    #### 🔍 Parâmetros de Query

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `filename` | `string` | ✅ | Nome do arquivo de imagem | `"engenharia-software.jpg"` |

    !!! info "Localização"
        Busca imagens no diretório `/images/subject`

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Imagem retornada |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Imagem não existe |

---

## 👨‍🏫 Professores {#professores}

### :material-format-list-bulleted: Listar Professores

!!! abstract "Visão Geral"
Retorna todos os professores cadastrados na plataforma.

=== "Requisição"

    **`GET`** `/professors`

    **Tags:** `Professors`

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de professores retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Prof. João Silva",
            "email": "joao.silva@university.edu",
            "department": "Engenharia de Software",
            "registration": "123456789",
            "active": true
          },
          {
            "id": 2,
            "name": "Prof. Maria Santos",
            "email": "maria.santos@university.edu",
            "department": "Inteligência Artificial",
            "registration": "987654321",
            "active": true
          }
        ]
        ```

---

## 📋 Projetos {#projetos}

### :material-format-list-bulleted: Listar Projetos

!!! abstract "Visão Geral"
Retorna uma lista de projetos cadastrados com opções de filtro avançadas para facilitar a busca.

=== "Requisição"

    **`GET`** `/project`

    **Tags:** `Projects`

    #### 🔍 Parâmetros de Query

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `name` | `string` | ❌ | Nome do projeto | `"Sistema Web"` |
    | `userId` | `integer` | ❌ | ID do usuário criador | `123` |
    | `subjectId` | `integer` | ❌ | ID da disciplina | `5` |
    | `semesterId` | `integer` | ❌ | ID do semestre | `1` |
    | `status` | `string` | ❌ | Status do projeto | `"ativo"` |

    !!! tip "Filtros Combinados"
        Você pode combinar múltiplos parâmetros para refinar sua busca e obter resultados mais precisos.

    !!! example "Exemplo de Requisição"
        ```
        GET /project?name=Sistema&status=ativo&subjectId=5
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de projetos retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Sistema de Gestão Acadêmica",
            "userId": 123,
            "userName": "João Silva",
            "subjectId": 5,
            "subjectName": "Engenharia de Software",
            "semesterId": 1,
            "status": "ativo",
            "createdAt": "2024-01-15T10:00:00Z",
            "expectedResult": "Facilitar o controle acadêmico",
            "problem": "Falta de sistema integrado"
          }
        ]
        ```

---

### :material-plus-circle: Criar Projeto

!!! abstract "Visão Geral"
Cria um novo projeto no sistema com todas as informações necessárias, incluindo palavras-chave e documentos.

=== "Requisição"

    **`POST`** `/project`

    **Tags:** `Projects`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do usuário criador | `3` |
    | `semesterId` | `integer` | ✅ | ID do semestre | `7` |
    | `name` | `string` | ✅ | Nome do projeto | `"My new project"` |
    | `expectedResult` | `string` | ❌ | Resultado esperado | `"New clients to my company"` |
    | `feedback` | `string` | ❌ | Feedback do projeto | `"It is a feedback"` |
    | `problem` | `string` | ✅ | Descrição do problema a resolver | `"My company does not have clients"` |
    | `status` | `string` | ❌ | Status inicial | `"created"` |
    | `keywords` | `array` | ❌ | Palavras-chave do projeto | Ver estrutura abaixo |
    | `pdf` | `string` | ❌ | PDF em base64 | `"data:application/pdf;base64,..."` |

    #### 🏷️ Estrutura de Keywords

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `keywordid` | `integer` | ✅ | ID da palavra-chave | `1` |
    | `main` | `boolean` | ❌ | Se é palavra-chave principal | `true` |

    !!! info "Status Válidos"
        - `created` - Projeto criado
        - `em_execucao` - Em execução
        - `concluido` - Concluído
        - `rejeitado` - Rejeitado

    !!! example "Exemplo de Requisição"
        ```json
        {
          "userId": 3,
          "semesterId": 7,
          "name": "Sistema de Gestão Acadêmica",
          "expectedResult": "Facilitar o controle acadêmico",
          "problem": "Falta de sistema integrado para gestão",
          "status": "created",
          "keywords": [
            {
              "keywordid": 1,
              "main": true
            },
            {
              "keywordid": 2,
              "main": false
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**201**</span> | ✅ Criado | Projeto criado com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos na requisição |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Usuário ou semestre não encontrado |

---

### :material-pencil: Alterar Projeto

!!! abstract "Visão Geral"
Modifica os dados de um projeto existente, permitindo atualizações parciais.

=== "Requisição"

    **`PUT`** `/project`

    **Tags:** `Projects`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `projectid` | `integer` | ✅ | ID do projeto | `5` |
    | `problem` | `string` | ❌ | Novo problema a resolver | `"Problem to solve"` |
    | `expectedresult` | `string` | ❌ | Novo resultado esperado | `"A new expected result here"` |
    | `keywords` | `array` | ❌ | Novas palavras-chave | Ver estrutura anterior |

    !!! info "Atualização Parcial"
        Envie apenas os campos que deseja alterar. Campos não informados manterão seus valores atuais.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "projectid": 5,
          "problem": "Novo problema identificado",
          "expectedresult": "Resultados atualizados esperados",
          "keywords": [
            {
              "keywordid": 3,
              "main": true
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Projeto atualizado |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Projeto não existe |

---

## Listar Abstracts.

**Método:** `GET`
**Caminho:** `/abstract`
**Tags:** Abstract

Listar Abstracts.

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Retornar projetos concluídos existentes

**Método:** `GET`
**Caminho:** `/projectEC`
**Tags:** Projects

Retorna lista de projetos concluídos

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Listar semestre ligadas em projetos.

**Método:** `GET`
**Caminho:** `/projectSemester`
**Tags:** Projects

Lista semestres ligadas em projetos.

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Avaliar projeto

**Método:** `PUT`
**Caminho:** `/project/evaluate`
**Tags:** Projects

Avalia um projeto

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição                            | Exemplo                   | Obrigatório |
| ----------- | -------- | ------------------------------------ | ------------------------- | ----------- |
| `projectid` | `number` | Id do projeto                        | `5`                       | Não         |
| `status`    | `string` | N/A                                  | `em_execucao`             | Não         |
| `feedback`  | `string` | Conteúdo do feedback dado ao projeto | `This was a good project` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Realocar projeto

**Método:** `PUT`
**Caminho:** `/project/reallocate`
**Tags:** Projects

Realoca um projeto.

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição        | Exemplo | Obrigatório |
| ----------- | -------- | ---------------- | ------- | ----------- |
| `projectid` | `number` | Id do projeto    | `1`     | Não         |
| `subjectId` | `number` | Id da disciplina | `5`     | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Listar palavras-chaves disponíveis

**Método:** `GET`
**Caminho:** `/project/keywords`
**Tags:** Projects

Lista as palavras-chaves disponíveis para utilização em um projeto.

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Exibir dados do projeto

**Método:** `GET`
**Caminho:** `/project/{projectId}`
**Tags:** Projects

Exibe os dados do projeto.

### Parâmetros

| Nome        | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| ----------- | ------ | -------- | ------------- | ----------- | ------- |
| `projectId` | `path` | `number` | Id do projeto | Sim         | `4`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Adicionar subcategoria a projeto

**Método:** `POST`
**Caminho:** `/project/{projectId}`
**Tags:** Projects

Adiciona uma subcategoria a um projeto

### Parâmetros

| Nome        | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| ----------- | ------ | -------- | ------------- | ----------- | ------- |
| `projectId` | `path` | `number` | ID do projeto | Sim         | `2`     |

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade    | Tipo     | Descrição    | Exemplo       | Obrigatório |
| -------------- | -------- | ------------ | ------------- | ----------- |
| `subcategoria` | `string` | Subcategoria | `Confeitaria` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `201`  | Sucesso   |         |

### :material-delete: Excluir Projeto

!!! abstract "Visão Geral"
Remove permanentemente um projeto do sistema.

=== "Requisição"

    **`DELETE`** `/project/{projectId}`

    **Tags:** `Projects`

    #### 🔍 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `projectId` | `integer` | ✅ | ID do projeto a excluir | `4` |

    !!! warning "Ação Irreversível"
        Esta operação é permanente e não pode ser desfeita. Certifique-se de que deseja realmente excluir o projeto.

    !!! example "Exemplo de Requisição"
        ```
        DELETE /project/4
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Projeto excluído |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Projeto não existe |

---

## :material-school: Disciplinas

### :material-plus-circle: Criar Disciplina

!!! abstract "Visão Geral"
Cria uma nova disciplina na plataforma com professores, palavras-chave e subáreas associadas.

=== "Requisição"

    **`POST`** `/subject`

    **Tags:** `Subjects`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `subject` | `object` | ❌ | Dados da disciplina | Ver estrutura abaixo |
    | `keywords` | `array` | ❌ | Palavras-chave da disciplina | Ver estrutura abaixo |
    | `subareas` | `array` | ❌ | Subáreas da disciplina | Ver estrutura abaixo |
    | `professors` | `array` | ❌ | Professores associados | Ver estrutura abaixo |
    | `image` | `string` | ❌ | Imagem em base64 | `"data:image/jpeg;base64,..."` |

    #### 🏷️ Estrutura de Keywords

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `keywordid` | `integer` | ❌ | ID da palavra-chave disponível | `2` |

    #### 🏷️ Estrutura de Subareas

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `subareaid` | `integer` | ❌ | ID da subárea | `4` |

    #### 🏷️ Estrutura de Professors

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `regnumber` | `string` | ❌ | Matrícula do professor | `"123456789"` |

    !!! info "Palavras-chave Únicas"
        Para v0, a disciplina deve conter apenas 1 palavra-chave que não esteja associada a nenhuma outra disciplina.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "subject": {
            "name": "Engenharia de Software",
            "description": "Disciplina sobre desenvolvimento de software",
            "code": "ENG001"
          },
          "keywords": [
            {
              "keywordid": 2
            }
          ],
          "subareas": [
            {
              "subareaid": 4
            }
          ],
          "professors": [
            {
              "regnumber": "123456789"
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Disciplina criada |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos |
    | <span style="color: red">**409**</span> | ❌ Conflito | Palavra-chave já associada |

---

### :material-format-list-bulleted: Listar Disciplinas

!!! abstract "Visão Geral"
Lista todas as disciplinas cadastradas na plataforma com informações básicas.

=== "Requisição"

    **`GET`** `/subject`

    **Tags:** `Subjects`

    !!! example "Exemplo de Requisição"
        ```
        GET /subject
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de disciplinas retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Engenharia de Software",
            "code": "ENG001",
            "description": "Disciplina sobre desenvolvimento de software",
            "createdAt": "2024-01-15T10:00:00Z",
            "keywords": ["desenvolvimento", "software"],
            "subareas": ["Tecnologia"],
            "professors": ["Prof. João Silva"]
          }
        ]
        ```

---

### :material-link: Listar Disciplinas com Projetos

!!! abstract "Visão Geral"
Lista as disciplinas que possuem projetos associados.

=== "Requisição"

    **`GET`** `/subject/project`

    **Tags:** `Subject`

    !!! info "Filtro Especial"
        Esta lista retorna apenas disciplinas que têm pelo menos um projeto ativo ou concluído.

    !!! example "Exemplo de Requisição"
        ```
        GET /subject/project
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de disciplinas com projetos |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Engenharia de Software",
            "projectCount": 5,
            "activeProjects": 3,
            "completedProjects": 2
          }
        ]
        ```

---

### :material-tag-multiple: Listar Palavras-chave de Disciplinas

!!! abstract "Visão Geral"
Lista todas as palavras-chave utilizadas pelas disciplinas cadastradas.

=== "Requisição"

    **`GET`** `/subject/keywords`

    **Tags:** `Subjects`

    !!! example "Exemplo de Requisição"
        ```
        GET /subject/keywords
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de palavras-chave |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "desenvolvimento",
            "subjectId": 1,
            "subjectName": "Engenharia de Software",
            "usageCount": 3
          }
        ]
        ```

---

### :material-file-document: Exibir Disciplina

!!! abstract "Visão Geral"
Retorna os dados detalhados de uma disciplina específica.

=== "Requisição"

    **`GET`** `/subject/{subjectId}`

    **Tags:** `Subjects`

    #### 🔍 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `subjectId` | `integer` | ✅ | ID da disciplina | `2` |

    !!! example "Exemplo de Requisição"
        ```
        GET /subject/2
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Dados da disciplina |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Disciplina não existe |

    !!! success "Resposta de Sucesso (200)"
        ```json
        {
          "id": 2,
          "name": "Engenharia de Software",
          "code": "ENG001",
          "description": "Disciplina sobre desenvolvimento de software",
          "keywords": [
            {
              "id": 1,
              "name": "desenvolvimento"
            }
          ],
          "subareas": [
            {
              "id": 4,
              "name": "Tecnologia"
            }
          ],
          "professors": [
            {
              "regnumber": "123456789",
              "name": "Prof. João Silva"
            }
          ],
          "projectCount": 5,
          "createdAt": "2024-01-15T10:00:00Z"
        }
        ```

---

### :material-pencil: Editar Disciplina

!!! abstract "Visão Geral"
Atualiza os dados de uma disciplina existente.

=== "Requisição"

    **`PUT`** `/subject/{subjectId}`

    **Tags:** `Subjects`

    #### 🔍 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `subjectId` | `integer` | ✅ | ID da disciplina | `2` |

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    !!! info "Atualização Parcial"
        Envie apenas os campos que deseja alterar. Campos não informados manterão seus valores atuais.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "name": "Engenharia de Software Avançada",
          "description": "Disciplina atualizada sobre desenvolvimento",
          "keywords": [
            {
              "keywordid": 3
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Disciplina atualizada |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Disciplina não existe |

---

### :material-delete: Excluir Disciplina

!!! abstract "Visão Geral"
Remove permanentemente uma disciplina do sistema.

=== "Requisição"

    **`DELETE`** `/subject/{subjectId}`

    **Tags:** `Subjects`

    #### 🔍 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `subjectId` | `integer` | ✅ | ID da disciplina | `2` |

    !!! warning "Ação Irreversível"
        Esta operação é permanente e afetará todos os projetos associados à disciplina.

    !!! example "Exemplo de Requisição"
        ```
        DELETE /subject/2
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Disciplina excluída |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Disciplina não existe |
    | <span style="color: red">**409**</span> | ❌ Conflito | Disciplina possui projetos associados |

---

## :material-layers: Subáreas

### :material-format-list-bulleted: Listar Subáreas

!!! abstract "Visão Geral"
Lista todas as subáreas cadastradas na plataforma com informações básicas.

=== "Requisição"

    **`GET`** `/subareas`

    **Tags:** `Areas`

    !!! example "Exemplo de Requisição"
        ```
        GET /subareas
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de subáreas retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Tecnologia da Informação",
            "description": "Área focada em TI",
            "areaId": 1,
            "areaName": "Ciências Exatas",
            "createdAt": "2024-01-15T10:00:00Z"
          }
        ]
        ```

---

## :material-account: Usuários

### :material-format-list-bulleted: Listar Propostas do Usuário

!!! abstract "Visão Geral"
Lista todas as propostas de projeto criadas por um usuário específico.

=== "Requisição"

    **`GET`** `/userProposals/{userId}`

    **Tags:** `Projects`

    #### 🔍 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `integer` | ✅ | ID do usuário | `5` |

    !!! example "Exemplo de Requisição"
        ```
        GET /userProposals/5
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de propostas retornada |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Usuário não existe |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Sistema de Gestão",
            "status": "created",
            "createdAt": "2024-01-15T10:00:00Z",
            "problem": "Necessidade de automatização",
            "expectedResult": "Maior eficiência"
          }
        ]
        ```

---

### :material-school-outline: Listar Turmas do Estudante

!!! abstract "Visão Geral"
Lista todas as turmas em que um estudante específico está matriculado com detalhes dos horários.

=== "Requisição"

    **`GET`** `/users/student/{userId}/class`

    **Tags:** `Users`

    #### 🔍 Parâmetros de Path

    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `string` | ✅ | ID do estudante | `"123"` |

    !!! example "Exemplo de Requisição"
        ```
        GET /users/student/123/class
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de turmas retornada |
    | <span style="color: red">**400**</span> | ❌ Erro | Requisição inválida |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "classId": 1,
            "subjectId": 1,
            "classNumber": 1,
            "studentJoinMethod": "codigo",
            "accessCode": "ABCD1234",
            "semester": "1",
            "year": 2023,
            "active": true,
            "periods": [
              {
                "day": "segunda",
                "timeStart": "08:00",
                "timeFinish": "09:30"
              }
            ]
          }
        ]
        ```

    !!! failure "Resposta de Erro (400)"
        ```json
        {
          "error": "Error fetching classes"
        }
        ```

---

## :material-priority-high: Priorização e Alocação

### :material-plus-circle: Criar Priorização de Projeto

!!! abstract "Visão Geral"
Associa uma priorização de um aluno presente em uma classe a um projeto específico.

=== "Requisição"

    **`POST`** `/priorization`

    **Tags:** `Projects`, `Classes`, `Users`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `priorizations` | `array` | ❌ | Lista de priorizações | Ver estrutura abaixo |

    #### 🏷️ Estrutura de Priorizations

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `priorization` | `integer` | ❌ | Prioridade do projeto (1 = mais alta) | `1` |
    | `projectId` | `integer` | ❌ | ID do projeto | `1` |
    | `userId` | `integer` | ❌ | ID do usuário | `1` |
    | `classId` | `integer` | ❌ | ID da classe | `1` |

    !!! info "Sistema de Priorização"
        - **1** = Prioridade máxima
        - **2** = Segunda prioridade
        - **3** = Terceira prioridade, etc.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "priorizations": [
            {
              "priorization": 1,
              "projectId": 1,
              "userId": 1,
              "classId": 1
            },
            {
              "priorization": 2,
              "projectId": 2,
              "userId": 1,
              "classId": 1
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**201**</span> | ✅ Criado | Priorização criada com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Dados inválidos |
    | <span style="color: red">**404**</span> | ❌ Não encontrado | Usuário, projeto ou classe não existe |

---

### :material-account-group: Alocar Equipe no Projeto

!!! abstract "Visão Geral"
Executa a alocação automática de equipes nos projetos baseada nas priorizações dos estudantes.

=== "Requisição"

    **`POST`** `/assign-projects`

    **Tags:** `Projects`, `Classes`

    !!! info "Algoritmo de Alocação"
        O sistema utiliza as priorizações dos estudantes para formar equipes balanceadas nos projetos disponíveis.

    !!! example "Exemplo de Requisição"
        ```
        POST /assign-projects
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Equipes alocadas com sucesso |
    | <span style="color: red">**400**</span> | ❌ Erro | Erro na alocação |

    !!! success "Resposta de Sucesso (200)"
        ```json
        {
          "message": "Equipes alocadas com sucesso",
          "allocations": [
            {
              "projectId": 1,
              "projectName": "Sistema de Gestão",
              "team": [
                {
                  "userId": 1,
                  "userName": "João Silva",
                  "priorization": 1
                }
              ]
            }
          ]
        }
        ```

---

!!! success "✅ Documentação Concluída"
A documentação do ProjectService foi totalmente transformada com recursos visuais avançados, exemplos práticos e organização intuitiva usando Material for MkDocs.

!!! info "📚 Recursos Implementados" - **Visual Design**: Ícones, cores e indicadores de status - **Organização**: Separação por abas (Requisição/Resposta) - **Exemplos Práticos**: JSON samples para todos os endpoints - **Navegação**: Âncoras e estrutura hierárquica clara - **Feedback Visual**: Admonitions para destacar informações importantes

## :material-account-multiple: Alocar Usuários em Projetos

!!! abstract "Visão Geral"
Realiza a alocação de usuários em projetos, dividindo proporcionalmente o número de pessoas na turma pelo número de projetos.

=== "Requisição"

**`POST`** `/assign-users-to-projects`

**Tags:** `Projects`, `Classes`

#### 📝 Corpo da Requisição

**Content-Type:** `application/json`

| Campo     | Tipo   | Obrigatório | Descrição          | Exemplo                                  |
| --------- | ------ | :---------: | ------------------ | ---------------------------------------- |
| `classId` | string |     ❌      | ID da turma (UUID) | `"123e4567-e89b-12d3-a456-426614174000"` |

=== "Resposta"

#### ✅ Respostas

| Código                                    | Status    | Descrição                     |
| ----------------------------------------- | --------- | ----------------------------- |
| <span style="color: green">**201**</span> | ✅ Criado | Usuários alocados com sucesso |

---

## :material-link-variant: Associar Turmas a Projeto

!!! abstract "Visão Geral"
Associa uma ou várias turmas a um projeto específico.

=== "Requisição"

**`POST`** `/projetoTurmas`

**Tags:** `Projects`, `Classes`

#### 📝 Corpo da Requisição

**Content-Type:** `application/json`

| Campo       | Tipo    | Obrigatório | Descrição                 | Exemplo                                                                            |
| ----------- | ------- | :---------: | ------------------------- | ---------------------------------------------------------------------------------- |
| `projectId` | integer |     ❌      | ID do projeto             | `1`                                                                                |
| `classIds`  | array   |     ❌      | Array de UUIDs das turmas | `["eab020f9-c2af-4824-8e64-7b1385ac1e98", "55b8f4fb-e9b9-4639-9b8e-a3d4ace64b07"]` |

=== "Resposta"

#### ✅ Respostas

| Código                                    | Status    | Descrição                        |
| ----------------------------------------- | --------- | -------------------------------- |
| <span style="color: green">**201**</span> | ✅ Criado | Associação realizada com sucesso |

---

## :material-link-off: Remover Associação de Turmas a Projeto

!!! abstract "Visão Geral"
Remove a associação de uma ou várias turmas a um projeto.

=== "Requisição"

**`DELETE`** `/projetoTurmas`

**Tags:** `Projects`, `Classes`

#### 📝 Corpo da Requisição

**Content-Type:** `application/json`

| Campo       | Tipo    | Obrigatório | Descrição                 | Exemplo                                                                            |
| ----------- | ------- | :---------: | ------------------------- | ---------------------------------------------------------------------------------- |
| `projectId` | integer |     ❌      | ID do projeto             | `1`                                                                                |
| `classIds`  | array   |     ❌      | Array de UUIDs das turmas | `["eab020f9-c2af-4824-8e64-7b1385ac1e98", "55b8f4fb-e9b9-4639-9b8e-a3d4ace64b07"]` |

=== "Resposta"

#### ✅ Respostas

| Código                                    | Status     | Descrição                       |
| ----------------------------------------- | ---------- | ------------------------------- |
| <span style="color: green">**200**</span> | ✅ Sucesso | Associação removida com sucesso |

---

## :material-file-pdf-box: Obter PDF do Projeto

!!! abstract "Visão Geral"
Retorna o PDF associado a um projeto específico.

=== "Requisição"

**`GET`** `/project/{projectId}/pdf`

**Tags:** `Projects`, `Files`

#### 🎯 Parâmetros de Path

| Parâmetro   | Tipo   | Obrigatório | Descrição     | Exemplo                                  |
| ----------- | ------ | :---------: | ------------- | ---------------------------------------- |
| `projectId` | string |     ✅      | ID do projeto | `"123e4567-e89b-12d3-a456-426614174000"` |

=== "Resposta"

#### ✅ Respostas

| Código                                    | Status     | Descrição                |
| ----------------------------------------- | ---------- | ------------------------ |
| <span style="color: green">**200**</span> | ✅ Sucesso | PDF do projeto retornado |
