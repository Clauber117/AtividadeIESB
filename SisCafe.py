#Lógica Algoritmos e Programação de Computadores
#Prof.: Francisco Lima
#aluno: Clauber Araújo Lima
#Id Aluno: 2586101058

import os

cardapio={
    1: {"prodnome": "Café Expresso",
        "ingredientes": ["café moído", "água quente"],
        "preco": 5.50},
    2: {"prodnome": "Cappuccino",
        "ingredientes": ["café expresso", "leite vaporizado", "espuma de leite", "canela"],
        "preco": 8.90},
    3: {"prodnome": "Latte",
        "ingredientes": ["café expresso", "leite vaporizado"],
        "preco": 9.50},
    4: {"prodnome": "Mocha",
        "ingredientes": ["café expresso", "leite", "chocolate", "chantilly"],
        "preco": 12.00},
    5: {"prodnome": "Chá Verde",
        "ingredientes": ["folhas de chá verde", "água quente", "mel (opcional)"],
        "preco": 7.00},
    6: {"prodnome": "Macchiato",
        "ingredientes": ["café expresso", "espuma de leite"],
        "preco": 7.50}
}

def abertura():
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



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    abertura()

    print("Produtos disponíveis na cafeteria:")
    for id_produto, dados in cardapio.items():
        print(f"\nID: {id_produto}")
        print(f"Nome: {dados['prodnome']}")
        print(f"Ingredientes: {', '.join(dados['ingredientes'])}")
        print(f"Preço: R$ {dados['preco']:.2f}")

    print("/n")
    print(cardapio[3]["ingredientes"])

if __name__== "__main__":
    main()

