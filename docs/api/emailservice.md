
# :material-api: Emailservice API

!!! info "Visão Geral"
    A **Emailservice API** gerencia o envio de notificações por email para recuperação de senha, avaliação de projetos e comunicação com stakeholders no sistema PUMA.

## :material-chart-timeline: Sumário de Endpoints

| Grupo | Endpoints | Descrição |
|-------|-----------|-----------|
| [📧 Recuperação de Senha](#recuperacao-de-senha) | 1 endpoint | Envio de email para recuperação de senha |
| [📢 Avaliação de Projeto](#avaliacao-de-projeto) | 2 endpoints | Notificações sobre avaliação e andamento de projetos |
| [🔗 Avalie Projeto](#avalie-projeto) | 1 endpoint | Notificação para avaliação de projeto |

---

## 📧 Recuperação de Senha {#recuperacao-de-senha}

### :material-email: Enviar email de recuperação

!!! abstract "Visão Geral"
    Envia email de recuperação de senha.

=== "Requisição"

    **`POST`** `/mails/recover`
    
    **Tags:** `Mail`

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

## 📢 Avaliação de Projeto {#avaliacao-de-projeto}

### :material-email: Enviar email sobre avaliação de projeto

!!! abstract "Visão Geral"
    Envia email avisando sobre avaliação de projeto (Recusado ou Aprovado) com texto de feedback.

=== "Requisição"

    **`POST`** `/mails/evaluate`
    
    **Tags:** `Mail`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `name` | `string` | ❌ | Nome do usuário | `John Doe` |
    | `email` | `string` | ❌ | Email do usuário | `johndoe@email.com` |
    | `status` | `string` | ❌ | Sigla do status do projeto | `concluido` |
    | `feedback` | `string` | ❌ | Feedback da avaliação | `Este projeto foi muito bom` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "name": "John Doe",
          "email": "johndoe@email.com",
          "status": "concluido",
          "feedback": "Este projeto foi muito bom"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Email de avaliação enviado |

---

### :material-email: Enviar email sobre andamento do projeto

!!! abstract "Visão Geral"
    Envia email avisando sobre o andamento do projeto para o stakeholder em projetos que estão em andamento.

=== "Requisição"

    **`POST`** `/mails/recadoStakeholder`
    
    **Tags:** `Mail`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `name` | `string` | ❌ | Nome do usuário | `John Doe` |
    | `email` | `string` | ❌ | Email do usuário | `johndoe@email.com` |
    | `status` | `string` | ❌ | Sigla do status do projeto | `em_execucao` |
    | `feedback` | `string` | ❌ | Feedback da avaliação | `Este projeto foi muito bom` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "name": "John Doe",
          "email": "johndoe@email.com",
          "status": "em_execucao",
          "feedback": "Este projeto foi muito bom"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Email de andamento enviado |

---

## 🔗 Avalie Projeto {#avalie-projeto}

### :material-email: Enviar email para avaliação de projeto

!!! abstract "Visão Geral"
    Envia um email notificando o usuário sobre a avaliação de seu projeto. O email inclui um link para o projeto, onde o usuário pode avaliar o andamento do projeto.

=== "Requisição"

    **`POST`** `/mails/avalieProjeto`
    
    **Tags:** `Mail`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `name` | `string` | ❌ | Nome do usuário | `John Doe` |
    | `email` | `string` | ❌ | Email do usuário | `johndoe@email.com` |
    | `projectId` | `string` | ❌ | ID único do projeto que está sendo avaliado | `123` |

    !!! example "Exemplo de Requisição"
        ```json
        {
          "name": "John Doe",
          "email": "johndoe@email.com",
          "projectId": "123"
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Email de avaliação enviado |

## Envia email avisando sobre avaliação de projeto

**Método:** `POST`
**Caminho:** `/mails/evaluate`
**Tags:** Mail

Envia email avisando sobre avaliação de projeto (Recusado ou Aprovado) com texto de feedback

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição                  | Exemplo                      | Obrigatório |
| ----------- | -------- | -------------------------- | ---------------------------- | ----------- |
| `name`      | `string` | Nome do usuário            | `John Doe`                   | Não         |
| `email`     | `string` | Email do usuário           | `johndoe@email.com`          | Não         |
| `status`    | `string` | Sigla do status do projeto | `concluido`                  | Não         |
| `feedback`  | `string` | Feedback da avaliação      | `Este projeto foi muito bom` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Envia email avisando sobre o andamento do projeto

**Método:** `POST`
**Caminho:** `/mails/recadoStakeholder`
**Tags:** Mail

Envia email avisando sobre o andamento do projeto para o stakeholder em projetos que estão em andamento

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição                  | Exemplo                      | Obrigatório |
| ----------- | -------- | -------------------------- | ---------------------------- | ----------- |
| `name`      | `string` | Nome do usuário            | `John Doe`                   | Não         |
| `email`     | `string` | Email do usuário           | `johndoe@email.com`          | Não         |
| `status`    | `string` | Sigla do status do projeto | `em_execucao`                | Não         |
| `feedback`  | `string` | Feedback da avaliação      | `Este projeto foi muito bom` | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |

## Envia email avisando sobre a avaliação do projeto

**Método:** `POST`
**Caminho:** `/mails/avalieProjeto`
**Tags:** Mail

Envia um email notificando o usuário sobre a avaliação de seu projeto. O email inclui um link para o projeto, onde o usuário pode avaliar o andamento do projeto.

### Corpo da Requisição

**Tipo de Conteúdo:** `application/json`

**Propriedades:**

| Propriedade | Tipo     | Descrição                                    | Exemplo             | Obrigatório |
| ----------- | -------- | -------------------------------------------- | ------------------- | ----------- |
| `name`      | `string` | Nome do usuário                              | `John Doe`          | Não         |
| `email`     | `string` | Email do usuário                             | `johndoe@email.com` | Não         |
| `projectId` | `string` | ID único do projeto que está sendo avaliado. | `123`               | Não         |

### Respostas

| Código | Descrição | Esquema |
| ------ | --------- | ------- |
| `200`  | Sucesso   |         |
