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
