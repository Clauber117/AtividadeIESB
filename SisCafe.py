#Lógica Algoritmos e Programação de Computadores
#Prof.: Francisco Lima
#aluno: Clauber Araújo Lima
#Id Aluno: 2586101058
#Ver.: 20250717.1806

import os, curses
import funcoes

cardapio={
    1: {"prodnome": "Cafe Expresso",
        "ingredientes": "cafe moído agua quente",
        "preco": 5.50},
    2: {"prodnome": "Cafe Cappuccino",
        "ingredientes": "cafe expresso, leite vaporizado, espuma de leite, canela",
        "preco": 8.90},
    3: {"prodnome": "Cafe com Leite",
        "ingredientes": "cafe expresso, leite vaporizado",
        "preco": 9.50},
    4: {"prodnome": "Cafe Mocha",
        "ingredientes": "cafe expresso, leite, chocolate, chantilly",
        "preco": 12.00},
    5: {"prodnome": "Cha Verde",
        "ingredientes": "folhas de cha verde, água quente, mel (opcional)",
        "preco": 7.00},
    7: {"prodnome": "Toddy",
        "ingredientes": "Toddy e leite",
        "preco": 4.00},
    8: {"prodnome": "Nescau",
        "ingredientes": "Nescau e leite",
        "preco": 4.00},
    9: {"prodnome": "Pao de Queijo",
        "ingredientes": "Pao de Queijo",
        "preco": 3.50},
   10: {"prodnome": "Coxinha",
        "ingredientes": "Coxinha",
        "preco": 4.50}
}

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def abertura():
    limparTela()
    print("+----------------------------------------------------------------+")
    print("+                     Coffee Shops Tia Rosa                      +")
    print("+----------------------------------------------------------------+")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("|                                                                |")
    print("+----------------------------------------------------------------+")

def ListarCardapio():
    limparTela()
    print("CARDAPIO:")
    for id_produto, dados in cardapio.items():
        print(f"\n{id_produto}",f"{dados['prodnome']}..............",f"Preço: R$ {dados['preco']:.2f}")
        #print(f"Nome: {dados['prodnome']}")
        print(f"Ingredientes: {dados['ingredientes']}")
        #print(f"Preço: R$ {dados['preco']:.2f}")


def main():
    opcao=0
    abertura()
    opcao=int(input("Escolha a operação:") or 1)
    ListarCardapio()

    print("\n")
    #print(cardapio[3]["ingredientes"])
    funcoes.teste()

if __name__== "__main__":
    main()
