## 2. Arquitetura

### **2.1 Visão Geral da Arquitetura**

A aplicação adota uma **arquitetura monolítica modularizada** com separação explícita entre as camadas de **apresentação**, **negócio** e **persistência**, e foi projetada para ser **flexível, portável e resiliente**.

**Princípios da arquitetura:**

- **Modularidade funcional**: cada domínio do sistema (ex.: issues, usuários, comentários) está isolado em módulos autocontidos com camadas internas (controller, service, repository).
- **Baixo acoplamento e alta coesão**, com uso sistemático de **interfaces e contratos abstratos** que permitem substituição transparente de tecnologias externas (como banco de dados, autenticação ou serviços de IA/chatbot).
- **Infraestrutura conteinerizada com Docker**, para facilitar deploy local ou remoto em serviços gratuitos.
- **Resiliência informacional**, com redundância por exportação para ferramentas externas (ClickUp, CSV), que atuam como backup informativo.

**Benefícios diretos:**

- **Troca de banco de dados com mínimo impacto**, via repositórios e contratos desacoplados;
- **Integração e troca de serviços inteligentes** (ex: chatbot, modelos de classificação) com base em interfaces implementáveis;
- **Escalabilidade vertical (modular) e horizontal (via serviços autônomos, se desejado futuramente)**.

---

### **2.2 Tecnologias por Camada**

| **Camada**          | **Tecnologia**                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| **Frontend**        | Vue 3, TypeScript, Tailwind CSS, Pinia, Vue Router, Vite                                          |
| **Backend**         | Node.js, Express, **Prisma ORM** (substituível por qualquer driver via abstração de repositórios) |
| **Negócio**         | Serviços desacoplados baseados em **interfaces de domínio (ex: `IIssueService`)**                 |
| **Banco de Dados**  | PostgreSQL, com possível substituição por MySQL ou SQLite via Prisma                              |
| **Autenticação**    | JWT com middlewares de roles; possível troca por OAuth2, Supabase Auth, Clerk etc.                |
| **Chatbot/IA**      | Integração com provedores via **contrato `IChatbotService`** (ex: OpenAI, HuggingFace, local)     |
| **Armazenamento**   | Abstração `IStorageService` para alternar entre local, Supabase Storage, Backblaze, S3            |
| **CI/CD**           | GitHub Actions com ambientes separados por branch                                                 |
| **Containerização** | Docker + docker-compose (com volumes nomeados, `.env`, rede interna e saúde de serviços)          |

---
