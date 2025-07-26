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
