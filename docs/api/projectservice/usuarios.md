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
