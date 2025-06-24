# **ERP – Conceito, Implantação e Gestão**  

## **O que é um ERP?**  
**Definição:**  
> *"Sistema integrado que gerencia processos empresariais em tempo real."*  

**Principais Características:**  
✔ Integração de dados  
✔ Automação de processos  
✔ Tomada de decisão baseada em dados  

**Exemplos:** SAP, Oracle, TOTVS, MV, E-SIG.  

## **Benefícios do ERP**  
- **Redução de custos** (💰)  
- **Eficiência operacional** (⚙️)  
- **Visão unificada** (📊)  
- **Conformidade fiscal** (📑)  

## **Módulos Comuns de um ERP**  
**Áreas mais comuns:**  
| Área          | Exemplos de Funcionalidades       |  
|---------------|-----------------------------------|  
| Financeiro    | Contas a pagar, fluxo de caixa    |  
| Vendas        | Pedidos, CRM                      |  
| Estoque       | Controle de entrada/saída         |  
| RH            | Folha de pagamento, recrutamento  |  


## **Etapas de Implantação (Visão Geral)**  
**Fluxograma simplificado:**  
1. Planejamento  
2. Seleção do ERP  
3. Preparação  
4. Implementação  
5. Treinamento  
6. Go-Live  
7. Pós-implantação  

## **Fase 1 – Planejamento**  
**Checklist:**  
- [ ] Definir objetivos  
- [ ] Mapear processos atuais  
- [ ] Formar comitê de projeto  

**Dica:** *"Sem planejamento, 70% das implantações falham."*  

A fase de planejamento é a **base crítica** que determina o destino do projeto. Segundo a Panorama Consulting, 70% das falhas em implantações de ERP estão ligadas a deficiências nesta etapa. Vamos desconstruir cada elemento com profundidade estratégica:


### **1. Definição de Objetivos (O "Porquê" do Projeto)**  
 **Metodologia SMART**  
| Letra | Critério          | Exemplo Concreto para ERP              |
|-------|-------------------|----------------------------------------|
| S     | Específico        | "Reduzir tempo de fechamento fiscal em 30%" |
| M     | Mensurável        | "Diminuir custos operacionais em R$ 2,5 mi/ano" |
| A     | Alcançável        | "Implementar módulo financeiro em 6 meses" |
| R     | Relevante         | "Alinhado à estratégia de expansão para 3 novos países" |
| T     | Temporal          | "Concluir Go-Live até Q2/2025"         |

**Ferramenta Complementar:**  
▶ **BSC (Balanced Scorecard):** Alinhe objetivos do ERP às 4 perspectivas:  
- Financeira  
- Clientes  
- Processos Internos  
- Aprendizado organizacional  


### **2. Mapeamento de Processos Atuais (AS-IS)**  
**Técnicas Avançadas:**  
1. **Value Stream Mapping**  
   - Identificar desperdícios em fluxos de valor  
   - Exemplo: 40% do tempo da equipe de compras com aprovações manuais  

2. **SIPOC (Fornecedores-Inputs-Processos-Outputs-Clientes)**  
   - Mapear relações críticas:  
     *Input → Processo → Output*  
     *Ex.: Pedido do cliente (input) → Separação no estoque (processo) → Entrega (output)*  

3. **Matriz RACI para Donos de Processo**  
   | Processo          | Responsible | Accountable | Consulted | Informed |  
   |-------------------|-------------|-------------|-----------|----------|  
   | Faturamento       | Assistente  | Gerente     | Fiscal    | Logística|  

**Ferramentas Visuais:**  
- Bizagi Modeler  

### **3. Formação do Comitê de Projeto**  
**Estrutura Ideal (Multi-disciplinar)**  

**C-Level**  
- **Patrocinador Executivo:** CEO/CFO (aprova orçamentos)  
- **Gerente de Projeto:** PMO experiente em ERP  

**Líderes Funcionais**  
- TI (Arquiteto de Soluções)  
- Operações (Especialista em Processos)  
- RH (Gestor de Mudança Organizacional)  

**Nível Tático**  
- "Embaixadores" por área (usuários-chave operacionais)  
- Consultores externos (para gaps de conhecimento)  

**Governança:**  
- Reuniões quinzenais de alinhamento  
- Matriz de decisão (o que o comitê pode decidir vs. escalar)  

