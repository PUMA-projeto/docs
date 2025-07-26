## 📋 Projetos {#projetos}

### :material-format-list-bulleted: Listar Projetos

!!! abstract "Visão Geral"
Retorna uma lista de projetos cadastrados com opções de filtro avançadas para facilitar a busca.

=== "Requisição"

    **`GET`** `/project`

    **Tags:** `Projects`

    #### 🔍 Parâmetros de Query

    | Parâmetro    | Tipo      | Obrigatório | Descrição             | Exemplo         |
    | ------------ | --------- | :---------: | --------------------- | --------------- |
    | `name`       | `string`  |      ❌      | Nome do projeto       | `"Sistema Web"` |
    | `userId`     | `integer` |      ❌      | ID do usuário criador | `123`           |
    | `subjectId`  | `integer` |      ❌      | ID da disciplina      | `5`             |
    | `semesterId` | `integer` |      ❌      | ID do semestre        | `1`             |
    | `status`     | `string`  |      ❌      | Status do projeto     | `"ativo"`       |

    !!! tip "Filtros Combinados"
        Você pode combinar múltiplos parâmetros para refinar sua busca e obter resultados mais precisos.

    !!! example "Exemplo de Requisição"
        ```
        GET /project?name=Sistema&status=ativo&subjectId=5
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código                                    | Status    | Descrição                   |
    | ----------------------------------------- | --------- | --------------------------- |
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de projetos retornada |

    !!! success "Resposta de Sucesso (200)"
        ```json
        [
          {
            "id": 1,
            "name": "Sistema de Gestão Acadêmica",
            "userId": 123,
            "userName": "João Silva",
            "subjectId": 5,
            "subjectName": "Engenharia de Software",
            "semesterId": 1,
            "status": "ativo",
            "createdAt": "2024-01-15T10:00:00Z",
            "expectedResult": "Facilitar o controle acadêmico",
            "problem": "Falta de sistema integrado"
          }
        ]
        ```

---

### :material-plus-circle: Criar Projeto

!!! abstract "Visão Geral"
Cria um novo projeto no sistema com todas as informações necessárias, incluindo palavras-chave e documentos.

=== "Requisição"

    **`POST`** `/project`

    **Tags:** `Projects`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo            | Tipo      | Obrigatório | Descrição                        | Exemplo                              |
    | ---------------- | --------- | :---------: | -------------------------------- | ------------------------------------ |
    | `userId`         | `integer` |      ✅      | ID do usuário criador            | `3`                                  |
    | `semesterId`     | `integer` |      ✅      | ID do semestre                   | `7`                                  |
    | `name`           | `string`  |      ✅      | Nome do projeto                  | `"My new project"`                   |
    | `expectedResult` | `string`  |      ❌      | Resultado esperado               | `"New clients to my company"`        |
    | `feedback`       | `string`  |      ❌      | Feedback do projeto              | `"It is a feedback"`                 |
    | `problem`        | `string`  |      ✅      | Descrição do problema a resolver | `"My company does not have clients"` |
    | `status`         | `string`  |      ❌      | Status inicial                   | `"created"`                          |
    | `keywords`       | `array`   |      ❌      | Palavras-chave do projeto        | Ver estrutura abaixo                 |
    | `pdf`            | `string`  |      ❌      | PDF em base64                    | `"data:application/pdf;base64,..."`  |

    #### 🏷️ Estrutura de Keywords

    | Campo       | Tipo      | Obrigatório | Descrição                    | Exemplo |
    | ----------- | --------- | :---------: | ---------------------------- | ------- |
    | `keywordid` | `integer` |      ✅      | ID da palavra-chave          | `1`     |
    | `main`      | `boolean` |      ❌      | Se é palavra-chave principal | `true`  |

    !!! info "Status Válidos"
        - `created` - Projeto criado
        - `em_execucao` - Em execução
        - `concluido` - Concluído
        - `rejeitado` - Rejeitado

    !!! example "Exemplo de Requisição"
        ```json
        {
          "userId": 3,
          "semesterId": 7,
          "name": "Sistema de Gestão Acadêmica",
          "expectedResult": "Facilitar o controle acadêmico",
          "problem": "Falta de sistema integrado para gestão",
          "status": "created",
          "keywords": [
            {
              "keywordid": 1,
              "main": true
            },
            {
              "keywordid": 2,
              "main": false
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código                                    | Status           | Descrição                          |
    | ----------------------------------------- | ---------------- | ---------------------------------- |
    | <span style="color: green">**201**</span> | ✅ Criado         | Projeto criado com sucesso         |
    | <span style="color: red">**400**</span>   | ❌ Erro           | Dados inválidos na requisição      |
    | <span style="color: red">**404**</span>   | ❌ Não encontrado | Usuário ou semestre não encontrado |

---

### :material-pencil: Alterar Projeto

!!! abstract "Visão Geral"
Modifica os dados de um projeto existente, permitindo atualizações parciais.

=== "Requisição"

    **`PUT`** `/project`

    **Tags:** `Projects`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo            | Tipo      | Obrigatório | Descrição                | Exemplo                        |
    | ---------------- | --------- | :---------: | ------------------------ | ------------------------------ |
    | `projectid`      | `integer` |      ✅      | ID do projeto            | `5`                            |
    | `problem`        | `string`  |      ❌      | Novo problema a resolver | `"Problem to solve"`           |
    | `expectedresult` | `string`  |      ❌      | Novo resultado esperado  | `"A new expected result here"` |
    | `keywords`       | `array`   |      ❌      | Novas palavras-chave     | Ver estrutura anterior         |

    !!! info "Atualização Parcial"
        Envie apenas os campos que deseja alterar. Campos não informados manterão seus valores atuais.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "projectid": 5,
          "problem": "Novo problema identificado",
          "expectedresult": "Resultados atualizados esperados",
          "keywords": [
            {
              "keywordid": 3,
              "main": true
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código                                    | Status           | Descrição          |
    | ----------------------------------------- | ---------------- | ------------------ |
    | <span style="color: green">**200**</span> | ✅ Sucesso        | Projeto atualizado |
    | <span style="color: red">**400**</span>   | ❌ Erro           | Dados inválidos    |
    | <span style="color: red">**404**</span>   | ❌ Não encontrado | Projeto não existe |

---

## Listar Abstracts.

**Método:** `GET`
**Caminho:** `/abstract`
**Tags:** Abstract

Listar Abstracts.

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Retornar projetos concluídos existentes

**Método:** `GET`
**Caminho:** `/projectEC`
**Tags:** Projects

Retorna lista de projetos concluídos

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Listar semestre ligadas em projetos.

**Método:** `GET`
**Caminho:** `/projectSemester`
**Tags:** Projects

Lista semestres ligadas em projetos.

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Avaliar projeto

**Método:** `PUT`
**Caminho:** `/project/evaluate`
**Tags:** Projects

Avalia um projeto

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição                            | Exemplo                   | Obrigatório |
| ----------- | -------- | ------------------------------------ | ------------------------- | ----------- |
| `projectid` | `number` | Id do projeto                        | `5`                       | Não         |
| `status`    | `string` | N/A                                  | `em_execucao`             | Não         |
| `feedback`  | `string` | Conteúdo do feedback dado ao projeto | `This was a good project` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Realocar projeto

**Método:** `PUT`
**Caminho:** `/project/reallocate`
**Tags:** Projects

Realoca um projeto.

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição        | Exemplo | Obrigatório |
| ----------- | -------- | ---------------- | ------- | ----------- |
| `projectid` | `number` | Id do projeto    | `1`     | Não         |
| `subjectId` | `number` | Id da disciplina | `5`     | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Listar palavras-chaves disponíveis

**Método:** `GET`
**Caminho:** `/project/keywords`
**Tags:** Projects

Lista as palavras-chaves disponíveis para utilização em um projeto.

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Exibir dados do projeto

**Método:** `GET`
**Caminho:** `/project/{projectId}`
**Tags:** Projects

Exibe os dados do projeto.

### Parâmetros

| Nome        | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| ----------- | ------ | -------- | ------------- | ----------- | ------- |
| `projectId` | `path` | `number` | Id do projeto | Sim         | `4`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Adicionar subcategoria a projeto

**Método:** `POST`
**Caminho:** `/project/{projectId}`
**Tags:** Projects

Adiciona uma subcategoria a um projeto

### Parâmetros

| Nome        | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| ----------- | ------ | -------- | ------------- | ----------- | ------- |
| `projectId` | `path` | `number` | ID do projeto | Sim         | `2`     |

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade    | Tipo     | Descrição    | Exemplo       | Obrigatório |
| -------------- | -------- | ------------ | ------------- | ----------- |
| `subcategoria` | `string` | Subcategoria | `Confeitaria` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `201`  | Sucesso   |         |

### :material-delete: Excluir Projeto

!!! abstract "Visão Geral"
Remove permanentemente um projeto do sistema.

=== "Requisição"

    **`DELETE`** `/project/{projectId}`

    **Tags:** `Projects`

    #### 🔍 Parâmetros de Path

    | Parâmetro   | Tipo      | Obrigatório | Descrição               | Exemplo |
    | ----------- | --------- | :---------: | ----------------------- | ------- |
    | `projectId` | `integer` |      ✅      | ID do projeto a excluir | `4`     |

    !!! warning "Ação Irreversível"
        Esta operação é permanente e não pode ser desfeita. Certifique-se de que deseja realmente excluir o projeto.

    !!! example "Exemplo de Requisição"
        ```
        DELETE /project/4
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código                                    | Status           | Descrição          |
    | ----------------------------------------- | ---------------- | ------------------ |
    | <span style="color: green">**200**</span> | ✅ Sucesso        | Projeto excluído   |
    | <span style="color: red">**404**</span>   | ❌ Não encontrado | Projeto não existe |

---

## :material-priority-high: Priorização e Alocação

### :material-plus-circle: Criar Priorização de Projeto

!!! abstract "Visão Geral"
Associa uma priorização de um aluno presente em uma classe a um projeto específico.

=== "Requisição"

    **`POST`** `/priorization`

    **Tags:** `Projects`, `Classes`, `Users`

    #### 📝 Corpo da Requisição

    **Content-Type:** `application/json`

    | Campo           | Tipo    | Obrigatório | Descrição             | Exemplo              |
    | --------------- | ------- | :---------: | --------------------- | -------------------- |
    | `priorizations` | `array` |      ❌      | Lista de priorizações | Ver estrutura abaixo |

    #### 🏷️ Estrutura de Priorizations

    | Campo          | Tipo      | Obrigatório | Descrição                             | Exemplo |
    | -------------- | --------- | :---------: | ------------------------------------- | ------- |
    | `priorization` | `integer` |      ❌      | Prioridade do projeto (1 = mais alta) | `1`     |
    | `projectId`    | `integer` |      ❌      | ID do projeto                         | `1`     |
    | `userId`       | `integer` |      ❌      | ID do usuário                         | `1`     |
    | `classId`      | `integer` |      ❌      | ID da classe                          | `1`     |

    !!! info "Sistema de Priorização"
        - **1** = Prioridade máxima
        - **2** = Segunda prioridade
        - **3** = Terceira prioridade, etc.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "priorizations": [
            {
              "priorization": 1,
              "projectId": 1,
              "userId": 1,
              "classId": 1
            },
            {
              "priorization": 2,
              "projectId": 2,
              "userId": 1,
              "classId": 1
            }
          ]
        }
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código                                    | Status           | Descrição                             |
    | ----------------------------------------- | ---------------- | ------------------------------------- |
    | <span style="color: green">**201**</span> | ✅ Criado         | Priorização criada com sucesso        |
    | <span style="color: red">**400**</span>   | ❌ Erro           | Dados inválidos                       |
    | <span style="color: red">**404**</span>   | ❌ Não encontrado | Usuário, projeto ou classe não existe |

---

### :material-account-group: Alocar Equipe no Projeto

!!! abstract "Visão Geral"
Executa a alocação automática de equipes nos projetos baseada nas priorizações dos estudantes.

=== "Requisição"

    **`POST`** `/assign-projects`

    **Tags:** `Projects`, `Classes`

    !!! info "Algoritmo de Alocação"
        O sistema utiliza as priorizações dos estudantes para formar equipes balanceadas nos projetos disponíveis.

    !!! example "Exemplo de Requisição"
        ```
        POST /assign-projects
        ```

=== "Resposta"

    #### ✅ Respostas

    | Código                                    | Status    | Descrição                    |
    | ----------------------------------------- | --------- | ---------------------------- |
    | <span style="color: green">**200**</span> | ✅ Sucesso | Equipes alocadas com sucesso |
    | <span style="color: red">**400**</span>   | ❌ Erro    | Erro na alocação             |

    !!! success "Resposta de Sucesso (200)"
        ```json
        {
          "message": "Equipes alocadas com sucesso",
          "allocations": [
            {
              "projectId": 1,
              "projectName": "Sistema de Gestão",
              "team": [
                {
                  "userId": 1,
                  "userName": "João Silva",
                  "priorization": 1
                }
              ]
            }
          ]
        }
        ```

---

!!! success "✅ Documentação Concluída"
A documentação do ProjectService foi totalmente transformada com recursos visuais avançados, exemplos práticos e organização intuitiva usando Material for MkDocs.

!!! info "📚 Recursos Implementados" - **Visual Design**: Ícones, cores e indicadores de status - **Organização**: Separação por abas (Requisição/Resposta) - **Exemplos Práticos**: JSON samples para todos os endpoints - **Navegação**: Âncoras e estrutura hierárquica clara - **Feedback Visual**: Admonitions para destacar informações importantes

## :material-account-multiple: Alocar Usuários em Projetos

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

## :material-link-variant: Associar Turmas a Projeto

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

## :material-link-off: Remover Associação de Turmas a Projeto

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

---

## :material-file-pdf-box: Obter PDF do Projeto

!!! abstract "Visão Geral"
Retorna o PDF associado a um projeto específico.

=== "Requisição"

**`GET`** `/project/{projectId}/pdf`

**Tags:** `Projects`, `Files`

#### 🎯 Parâmetros de Path

| Parâmetro   | Tipo   | Obrigatório | Descrição     | Exemplo                                  |
| ----------- | ------ | :---------: | ------------- | ---------------------------------------- |
| `projectId` | string |     ✅      | ID do projeto | `"123e4567-e89b-12d3-a456-426614174000"` |

=== "Resposta"

#### ✅ Respostas

| Código                                    | Status     | Descrição                |
| ----------------------------------------- | ---------- | ------------------------ |
| <span style="color: green">**200**</span> | ✅ Sucesso | PDF do projeto retornado |
