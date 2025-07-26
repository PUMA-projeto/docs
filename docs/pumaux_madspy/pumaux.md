## **1. Objetivos da Aplicação**

Esta aplicação visa ser uma **plataforma centralizada para a gestão de problemas de usabilidade e acessibilidade**, fundamentada nas diretrizes de **Interação Humano-Computador (IHC)**. Entre seus principais objetivos estão:

* **Apoiar equipes de produto, design, desenvolvimento e QA** na **identificação, análise, categorização e acompanhamento** de problemas de usabilidade em produtos digitais.
* **Padronizar a avaliação e classificação dos problemas** com base em um **guia de acessibilidade estruturado segundo os princípios da IHC**, incluindo as **10 heurísticas de Nielsen** como parte fundamental.
* **Oferecer fontes complementares para a análise de problemas**, integrando:

  * **Documentação técnica das áreas de desenvolvimento e design**;
  * **Protótipos de alta fidelidade disponíveis no Figma**.
* **Registrar o histórico de ações e decisões**, promovendo rastreabilidade e evolução contínua das soluções aplicadas.
* **Fornecer visualizações analíticas** sobre os problemas identificados, severidade, taxa de resolução e padrões recorrentes.
* **Permitir redundância de segurança por meio da exportação e sincronização com ferramentas externas** (ex.: ClickUp), que funcionam como **backups informacionais**, sem afetar o fluxo principal de trabalho da aplicação.

---

## 2. Arquitetura

### **2.1 Visão Geral da Arquitetura**

A aplicação adota uma **arquitetura monolítica modularizada** com separação explícita entre as camadas de **apresentação**, **negócio** e **persistência**, e foi projetada para ser **flexível, portável e resiliente**.

**Princípios da arquitetura:**

* **Modularidade funcional**: cada domínio do sistema (ex.: issues, usuários, comentários) está isolado em módulos autocontidos com camadas internas (controller, service, repository).
* **Baixo acoplamento e alta coesão**, com uso sistemático de **interfaces e contratos abstratos** que permitem substituição transparente de tecnologias externas (como banco de dados, autenticação ou serviços de IA/chatbot).
* **Infraestrutura conteinerizada com Docker**, para facilitar deploy local ou remoto em serviços gratuitos.
* **Resiliência informacional**, com redundância por exportação para ferramentas externas (ClickUp, CSV), que atuam como backup informativo.

**Benefícios diretos:**

* **Troca de banco de dados com mínimo impacto**, via repositórios e contratos desacoplados;
* **Integração e troca de serviços inteligentes** (ex: chatbot, modelos de classificação) com base em interfaces implementáveis;
* **Escalabilidade vertical (modular) e horizontal (via serviços autônomos, se desejado futuramente)**.

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

## **3. Frontend**

### **3.1 Visão Geral**

O frontend da aplicação é uma **SPA (Single Page Application)** desenvolvida em **Vue 3 com TypeScript**, focada na **experiência do usuário**, responsividade e modularidade. A camada de apresentação segue o princípio de **Design-Driven Development**, priorizando usabilidade e aderência às heurísticas de IHC.

A arquitetura do frontend é baseada em três pilares:

* **Separação de responsabilidade por domínio** (ex: issues, comentários, usuários);
* **Reutilização e isolamento de componentes** com base em atomic design;
* **Abstração de serviços externos** (como API REST, autenticação e armazenamento) por meio de composables desacoplados.

A estrutura proposta permite:

* **Manutenção facilitada** por equipes diferentes (design, front e QA);
* **Testabilidade** com suporte a testes unitários e end-to-end;
* **Facilidade de migração futura** para outros frameworks/componentes de UI, se necessário.

---

### **3.2 Estrutura de Diretórios**

```bash
/src
  /assets           # Estilos globais, imagens, fontes
  /components       # Componentes reaproveitáveis (ex: Modal, Button, Badge)
  /layouts          # Estrutura base das páginas (com Header, Sidebar etc.)
  /pages            # Views principais da aplicação (ex: Dashboard, Kanban, Login)
  /modules
    /issues         # Componentes e lógica específica de problemas de usabilidade
    /comments       # Thread de comentários e formulários
    /users          # Gestão de usuários e perfis
  /composables      # Funções reutilizáveis: API, Auth, Storage
  /router           # Vue Router com guards e rotas protegidas
  /store            # Gerenciamento global de estado com Pinia
  /types            # Tipagens globais e interfaces
  /utils            # Funções utilitárias (ex: formatadores, validadores)
```

---

### **3.3 Bibliotecas e Convenções**