### **Checklist Expandido de Planejamento**  

**Análise Estratégica**  
- [ ] SWOT do projeto (Forças/Fraquezas/Oportunidades/Ameaças)  
- [ ] Benchmarking com concorrentes (quais ERPs eles usam?)  

**Aspectos Técnicos**  
- [ ] Avaliação de legado tecnológico (quais sistemas serão desativados?)  
- [ ] Pré-requisitos de infraestrutura (cloud/on-premise)  

**Gestão de Mudança**  
- [ ] Pesquisa de clima sobre resistência à mudança  
- [ ] Plano de comunicação para diferentes stakeholders  

### **Riscos Críticos e Mitigações**  

| Risco                          | Probabilidade | Impacto | Mitigação                              |
|--------------------------------|---------------|---------|----------------------------------------|
| Subestimação de custos         | Alta          | Grave   | Criar reserva de 15-20% do orçamento   |
| Resistência dos usuários       | Média-Alta    | Crítico | Envolvimento early-stage + gamificação |
| Escopo crescente ("Scope Creep")| Alta          | Grave   | Congelar requisitos após fase de blueprint |


### **Cronograma de Planejamento Detalhado**  

| Atividade                     | Duração   | Entregáveis                          |
|-------------------------------|-----------|--------------------------------------|
| Workshop de definição de objetivos | 2 semanas | Documento de escopo assinado         |
| Mapeamento AS-IS              | 4 semanas | Fluxogramas + matriz SIPOC           |
| Avaliação de fornecedores      | 3 semanas | Scorecard comparativo (SAP vs Oracle)|
| Planejamento de recursos       | 2 semanas | Alocação de equipe + orçamento       |


### **Ferramentas Recomendadas**  
1. **Project Management:** MS Project / Jira  
2. **Gestão de Requisitos:** IBM DOORS / Jama Connect  
3. **Collaboration:** Confluence / Notion  

## **Fase 2 – Seleção do ERP**  
**Comparativo:**  
| Critério       | SAP    | TOTVS  | A      | B      | C      |  
|----------------|--------|--------|--------|--------|--------|  
| Custo          | Alto   | Médio  | Baixo  | Médio  | Baixo   |  
| Customização   | Complexa | Moderada | Fácil |Moderada | Fácil |  

A seleção do ERP é uma decisão estratégica que impactará a empresa por 5-10 anos. Este guia detalha um **método sistemático** para avaliação, com critérios técnicos, financeiros e operacionais.  

### **1. Critérios Essenciais para Seleção**  
**Matriz de Avaliação Ponderada**  
*(Nota: Adapte os pesos conforme prioridades da sua empresa)*  

| Critério               | Peso (%) | SAP  | TOTVS | Oracle | A         | B    |
|------------------------|----------|------|-------|--------|-----------|------|
| **Custo Total (TCO)**  | 25       | 2/5  | 4/5   | 3/5    | 3/5       | 5/5  |
| **Flexibilidade**      | 20       | 3/5  | 4/5   | 4/5    | 5/5       | 5/5  |
| **Escalabilidade**     | 15       | 5/5  | 4/5   | 5/5    | 4/5       | 3/5  |
| **Suporte Local**      | 10       | 4/5  | 5/5   | 3/5    | 4/5       | 2/5  |
| **Integrações**        | 10       | 5/5  | 4/5   | 5/5    | 5/5       | 3/5  |
| **UI/UX**              | 10       | 3/5  | 4/5   | 4/5    | 5/5       | 4/5  |
| **Conformidade Fiscal**| 10       | 5/5  | 5/5   | 4/5    | 4/5       | 3/5  |

**Como calcular:**  
`(Nota × Peso) p/ cada critério → Soma total`  
*Ex.: SAP em Custo = 2 × 25% = 0.5*

### **2. Análise Detalhada por Critério**  
 **A. Custo Total de Propriedade (TCO)**  
| Componente               | SAP (R$) | TOTVS (R$) | Odoo (R$) | A (R$)    | B (R$)    |
|--------------------------|----------|------------|-----------|-----------|-----------|
| Licenças (5 anos)        | 1.2M     | 600k       | 120k      | 110k      | 100k      |
| Implementação            | 800k     | 400k       | 200k      | 150k      | 150k      |
| Infraestrutura           | 300k     | 150k       | 50k       | 40k       | 60k       |
| Suporte Anual            | 200k/ano | 100k/ano   | 30k/ano   | 20k/ano   | 30k/ano   |
| **TCO 5 anos**           | **3.5M** | **1.65M**  | **420k**  | **300k**  | **400k**  |

