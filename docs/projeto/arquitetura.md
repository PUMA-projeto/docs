## Arquitetura do Sistema PUMA

A arquitetura do sistema PUMA foi projetada para ser **modular, escalável e resiliente**, integrando múltiplos serviços e camadas de segurança, conforme ilustrado no diagrama acima e detalhado na documentação técnica do projeto.

### Visão Geral

O acesso ao sistema é realizado por meio de domínios distintos (ex: `api-test.pumapbl.com` e `test.pumapbl.com`), protegidos por **Cloudflare** para segurança e performance. As requisições passam por um **proxy NGINX**, que atua como ponto de entrada único, roteando o tráfego para os serviços apropriados:

- **API Gateway**: Responsável por autenticação, autorização e orquestração das chamadas para os microserviços internos.
- **Serviços de Negócio**: Incluem UserService, ProjectService, NotificationService e ClassService, cada um responsável por um domínio funcional do sistema.
- **Serviço de Arquivos Estáticos**: Gerencia e serve arquivos estáticos (frontend, assets, documentação, etc.).
- **Banco de Dados**: Cada serviço possui seu próprio schema dedicado (ex: `userservice_db`, `projectservice_db`), promovendo isolamento e segurança dos dados.

### Princípios Arquiteturais

- **Modularidade funcional**: Cada domínio do sistema é isolado em módulos autocontidos, com camadas internas (controller, service, repository), facilitando manutenção e evolução.
- **Baixo acoplamento e alta coesão**: Uso sistemático de interfaces e contratos abstratos, permitindo substituição transparente de tecnologias externas (banco de dados, autenticação, IA/chatbot).
- **Infraestrutura conteinerizada**: Utilização de Docker e Docker Compose para ambientes replicáveis e portáveis, tanto para desenvolvimento quanto produção.
- **Segurança**: Autenticação baseada em JWT, controle de acesso por perfil, proteção contra abusos (rate limit, CORS) e logs de auditoria para rastreabilidade.
- **Resiliência e redundância**: Backup automático dos bancos, exportação de dados para plataformas externas (ClickUp, CSV), e replicação de anexos.

### Tecnologias por Camada

| Camada         | Tecnologias principais                                                                 |
|--------------- |--------------------------------------------------------------------------------------|
| Frontend       | Vue 3, TypeScript, Tailwind CSS, Pinia, Vue Router, Vite                             |
| Backend        | Node.js, Express, Prisma ORM (substituível por outros via abstração de repositórios) |
| Negócio        | Serviços desacoplados baseados em interfaces de domínio                              |
| Banco de Dados | PostgreSQL (possível troca por MySQL/SQLite via Prisma)                             |
| Autenticação   | JWT (com possibilidade de OAuth2, Supabase Auth, Clerk, etc.)                        |

### Fluxo de Dados e Componentes

1. **Usuário** acessa o sistema via navegador, passando pelo Cloudflare.
2. O **NGINX Proxy** direciona a requisição para o API Gateway ou para o serviço de arquivos estáticos.
3. O **API Gateway** valida autenticação e repassa a requisição ao serviço de negócio correspondente.
4. Cada **serviço** acessa seu schema de banco de dados dedicado, garantindo isolamento.
5. Respostas e arquivos estáticos são servidos de volta ao usuário, sempre protegidos por camadas de segurança.

### Benefícios

- **Escalabilidade**: Possibilidade de escalar serviços de forma independente.
- **Portabilidade**: Deploy facilitado em ambientes cloud ou on-premise, com suporte a hospedagem gratuita.
- **Manutenção**: Estrutura modular e contratos abstratos facilitam evolução e troca de tecnologias.
- **Segurança e Confiabilidade**: Camadas de proteção, backup e logs garantem integridade e disponibilidade.
