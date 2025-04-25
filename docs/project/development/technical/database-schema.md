# Banco de Dados

## 1. Tabelas

### 1.1. Knowledge_Area
Tabela que armazena áreas de conhecimento.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| knowledgeAreaId    | INTEGER  | Identificador único para a área de conhecimento (Primary Key). |
| knowledgeArea      | STRING   | Nome da área de conhecimento (Unique).         |
| deleted            | BOOLEAN  | Indica se o registro está excluído.            |

### 1.2. Subarea
Tabela que armazena subáreas relacionadas às áreas de conhecimento.

| Campo              | Tipo     | DescriçFão                                      |
|--------------------|----------|------------------------------------------------|
| subAreaId          | INTEGER  | Identificador único para a subárea (Primary Key). |
| knowledgeAreaId    | INTEGER  | Referência para a área de conhecimento (Foreign Key). |
| description        | STRING   | Descrição da subárea (Unique).                 |
| deleted            | BOOLEAN  | Indica se o registro está excluído.            |

**Restrições:**
- **Unique Constraint:** SUBAREA_UK garante que não existam subáreas duplicadas para a mesma área de conhecimento.

### 1.3. Subject
Tabela que armazena disciplinas.

| Campo                  | Tipo     | Descrição                                      |
|------------------------|----------|------------------------------------------------|
| subjectId              | INTEGER  | Identificador único para a disciplina (Primary Key). |
| name                   | STRING   | Nome da disciplina (Unique).                  |
| acronym                | STRING   | Acrônimo da disciplina.                       |
| ImageHashName          | STRING   | Nome hash da imagem da disciplina.            |
| subjectGeneralObjective| STRING   | Objetivo geral da disciplina.                 |
| courseSyllabus         | STRING   | Ementa da disciplina.                         |
| creatorUserId          | INTEGER  | Referência ao usuário que criou a disciplina. |
| deleted                | BOOLEAN  | Indica se o registro está excluído.           |

### 1.4. Identifies
Tabela que estabelece a relação entre subáreas e disciplinas.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| subAreaId          | INTEGER  | Referência para a subárea (Foreign Key).       |
| subjectId          | INTEGER  | Referência para a disciplina (Foreign Key).    |

**Restrições:**
- **Chave Primária Composta:** (subAreaId, subjectId).
- **Unique Constraint:** identifies_UK.

### 1.5. Teacher
Tabela que armazena informações dos professores.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| userId             | INTEGER  | Referência para o usuário (Foreign Key).       |
| regNumber          | STRING   | Número de registro do professor (Primary Key). |

### 1.6. Student
Tabela que armazena informações dos estudantes.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| userId             | INTEGER  | Referência para o usuário (Foreign Key).       |
| regNumber          | STRING   | Número de registro do estudante (Primary Key). |
| softSkills         | STRING   | Soft skills do estudante.                      |

### 1.7. Semester
Tabela que armazena informações dos semestres.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| semesterId         | INTEGER  | Identificador único para o semestre (Primary Key). |
| subjectId          | INTEGER  | Referência para a disciplina (Foreign Key).    |
| year               | STRING   | Ano do semestre.                               |
| semester           | ENUM     | Período do semestre (1, 2).                    |
| status             | ENUM     | Status do semestre (AD, CD).                   |
| deleted            | BOOLEAN  | Indica se o registro está excluído.            |

**Restrições:**
- **Unique Constraint:** SEMESTRE_UK.

### 1.8. Lectures
Tabela que estabelece a relação entre professores e disciplinas.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| regNumber          | STRING   | Referência para o professor (Foreign Key).     |
| subjectId          | INTEGER  | Referência para a disciplina (Foreign Key).    |

**Restrições:**
- **Chave Primária Composta:** (regNumber, subjectId).

### 1.9. Project
Tabela que armazena informações dos projetos.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| projectId          | INTEGER  | Identificador único para o projeto (Primary Key). |
| userId             | INTEGER  | Referência para o usuário (Foreign Key).       |
| subjectId          | INTEGER  | Referência para a disciplina (Foreign Key).    |
| semesterId         | INTEGER  | Referência para o semestre (Foreign Key).      |
| categoriaId        | INTEGER  | Referência para a categoria (Foreign Key).     |
| subcategoria       | STRING   | Subcategoria do projeto.                       |
| name               | STRING   | Nome do projeto.                               |
| expectedResult     | STRING   | Resultado esperado do projeto.                 |
| feedback           | STRING   | Feedback para o projeto.                       |
| problem            | STRING   | Problema abordado pelo projeto.                |
| status             | ENUM     | Status do projeto (SB, RL, etc.).              |
| pdf                | STRING   | Caminho para o PDF do projeto.                 |
| deleted            | BOOLEAN  | Indica se o registro está excluído.            |

### 1.10. Peer_Review
Tabela que armazena informações de revisões por pares.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| peerReviewId       | INTEGER  | Identificador único para a revisão por pares (Primary Key). |
| reviewSolicitationId | INTEGER | Referência para a solicitação de revisão (Foreign Key). |
| reviewerId         | INTEGER  | Referência para o revisor (Foreign Key).       |
| projectId          | INTEGER  | Referência para o projeto (Foreign Key).       |

### 1.11. Peer_Grade
Tabela que armazena notas de revisões por pares.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| peerGradeId        | INTEGER  | Identificador único para a nota por pares (Primary Key). |
| peerReviewId       | INTEGER  | Referência para a revisão por pares (Foreign Key). |
| reviewedId         | STRING   | Referência para o estudante avaliado (Foreign Key). |
| reviewMicroId      | INTEGER  | Referência para a micro competência (Foreign Key). |
| grade              | DECIMAL  | Nota atribuída pelo revisor.                   |

**Restrições:**
- **Unique Constraint:** Peer_Grade_UK.

### 1.12. Macro_Competence
Tabela que armazena macro competências.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| macroCompetenceId  | INTEGER  | Identificador único para a macro competência (Primary Key). |
| name               | STRING   | Nome da macro competência.                     |
| description        | STRING   | Descrição da macro competência.                |
| creatorId          | INTEGER  | Referência para o criador (Foreign Key).       |
| type               | ENUM     | Tipo da competência (template, etc.).          |

### 1.13. Micro_Competence
Tabela que armazena micro competências.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| microCompetenceId  | INTEGER  | Identificador único para a micro competência (Primary Key). |
| name               | STRING   | Nome da micro competência.                     |
| description        | STRING   | Descrição da micro competência.                |
| macroCompetenceId  | INTEGER  | Referência para a macro competência (Foreign Key). |

### 1.14. Keyword
Tabela que armazena palavras-chave.

| Campo              | Tipo     | Descrição                                      |
|--------------------|----------|------------------------------------------------|
| keywordId          | INTEGER  | Identificador único para a palavra-chave (Primary Key). |
| keyword            | STRING   | A própria palavra-chave.                       |
| psp                | STRING   | PSP associado à palavra-chave.                 |
| deleted            | BOOLEAN  | Indica se o registro está excluído.            |

## Histórico de Revisões

| Data       | Versão | Alterações                        | Autores |
|------------|--------|-----------------------------------|---------|
| 25/04/2025 | 0.1    | Adição do esquema do banco de dados | [Mateus Vieira](https://github.com/matix0) |

[← Voltar para a Página Principal](../../../index.md)