**Dica:** Inclua custos ocultos (treinamento, paralização operacional durante migração).

### **B. Customização vs. Processos Padrão**  
| Sistema   | Vantagens                           | Riscos                                  |
|-----------|-------------------------------------|-----------------------------------------|
| **SAP**   | Melhores práticas globais           | Alto custo para adaptações              |
| **TOTVS** | Adaptado à legislação brasileira    | Limitações em operações internacionais  |
| **Odoo**  | Open-source (flexibilidade total)   | Requer equipe técnica qualificada       |
| **A**     | Open-source (flexibilidade total)   | Requer equipe técnica qualificada       |
| **B**     | Open-source (flexibilidade total)   | Requer equipe técnica qualificada       |

### **3. Processo de Seleção em 5 Etapas**  

**Etapa 1: Pré-seleção**  
- **Lista longa:** 8-10 fornecedores (pesquisa Gartner, consultorias)  
- **Critério de corte:** Fit geográfico (ex.: TOTVS para Brasil), porte da empresa  

**Etapa 2: RFI (Request for Information)**  
Documento com:  
- Requisitos obrigatórios (ex.: emissão automática de NF-e)  
- Perguntas sobre arquitetura, roadmap de updates  

**Etapa 3: Demonstrações Técnicas**  
**Checklist para avaliação:**  
✔ Testar fluxo crítico (ex.: compra → recebimento → pagamento)  

**Etapa 4: Due Diligence**  
- Visitar 2-3 clientes atuais do fornecedor  

**Etapa 5: Prova de Conceito (POC)**  
- Implementar módulo prioritário (ex.: finanças) por 30 dias  
- Métricas de sucesso:  
  - 95% de acurácia nos dados migrados  
  - Tempo de processamento < 3 segundos para relatórios críticos  

### **Planilha de Apoio à Decisão**  

| Critério               | Peso | Fornecedor A | Fornecedor B | ... |  
|------------------------|------|-------------|-------------|-----|  
| **Funcionalidades**    | 30%  |             |             |     |  
| **Custo 5 anos**       | 25%  |             |             |     |  
| **Suporte**            | 20%  |             |             |     |  
| **Flexibilidade**      | 15%  |             |             |     |  
| **UI/UX**              | 10%  |             |             |     |  
| **Total**              | 100% |             |             |     |  

**Como usar:**  
1. Atribua notas de 1-5 para cada critério  
2. Multiplique pelo peso  
3. Some os valores parciais  

### **Erros Fatais a Evitar**  
❌ **Viés do "ERP do vizinho"** (soluções boas para um setor podem ser ruins para outro)  
❌ **Negligenciar custos de migração** (em média 1.5x o custo das licenças)  
❌ **Subestimar treinamento** (alocar menos de 10% do budget para capacitação)  

## **Fase 3 – Preparação**   
- **Dados:** Limpeza e organização  
- **Processos:** Documentação  
- **Infraestrutura:** Nuvem vs. On-premise  

A fase de **Preparação** é onde a empresa estrutura os alicerces para o ERP funcionar sem problemas. Se mal executada, pode levar a **migração falha, resistência dos usuários e custos extras**.  

Abaixo, seguem os **3 pilares dessa fase**, com checklists e exemplos práticos:  


### **1. Dados: Limpeza e Organização**  
 **O que fazer?**  
- **Identificar fontes de dados:** Quais sistemas atuais serão migrados (planilhas, softwares legados)?  
- **Padronizar informações:**  
  - Unificar formatos (ex.: datas como DD/MM/AAAA, CPF/CNPJ sem pontuação).  
  - Eliminar duplicidades (clientes, produtos cadastrados múltiplas vezes).  
- **Validar integridade:**  
  - Dados incompletos (ex.: clientes sem e-mail ou CEP).  
  - Relacionamentos corrompidos (ex.: pedidos vinculados a clientes inexistentes).  