| Função                  | Tecnologia/Biblioteca              | Observação                                             |
| ----------------------- | ---------------------------------- | ------------------------------------------------------ |
| Framework SPA           | Vue 3 + Composition API            | Modular, reativo e escalável                           |
| Linguagem               | TypeScript                         | Tipagem estática para previsibilidade e segurança      |
| Estilização             | Tailwind CSS                       | Utilizado com design tokens customizados               |
| UI Components           | Headless UI ou shadcn (Vue port)   | Componentes acessíveis e personalizáveis               |
| State Management        | Pinia                              | Substitui Vuex com abordagem moderna                   |
| Roteamento              | Vue Router                         | Suporte a rotas aninhadas e proteção por middleware    |
| Validação de Formulário | Zod ou VeeValidate                 | Validadores reutilizáveis e tipados                    |
| Composables de serviços | `useApi`, `useAuth`, `useStorage`  | Camadas de abstração para API, autenticação e arquivos |
| Gerenciamento de sessão | JWT via localStorage ou cookies    | Autenticação persistente com refresh token opcional    |
| Testes                  | Vitest (unitários) / Cypress (e2e) | Ambiente completo de testes integrado ao CI/CD         |

---

### **3.4 Padrões de Interface e Acessibilidade**

* Interfaces criadas com base em **design system acessível**, seguindo:

  * **WCAG 2.1**;
  * **10 heurísticas de Nielsen**;
  * Contrastes e tipografia validados.
* Suporte completo à **navegação por teclado**;
* Uso de `aria-*`, `role`, e semântica adequada nos componentes;
* Feedback visual e sonoro para usuários com diferentes perfis.

---

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

## **6. Funcionalidades Principais**

---

### 🔹 **6.1 Dashboard Analytics**

**Objetivo**: Fornecer uma visão geral e analítica da saúde da usabilidade no sistema, com dados quantitativos e visuais.

**Ações disponíveis:**

* Visualização de gráficos por:

  * Severidade média por heurística
  * Distribuição de status de problemas
  * Taxa de resolução ao longo do tempo
  * Problemas por autor, módulo e heurística
* Filtros por:

  * Período
  * Heurística
  * Severidade
  * Responsável

**Usuários autorizados**: `ADMIN`, `AVALIADOR`

**Critérios funcionais:**

* Atualização em tempo real (ou próximo disso)
* Indicadores destacados (ex: % problemas críticos abertos)
* Permite exportação dos dados analíticos (CSV/JSON)

---

### 🔹 **6.2 Catálogo de Problemas (Issues)**

**Objetivo**: Permitir o cadastro, visualização, análise e acompanhamento de problemas de usabilidade.

**Ações disponíveis:**

* Criar novo problema
* Editar título, descrição, heurística e severidade
* Alterar status do problema
* Anexar arquivos (imagens, vídeos, PDFs)
* Importar em lote (CSV)
* Exportar problemas (CSV/ClickUp)

**Usuários autorizados**:

* Criação e edição: `AVALIADOR`, `ADMIN`
* Visualização: todos

**Critérios funcionais:**

* Validação por schema (ex: título obrigatório, severidade entre 0–4)
* Suporte a anexos múltiplos por problema
* Classificação obrigatória por heurística
* Registro automático no histórico (`IssueHistory`) a cada alteração

---

### 🔹 **6.3 Kanban Board**

**Objetivo**: Visualizar e gerenciar o fluxo de resolução dos problemas identificados.

**Colunas fixas**:
`Novo → Aceito → Planejado → Em Execução → Concluído`

**Ações disponíveis:**

* Arrastar cards entre colunas (drag &amp; drop)
* Alterar responsável e prazo diretamente no card
* Visualizar resumo expandido (com comentários e anexos)
* Filtrar por heurística, severidade e responsável

**Usuários autorizados**: `ADMIN`, `AVALIADOR`

**Critérios funcionais:**

* Mudança de status gera log em `IssueHistory`
* Cards com cores visuais por severidade
* Interface acessível e responsiva

---

### 🔹 **6.4 Sistema de Comentários**

**Objetivo**: Registrar e acompanhar discussões sobre problemas identificados.

**Ações disponíveis:**

* Adicionar comentários com markdown básico
* Responder em thread
* Editar e deletar próprios comentários

**Usuários autorizados**: todos os usuários logados

**Critérios funcionais:**

* Mostra autor e data de cada comentário
* Comentários organizados por ordem cronológica
* Associações automáticas ao `IssueId`

---

### 🔹 **6.5 Gestão de Usuários**

**Objetivo**: Controlar acesso, permissões e perfis de uso no sistema.

**Ações disponíveis (Admin):**

* Listar usuários e seus papéis
* Promover ou rebaixar usuários
* Remover contas inativas
* Convidar novos usuários por e-mail

**Papéis disponíveis:**

* `ADMIN`: acesso total
* `AVALIADOR`: cria, edita e analisa problemas
* `CONVIDADO`: visualiza e comenta

**Critérios funcionais:**

