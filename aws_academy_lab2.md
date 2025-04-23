**Laboratório 2** do curso "Tópicos em Engenharia de Software" da AWS Academy, focado na criação de uma VPC (Virtual Private Cloud) na AWS, configuração de sub-redes, tabelas de rotas, grupos de segurança e implantação de uma instância de servidor web. Abaixo está um resumo estruturado do conteúdo:

---

### **Visão Geral do Laboratório**
- **Objetivo**: Criar uma infraestrutura de rede personalizada na AWS usando VPC, sub-redes, tabelas de rotas, grupos de segurança e uma instância EC2 como servidor web.
- **Ferramentas**: Console AWS Academy (Learner Lab), com acesso restrito e sessões de 4 horas.
- **Pontuação**: 100 pontos, sem prazo de entrega definido.

---

### **Tarefas Principais**

#### **Tarefa 1: Criar a VPC**
- **Recursos criados**:
  - VPC com bloco CIDR `10.0.0.0/16`.
  - Sub-redes pública (`10.0.0.0/24`) e privada (`10.0.1.0/24`) em uma Zona de Disponibilidade (us-east-1a).
  - Gateway de Internet e Gateway NAT.
  - Tabelas de rotas pública (roteia tráfego para o Gateway de Internet) e privada (roteia tráfego para o Gateway NAT).
- **Configurações**:
  - Nomes automáticos gerados com prefixo "lab".
  - DNS e resolução de nomes habilitados.

#### **Tarefa 2: Criar Sub-redes Adicionais**
- **Objetivo**: Alta disponibilidade com sub-redes em uma segunda Zona de Disponibilidade (us-east-1b).
  - Sub-rede pública: `10.0.2.0/24`.
  - Sub-rede privada: `10.0.3.0/24`.
- **Associação às tabelas de rotas**:
  - Sub-redes públicas associadas à tabela de rotas pública.
  - Sub-redes privadas associadas à tabela de rotas privada.

#### **Tarefa 3: Criar Grupo de Segurança**
- **Configuração**:
  - Nome: `web_security_group`.
  - Descrição: "Enable HTTP access".
  - Regra de entrada: Permite tráfego HTTP (porta 80) de qualquer origem IPv4 (`0.0.0.0/0`).

#### **Tarefa 4: Executar Instância EC2 como Servidor Web**
- **Configuração da instância**:
  - AMI: Amazon Linux 2023.
  - Tipo: `t2.micro` (elegível para o nível gratuito).
  - Sub-rede: Sub-rede pública (`10.0.2.0/24`).
  - Grupo de segurança: `web_security_group`.
- **Script de inicialização (User Data)**:
  - Instala Apache, PHP e MariaDB.
  - Baixa e implanta um aplicativo web PHP.
- **Verificação**:
  - Acesso à página web via DNS público da instância, exibindo metadados e logotipo da AWS.

---

### **Arquitetura Final**
- **VPC**: `10.0.0.0/16` com sub-redes públicas e privadas em duas Zonas de Disponibilidade.
- **Roteamento**:
  - Público: Tráfego para internet via Gateway de Internet.
  - Privado: Tráfego para internet via Gateway NAT.
- **Segurança**: Grupo de segurança permitindo tráfego HTTP.
- **Servidor Web**: Instância EC2 na sub-rede pública, configurada automaticamente via script.

---

Este resumo destaca os conceitos práticos de redes na AWS, como VPC, sub-redes, segurança e implantação de serviços, essenciais para a engenharia de software em ambientes cloud.