**Checklist**  
✔ Criar um **dicionário de dados** (definições de campos como "Código do Produto").  
✔ Definir **responsáveis por área** para validar informações (ex.: RH checa cadastro de funcionários).  
✔ Usar **ferramentas de ETL** (como SQL Server Integration Services ou Talend) para limpeza automatizada.  


### **2. Processos: Documentação**  
**O que fazer?**  
- **Mapear processos atuais ("AS-IS"):**  
  - Como cada departamento opera hoje (ex.: fluxo de aprovação de compras).  
  - Identificar gargalos (ex.: aprovações manuais que podem ser automatizadas).  
- **Definir processos futuros ("TO-BE"):**  
  - Como funcionarão **no ERP** (ex.: aprovação por workflow eletrônico).  
  - Documentar exceções (casos que fogem do padrão).  

**Checklist**  
✔ Usar **fluxogramas** (Ferramentas: Lucidchart, Bizagi).  
✔ Criar **manuais de procedimentos** por área (ex.: "Como lançar uma NF no ERP").  
✔ Realizar **workshops** com usuários-chave para validar os novos fluxos.  

### **3. Infraestrutura: Nuvem vs. On-Premise**  
**Comparativo Técnico**  

| **Critério**       | **Nuvem (SaaS)**                          | **On-Premise**                          |  
|--------------------|-------------------------------------------|------------------------------------------|  
| **Custo Inicial**  | ✅ Baixo (assinatura mensal)              | ❌ Alto (hardware, licenças permanentes) |  
| **Manutenção**     | ✅ Provider responsável                   | ❌ Equipe interna necessária              |  
| **Customização**   | ❌ Limitada                               | ✅ Total                                 |  
| **Segurança**      | 🔄 Compartilhada (depende do provider)    | ✅ Controle total                        |  
| **Escalabilidade** | ✅ Ajuste rápido de recursos              | ❌ Requer upgrades físicos                |  

### **Checklist de Decisão**  
✔ **Nuvem é ideal para:**  
  - Empresas com TI enxuta.  
  - Necessidade de acesso remoto (ex.: filiais em vários locais).  
✔ **On-Premise é ideal para:**  
  - Indústrias com dados ultrassensíveis (ex.: defesa, saúde).  
  - Requisitos legais de soberania de dados (ex.: governo).  

### **Plano de Ação para a Fase de Preparação**  

| **Pilar**         | **Ações**                                  | **Timeline**   |  
|--------------------|--------------------------------------------|----------------|  
| **Dados**          | - Limpeza de cadastros.<br>- Teste de migração em ambiente controlado. | 2-4 semanas    |  
| **Processos**      | - Workshops de mapeamento.<br>- Validação com gestores. | 3-6 semanas    |  
| **Infraestrutura** | - Instalação de servidores (se on-premise).<br>- Contratação de SaaS. | 1-3 semanas    |  


### **Riscos e Como Mitigá-los**  
⚠ **Dados sujos:**  
- *Solução:* Execute uma **migração teste** e valide com usuários antes do Go-Live.  

⚠ **Resistência a novos processos:**  
- *Solução:* Envolva os colaboradores no mapeamento ("TO-BE") para aumentar adesão.  

⚠ **Falhas na infraestrutura:**  
- *Solução:* Para nuvem, cheque SLA do provider; para on-premise, faça testes de carga.  

## **Fase 4 – Implementação**  

🔧 **Configuração** (parâmetros do sistema)  
📤 **Migração de dados** (importação segura)  
🧪 **Testes** (unitários, integrados, carga)  

A fase de **Implementação** é onde o ERP ganha vida, passando do planejamento para a operação real. É uma etapa crítica que exige atenção meticulosa para evitar falhas no Go-Live.  

Abaixo, seguem os **3 componentes essenciais** desta fase, com metodologias, melhores práticas e exemplos concretos:  


### **1. 🔧 Configuração do Sistema**  
**O que é?**  
Ajustar o ERP aos processos da empresa através de:  
- **Parâmetros básicos:** Moeda, fuso horário, idioma.  
- **Regras de negócio:** Condições de pagamento, hierarquia de aprovações.  
- **Customizações (se necessárias):** Campos adicionais, relatórios personalizados.  

**Passo a Passo:**  
1. **Configuração Inicial**  
   - Definir estrutura organizacional (filiais, departamentos).  
   - Estabelecer níveis de acesso por perfil (ex.: gerente x operador).  

