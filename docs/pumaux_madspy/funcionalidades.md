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
