# Funcoes
#Criacao: 20250718.1124
__versao__ = 20250720.1147

import os, json


def MenuPrincipal():
    limparTela()
    print("----------------------------------------------------------------")
    print("                     Coffee Shops Tia Rosa                      ")
    print("----------------------------------------------------------------")
    print()
    print("           1- Cardapio                                          ")
    print("           2- Abrir Pedido                                      ")
    print("           3- Clientes                                          ")
    print("           0- Sair                                              ")
    print()
    print()
    print()
    print()
    print()
    print()
    print("----------------------------------------------------------------")

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def listarCardapio(cardapio):
    limparTela()
    with open("cardapio.json",'r',encoding="utf-8") as f:
        cardapio=json.load(f)
    print("CARDAPIO:")
    for id_produto, dados in cardapio.items():
        print(f"\n{id_produto}",f"{dados['prodnome']}..............",f"Preço: R$ {dados['preco']:.2f}")
        #print(f"Nome: {dados['prodnome']}")
        print(f"Ingredientes: {dados['ingredientes']}")
        #print(f"Preço: R$ {dados['preco']:.2f}")


