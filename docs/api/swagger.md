# PUMA API - Documentação

Documentação da API do PUMA. Mantenha essa documentação atualizada para o correto funcionamento das rotas.

---

## Endpoints

### Avaliação por Pares

#### POST `/solicitation/create`

- **Descrição:** Cria solicitação de avaliação por pares, com as turmas e competências associadas.
- **Body:**
  - `name`: string
  - `classIds`: array (obrigatório)
  - `startDate`: string (obrigatório)
  - `endDate`: string (obrigatório)
  - `microCompetenceIds`: array (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/solicitations`

- **Descrição:** Retorna solicitações de avaliação por pares.
- **Parâmetros de Query:**
  - `creatorId`: integer (opcional)
  - `classId`: string (opcional)
  - `competence`: boolean (opcional)
  - `class`: boolean (opcional)
  - `creator`: boolean (opcional)
- **Resposta:** 200 - Sucesso

---

### Competências

#### DELETE `/competence/macro/{macroComptenceId}`

- **Descrição:** Deleta Macro competências com o macroComptenceId especificado.
- **Parâmetro de Path:**
  - `macroComptenceId`: integer (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/competences/{creatorId}`

- **Descrição:** Retorna todas as competências cadastradas.
- **Parâmetros de Query:**
  - `creatorId`: integer (opcional)
- **Resposta:** 200 - Sucesso

#### POST `/competences`

- **Descrição:** Envia lista de competências para cadastro.
- **Body:**
  - `macros`: array de objetos
    - `name`: string
    - `description`: string
    - `micros`: array de objetos
      - `name`: string
      - `description`: array
- **Resposta:** 200 - Sucesso

---

### Arquivos

#### POST `/files/pdf-project`

- **Descrição:** Envia PDF em string de base 64 e retorna o link do arquivo.
- **Body:**
  - `pdf`: string (base64)
- **Resposta:** 200 - Sucesso

#### GET `/files/pdf-project/{PdfHashName}`

- **Descrição:** Recupera pdf de projeto que tenha nome igual a PdfHashName.
- **Parâmetro de Path:**
  - `PdfHashName`: string (obrigatório)
- **Resposta:** 200 - Sucesso (application/pdf)

#### DELETE `/files/pdf-project/{PdfHashName}`

- **Descrição:** Exclui pdf de projeto que tenha nome igual a PdfHashName.
- **Parâmetro de Path:**
  - `PdfHashName`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/files/subjectImage`

- **Descrição:** Envia imagem em string de base 64 e retorna o hash do nome do arquivo.
- **Body:**
  - `image`: string (base64)
- **Resposta:** 200 - Sucesso

#### GET `/files/subjectImage/{ImageHashName}`

- **Descrição:** Busca imagem de usuário no provedor de arquivos.
- **Parâmetro de Path:**
  - `ImageHashName`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### DELETE `/files/subjectImage/{ImageHashName}`

- **Descrição:** Exclui imagem de disciplina que tenha nome igual a ImageHashName.
- **Parâmetro de Path:**
  - `ImageHashName`: string (obrigatório)
- **Resposta:** 200 - Sucesso

---

### Categorias

#### GET `/categoria`

- **Descrição:** Retorna todas as categorias cadastradas.
- **Resposta:** 200 - Sucesso

#### POST `/categoria`

- **Descrição:** Cria uma nova categoria para utilização nos projetos.
- **Body:**
  - `categoria`: string
- **Resposta:** 201 - Sucesso

#### DELETE `/categoria/{categoriaId}`

- **Descrição:** Deleta uma categoria existente.
- **Parâmetro de Path:**
  - `categoriaId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/categoria/{projectId}`

- **Descrição:** Adiciona uma categoria já existente a um projeto.
- **Parâmetro de Path:**
  - `projectId`: number (obrigatório)
- **Body:**
  - `categoria`: string
- **Resposta:** 201 - Sucesso

---

### Turmas

#### POST `/class`

- **Descrição:** Criar uma Turma de uma disciplina.
- **Body:**
  - `subjectId`: string
  - `semester`: string
  - `year`: string
  - `periods`: array de objetos
  - `teachers`: array de números
  - `monitors`: array de números
- **Resposta:** 200 - Sucesso

#### GET `/class`

- **Descrição:** Lista todas as Turmas.
- **Resposta:** 200 - Sucesso

#### GET `/class-extra-attributes`

- **Descrição:** Lista todas as Turmas com detalhes extras.
- **Parâmetros de Query:**
  - `userType`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/my-classes-extra-attributes/{userId}`

- **Descrição:** Lista Minhas Turmas Professor com detalhes extras.
- **Parâmetro de Path:**
  - `userId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/class/{userId}/student`

- **Descrição:** Lista Minhas Turmas Aluno com detalhes extras.
- **Parâmetro de Path:**
  - `userId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/{classId}/projetos`

- **Descrição:** Retorna a lista de projetos associados a uma determinada turma.
- **Parâmetro de Path:**
  - `classId`: string (obrigatório)
- **Resposta:** 200 - Sucesso | 400 - Requisição inválida | 500 - Erro interno

#### GET `/joinable-classes`

- **Descrição:** Lista todas as turmas disponíveis para ingresso.
- **Parâmetros de Query:**
  - `userId`: string (obrigatório)
  - `limit`: integer (obrigatório)
  - `offset`: integer (obrigatório)
- **Resposta:** 200 - Sucesso | 400 - Requisição inválida

#### GET `/class/{classId}/students`

- **Descrição:** Lista todos os alunos de uma turma pelo ID da turma.
- **Parâmetro de Path:**
  - `classId`: uuid (obrigatório)
- **Resposta:** 200 - Sucesso | 400 - Requisição inválida

#### POST `/class/{classId}/join`

- **Descrição:** Aluno ingressar em uma turma utilizando o Código de Acesso.
- **Parâmetro de Path:**
  - `classId`: string (obrigatório)
- **Body:**
  - `userId`: string (obrigatório)
  - `accessCode`: string (obrigatório)
- **Resposta:** 200 - Sucesso | 400 - Requisição inválida | 404 - Turma ou usuário não encontrado | 500 - Erro interno

#### POST `/class/{classId}/join/manual`

- **Descrição:** Adiciona um aluno em uma turma já existente.
- **Parâmetro de Path:**
  - `classId`: number (obrigatório)
- **Body:**
  - `userId`: string
- **Resposta:** 201 - Sucesso

#### GET `/class/{classId}`

- **Descrição:** Exibe os detalhes de uma turma.
- **Parâmetro de Path:**
  - `classId`: number (obrigatório)
- **Parâmetros de Query:**
  - `userId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### PUT `/class/{classId}`

- **Descrição:** Editar uma Turma de uma disciplina.
- **Parâmetro de Path:**
  - `classId`: string (obrigatório)
- **Body:**
  - `studentJoinMethod`: string
  - `accessCode`: string
  - `semester`: string
  - `year`: string
  - `periods`: array de objetos
  - `teachers`: array de números
  - `monitors`: array de números
- **Resposta:** 200 - Sucesso | 400 - Requisição inválida | 404 - Turma não encontrada | 500 - Erro interno

#### DELETE `/class/{classId}`

- **Descrição:** Exclui uma classe.
- **Parâmetro de Path:**
  - `classId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### PATCH `/class/{classId}`

- **Descrição:** Atualiza a chave de acesso utilizada por alunos ou usuários para ingressar em uma turma.
- **Parâmetro de Path:**
  - `classId`: uuid (obrigatório)
- **Body:**
  - `accessCode`: string (obrigatório)
- **Resposta:** 200 - Sucesso | 404 - Turma não encontrada

#### DELETE `/class/{classId}/student`

- **Descrição:** Remove um aluno de uma turma pelo ID da turma e do aluno.
- **Parâmetro de Path:**
  - `classId`: uuid (obrigatório)
- **Body:**
  - `userId`: number
- **Resposta:** 200 - Sucesso

---

### Keywords

#### GET `/keyword`

- **Descrição:** Lista as palavras-chaves cadastradas na plataforma.
- **Parâmetros de Query:**
  - `keyword`: string (opcional)
- **Resposta:** 200 - Sucesso

#### POST `/keyword`

- **Descrição:** Cria uma nova palavra-chave para utilização nos projetos.
- **Body:**
  - `keyword`: string
  - `psp`: string
- **Resposta:** 200 - Sucesso

#### GET `/keyword/abstract`

- **Descrição:** Lista as palavras-chaves relacionadas a algum projeto.
- **Resposta:** 200 - Sucesso

#### GET `/keyword/available`

- **Descrição:** Lista as palavras-chaves não associadas a nenhuma disciplina.
- **Resposta:** 200 - Sucesso

#### PUT `/keyword/available`

- **Descrição:** Edita o valor de uma palavra-chave já cadastrada na plataforma.
- **Body:**
  - `keywordid`: number
  - `newKeyword`: string
- **Resposta:** 200 - Sucesso

#### POST `/keyword/subject`

- **Descrição:** Associa uma disciplina a uma palavra-chave.
- **Body:**
  - `keywordid`: number
  - `subjectid`: number
- **Resposta:** 200 - Sucesso

#### PUT `/keyword/subject`

- **Descrição:** Edita a associação entre uma palavra-chave e uma disciplina.
- **Body:**
  - `keywordid`: number
  - `subjectid`: number
- **Resposta:** 200 - Sucesso

#### GET `/keyword/subject/{keywordId}`

- **Descrição:** Exibe matéria relacionada a palavra chave.
- **Parâmetro de Path:**
  - `keywordId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### DELETE `/keyword/{keywordId}`

- **Descrição:** Exclui uma palavra-chave da plataforma.
- **Parâmetro de Path:**
  - `keywordId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

---

### Areas

#### GET `/knowledgeareas`

- **Descrição:** Lista todas as subáreas cadastradas na plataforma.
- **Resposta:** 200 - Sucesso

#### GET `/subareas`

- **Descrição:** Lista todas as subáreas cadastradas na plataforma.
- **Resposta:** 200 - Sucesso

---

### Professors

#### GET `/professors`

- **Descrição:** Lista todos os professores cadastrados na plataforma.
- **Resposta:** 200 - Sucesso

---

### Subjects

#### POST `/subject`

- **Descrição:** Cria uma disciplina na plataforma.
- **Body:**
  - `subject`: objeto
    - `name`: string
    - `acronym`: string
    - `subjectGeneralObjective`: string
    - `courseSyllabus`: string
  - `keywords`: array de objetos
    - `keywordid`: number
  - `subareas`: array de objetos
    - `subareaid`: number
  - `professors`: array de objetos
    - `regnumber`: string
  - `image`: string (base64)
- **Resposta:** 200 - Sucesso

#### GET `/subject`

- **Descrição:** Lista todas as disciplinas cadastradas na plataforma.
- **Resposta:** 200 - Sucesso

#### GET `/subject/project`

- **Descrição:** Lista as disciplinas ligadas em projetos.
- **Resposta:** 200 - Sucesso

#### GET `/subject/keywords`

- **Descrição:** Lista as palavras-chaves de disciplinas cadastradas na plataforma.
- **Resposta:** 200 - Sucesso

#### GET `/subject/{subjectId}`

- **Descrição:** Exibe uma disciplina.
- **Parâmetro de Path:**
  - `subjectId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### PUT `/subject/{subjectId}`

- **Descrição:** Edita uma disciplina.
- **Parâmetro de Path:**
  - `subjectId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### DELETE `/subject/{subjectId}`

- **Descrição:** Exclui uma disciplina.
- **Parâmetro de Path:**
  - `subjectId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

---

### Projects

#### GET `/project`

- **Descrição:** Retorna lista de projetos cadastrados.
- **Parâmetros de Query:**
  - `name`: string (opcional)
  - `userId`: inteiro (opcional)
  - `subjectId`: inteiro (opcional)
  - `semesterId`: inteiro (opcional)
  - `status`: string (opcional)
- **Resposta:** 200 - Sucesso

#### POST `/project`

- **Descrição:** Cria um novo projeto.
- **Body:**
  - `userId`: number (obrigatório)
  - `semesterId`: number (obrigatório)
  - `name`: string (obrigatório)
  - `expectedResult`: string (obrigatório)
  - `feedback`: string (obrigatório)
  - `problem`: string (obrigatório)
  - `status`: string (obrigatório)
  - `keywords`: array de objetos (obrigatório)
  - `pdf`: string (base64)
- **Resposta:** 200 - Sucesso

#### PUT `/project`

- **Descrição:** Altera os dados do projeto.
- **Body:**
  - `projectid`: number
  - `problem`: string
  - `expectedresult`: string
  - `keywords`: array de objetos
- **Resposta:** 200 - Sucesso

#### GET `/project/{projectId}`

- **Descrição:** Exibe os dados do projeto.
- **Parâmetro de Path:**
  - `projectId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/project/{projectId}`

- **Descrição:** Adiciona uma subcategoria a um projeto.
- **Parâmetro de Path:**
  - `projectId`: number (obrigatório)
- **Body:**
  - `subcategoria`: string
- **Resposta:** 201 - Sucesso

#### DELETE `/project/{projectId}`

- **Descrição:** Exclui um projeto.
- **Parâmetro de Path:**
  - `projectId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/project/{projectId}/pdf`

- **Descrição:** Retorna o PDF do projeto.
- **Parâmetro de Path:**
  - `projectId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

#### PUT `/project/evaluate`

- **Descrição:** Avalia um projeto.
- **Body:**
  - `projectid`: number
  - `status`: string
  - `feedback`: string
- **Resposta:** 200 - Sucesso

#### PUT `/project/reallocate`

- **Descrição:** Realoca um projeto.
- **Body:**
  - `projectid`: number
  - `subjectId`: number
- **Resposta:** 200 - Sucesso

#### GET `/project/keywords`

- **Descrição:** Lista as palavras-chaves disponíveis para utilização em um projeto.
- **Resposta:** 200 - Sucesso

#### GET `/projectEC`

- **Descrição:** Retorna lista de projetos concluídos.
- **Resposta:** 200 - Sucesso

#### GET `/projectSemester`

- **Descrição:** Lista semestres ligadas em projetos.
- **Resposta:** 200 - Sucesso

---

### Users

#### POST `/users`

- **Descrição:** Cria um usuário na plataforma.
- **Body:**
  - `name`: string (obrigatório)
  - `email`: string (obrigatório)
  - `password`: string (obrigatório)
  - `type`: string (obrigatório)
  - `phoneNumber`: string (obrigatório)
  - ... (demais campos opcionais)
- **Resposta:** 201 - Sucesso

#### PUT `/users/{userId}`

- **Descrição:** Editar o perfil de um usuário da plataforma.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Body:**
  - `name`: string (obrigatório)
  - `phoneNumber`: string (obrigatório)
  - `matricula`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/users/sessions`

- **Descrição:** Autentica um usuário com email e senha e retorna um token de autenticação.
- **Body:**
  - `email`: string (obrigatório)
  - `password`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/getUser/{userId}`

- **Descrição:** Obtém todos os dados de um usuário.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/aluno/{userId}`

- **Descrição:** Obtém os dados de um usuário.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/aluno`

- **Descrição:** Retorna uma lista de todos os alunos cadastrados no sistema.
- **Parâmetros de Query:**
  - `search`: string (opcional)
  - `limit`: integer (opcional)
  - `orderBy`: string (opcional)
- **Resposta:** 200 - Sucesso

#### PUT `/users/password/{email}`

- **Descrição:** Altera a senha do usuário.
- **Parâmetro de Path:**
  - `email`: string (obrigatório)
- **Body:**
  - `password`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/users/recover`

- **Descrição:** Solicita uma nova senha por email.
- **Body:**
  - `email`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/users/confirmReset`

- **Descrição:** Confirma que o token de recuperação é válido.
- **Body:**
  - `token`: string (obrigatório)
  - `id`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/users/reset`

- **Descrição:** Reseta e redefine a senha do usuário.
- **Body:**
  - `id`: string (obrigatório)
  - `password`: string (obrigatório)
  - `token`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/user-types`

- **Descrição:** Cria um tipo de usuário.
- **Body:**
  - `typeName`: string (obrigatório)
  - `description`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/user-types`

- **Descrição:** Lista todos os tipos de usuários cadastrados na plataforma.
- **Resposta:** 200 - Sucesso

#### GET `/user-types/{UserTypeid}`

- **Descrição:** Visualiza os dados de um tipo de usuário.
- **Parâmetro de Path:**
  - `UserTypeid`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### PUT `/user-types/{UserTypeid}`

- **Descrição:** Edita um tipo de usuário.
- **Parâmetro de Path:**
  - `UserTypeid`: string (obrigatório)
- **Body:**
  - `typeName`: string (obrigatório)
  - `description`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### DELETE `/user-types/{UserTypeid}`

- **Descrição:** Apaga um tipo de usuário.
- **Parâmetro de Path:**
  - `UserTypeid`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/cpf/{userId}`

- **Descrição:** Retorna o CPF do usuário.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/juridical/{userId}`

- **Descrição:** Retorna o usuário jurídico do userId dado.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/professor/{userId}`

- **Descrição:** Retorna o professor do userId dado.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/student/{userId}`

- **Descrição:** Retorna o estudante do userId dado.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/student/{userId}/class`

- **Descrição:** Lista todas as turmas em que um estudante específico está matriculado.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/users/editalEmail`

- **Descrição:** Registra email quando não há edital aberto.
- **Body:**
  - `email`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/hasEditalEmail`

- **Descrição:** Checar se já existe um email cadastro para o edital.
- **Body:**
  - `email`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### GET `/users/image/{userId}`

- **Descrição:** Retorna a imagem de perfil do usuário.
- **Parâmetro de Path:**
  - `userId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

---

### Mail

#### POST `/mails/recover`

- **Descrição:** Envia email de recuperação de senha.
- **Body:**
  - `email`: string (obrigatório)
- **Resposta:** 200 - Sucesso

#### POST `/mails/evaluate`

- **Descrição:** Envia email avisando sobre avaliação de projeto.
- **Body:**
  - `name`: string (obrigatório)
  - `email`: string (obrigatório)
  - `status`: string (obrigatório)
  - `feedback`: string
- **Resposta:** 200 - Sucesso

#### POST `/mails/recadoStakeholder`

- **Descrição:** Envia email avisando sobre o andamento do projeto para o stakeholder.
- **Body:**
  - `name`: string (obrigatório)
  - `email`: string (obrigatório)
  - `status`: string (obrigatório)
  - `feedback`: string
- **Resposta:** 200 - Sucesso

#### POST `/mails/avalieProjeto`

- **Descrição:** Envia email avisando sobre a avaliação do projeto.
- **Body:**
  - `name`: string (obrigatório)
  - `email`: string (obrigatório)
  - `projectId`: string (obrigatório)
- **Resposta:** 200 - Sucesso

---

### Outras rotas

#### GET `/getImage`

- **Descrição:** Obtem uma imagem presente em /images/subject.
- **Resposta:** 200 - Sucesso

#### POST `/priorization`

- **Descrição:** Associa uma priorização de um aluno presente em uma classe a um projeto.
- **Body:**
  - `priorizations`: array de objetos
    - `priorization`: integer
    - `projectId`: integer
  - `userId`: integer
  - `classId`: integer
- **Resposta:** 201 - Sucesso

#### POST `/assign-projects`

- **Descrição:** Associa X usuários dentro de um projeto.
- **Body:**
  - `classId`: string (UUID)
- **Resposta:** 201 - Sucesso

#### POST `/projetoTurmas`

- **Descrição:** Associa uma ou várias Turmas a um Projeto.
- **Body:**
  - `projectId`: integer
  - `classIds`: array de UUIDs
- **Resposta:** 201 - Sucesso

#### DELETE `/projetoTurmas`

- **Descrição:** Remove associação de uma ou várias Turmas a um Projeto.
- **Body:**
  - `projectId`: integer
  - `classIds`: array de UUIDs
- **Resposta:** 200 - Sucesso

#### GET `/abstract`

- **Descrição:** Listar Abstracts.
- **Resposta:** 200 - Sucesso

#### GET `/project/{projectId}/pdf`

- **Descrição:** Retorna o PDF do projeto.
- **Parâmetro de Path:**
  - `projectId`: number (obrigatório)
- **Resposta:** 200 - Sucesso

---

> **Observação:** Esta documentação foi gerada automaticamente a partir do arquivo swagger.yaml. Para detalhes completos de cada endpoint, consulte o arquivo original.
