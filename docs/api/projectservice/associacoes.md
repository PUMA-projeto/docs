# Associações

Documentação dos endpoints relacionados a vínculos entre projetos e turmas.

## :material-link-variant: Associações

### :material-account-multiple: Alocar Usuários em Projetos

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

### :material-link-variant: Associar Turmas a Projeto

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

### :material-link-off: Remover Associação de Turmas a Projeto

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
