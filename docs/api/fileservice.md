# :material-api: Fileservice API

!!! info "Visão Geral"
A **Fileservice API** gerencia o upload, download e exclusão de arquivos PDF de projetos e imagens de disciplinas no sistema PUMA. Todos os endpoints exigem autenticação via token Bearer no header `Authorization`.

## :material-chart-timeline: Sumário de Endpoints

| Grupo                                                | Endpoints   | Descrição                                             |
| ---------------------------------------------------- | ----------- | ----------------------------------------------------- |
| [📄 PDFs de Projetos](#pdfs-de-projetos)             | 3 endpoints | Upload, download e exclusão de PDFs de projetos       |
| [🖼️ Imagens de Disciplinas](#imagens-de-disciplinas) | 3 endpoints | Upload, download e exclusão de imagens de disciplinas |

---

## 📄 PDFs de Projetos {#pdfs-de-projetos}

### :material-file-upload: Upload de PDF de Projeto

!!! abstract "Visão Geral"
Permite o upload de um arquivo PDF codificado em base64 para um projeto específico, retornando o link do arquivo após o processamento.

=== "Requisição"

    **`POST`** `/files/pdf-project`

    **Tags:** `Files`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `pdf` | `string` | ❌ | PDF codificado em base64 | `data:application/pdf;base64,JVBERi0xLjQKMSAwIG9iago...` |

    !!! tip "Formato do PDF"
        O PDF deve estar no formato `data:application/pdf;base64,{conteúdo_base64}` para ser processado corretamente.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "pdf": "data:application/pdf;base64,JVBERi0xLjQKMSAwIG9iago8PAovVHlwZSAvQ2F0YWxvZwovUGFnZXMgMiAwIFI+PgplbmRvYmoK..."
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | PDF salvo com sucesso e link retornado |
    | <span style="color: orange">**400**</span> | ⚠️ Erro de Requisição | Dados inválidos ou formato de PDF incorreto |
    | <span style="color: red">**500**</span> | ❌ Erro Interno | Falha no processamento ou armazenamento |

    !!! example "Exemplo de Resposta (200 OK)"
        ```json
        {
          "success": true,
          "fileUrl": "https://storage.example.com/projects/a1b2c3d4e5f6.pdf",
          "hashName": "a1b2c3d4e5f6.pdf"
        }
        ```

---

### :material-file-download: Buscar PDF de Projeto

!!! abstract "Visão Geral"
Recupera um arquivo PDF específico através do seu nome hash único.

=== "Requisição"

    **`GET`** `/files/pdf-project/{PdfHashName}`

    **Tags:** `Files`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `PdfHashName` | `string` | ✅ | Nome hash do PDF (incluindo extensão .pdf) | `a1b2c3d4e5f6789.pdf` |

    !!! warning "Importante"
        O `PdfHashName` deve incluir obrigatoriamente a extensão `.pdf` e corresponder exatamente ao hash gerado durante o upload.

    !!! example "Exemplo de Requisição"
        ```bash
        curl -X GET \
          "https://api.example.com/files/pdf-project/a1b2c3d4e5f6789.pdf" \
          -H "Authorization: Bearer {seu_token}" \
          -H "Accept: application/pdf"
        ```

=== "Resposta"

    | Código | Status | Descrição | Tipo de Conteúdo |
    |--------|--------|-----------|------------------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Arquivo PDF retornado | `application/pdf` |
    | <span style="color: orange">**404**</span> | ⚠️ Não Encontrado | PDF não existe ou hash inválido | `application/json` |
    | <span style="color: red">**500**</span> | ❌ Erro Interno | Falha na recuperação do arquivo | `application/json` |

---

### :material-delete: Deletar PDF de Projeto

!!! abstract "Visão Geral"
Remove permanentemente um arquivo PDF do sistema através do seu nome hash.

=== "Requisição"

    **`DELETE`** `/files/pdf-project/{PdfHashName}`

    **Tags:** `Files`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `PdfHashName` | `string` | ✅ | Nome hash do PDF a ser excluído | `a1b2c3d4e5f6789.pdf` |

    !!! danger "Atenção"
        Esta operação é **irreversível**. Certifique-se de que o arquivo não é mais necessário antes de prosseguir.

    !!! example "Exemplo de Requisição"
        ```bash
        curl -X DELETE \
          "https://api.example.com/files/pdf-project/a1b2c3d4e5f6789.pdf" \
          -H "Authorization: Bearer {seu_token}"
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | PDF excluído com sucesso |
    | <span style="color: orange">**404**</span> | ⚠️ Não Encontrado | PDF não existe no sistema |
    | <span style="color: red">**500**</span> | ❌ Erro Interno | Falha na exclusão do arquivo |

---

## 🖼️ Imagens de Disciplinas {#imagens-de-disciplinas}

### :material-image: Upload de Imagem de Disciplina

!!! abstract "Visão Geral"
Envia uma imagem codificada em base64 para uma disciplina e retorna o hash único do arquivo.

=== "Requisição"

    **`POST`** `/files/subjectImage`

    **Tags:** `Files`

    #### 📝 Corpo da Requisição
    **Content-Type:** `application/json`

    | Campo | Tipo | Obrigatório | Descrição | Exemplo |
    |-------|------|:-----------:|-----------|---------|
    | `image` | `string` | ❌ | Imagem codificada em base64 | `data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEA...` |

    !!! info "Formatos Suportados"
        Formatos aceitos: JPEG, PNG, GIF, WebP. Tamanho máximo recomendado: 5MB.

    !!! example "Exemplo de Requisição"
        ```json
        {
          "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcU..."
        }
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Imagem salva e hash retornado |
    | <span style="color: orange">**400**</span> | ⚠️ Erro de Requisição | Formato de imagem inválido |
    | <span style="color: red">**500**</span> | ❌ Erro Interno | Falha no processamento da imagem |

    !!! example "Exemplo de Resposta (200 OK)"
        ```json
        {
          "success": true,
          "imageHash": "b7c8d9e0f1g2h3i4j5k6",
          "imageUrl": "https://storage.example.com/subjects/b7c8d9e0f1g2h3i4j5k6.jpg"
        }
        ```

---

### :material-image: Download de Imagem de Disciplina

!!! abstract "Visão Geral"
Busca e retorna uma imagem de disciplina através do seu hash único.

=== "Requisição"

    **`GET`** `/files/subjectImage/{ImageHashName}`

    **Tags:** `Files`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `ImageHashName` | `string` | ✅ | Hash único da imagem | `b7c8d9e0f1g2h3i4j5k6` |

    !!! example "Exemplo de Requisição"
        ```bash
        curl -X GET \
          "https://api.example.com/files/subjectImage/b7c8d9e0f1g2h3i4j5k6" \
          -H "Authorization: Bearer {seu_token}" \
          -H "Accept: image/*"
        ```

=== "Resposta"

    | Código | Status | Descrição | Tipo de Conteúdo |
    |--------|--------|-----------|------------------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Imagem retornada | `image/*` |
    | <span style="color: orange">**404**</span> | ⚠️ Não Encontrado | Imagem não existe | `application/json` |
    | <span style="color: red">**500**</span> | ❌ Erro Interno | Falha na recuperação | `application/json` |

---

### :material-delete: Deletar Imagem de Disciplina

!!! abstract "Visão Geral"
Remove permanentemente uma imagem de disciplina do sistema.

=== "Requisição"

    **`DELETE`** `/files/subjectImage/{ImageHashName}`

    **Tags:** `Files`

    #### 🎯 Parâmetros de Path
    | Parâmetro | Tipo | Obrigatório | Descrição | Exemplo |
    |-----------|------|:-----------:|-----------|---------|
    | `ImageHashName` | `string` | ✅ | Hash da imagem a ser excluída | `b7c8d9e0f1g2h3i4j5k6` |

    !!! danger "Operação Irreversível"
        Uma vez excluída, a imagem não poderá ser recuperada. Verifique se não há dependências antes de deletar.

    !!! example "Exemplo de Requisição"
        ```bash
        curl -X DELETE \
          "https://api.example.com/files/subjectImage/b7c8d9e0f1g2h3i4j5k6" \
          -H "Authorization: Bearer {seu_token}"
        ```

=== "Resposta"

    | Código | Status | Descrição |
    |--------|--------|-----------|
    | <span style="color: green">**200**</span> | ✅ Sucesso | Imagem excluída com sucesso |
    | <span style="color: orange">**404**</span> | ⚠️ Não Encontrado | Imagem não existe |
    | <span style="color: red">**500**</span> | ❌ Erro Interno | Falha na exclusão |

---

## 🔧 Códigos de Status HTTP

| Código                                     | Nome                  | Quando Ocorre                                |
| ------------------------------------------ | --------------------- | -------------------------------------------- |
| <span style="color: green">**200**</span>  | OK                    | Operação realizada com sucesso               |
| <span style="color: orange">**400**</span> | Bad Request           | Dados da requisição inválidos ou malformados |
| <span style="color: orange">**404**</span> | Not Found             | Recurso solicitado não encontrado            |
| <span style="color: red">**500**</span>    | Internal Server Error | Erro interno do servidor                     |

---

## 💡 Boas Práticas

!!! tip "Recomendações" - **Validação**: Sempre valide o formato base64 antes de enviar - **Tamanho**: Mantenha arquivos PDF abaixo de 10MB e imagens abaixo de 5MB - **Nomeação**: Guarde os hashes retornados para referências futuras - **Cache**: Implemente cache local para evitar downloads desnecessários

!!! warning "Limitações" - Máximo de 100 uploads por usuário por hora - Formatos suportados: PDF para documentos, JPEG/PNG/GIF/WebP para imagens - Tempo limite de 30 segundos por requisição

!!! tip "Formato do PDF"
O PDF deve estar no formato `data:application/pdf;base64,{conteúdo_base64}` para ser processado corretamente.

#### Respostas

| Código                                       | Status                | Descrição                                   |
| -------------------------------------------- | --------------------- | ------------------------------------------- |
| <span style="color: #28a745;">**200**</span> | ✅ Sucesso            | PDF salvo com sucesso e link retornado      |
| <span style="color: #ffc107;">**400**</span> | ⚠️ Erro de Requisição | Dados inválidos ou formato de PDF incorreto |
| <span style="color: #dc3545;">**500**</span> | ❌ Erro Interno       | Falha no processamento ou armazenamento     |

#### Exemplo de Requisição

```json
{
  "pdf": "data:application/pdf;base64,JVBERi0xLjQKMSAwIG9iago8PAovVHlwZSAvQ2F0YWxvZwovUGFnZXMgMiAwIFI+PgplbmRvYmoK..."
}
```

#### Exemplo de Resposta (200 OK)

```json
{
  "success": true,
  "fileUrl": "https://storage.example.com/projects/a1b2c3d4e5f6.pdf",
  "hashName": "a1b2c3d4e5f6.pdf"
}
```

---

### <span style="color: #007bff;">GET</span> Buscar PDF de Projeto

**Endpoint:** `GET /files/pdf-project/{PdfHashName}`

Recupera um arquivo PDF específico através do seu nome hash único.

#### Parâmetros de Caminho

| Nome          | Tipo     | Descrição                                      | Obrigatório | Exemplo               |
| ------------- | -------- | ---------------------------------------------- | ----------- | --------------------- |
| `PdfHashName` | `string` | **Nome hash do PDF** (incluindo extensão .pdf) | ✅          | `a1b2c3d4e5f6789.pdf` |

!!! warning "Importante"
O `PdfHashName` deve incluir obrigatoriamente a extensão `.pdf` e corresponder exatamente ao hash gerado durante o upload.

#### Respostas

| Código                                       | Status            | Descrição                       | Tipo de Conteúdo   |
| -------------------------------------------- | ----------------- | ------------------------------- | ------------------ |
| <span style="color: #28a745;">**200**</span> | ✅ Sucesso        | Arquivo PDF retornado           | `application/pdf`  |
| <span style="color: #ffc107;">**404**</span> | ⚠️ Não Encontrado | PDF não existe ou hash inválido | `application/json` |
| <span style="color: #dc3545;">**500**</span> | ❌ Erro Interno   | Falha na recuperação do arquivo | `application/json` |

#### Exemplo de Requisição

```bash
curl -X GET \
  "https://api.example.com/files/pdf-project/a1b2c3d4e5f6789.pdf" \
  -H "Authorization: Bearer {seu_token}" \
  -H "Accept: application/pdf"
```

---

### <span style="color: #dc3545;">DELETE</span> Deletar PDF de Projeto

**Endpoint:** `DELETE /files/pdf-project/{PdfHashName}`

Remove permanentemente um arquivo PDF do sistema através do seu nome hash.

#### Parâmetros de Caminho

| Nome          | Tipo     | Descrição                           | Obrigatório | Exemplo               |
| ------------- | -------- | ----------------------------------- | ----------- | --------------------- |
| `PdfHashName` | `string` | **Nome hash do PDF** a ser excluído | ✅          | `a1b2c3d4e5f6789.pdf` |

!!! danger "Atenção"
Esta operação é **irreversível**. Certifique-se de que o arquivo não é mais necessário antes de prosseguir.

#### Respostas

| Código                                       | Status            | Descrição                    |
| -------------------------------------------- | ----------------- | ---------------------------- |
| <span style="color: #28a745;">**200**</span> | ✅ Sucesso        | PDF excluído com sucesso     |
| <span style="color: #ffc107;">**404**</span> | ⚠️ Não Encontrado | PDF não existe no sistema    |
| <span style="color: #dc3545;">**500**</span> | ❌ Erro Interno   | Falha na exclusão do arquivo |

#### Exemplo de Requisição

```bash
curl -X DELETE \
  "https://api.example.com/files/pdf-project/a1b2c3d4e5f6789.pdf" \
  -H "Authorization: Bearer {seu_token}"
```

---

## 🖼️ Gerenciamento de Imagens de Disciplinas

### <span style="color: #28a745;">POST</span> Upload de Imagem de Disciplina

**Endpoint:** `POST /files/subjectImage`

Envia uma imagem codificada em base64 para uma disciplina e retorna o hash único do arquivo.

#### Corpo da Requisição

| Propriedade | Tipo     | Descrição                       | Obrigatório | Exemplo                                          |
| ----------- | -------- | ------------------------------- | ----------- | ------------------------------------------------ |
| `image`     | `string` | **Imagem codificada em base64** | ❌          | `data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEA...` |

!!! info "Formatos Suportados"
Formatos aceitos: JPEG, PNG, GIF, WebP. Tamanho máximo recomendado: 5MB.

#### Respostas

| Código                                       | Status                | Descrição                        |
| -------------------------------------------- | --------------------- | -------------------------------- |
| <span style="color: #28a745;">**200**</span> | ✅ Sucesso            | Imagem salva e hash retornado    |
| <span style="color: #ffc107;">**400**</span> | ⚠️ Erro de Requisição | Formato de imagem inválido       |
| <span style="color: #dc3545;">**500**</span> | ❌ Erro Interno       | Falha no processamento da imagem |

#### Exemplo de Requisição

```json
{
  "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcU..."
}
```

#### Exemplo de Resposta (200 OK)

```json
{
  "success": true,
  "imageHash": "b7c8d9e0f1g2h3i4j5k6",
  "imageUrl": "https://storage.example.com/subjects/b7c8d9e0f1g2h3i4j5k6.jpg"
}
```

---

### <span style="color: #007bff;">GET</span> Download de Imagem de Disciplina

**Endpoint:** `GET /files/subjectImage/{ImageHashName}`

Busca e retorna uma imagem de disciplina através do seu hash único.

#### Parâmetros de Caminho

| Nome            | Tipo     | Descrição                | Obrigatório | Exemplo                |
| --------------- | -------- | ------------------------ | ----------- | ---------------------- |
| `ImageHashName` | `string` | **Hash único da imagem** | ✅          | `b7c8d9e0f1g2h3i4j5k6` |

#### Respostas

| Código                                       | Status            | Descrição            | Tipo de Conteúdo   |
| -------------------------------------------- | ----------------- | -------------------- | ------------------ |
| <span style="color: #28a745;">**200**</span> | ✅ Sucesso        | Imagem retornada     | `image/*`          |
| <span style="color: #ffc107;">**404**</span> | ⚠️ Não Encontrado | Imagem não existe    | `application/json` |
| <span style="color: #dc3545;">**500**</span> | ❌ Erro Interno   | Falha na recuperação | `application/json` |

#### Exemplo de Requisição

```bash
curl -X GET \
  "https://api.example.com/files/subjectImage/b7c8d9e0f1g2h3i4j5k6" \
  -H "Authorization: Bearer {seu_token}" \
  -H "Accept: image/*"
```

---

### <span style="color: #dc3545;">DELETE</span> Deletar Imagem de Disciplina

**Endpoint:** `DELETE /files/subjectImage/{ImageHashName}`

Remove permanentemente uma imagem de disciplina do sistema.

#### Parâmetros de Caminho

| Nome            | Tipo     | Descrição                         | Obrigatório | Exemplo                |
| --------------- | -------- | --------------------------------- | ----------- | ---------------------- |
| `ImageHashName` | `string` | **Hash da imagem** a ser excluída | ✅          | `b7c8d9e0f1g2h3i4j5k6` |

!!! danger "Operação Irreversível"
Uma vez excluída, a imagem não poderá ser recuperada. Verifique se não há dependências antes de deletar.

#### Respostas

| Código                                       | Status            | Descrição                   |
| -------------------------------------------- | ----------------- | --------------------------- |
| <span style="color: #28a745;">**200**</span> | ✅ Sucesso        | Imagem excluída com sucesso |
| <span style="color: #ffc107;">**404**</span> | ⚠️ Não Encontrado | Imagem não existe           |
| <span style="color: #dc3545;">**500**</span> | ❌ Erro Interno   | Falha na exclusão           |

#### Exemplo de Requisição

```bash
curl -X DELETE \
  "https://api.example.com/files/subjectImage/b7c8d9e0f1g2h3i4j5k6" \
  -H "Authorization: Bearer {seu_token}"
```

---

## 🔧 Códigos de Status HTTP

| Código                                       | Nome                  | Quando Ocorre                                |
| -------------------------------------------- | --------------------- | -------------------------------------------- |
| <span style="color: #28a745;">**200**</span> | OK                    | Operação realizada com sucesso               |
| <span style="color: #ffc107;">**400**</span> | Bad Request           | Dados da requisição inválidos ou malformados |
| <span style="color: #ffc107;">**404**</span> | Not Found             | Recurso solicitado não encontrado            |
| <span style="color: #dc3545;">**500**</span> | Internal Server Error | Erro interno do servidor                     |

---

## 💡 Boas Práticas

!!! tip "Recomendações" - **Validação**: Sempre valide o formato base64 antes de enviar - **Tamanho**: Mantenha arquivos PDF abaixo de 10MB e imagens abaixo de 5MB - **Nomeação**: Guarde os hashes retornados para referências futuras - **Cache**: Implemente cache local para evitar downloads desnecessários

!!! warning "Limitações" - Máximo de 100 uploads por usuário por hora - Formatos suportados: PDF para documentos, JPEG/PNG/GIF/WebP para imagens - Tempo limite de 30 segundos por requisição
