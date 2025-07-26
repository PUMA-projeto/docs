## **9. Hospedagem e Infraestrutura**

A infraestrutura da aplicação foi planejada para ser **leve, portátil e fácil de escalar**, permitindo hospedagem gratuita ou de baixo custo sem comprometer a confiabilidade do sistema. O deploy padrão utiliza **Docker e Docker Compose**, viabilizando ambientes replicáveis para desenvolvimento, homologação e produção.

---

### 🔹 **9.1 Estrutura de Contêineres (Docker)**

A aplicação é composta pelos seguintes serviços:

| Serviço         | Descrição                                                       |
| --------------- | --------------------------------------------------------------- |
| `frontend`      | SPA Vue 3 servida via Nginx                                     |
| `backend`       | API Node.js/Express com Prisma ORM                              |
| `db`            | PostgreSQL com persistência de dados via volume                 |
| `pgadmin`       | Interface de administração para o PostgreSQL                    |
| `chatbot`       | Serviço de IA local ou ponte para provedor externo via contrato |
| `reverse-proxy` | Nginx para HTTPS, proxy e redirecionamento de portas            |

**Exemplo de `docker-compose.yml`:**

```yaml
services:
  frontend:
    build: ./frontend
    ports: [ &#34;8080:80&#34; ]

  backend:
    build: ./backend
    environment:
      DATABASE_URL: postgres://appuser:password@db:5432/usabilidade
    ports: [ &#34;3000:3000&#34; ]
    depends_on: [ db ]

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: password
      POSTGRES_DB: usabilidade
    volumes:
      - pgdata:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    ports: [ &#34;5050:80&#34; ]
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin

volumes:
  pgdata:
```

---

### 🔹 **9.2 Serviços de Hospedagem Gratuita Recomendados**

| Serviço          | Uso Ideal                            | Observações                                              |
| ---------------- | ------------------------------------ | -------------------------------------------------------- |
| **Render**       | Backend + banco ou frontend separado | Suporte a deploy automático via GitHub                   |
| **Railway**      | Banco de dados + Backend             | Fácil de usar, plano gratuito com boa tolerância         |
| **Vercel**       | Frontend (Vue)                       | Ideal para SPAs com roteamento estático                  |
| **Fly.io**       | Full stack com Docker                | Suporte a deploy de projetos Dockerizados, banco incluso |
| **Supabase**     | PostgreSQL + Auth + Storage          | Pode ser usado como base da aplicação se desejado        |
| **Backblaze B2** | Armazenamento de arquivos            | Alternativa gratuita ao S3 para anexos                   |

---

### 🔹 **9.3 Estratégia de Backup e Redundância**

* **Banco de dados**: backup automático via cronjob + export manual via `pg_dump`
* **Anexos**: armazenamento em buckets com replicação local se necessário
* **Histórico de Issues**: persistido em tabela separada (`IssueHistory`)
* **Exportação externa**: exportação dos dados para CSV ou integração com ClickUp
* **Ambiente .env**: armazenado com criptografia e versionamento protegido no CI

---

### 🔹 **9.4 CI/CD com GitHub Actions**

* **Build e Testes**:

  * `Vitest` para frontend
  * `Jest` ou `Supertest` para backend
* **Deploy automático**:

  * Para Render, Railway ou Fly.io via push em branch principal
* **Lint e validações de schema** em cada PR
* **Notificações de erro** via e-mail ou logs persistentes no contêiner

---
