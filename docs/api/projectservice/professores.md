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
