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