2. **Adaptação de Processos**  
   - Exemplo: Se a empresa usa 3 níveis de aprovação para compras, configurar esse workflow no ERP.  

3. **Integrações**  
   - Conectar o ERP a sistemas externos (ex.: e-commerce, BI).  

**Checklist de Configuração**  
✔ Validar todos os parâmetros com usuários-chave antes da migração.  
✔ Documentar cada alteração para futuras auditorias.  

**Exemplo Prático:**  
*"Uma farmacêutica configurou o SAP para bloquear vendas de medicamentos controlados sem a assinatura digital do responsável, atendendo à Anvisa."*  


### **2. 📤 Migração de Dados**  
 **Tipos de Dados Migrados**  
- **Mestres:** Clientes, fornecedores, produtos.  
- **Transacionais:** Pedidos em aberto, contas a pagar.  
- **Históricos:** Dados fiscais dos últimos 5 anos (se aplicável).  

**Metodologia Recomendada**  
1. **Extração**  
   - Exportar dados do sistema antigo para formatos intermediários (CSV, XML).  

2. **Transformação**  
   - Aplicar regras de validação (ex.: CPF/CNPJ válido).  
   - Converter formatos (ex.: data de "01-Jan-2023" para "01/01/2023").  

3. **Carga (ETL)**  
   - Usar ferramentas como **SAP Data Services** ou **Microsoft SSIS**.  
   - Realizar carga em ambiente de teste antes da produção.  

**Riscos e Mitigações**  
⚠ **Dados corrompidos:**  
- *Solução:* Executar pré-validações com scripts SQL.  

⚠ **Falhas de relacionamento:**  
- *Solução:* Mapear chaves primárias/estrangeiras (ex.: código do cliente no pedido).  


### **3. 🧪 Testes**  
**Tipos de Testes**  
| **Tipo**          | **Objetivo**                                  | **Exemplo**                              |  
|-------------------|-----------------------------------------------|------------------------------------------|  
| **Unitários**     | Verificar funcionalidades isoladas.           | Testar emissão de NF-e no módulo fiscal.|  
| **Integrados**    | Validar comunicação entre módulos.            | Pedido de venda → Fatura → Contabilidade.|  
| **Carga**         | Avaliar desempenho sob uso intenso.           | Simular 500 usuários acessando simultaneamente.|  

**Ferramentas Úteis**  
- **Testes manuais:** Planilhas de cenários (ex.: "Caso 1: Cadastrar novo cliente").  
- **Automatização:** Selenium (para interfaces web), LoadRunner (teste de carga).  

**Checklist de Testes**  
✔ Envolver usuários finais nos testes integrados.  
✔ Testar cenários de exceção (ex.: cancelamento de pedido após faturamento).  

**Exemplo de Problema Detectado:**  
*"Em testes no módulo de RH, identificou-se que o sistema não calculava corretamente horas extras para turnos noturnos. A correção foi feita antes do Go-Live."*  


### **Plano de Ação para Implementação**  

| **Etapa**         | **Atividades**                               | **Duração Típica** |  
|--------------------|---------------------------------------------|--------------------|  
| **Configuração**   | - Definir parâmetros globais.<br>- Configurar workflows. | 2-4 semanas       |  
| **Migração**       | - Extrair, transformar e carregar dados.<br>- Validar integridade. | 3-6 semanas       |  
| **Testes**         | - Executar testes unitários/integrados.<br>- Ajustar com base em falhas. | 4-8 semanas       |  

### **Erros Comuns e Soluções**  
❌ **Customizações excessivas:**  
- *Solução:* Priorize adaptar processos ao ERP, não o contrário.  

❌ **Migração sem backup:**  
- *Solução:* Mantenha uma cópia do ambiente antigo até a estabilização.  

❌ **Testes superficiais:**  
- *Solução:* Crie cenários que cubram 80% dos casos de uso diários.  


## **Fase 5 – Treinamento**  
**Tópicos:**  
- Cursos por área  
- Manuais e tutoriais  
- "Embaixadores" do ERP  


A fase de treinamento é **crítica** para garantir a adoção eficaz do ERP. Um treinamento bem-executado reduz resistência, aumenta a produtividade e minimiza erros pós-implantação.  

