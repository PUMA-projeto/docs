## **4. Backend**

### **4.1 Visão Geral**

O backend da aplicação é construído com **Node.js** e **Express**, estruturado em uma arquitetura **modular em camadas**, com responsabilidade clara para **controller, service e repository**. Utiliza **Prisma ORM** para comunicação com o banco de dados PostgreSQL, e adota **contratos de abstração (interfaces)** para garantir flexibilidade e independência de implementação.

Os objetivos principais da arquitetura do backend são:

* **Escalabilidade vertical** por domínio (ex: `issues`, `users`);
* **Flexibilidade na substituição de ferramentas** como bancos de dados, serviços de IA, autenticação ou armazenamento;
* **Facilidade de testes e manutenção**, por meio de injeção de dependências e camadas bem isoladas;
* **Segurança robusta com autenticação baseada em JWT e controle de permissões por perfil**.

---

### **4.2 Organização Modular**

Estrutura de diretórios:

```bash
/src
  /modules
    /issues
      issue.controller.ts
      issue.service.ts
      issue.repository.ts
      issue.routes.ts
      issue.schema.ts
      dto/
      interfaces/
    /users
    /comments
    /attachments
  /core
    /auth              # JWT middleware, role guard, hash utils
    /config            # Variáveis de ambiente, banco, etc.
    /exceptions        # Custom error handling
    /middlewares       # Express middlewares
    /services          # Serviços transversais (chatbot, storage)
    /interfaces        # Interfaces comuns e contratos
    /utils             # Funções auxiliares e helpers
```

---

### **4.3 Contratos Abstratos (Interfaces)**

Para garantir desacoplamento de implementações específicas, a arquitetura define contratos para:

| Serviço/Componente | Interface          | Finalidade                                                         |
| ------------------ | ------------------ | ------------------------------------------------------------------ |
| Banco de dados     | `IIssueRepository` | Permite troca do ORM ou banco mantendo a lógica de negócio intacta |
| Autenticação       | `IAuthService`     | Permite alternar entre JWT, OAuth, Supabase Auth, Clerk, etc.      |
| Armazenamento      | `IStorageService`  | Suporte a local, Supabase, AWS S3, Backblaze, etc.                 |
| Chatbot/IA         | `IChatbotService`  | Permite alternar entre OpenAI, HuggingFace, ou modelos locais      |
| Logger             | `ILoggerService`   | Troca entre Winston, Pino, Logtail, etc.                           |

Exemplo de interface para repositório:

```ts
export interface IIssueRepository {
  create(issue: CreateIssueDTO): Promise&lt;Issue&gt;;
  findById(id: string): Promise&lt;Issue | null&gt;;
  update(id: string, data: UpdateIssueDTO): Promise&lt;Issue&gt;;
  delete(id: string): Promise&lt;void&gt;;
  findByFilters(filters: IssueFilterDTO): Promise&lt;Issue[]&gt;;
}
```

---

### **4.4 Middlewares e Segurança**

| Recurso                       | Descrição                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------- |
| **Autenticação JWT**          | Emissão e verificação de tokens, com renovação opcional                      |
| **Controle de Acesso**        | Middleware por role (Admin, Avaliador, Convidado, etc.)                      |
| **Validação de entrada**      | Zod ou Joi, com validações de schema para todas as rotas                     |
| **Rate Limit e CORS**         | Proteção contra abusos e políticas de origem cruzada                         |
| **Logger**                    | Logs estruturados para acesso, erros e requisições (com contexto de usuário) |
| **Rastreamento de auditoria** | Persistência de ações sensíveis no banco (`issue_history`)                   |

---
