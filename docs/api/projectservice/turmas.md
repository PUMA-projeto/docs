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