Abaixo, detalho os **3 pilares do treinamento**, com estratégias práticas e exemplos:  

### **1. Cursos por Área (Treinamento Específico)**  
**Objetivo:**  
Capacitar cada departamento nas funcionalidades **relevantes para seu dia a dia**.  

**Como Implementar?**  
- **Mapeie necessidades por setor:**  
  - **Financeiro:** Lançamentos contábeis, conciliação bancária.  
  - **Vendas:** Cadastro de clientes, emissão de pedidos.  
  - **Estoque:** Movimentações, inventário.  
- **Formato:**  
  - **Treinamentos presenciais** (para processos complexos).  
  - **Webinars ou E-learning** (para atualizações rápidas).  
  - **Sessões práticas** (simulações no ambiente de teste).  

**Exemplo:**  
> *"O time de vendas da Empresa X passou por 8 horas de treinamento no módulo de CRM do SAP, com exercícios reais de fechamento de pedidos."*  

**Dica:**  
▶ Use **casos reais da empresa** nos exercícios (ex.: um cliente ou produto real).  


### **2. Manuais e Tutoriais (Documentação de Suporte)**  

**Objetivo:**  
Fornecer materiais de consulta rápida para usuários após o treinamento.  

**Tipos de Documentação:**  
- **Manuais técnicos:** Passo a passo detalhado (ex.: como gerar um relatório).  
- **Guias visuais:** Infográficos ou vídeos curtos (ex.: fluxo de aprovação de compras).  
- **FAQ (Perguntas Frequentes):** Soluções para erros comuns.  

**Boas Práticas:**  
✔ **Linguagem simples:** Evite jargões técnicos.  
✔ **Acesso fácil:** Hospede em um portal ou no próprio ERP.  
✔ **Atualização contínua:** Revise os materiais conforme o sistema evolui.  


### **3. "Embaixadores" do ERP (Multiplicadores Internos)**  
**Objetivo:**  
Identificar colaboradores-chave que **difundirão o conhecimento** e ajudarão colegas.  

**Perfil do Embaixador:**  
- Conhecimento técnico básico.  
- Boa comunicação.  
- Respeito entre colegas.  

**Funções:**  
- Ser o **primeiro ponto de contato** para dúvidas simples.  
- Coletar **feedback** dos usuários para a equipe de TI.  
- Promover a **cultura do novo sistema** (ex.: compartilhar dicas em reuniões).  

**Como Selecionar?**  
1. Indicação de líderes de área.  
2. Treinamento avançado (10-20% a mais que outros usuários).  
3. Reconhecimento formal (ex.: certificado ou benefício).  


### **Plano de Ação para o Treinamento**  

| **Etapa**       | **Ações**                                                                 | **Responsável**      |  
|-----------------|--------------------------------------------------------------------------|----------------------|  
| **Pré-Treinamento** | - Mapear processos críticos por área.<br>- Desenvolver materiais didáticos. | Equipe de TI + RH    |  
| **Execução**    | - Cursos presenciais/EAD.<br>- Sessões práticas em ambiente de teste.     | Consultores + Líderes |  
| **Pós-Treinamento** | - Disponibilizar manuais.<br>- Nomear embaixadores.<br>- Agendar reciclagens. | Gestores de Projeto  |  


### **Erros Comuns no Treinamento (e Como Evitá-los)**  
❌ **Treinar todos da mesma forma**  
→ *Solução:* Personalize por cargo (ex.: gerentes precisam de visão analítica; operadores, de funções específicas).  

❌ **Ignorar resistência à mudança**  
→ *Solução:* Use gamificação (ex.: rankings de usuários mais ativos no ERP).  

❌ **Não medir eficácia**  
→ *Solução:* Aplique testes pós-treinamento e monitore taxa de adoção.  


### **Métricas para Avaliar o Sucesso do Treinamento**  
- **Taxa de participação:** % de colaboradores que completaram o treinamento.  
- **Nível de proficiência:** Resultados em testes práticos.  
- **Redução de tickets de suporte:** Menos dúvidas = maior domínio do sistema.  

## **Fase 6 – Go-Live**  
**Estratégias:**  
1. **Big Bang** (rápido, porém arriscado)  
2. **Fases graduais** (seguro, mas demorado)  
3. **Piloto** (teste em um departamento)  

