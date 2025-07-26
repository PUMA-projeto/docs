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
