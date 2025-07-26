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
