## **5. Estrutura de Dados**

A modelagem segue os princípios de:

* **Normalização até 3FN**, evitando redundância;
* **Relacionamentos explícitos com integridade referencial**;
* **Rastreabilidade por tabelas auxiliares (ex: histórico de alterações)**;
* **Facilidade de indexação para filtros e análises (ex: heurísticas, severidade)**.

---

### **5.1 Entidades Principais**

---

#### 🔹 `User` (usuários)

| Campo        | Tipo                                     | Restrições                    |
| ------------ | ---------------------------------------- | ----------------------------- |
| `id`         | UUID                                     | PK                            |
| `name`       | String                                   | NOT NULL                      |
| `email`      | String                                   | UNIQUE, NOT NULL              |
| `role`       | Enum (`ADMIN`, `AVALIADOR`, `CONVIDADO`) | NOT NULL                      |
| `avatar_url` | String (URL)                             | Opcional                      |
| `created_at` | Timestamp                                | Default now()                 |
| `updated_at` | Timestamp                                | Atualizado a cada modificação |

---

#### 🔹 `Issue` (problemas de usabilidade)

| Campo            | Tipo                                                          | Restrições                      |
| ---------------- | ------------------------------------------------------------- | ------------------------------- |
| `id`             | UUID                                                          | PK                              |
| `title`          | String                                                        | NOT NULL                        |
| `description`    | Text                                                          | NOT NULL                        |
| `heuristic`      | Enum (`H1` a `H10`)                                           | Base nas heurísticas de Nielsen |
| `severity`       | Int (0–4)                                                     | NOT NULL                        |
| `status`         | Enum (`NOVO`, `ACEITO`, `PLANEJADO`, `EXECUCAO`, `CONCLUIDO`) | NOT NULL                        |
| `reported_by_id` | UUID (FK User)                                                | NOT NULL                        |
| `responsible_id` | UUID (FK User)                                                | Opcional                        |
| `deadline`       | Date                                                          | Opcional                        |
| `created_at`     | Timestamp                                                     | Default now()                   |
| `updated_at`     | Timestamp                                                     | Atualizado a cada alteração     |

---

#### 🔹 `Comment` (comentários)

| Campo        | Tipo            | Restrições    |
| ------------ | --------------- | ------------- |
| `id`         | UUID            | PK            |
| `issue_id`   | UUID (FK Issue) | NOT NULL      |
| `user_id`    | UUID (FK User)  | NOT NULL      |
| `content`    | Text            | NOT NULL      |
| `created_at` | Timestamp       | Default now() |

---

#### 🔹 `Attachment` (anexos)

| Campo         | Tipo            | Restrições    |
| ------------- | --------------- | ------------- |
| `id`          | UUID            | PK            |
| `issue_id`    | UUID (FK Issue) | NOT NULL      |
| `filename`    | String          | NOT NULL      |
| `url`         | String (URL)    | NOT NULL      |
| `uploaded_by` | UUID (FK User)  | NOT NULL      |
| `uploaded_at` | Timestamp       | Default now() |

---

#### 🔹 `IssueHistory` (log de alterações de problemas)

| Campo        | Tipo            | Restrições                             |
| ------------ | --------------- | -------------------------------------- |
| `id`         | UUID            | PK                                     |
| `issue_id`   | UUID (FK Issue) | NOT NULL                               |
| `changed_by` | UUID (FK User)  | NOT NULL                               |
| `field`      | String          | Campo alterado (ex: `status`, `title`) |
| `old_value`  | Text            | Valor anterior                         |
| `new_value`  | Text            | Valor novo                             |
| `changed_at` | Timestamp       | Default now()                          |

---

#### 🔹 `ReferenceMaterial` (documentos técnicos e protótipos)

| Campo      | Tipo                                       | Restrições    |
| ---------- | ------------------------------------------ | ------------- |
| `id`       | UUID                                       | PK            |
| `title`    | String                                     | NOT NULL      |
| `type`     | Enum (`DOCUMENTO`, `FIGMA`, `LINK`, `PDF`) | NOT NULL      |
| `url`      | String (URL)                               | NOT NULL      |
| `added_by` | UUID (FK User)                             | NOT NULL      |
| `added_at` | Timestamp                                  | Default now() |

---

### **5.2 Relacionamentos**

```plaintext
User 1 ────&lt; Issue.reported_by
User 1 ────&lt; Issue.responsible_id
User 1 ────&lt; Comment.user_id
User 1 ────&lt; Attachment.uploaded_by
User 1 ────&lt; IssueHistory.changed_by
User 1 ────&lt; ReferenceMaterial.added_by

Issue 1 ────&lt; Comment.issue_id
Issue 1 ────&lt; Attachment.issue_id
Issue 1 ────&lt; IssueHistory.issue_id
```

---