* Autenticação JWT com rotas protegidas
* Mudanças de role atualizadas em tempo real
* Avatar e nome visível nos comentários e dashboard

---

### 🔹 **6.6 Consulta a Materiais de Referência**

**Objetivo**: Permitir que avaliadores acessem documentação técnica e protótipos de forma integrada à análise de problemas.

**Ações disponíveis:**

* Visualizar e abrir links externos (Figma, PDFs, Documentação)
* Cadastrar novo material com tipo, título e URL

**Usuários autorizados**: `AVALIADOR`, `ADMIN`

**Critérios funcionais:**

* Acesso rápido no painel lateral ou junto aos problemas
* Validação de URLs
* Acesso rastreável via logs (opcional)

---

## **7. Fluxo de Trabalho**

O sistema adota um **fluxo sequencial estruturado** para a gestão dos problemas de usabilidade, refletido visualmente no **Kanban Board**. Cada problema percorre uma ou mais das seguintes etapas:

---

### 🔹 **Fase 1: Identificação**

&gt; **Objetivo**: Registrar um novo problema de usabilidade com base em análises, testes ou observações.

* **Responsável**: `AVALIADOR`, `ADMIN`
* **Ações permitidas**:

  * Criar novo problema (Issue)
  * Definir heurística, severidade, descrição
  * Adicionar anexos (ex: prints, vídeos)
  * Associar material de apoio (ex: Figma)
* **Status atribuído**: `NOVO`

✅ Critérios:

* Problema é salvo com status inicial `NOVO`
* Registro de `created_by` e `created_at`
* Validações obrigatórias no schema

---

### 🔹 **Fase 2: Triagem**

&gt; **Objetivo**: Revisar o problema reportado e decidir se ele será analisado ou rejeitado.

* **Responsável**: `ADMIN`, `AVALIADOR SÊNIOR` (configurável)
* **Ações permitidas**:

  * Revisar título, descrição, anexos
  * Modificar heurística ou severidade
  * Aprovar (mudar para `ACEITO`) ou deletar
* **Transição de status**:
  `NOVO → ACEITO`
  ou
  `NOVO → REMOVIDO` (via soft delete)

✅ Critérios:

* Cada mudança é registrada no `IssueHistory`
* Apenas administradores podem remover problemas

---

### 🔹 **Fase 3: Planejamento**

&gt; **Objetivo**: Atribuir responsáveis, definir prazos e organizar a resolução.

* **Responsável**: `ADMIN`
* **Ações permitidas**:

  * Definir `responsible_id`
  * Estimar prazo (`deadline`)
  * Adicionar comentários internos
  * Alterar status para `PLANEJADO`

✅ Transição válida:
`ACEITO → PLANEJADO`

---

### 🔹 **Fase 4: Execução**

&gt; **Objetivo**: Executar ajustes na interface, conteúdo ou código que resolvam o problema.

* **Responsável**: `responsável atribuído`
* **Ações permitidas**:

  * Adicionar anexos de solução
  * Atualizar descrição se necessário
  * Alterar status para `EM_EXECUCAO`
  * Marcar como `CONCLUIDO` após a resolução

✅ Transições válidas:

* `PLANEJADO → EM_EXECUCAO`
* `EM_EXECUCAO → CONCLUIDO`

⚠️ Observações:

* Toda mudança deve ter pelo menos 1 comentário ou anexo como evidência
* Apenas responsáveis ou admins podem concluir

---

### 🔹 **Fase 5: Conclusão**

&gt; **Objetivo**: Registrar a solução e disponibilizá-la para auditoria ou consulta futura.

* **Responsável**: `responsável atribuído`, `ADMIN`
* **Ações permitidas**:

  * Confirmar resolução com evidência
  * Encerrar discussão (comentários ainda permitidos)
  * Exportar problema para ClickUp, PDF ou CSV (opcional)

✅ Regras:

* Ao concluir, um snapshot do problema é registrado
* Logs completos disponíveis em `IssueHistory`

---

### 🔹 **Fase Paralela: Auditoria &amp; Histórico**

&gt; **Objetivo**: Rastrear e consultar todas as alterações feitas em um problema.

* **Acesso**: todos os papéis
* **Inclui**:

  * Alterações de status
  * Mudanças em heurística, severidade, descrição
  * Troca de responsáveis
  * Comentários e anexos

✅ Registrado automaticamente na tabela `IssueHistory`

---

## **8. Diferenciais da Aplicação**

Esta aplicação se destaca por oferecer **recursos especializados para a gestão de usabilidade**, combinando automação, metodologia formal e integração leve com ferramentas externas. Abaixo estão os principais diferenciais:

---

### 🔹 **8.1 Base Teórica Estruturada**

