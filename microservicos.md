# Definição das funcionalidades básicas do protótipo

## Objetivo: criar uma aplicação web combinando microserviços, arquitetura orientada a eventos e arquitetura limpa. 

## Definir as caractéristicas básicas de cada arcabouço

1. Identificar quais são as caraterísticas básicas e essencias de uma aplicação mínima usando os princípios de microserviços. 

2. Quais são os principais componentes que devem ser implementadados em uma arquitetura orientada a eventos? 

3. Quais os os princípios da arquitetura limpa e quais são os componentes básicos que devem ser implementados? 

## Escolher um domínio genérico para a aplicação

Qual seria o domínio que poderíamos escolher para implementar uma aplicação web com as seguintes features básicas: 

- F1. Controle de autenticação e autorização
- F2. Dashboard de usuário
- F3. Definir um CRUD simples para cada usuário da aplicação
- F4. Definir eventos críticos da aplicação
- F5. Definir uma feature de administração de usuários da aplicação

## Conjunto Básico de Features para o 1º Protótipo

**Entendendo o Trabalho**

O objetivo central do trabalho é demonstrar a viabilidade de combinar microsserviços, arquitetura orientada a eventos e arquitetura limpa em um projeto real. O protótipo deve servir como uma prova de conceito, validando os benefícios dessas abordagens e identificando os desafios práticos.

**Features Essenciais para o Protótipo**

Considerando os objetivos do trabalho, as seguintes features são essenciais para o primeiro protótipo:

1. **Microsserviços Core:**
   * **Serviço de Usuário:**
     * Cadastro de usuários
     * Autenticação
     * Autorização
     * Gestão de perfis
   * **Serviço de Produtos:**
     * Cadastro de produtos
     * Gestão de estoque
     * Catálogo de produtos
   * **Serviço de Pedidos:**
     * Criação de pedidos
     * Processamento de pagamentos
     * Gestão do fluxo de pedidos (criado, confirmado, enviado, entregue)

2. **Arquitetura Orientada a Eventos:**
   * **Bus de Eventos:**
     * Publicação de eventos (e.g., usuário cadastrado, pedido criado)
     * Assinatura de eventos por outros serviços
   * **Eventos-chave:**
     * Usuário cadastrado
     * Pedido criado
     * Pagamento confirmado
     * Produto adicionado ao carrinho

3. **Arquitetura Limpa:**
   * **Camadas bem definidas:**
     * Entidades: Representam os conceitos do domínio (usuário, produto, pedido)
     * Use Cases: Encapsulam a lógica de negócio (criar pedido, atualizar estoque)
     * Adapters: Interagem com o mundo externo (bancos de dados, serviços externos)
   * **Baixo acoplamento:**
     * Cada microsserviço deve ter suas próprias responsabilidades e depender o mínimo possível de outros serviços.

4. **Infraestrutura Básica:**
   * **Contêinerização:** Utilizar Docker para encapsular os microsserviços?
   * **Banco de dados:** Escolher um banco de dados relacional (PostgreSQL, MySQL) ou não relacional (MongoDB) para cada microsserviço, de acordo com suas necessidades.
   * **Bus de mensagens:** Utilizar uma ferramenta como RabbitMQ ou Kafka para implementar o bus de eventos.

**Features Adicionais (Opcionais):**

* **Monitoramento:** Implementar ferramentas de monitoramento para acompanhar o desempenho dos microsserviços.
* **Log:** Implementar um sistema de log centralizado para facilitar a depuração.
* **Testes automatizados:** Criar testes unitários, de integração e end-to-end para garantir a qualidade do código.
* **Documentação:** Documentar a arquitetura, os microsserviços e os fluxos de eventos.

**Considerações Adicionais:**

* **Simplicidade:** O foco inicial deve ser em demonstrar a viabilidade da arquitetura, evitando complexidades desnecessárias.
* **Escalabilidade:** O protótipo deve ser projetado para ser facilmente escalável, adicionando novos microsserviços e aumentando a capacidade dos existentes.
* **Resiliência:** Implementar mecanismos de falha e recuperação para garantir a disponibilidade do sistema.
