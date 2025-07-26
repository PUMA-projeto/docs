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