* A categorização dos problemas segue um **guia de acessibilidade fundamentado na área de Interação Humano-Computador (IHC)**;
* Integração das **10 heurísticas de Nielsen** como categorias obrigatórias no cadastro de problemas;
* Uso de materiais complementares (documentação técnica, Figma) como fontes formais de apoio à análise e decisão.

---

### 🔹 **8.2 Arquitetura Modular com Abstrações**

* Toda integração com serviços externos (ex: banco, armazenamento, IA) é feita por meio de **contratos abstratos**, facilitando a **troca de fornecedores** e manutenção a longo prazo;
* Suporte completo a deploy em **ambientes gratuitos e conteinerizados**, com Docker.

---

### 🔹 **8.3 Geração Automatizada de Testes com IA**

* Após um problema ser **aceito na triagem**, o sistema disponibiliza uma opção de **geração de testes unitários automatizados**;
* Um **chatbot técnico** (implementado via provedor plugável como OpenAI, HuggingFace ou local) analisa:

  * A descrição do problema;
  * A heurística afetada;
  * A severidade e contexto;
  * E propõe **testes unitários para validação da correção futura**.

**Exemplo de funcionalidade:**

```bash
[Bot] Foi detectado que este problema afeta a Heurística 4: Consistência e Padrões.
→ Sugestão de teste unitário:
- Deve garantir que todos os campos obrigatórios exibam mensagens de erro consistentes com os padrões definidos no guia de estilo da aplicação.
```

* Esses testes são apresentados ao usuário responsável, que pode:

  * Editar e confirmar a sugestão;
  * Adicionar aos registros do problema;
  * Exportar para o repositório de testes do time de QA.

---

### 🔹 **8.4 Redundância Informacional e Integrações Leves**

* A aplicação pode exportar dados para plataformas externas (ClickUp, CSV, JSON), **sem depender delas para o funcionamento interno**;
* Essa redundância visa garantir backup, rastreabilidade e relatórios de status sem quebrar o fluxo de trabalho nativo da aplicação.

---

### 🔹 **8.5 Interface Autoconsciente de UX**

* O próprio sistema é desenvolvido respeitando as heurísticas que ele cataloga;
* Isso cria uma **experiência de uso que reflete os padrões defendidos**, reforçando a consistência entre forma e função.

---

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

## **10. Segurança e Controle de Acesso**

A segurança da aplicação é projetada para garantir:

* **Autenticação confiável e extensível**
* **Permissões granulares por tipo de usuário**
* **Proteção contra ações maliciosas e uso indevido**
* **Rastreabilidade completa de ações críticas**

---

### 🔹 **10.1 Autenticação**

* Utiliza **JWT (JSON Web Token)** com assinatura HMAC (`HS256`);
* Tokens armazenados no **localStorage ou cookie HttpOnly** (configurável);
* **Refresh token opcional** com expiração configurável;
* Emissão de token realizada após login com e-mail/senha;
* Toda requisição autenticada inclui o token no header `Authorization: Bearer &lt;token&gt;`.

✅ Pode ser substituído por qualquer outro provedor (OAuth, Clerk, Supabase Auth) via interface `IAuthService`.

---

### 🔹 **10.2 Autorização e Perfis de Acesso**

| Papel       | Permissões                                                              |
| ----------- | ----------------------------------------------------------------------- |
| `ADMIN`     | Acesso total: gerenciar usuários, deletar problemas, alterar permissões |
| `AVALIADOR` | Criar e editar problemas, comentar, gerar testes com chatbot            |
| `CONVIDADO` | Visualização restrita e comentários                                     |

* Toda rota protegida verifica o papel do usuário por **middleware de roles**;
* As regras são centralizadas em uma estrutura como:

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

* Middleware de autenticação (`ensureAuthenticated`) em todas as rotas privadas;
* Middleware de autorização (`requireRole`) em ações sensíveis;
* **Rate limiting** para login e criação de problemas (evitar spam);
* **CORS configurado** para impedir requisições de domínios não autorizados;
* Uploads de arquivos com verificação de tipo e limite de tamanho.

---

### 🔹 **10.4 Logs e Auditoria**

* Toda ação crítica (edição, deleção, alteração de status, atribuições) é:

  * Registrada na tabela `IssueHistory`;
  * Associada ao usuário responsável;
  * Marcada com data e descrição da mudança.

* Logs podem ser exportados por admins em formato CSV;

* Integração futura opcional com ferramentas externas de log (ex: Logtail, Sentry).

---

### 🔹 **10.5 Proteção do Ambiente**

* Variáveis sensíveis armazenadas no `.env` e nunca versionadas;
* Tokens de API criptografados com libs como `crypto` ou `dotenv-vault`;
* Senhas armazenadas com **hashing Bcrypt** com salt seguro;
* Headers de segurança aplicados via middleware (`helmet` no Express);
* HTTPS obrigatório em produção (via proxy Nginx ou serviço de nuvem).

---