### **1. Big Bang (Implante Tudo de Uma Vez)**  

Todos os módulos e departamentos migram para o novo ERP **simultaneamente**, substituindo completamente o sistema antigo.  

**Vantagens**  
✅ **Rapidez:** Toda a empresa opera no novo sistema em um único momento.  
✅ **Custo reduzido:** Não há necessidade de manter sistemas paralelos.  
✅ **Alinhamento imediato:** Todos os departamentos começam juntos, evitando desencontros.  

**Desvantagens**  
❌ **Alto risco:** Problemas não detectados podem paralisar operações.  
❌ **Pressão sobre a equipe:** Suporte técnico e usuários podem ficar sobrecarregados.  
❌ **Dificuldade de reversão:** Voltar ao sistema antigo em caso de falha grave é complexo.  

**Quando usar?**  
- Empresas **pequenas ou com processos simples**.  
- Quando há **urgência** na implantação.  
- Se o **ERP já foi testado exaustivamente** em ambiente controlado.  

**Exemplo:**  
Uma startup de e-commerce migra seu sistema de gestão (vendas, estoque e financeiro) para o **Oracle NetSuite** em um único fim de semana.  

### **2. Fases Graduais (Módulo a Módulo ou Local a Local)**  

O ERP é implantado **progressivamente**, por:  
- **Módulos** (ex.: financeiro primeiro, depois estoque).  
- **Unidades de negócio** (ex.: matriz primeiro, filiais depois).  
- **Regiões geográficas** (ex.: Brasil antes de outros países).  

**Vantagens**  
✅ **Menos risco:** Problemas são contidos em áreas específicas.  
✅ **Aprendizado contínuo:** Ajustes são feitos antes de expandir.  
✅ **Suporte mais eficiente:** A equipe de TI foca em um grupo de usuários por vez.  

**Desvantagens**  
❌ **Tempo prolongado:** Pode levar meses ou anos para concluir.  
❌ **Custo maior:** Manter sistemas antigos e novos em paralelo.  
❌ **Desalinhamento temporário:** Dados podem ficar fragmentados entre sistemas.  

**Quando usar?**  
- Empresas **grandes ou com processos complexos**.  
- Quando há **resistência à mudança** (permite adaptação gradual).  
- Se o ERP exige **customizações específicas por área**.  

**Exemplo:**  
Uma multinacional implementa o **SAP** primeiro no departamento financeiro, depois em logística e, por último, em RH, ao longo de 12 meses.  


### **3. Piloto (Teste em um Departamento ou Unidade)**  

Um **grupo pequeno e controlado** (ex.: um departamento ou filial) usa o ERP antes do restante da empresa.  

**Vantagens**  
✅ **Baixo risco:** Falhas afetam apenas uma área.  
✅ **Feedback real:** Problemas são corrigidos antes do rollout geral.  
✅ **Treinamento eficaz:** Usuários-piloto tornam-se multiplicadores.  

**Desvantagens**  
❌ **Escala limitada:** Não testa integração em larga escala.  
❌ **Custo adicional:** Requer suporte dedicado ao grupo piloto.  
❌ **Possível frustração:** Usuários-piloto podem se sentir cobaias.  

**Quando usar?**  
- Para **validar a eficácia do ERP** antes da implantação total.  
- Em empresas com **múltiplas filiais** (testar em uma unidade antes de replicar).  
- Quando há **alta complexidade operacional**.  

**Exemplo:**  
Uma rede de varejo testa o **TOTVS Protheus** em uma loja física antes de implantar em todas as filiais.  


**Comparativo Resumido**  

| Estratégia    | Velocidade | Risco  | Custo  | Melhor Para...          |  
|--------------|-----------|--------|--------|-------------------------|  
| **Big Bang** | ⚡⚡⚡ (Rápido) | 🚨🚨 (Alto) | 💰 (Baixo) | Pequenas empresas, processos simples |  
| **Fases Graduais** | ⏳ (Lento) | 🟢 (Baixo) | 💰💰 (Médio) | Grandes empresas, projetos complexos |  
| **Piloto**   | 🟡 (Moderado) | 🟢 (Baixo) | 💰💰 (Médio) | Validação antes da expansão |  


