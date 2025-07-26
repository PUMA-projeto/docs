# **10. Segurança e Controle de Acesso**

A segurança da aplicação é projetada para garantir:

- **Autenticação confiável e extensível**
- **Permissões granulares por tipo de usuário**
- **Proteção contra ações maliciosas e uso indevido**
- **Rastreabilidade completa de ações críticas**

---

### 🔹 **10.1 Autenticação**

- Utiliza **JWT (JSON Web Token)** com assinatura HMAC (`HS256`);
- Tokens armazenados no **localStorage ou cookie HttpOnly** (configurável);
- **Refresh token opcional** com expiração configurável;
- Emissão de token realizada após login com e-mail/senha;
- Toda requisição autenticada inclui o token no header `Authorization: Bearer &lt;token&gt;`.

✅ Pode ser substituído por qualquer outro provedor (OAuth, Clerk, Supabase Auth) via interface `IAuthService`.

---

### 🔹 **10.2 Autorização e Perfis de Acesso**

| Papel       | Permissões                                                              |
| ----------- | ----------------------------------------------------------------------- |
| `ADMIN`     | Acesso total: gerenciar usuários, deletar problemas, alterar permissões |
| `AVALIADOR` | Criar e editar problemas, comentar, gerar testes com chatbot            |
| `CONVIDADO` | Visualização restrita e comentários                                     |

- Toda rota protegida verifica o papel do usuário por **middleware de roles**;
- As regras são centralizadas em uma estrutura como:

```ts
const Permissions = {
  issues: {
    create: [&#39;ADMIN&#39;, &#39;AVALIADOR&#39;],
    delete: [&#39;ADMIN&#39;],
    view: [&#39;ADMIN&#39;, &#39;AVALIADOR&#39;, &#39;CONVIDADO&#39;],
  },
};
```

---

### 🔹 **10.3 Proteção de Rotas e Dados**

- Middleware de autenticação (`ensureAuthenticated`) em todas as rotas privadas;
- Middleware de autorização (`requireRole`) em ações sensíveis;
- **Rate limiting** para login e criação de problemas (evitar spam);
- **CORS configurado** para impedir requisições de domínios não autorizados;
- Uploads de arquivos com verificação de tipo e limite de tamanho.

---

### 🔹 **10.4 Logs e Auditoria**

- Toda ação crítica (edição, deleção, alteração de status, atribuições) é:

  - Registrada na tabela `IssueHistory`;
  - Associada ao usuário responsável;
  - Marcada com data e descrição da mudança.

- Logs podem ser exportados por admins em formato CSV;

- Integração futura opcional com ferramentas externas de log (ex: Logtail, Sentry).

---

### 🔹 **10.5 Proteção do Ambiente**

- Variáveis sensíveis armazenadas no `.env` e nunca versionadas;
- Tokens de API criptografados com libs como `crypto` ou `dotenv-vault`;
- Senhas armazenadas com **hashing Bcrypt** com salt seguro;
- Headers de segurança aplicados via middleware (`helmet` no Express);
- HTTPS obrigatório em produção (via proxy Nginx ou serviço de nuvem).

---
