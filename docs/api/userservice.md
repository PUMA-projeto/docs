# :material-api: Userservice API

!!! info "Visão Geral"
A **Userservice API** gerencia usuários, autenticação, perfis, tipos de usuário e dados pessoais na plataforma PUMA. Oferece endpoints para cadastro, edição, login, recuperação de senha e consulta de dados.

## :material-chart-timeline: Sumário de Endpoints

| Grupo                                      | Endpoints   | Descrição                                                |
| ------------------------------------------ | ----------- | -------------------------------------------------------- |
| [👤 Usuários](#usuarios)                   | 6 endpoints | Cadastro, edição, login, consulta e recuperação de senha |
| [🔑 Tipos de Usuário](#tipos-de-usuario)   | 4 endpoints | Gerenciamento de tipos de usuário                        |
| [📧 Edital Email](#edital-email)           | 2 endpoints | Registro e verificação de email para edital              |
| [🖼️ Imagem de Usuário](#imagem-de-usuario) | 1 endpoint  | Consulta de imagem de perfil                             |

---

## 👤 Usuários {#usuarios}

### :material-plus-circle: Registrar novo usuário

!!! abstract "Visão Geral"
Cria um usuário na plataforma.

=== "Requisição"

    **`POST`** `/users`

    **Tags:** `Users`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `name` | `string` | ❌ | Nome do usuário | `John Doe` |
    | `email` | `string` | ❌ | Email do usuário | `johndoe@email.com` |
    | `password` | `string` | ❌ | Senha do usuário | `@Abcd1234` |
    | `type` | `string` | ❌ | Tipo de usuário | `Aluno` |
    | `externalAgentType` | `string` | ❌ | Tipo de agente externo | `N/A` |
    | `phoneNumber` | `string` | ❌ | Número do telefone | `11991234567` |
    | `cpf` | `string` | ❌ | Número do CPF | `25513933020` |
    | `cnpj` | `string` | ❌ | Número do CNPJ | `97089224000153` |
    | `companyName` | `string` | ❌ | Nome da empresa | `My Company Co.` |
    | `socialReason` | `string` | ❌ | Razão social da empresa | `My Company` |
    | `matricula` | `string` | ❌ | Matrícula do aluno/professor | `1234567` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "name": "John Doe",
          "email": "johndoe@email.com",
          "password": "@Abcd1234",
          "type": "Aluno"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**201**</span> | ✅ Sucesso | Usuário criado com sucesso |

---

### :material-pencil: Editar usuário

!!! abstract "Visão Geral"
Edita o perfil de um usuário da plataforma.

=== "Requisição"

    **`PUT`** `/users/{userId}`

    **Tags:** `Users`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `string` | ✅ | Matrícula do aluno | `1` |

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `name` | `string` | ❌ | Nome do usuário | `John Doe` |
    | `phoneNumber` | `string` | ❌ | Telefone do usuário | `61987654321` |
    | `matricula` | `string` | ❌ | Matrícula do usuário | `201234705` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "name": "John Doe",
          "phoneNumber": "61987654321"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Usuário editado com sucesso |

---

### :material-login: Efetuar login

!!! abstract "Visão Geral"
Autentica um usuário com email e senha e retorna um token de autenticação.

=== "Requisição"

    **`POST`** `/users/sessions`

    **Tags:** `Users`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `email` | `string` | ❌ | Email do usuário | `johndoe@email.com` |
    | `password` | `string` | ❌ | Senha do usuário | `@Abcd1234` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "email": "johndoe@email.com",
          "password": "@Abcd1234"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Token de autenticação retornado |

---

### :material-eye: Obter dados do usuário

!!! abstract "Visão Geral"
Obtém todos os dados de um usuário.

=== "Requisição"

    **`GET`** `/users/getUser/{userId}`

    **Tags:** `Users`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `string` | ✅ | Id do usuário | `1` |

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Dados do usuário retornados |

---

### :material-key: Alterar senha

!!! abstract "Visão Geral"
Altera a senha do usuário.

=== "Requisição"

    **`PUT`** `/users/password/{email}`

    **Tags:** `Users`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `email` | `string` | ✅ | Email do usuário | `johndoe@email.com` |

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `password` | `string` | ❌ | Nova senha | `@Abcd1234` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "password": "@Abcd1234"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Senha alterada com sucesso |

---

### :material-email: Solicitar nova senha

!!! abstract "Visão Geral"
Solicita uma nova senha por email.

=== "Requisição"

    **`POST`** `/users/recover`

    **Tags:** `Users`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `email` | `string` | ❌ | Email do usuário | `johndoe@email.com` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "email": "johndoe@email.com"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Email de recuperação enviado |

---

## 🔑 Tipos de Usuário {#tipos-de-usuario}

### :material-plus-circle: Criar tipo de usuário

!!! abstract "Visão Geral"
Cria um tipo de usuário.

=== "Requisição"

    **`POST`** `/user-types`

    **Tags:** `Users`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `typeName` | `string` | ❌ | Nome do tipo de usuário | `Novo tipo` |
    | `description` | `string` | ❌ | Descrição do novo tipo de usuário | `Este é um novo tipo de usuário` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "typeName": "Novo tipo",
          "description": "Este é um novo tipo de usuário"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Tipo de usuário criado |

---

### :material-format-list-bulleted: Listar tipos de usuários

!!! abstract "Visão Geral"
Lista todos os tipos de usuários cadastrados na plataforma.

=== "Requisição"

    **`GET`** `/user-types`

    **Tags:** `Users`

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Lista de tipos de usuários retornada |

---

### :material-eye: Visualizar tipo de usuário

!!! abstract "Visão Geral"
Visualiza os dados de um tipo de usuário.

=== "Requisição"

    **`GET`** `/user-types/{UserTypeid}`

    **Tags:** `Users`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `UserTypeid` | `string` | ✅ | Id do tipo de usuário | `1` |

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Dados do tipo de usuário retornados |

---

### :material-pencil: Editar tipo de usuário

!!! abstract "Visão Geral"
Edita um tipo de usuário.

=== "Requisição"

    **`PUT`** `/user-types/{UserTypeid}`

    **Tags:** `Users`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `UserTypeid` | `string` | ✅ | Id do tipo de usuário | `1` |

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `typeName` | `string` | ❌ | Novo nome do tipo de usuário | `Novo nome` |
    | `description` | `string` | ❌ | Nova descrição do tipo de usuário | `Nova descrição` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "typeName": "Novo nome",
          "description": "Nova descrição"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Tipo de usuário editado |

---

## 📧 Edital Email {#edital-email}

### :material-plus-circle: Registrar email para edital

!!! abstract "Visão Geral"
Registra email quando não há edital aberto.

=== "Requisição"

    **`POST`** `/users/editalEmail`

    **Tags:** `Users`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `email` | `string` | ❌ | Email do usuário | `johndoe@email.com` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "email": "johndoe@email.com"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Email registrado |

---

### :material-eye: Checar email para edital

!!! abstract "Visão Geral"
Checa se já existe um email cadastrado para o edital.

=== "Requisição"

    **`GET`** `/users/hasEditalEmail`

    **Tags:** `Users`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `email` | `string` | ❌ | Email do usuário | `johndoe@email.com` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "email": "johndoe@email.com"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Email verificado |

---

## 🖼️ Imagem de Usuário {#imagem-de-usuario}

### :material-image: Obter imagem de usuário

!!! abstract "Visão Geral"
Retorna a imagem de perfil do usuário.

=== "Requisição"

    **`GET`** `/users/image/{userId}`

    **Tags:** `Users, Files`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `userId` | `string` | ✅ | Id do usuário | `1` |

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Imagem de perfil retornada |

## Editar usuário

**Método:** `PUT`
**Caminho:** `/users/{userId}`
**Tags:** Users

Editar o perfil de um usuário da plataforma

### Parâmetros

| Nome     | Em     | Tipo     | Descrição          | Obrigatório | Exemplo |
| -------- | ------ | -------- | ------------------ | ----------- | ------- |
| `userId` | `path` | `string` | Matrícula do aluno | Sim         | `1`     |

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade   | Tipo     | Descrição            | Exemplo       | Obrigatório |
| ------------- | -------- | -------------------- | ------------- | ----------- |
| `name`        | `string` | Nome do usuário      | `John Doe`    | Não         |
| `phoneNumber` | `string` | Telefone do usuário  | `61987654321` | Não         |
| `matricula`   | `string` | Matricula do usuário | `201234705`   | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Efetuar login

**Método:** `POST`
**Caminho:** `/users/sessions`
**Tags:** Users

Autentica um usuário com email e senha e retorna um token de autenticação

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição        | Exemplo             | Obrigatório |
| ----------- | -------- | ---------------- | ------------------- | ----------- |
| `email`     | `string` | Email do usuário | `johndoe@email.com` | Não         |
| `password`  | `string` | Senha do usuário | `@Abcd1234`         | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Obter All Datas User

**Método:** `GET`
**Caminho:** `/users/getUser/{userId}`
**Tags:** Users

Obtém todos os dados de um usuário

### Parâmetros

| Nome     | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| -------- | ------ | -------- | ------------- | ----------- | ------- |
| `userId` | `path` | `string` | Id do usuário | Sim         | `1`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Obter usuário

**Método:** `GET`
**Caminho:** `/users/aluno/{userId}`
**Tags:** Users

Obtém os dados de um usuário

### Parâmetros

| Nome     | Em     | Tipo     | Descrição          | Obrigatório | Exemplo |
| -------- | ------ | -------- | ------------------ | ----------- | ------- |
| `userId` | `path` | `string` | Matrícula do aluno | Sim         | `1`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Obter todos os alunos

**Método:** `GET`
**Caminho:** `/users/aluno`
**Tags:** Users

Retorna uma lista de todos os alunos cadastrados no sistema. Suporta filtro por nome, ordenação e limitação de resultados.

### Parâmetros

| Nome      | Em      | Tipo      | Descrição                                                                        | Obrigatório | Exemplo |
| --------- | ------- | --------- | -------------------------------------------------------------------------------- | ----------- | ------- |
| `search`  | `query` | `string`  | Filtro de busca pelo nome do aluno (parcial, insensível a maiúsculas/minúsculas) | Não         | `N/A`   |
| `limit`   | `query` | `integer` | Número máximo de alunos a serem retornados                                       | Não         | `N/A`   |
| `orderBy` | `query` | `string`  | Campo utilizado para ordenação dos resultados                                    | Não         | `N/A`   |

### Respostas

| Código | Descrição                             | Esquema                     |
| ------ | ------------------------------------- | --------------------------- |
| `200`  | Lista de alunos retornada com sucesso | `application/json`: `array` |

**Itens do Array da Resposta:**

    | Propriedade | Tipo | Descrição | Exemplo | Obrigatório |
    |---|---|---|---|---|
    | `userId` | `string` | N/A | `123e4567-e89b-12d3-a456-426614174000` | Não |
    | `regNumber` | `string` | N/A | `2023123456` | Não |
    | `fullName` | `string` | N/A | `Maria da Silva` | Não |

|

## Alterar senha

**Método:** `PUT`
**Caminho:** `/users/password/{email}`
**Tags:** Users

Altera a senha do usuário

### Parâmetros

| Nome    | Em     | Tipo     | Descrição        | Obrigatório | Exemplo             |
| ------- | ------ | -------- | ---------------- | ----------- | ------------------- |
| `email` | `path` | `string` | Email do usuário | Sim         | `johndoe@email.com` |

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição  | Exemplo     | Obrigatório |
| ----------- | -------- | ---------- | ----------- | ----------- |
| `password`  | `string` | Nova senha | `@Abcd1234` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Solicitar nova senha

**Método:** `POST`
**Caminho:** `/users/recover`
**Tags:** Users

Solicita uma nova senha por email

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição        | Exemplo             | Obrigatório |
| ----------- | -------- | ---------------- | ------------------- | ----------- |
| `email`     | `string` | Email do usuário | `johndoe@email.com` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Confirma que o token de recuperação é valido

**Método:** `POST`
**Caminho:** `/users/confirmReset`
**Tags:** Users

Confirma que o token de recuperação é valido

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição            | Exemplo                               | Obrigatório |
| ----------- | -------- | -------------------- | ------------------------------------- | ----------- |
| `token`     | `string` | token de recuperação | `$2b$10$raO8GHQxbqzNFUDWkuO6Hu8eMB2h` | Não         |
| `id`        | `string` | id do usuario        | `1`                                   | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Reseta e redefine a senha do usuário

**Método:** `POST`
**Caminho:** `/users/reset`
**Tags:** Users

Reseta e redefine a senha do usuário

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição             | Exemplo                               | Obrigatório |
| ----------- | -------- | --------------------- | ------------------------------------- | ----------- |
| `id`        | `string` | id do usuario         | `1`                                   | Não         |
| `password`  | `string` | nova senha do usuario | `puma123456!`                         | Não         |
| `token`     | `string` | token de recuperação  | `$2b$10$raO8GHQxbqzNFUDWkuO6Hu8eMB2h` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Criar tipo de usuário

**Método:** `POST`
**Caminho:** `/user-types`
**Tags:** Users

Cria um tipo de usuário

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade   | Tipo     | Descrição                         | Exemplo                          | Obrigatório |
| ------------- | -------- | --------------------------------- | -------------------------------- | ----------- |
| `typeName`    | `string` | Nome do tipo de usuário           | `Novo tipo`                      | Não         |
| `description` | `string` | Descrição do novo tipo de usuário | `Este é um novo tipo de usuário` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Listar tipos de usuários

**Método:** `GET`
**Caminho:** `/user-types`
**Tags:** Users

Lista todos os tipos de usuários cadastrados na plataforma

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Visualizar tipo de usuário

**Método:** `GET`
**Caminho:** `/user-types/{UserTypeid}`
**Tags:** Users

Visualiza os dados de um tipo de usuário

### Parâmetros

| Nome         | Em     | Tipo     | Descrição             | Obrigatório | Exemplo |
| ------------ | ------ | -------- | --------------------- | ----------- | ------- |
| `UserTypeid` | `path` | `string` | Id do tipo de usuário | Sim         | `1`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Editar tipo de usuário

**Método:** `PUT`
**Caminho:** `/user-types/{UserTypeid}`
**Tags:** Users

Edita um tipo de usuário

### Parâmetros

| Nome         | Em     | Tipo     | Descrição             | Obrigatório | Exemplo |
| ------------ | ------ | -------- | --------------------- | ----------- | ------- |
| `UserTypeid` | `path` | `string` | Id do tipo de usuário | Sim         | `1`     |

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade   | Tipo     | Descrição                         | Exemplo          | Obrigatório |
| ------------- | -------- | --------------------------------- | ---------------- | ----------- |
| `typeName`    | `string` | Novo nome do tipo de usuário      | `Novo nome`      | Não         |
| `description` | `string` | Nova descrição do tipo de usuário | `Nova descrição` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Retornar CPF do usuário

**Método:** `GET`
**Caminho:** `/users/cpf/{userId}`
**Tags:** Users

Retorna o CPF do usuário

### Parâmetros

| Nome     | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| -------- | ------ | -------- | ------------- | ----------- | ------- |
| `userId` | `path` | `string` | Id do usuário | Sim         | `1`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Retornar o Usuário Jurídico

**Método:** `GET`
**Caminho:** `/users/juridical/{userId}`
**Tags:** Users

Retorna o usuário jurídico do userId dado

### Parâmetros

| Nome     | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| -------- | ------ | -------- | ------------- | ----------- | ------- |
| `userId` | `path` | `string` | Id do usuário | Sim         | `1`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Retornar o Professor

**Método:** `GET`
**Caminho:** `/users/professor/{userId}`
**Tags:** Users

Retorna o professor do userId dado

### Parâmetros

| Nome     | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| -------- | ------ | -------- | ------------- | ----------- | ------- |
| `userId` | `path` | `string` | Id do usuário | Sim         | `1`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Retornar o Estudante

**Método:** `GET`
**Caminho:** `/users/student/{userId}`
**Tags:** Users

Retorna o estudante do userId dado

### Parâmetros

| Nome     | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| -------- | ------ | -------- | ------------- | ----------- | ------- |
| `userId` | `path` | `string` | Id do usuário | Sim         | `1`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Registrar email para edital

**Método:** `POST`
**Caminho:** `/users/editalEmail`
**Tags:** Users

Registra email quando não há edital aberto

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição        | Exemplo             | Obrigatório |
| ----------- | -------- | ---------------- | ------------------- | ----------- |
| `email`     | `string` | Email do usuário | `johndoe@email.com` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Checar um email para o edital

**Método:** `GET`
**Caminho:** `/users/hasEditalEmail`
**Tags:** Users

Checar se já existe um email cadastro para o edital

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição        | Exemplo             | Obrigatório |
| ----------- | -------- | ---------------- | ------------------- | ----------- |
| `email`     | `string` | Email do usuário | `johndoe@email.com` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Obter imagem de usuário

**Método:** `GET`
**Caminho:** `/users/image/{userId}`
**Tags:** Users, Files

Retorna a imagem de perfil do usuário

### Parâmetros

| Nome     | Em     | Tipo     | Descrição     | Obrigatório | Exemplo |
| -------- | ------ | -------- | ------------- | ----------- | ------- |
| `userId` | `path` | `string` | Id do usuário | Sim         | `1`     |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |
