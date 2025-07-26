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
