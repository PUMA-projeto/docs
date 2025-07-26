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
