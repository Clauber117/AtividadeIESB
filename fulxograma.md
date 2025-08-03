```mermaid
graph TD
    A[Inicio] --> B{CarregarJSON}
    B-->C[Executar a funcao main()]
    C-->D[Inicio da funcao main()]
    D --> E[Inicializar opcao com 1]
    E --> F{Loop Principal (enquanto opcao != 0)}
    F -- "Sim" --> G[Exibir Menu Principal]
    G --> H[Solicitar opcao do usuario]
    H --> I{Tratar Erro de Entrada?}
    I -- "Sim (entrada invalida)" --> J[Exibir mensagem de erro]
    J --> K[Aguardar ENTER]
    K --> F

    I -- "Nao (entrada valida)" --> L{Opcao == 0?}
    L -- "Sim" --> M[Sair do loop (break)]

    L -- "Nao" --> N{Opcao == 1?}
    N -- "Sim" --> O[Chamar funcoes.listarCardapio()]

    N -- "Nao" --> P{Opcao == 2?}
    P -- "Sim" --> Q[Chamar funcoes.anotarPedido()]

    P -- "Nao" --> R{Opcao == 3?}
    R -- "Sim" --> S[Chamar funcoes.listarClientes()]

    R -- "Nao" --> T{Opcao == 4?}
    T -- "Sim" --> U[Chamar funcoes.listarVendas()]

    T -- "Nao" --> V[Exibir 'Opcao invalida']
    V --> W[Aguardar ENTER]
    W --> F

    O --> X[Exibir linha vazia]
    Q --> X
    S --> X
    U --> X

    X --> Y[Aguardar ENTER para voltar]
    Y --> F

    F -- "Nao (opcao == 0)" --> Z[Fim da funcao main()]
    Z --> Fim[Fim do Programa]
