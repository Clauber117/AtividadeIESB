# Funcoes
#Criacao: 20250718.1124
__versao__ = 20250725.1021

import os, json

def MenuPrincipal():
    limparTela()
    print(" ----------------------------------------------------------------")
    print("                      Coffee Shops Tia Rosa                      ")
    print(" ----------------------------------------------------------------")
    print()
    print("            1- Cardapio                                          ")
    print("            2- Abrir Pedido                                      ")
    print("            3- Clientes                                          ")
    print("            0- Sair                                              ")
    print()
    print()
    print()
    print()
    print()
    print()
    print(" ----------------------------------------------------------------")

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def listarCardapio(cardapio):
    limparTela()
    #with open("cardapio.json",'r',encoding="utf-8") as f:
    #    cardapio=json.load(f)
    print("----------------------------------------------------------------")
    print(" \033[1;32m CARDAPIO:\033[0m")
    print(" ----------------------------------------------------------------")
    for id_produto, dados in cardapio.items():
        nome=dados['prodnome']
        pontinhos='.'*(30-len(nome))#
        print(f"\n {id_produto} {nome}{pontinhos} Preço:\033[1;32m R$ {dados['preco']:.2f}\033[0m")
        #print(f"\n{id_produto}",f"{dados['prodnome']}...........................",f"Preço: R$ {dados['preco']:.2f}")
        #print(f"Nome: {dados['prodnome']}")
        print(f" Ingredientes: {dados['ingredientes']}")
        #print(f"Preço: R$ {dados['preco']:.2f}")

def listarClientes(clientes):
    limparTela()
    #with open("cardapio.json",'r',encoding="utf-8") as f:
    #    cardapio=json.load(f)
    print(" ----------------------------------------------------------------")
    print("\033[1;32m CADASTRO DE CLIENTES:\033[0m")
    print(" ----------------------------------------------------------------")
    for id_cliente, dados in sorted(clientes.items(),key=lambda item: item[1]['nome']):
        print(f"\n {id_cliente} {dados['cpf']} {dados['nome']}\033[0m")