**Dicas para Escolher a Melhor Estratégia**  
1. **Avalie o tamanho da empresa:** Startups podem preferir *Big Bang*; corporações, *fases graduais*.  
2. **Considere a criticidade dos processos:** Se um erro pode parar a produção, evite *Big Bang*.  
3. **Envolva os usuários:** Pilotos ajudam a ganhar adesão antes do lançamento total.  
4. **Tenha um plano B:** Prepare-se para rollback (volta ao sistema antigo) em emergências.  


## **Fase 7 – Pós-Implantação**  
**Checklist de Gestão:**  
- [ ] Monitorar KPIs  
- [ ] Coletar feedback  
- [ ] Aplicar atualizações  

### **O que são KPIs?**  
**KPI** (*Key Performance Indicator*, ou **Indicador-Chave de Performance**) é uma métrica quantificável usada para avaliar o sucesso de uma empresa, projeto ou processo em relação a objetivos estratégicos.  

### **Características de um Bom KPI**  
1. **Mensurável:** Pode ser quantificado (ex.: porcentagem, valor absoluto).  
2. **Relevante:** Alinhado aos objetivos do negócio.  
3. **Temporal:** Tem um período definido (ex.: mensal, anual).  
4. **Acionável:** Permite tomar decisões com base nos resultados.  

### **Exemplos de KPIs por Área**  

| **Área**         | **Exemplos de KPIs**                          |  
|------------------|-----------------------------------------------|  
| **Vendas**       | Taxa de conversão, Ticket médio, CAC (Custo de Aquisição por Cliente) |  
| **Marketing**    | Tráfego do site, Taxa de abertura de e-mails, ROI de campanhas |  
| **Financeiro**   | Lucratividade, Fluxo de caixa, Dívida líquida |  
| **Produção**     | Tempo de ciclo, Defeitos por mil unidades     |  
| **RH**           | Turnover, Satisfação de funcionários (eNPS)   |  
| **ERP**          | Tempo de implantação, Adoção pelos usuários, Redução de custos operacionais |  


### **Tipos de KPIs**  
1. **KPIs Estratégicos:** Medem o desempenho geral da empresa (ex.: crescimento de receita).  
2. **KPIs Operacionais:** Acompanham processos diários (ex.: produtividade por hora).  
3. **KPIs de Resultado:** Mostram o impacto final (ex.: lucro líquido).  
4. **KPIs de Processo:** Avaliam eficiência (ex.: tempo médio de atendimento).  

### **Como Definir KPIs Eficientes**  
1. **Conecte-os aos objetivos:** Ex.: Se o foco é redução de custos, monitore "gastos operacionais".  
2. **Escolha métricas simples:** Evite indicadores complexos demais.  
3. **Use benchmarks:** Compare com metas históricas ou do mercado.  
4. **Revise periodicamente:** KPIs podem mudar conforme as prioridades da empresa.  


### **Exemplo Prático: KPIs para Implantação de ERP**  
- **Taxa de adoção:** % de usuários ativos no sistema.  
- **Redução de erros:** Queda em inconsistências nos relatórios.  
- **Retorno sobre investimento (ROI):** Economia gerada vs. custo do ERP.  


### **Ferramentas para Monitorar KPIs**  
- **Dashboards:** Power BI, Tableau, Google Data Studio.  
- **ERPs:** Módulos de analytics (ex.: SAP Analytics Cloud).  
- **Planilhas:** Excel/Google Sheets com gráficos dinâmicos.  


### **Por que KPIs são Importantes?**  
✔ **Tomada de decisão baseada em dados** (não em "achismos").  
✔ **Identificação rápida de problemas**.  
✔ **Comunicação clara** de metas entre equipes.  

**Dica:** *"O que não é medido, não pode ser melhorado."* (Peter Drucker)*  

## **Administração do ERP**  
**4 Pilares:**  
1. **Manutenção** (upgrades, correções)  
2. **Gestão de usuários** (perfis de acesso)  
3. **Backup e segurança** (proteção de dados)  
4. **Melhoria contínua** (otimizações)  


## **Erros Comuns na Implantação**  
**Atenção:**  
❌ Personalizações excessivas  
❌ Falta de treinamento  
❌ Migração de dados desorganizados  

## **Conclusão**  
**Mensagem-chave:**  
*"ERP é uma jornada contínua – implante, monitore e melhore!"*  
