```mermaid
flowchart TD
    A[Coleta] --> B[Triagem]
    B --> C[Desmontagem]
    C --> D[Separação de Materiais]
    D --> E[Reuso - Equipamentos e Peças]
    D --> F[Reciclagem - Metais e Plásticos]
    D --> G[Descarte Seguro - Resíduos Perigosos]
    
    subgraph Detalhes
    A1[Pontos de Entrega Voluntária] --> A
    A2[Campanhas de Arrecadação] --> A
    A3[Retirada Agendada] --> A
    
    B1[Classificação por tipo e condição] --> B
    B2[Separação inicial de componentes perigosos] --> B
    
    C1[Equipe treinada e EPI obrigatório] --> C
    
    D1[Metais] --> F
    D2[Plásticos] --> F
    D3[Baterias] --> G
    D4[Placas Eletrônicas] --> F
    D5[Peças reutilizáveis] --> E
    end
`
