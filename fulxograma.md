graph TD
    A[Início do Programa] --> B{Carregar arquivos JSON};
    B --> C[Executar a função main()];
    C --> D[Início da função main()];
    D --> E[Inicializar opção com 1];
    E --> F{Loop Principal (enquanto opção != 0)};
    F -- Sim --> G[Exibir Menu Principal];
    G --> H[Solicitar opção do usuário];
    H --> I{Tratar Erro de Entrada?};
    I -- Sim (entrada inválida) --> J[Exibir mensagem de erro];
    J --> K[Aguardar ENTER];
    K --> F;
    
    I -- Não (entrada válida) --> L{Opção == 0?};
    L -- Sim --> M[Sair do loop (break)];
    
    L -- Não --> N{Opção == 1?};
    N -- Sim --> O[Chamar funcoes.listarCardapio()];
    
    N -- Não --> P{Opção == 2?};
    P -- Sim --> Q[Chamar funcoes.anotarPedido()];
    
    P -- Não --> R{Opção == 3?};
    R -- Sim --> S[Chamar funcoes.listarClientes()];
    
    R -- Não --> T{Opção == 4?};
    T -- Sim --> U[Chamar funcoes.listarVendas()];
    
    T -- Não --> V[Exibir "Opção inválida"];
    V --> W[Aguardar ENTER];
    W --> F;
    
    O --> X[Exibir linha vazia];
    Q --> X;
    S --> X;
    U --> X;

    X --> Y[Aguardar ENTER para voltar];
    Y --> F;
    
    F -- Não (opção == 0) --> Z[Fim da função main()];
    Z --> Fim[Fim do Programa];
