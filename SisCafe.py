#Lógica Algoritmos e Programação de Computadores
#Prof.  : Francisco Filho
#Id Al  : 2586101058
#aluno  : Clauber Araújo Lima
#Turma  : EADADS3A
#Criacao: 20250716.1334
__versao__ = 20250802.1146

import os, json
import funcoes

# Objetos de dados Globais cardapio, clientes e pedidos

#Aqui carregamos o cardapio.
with open("cardapio.json",'r',encoding="utf-8") as f:
    cardapio=json.load(f)
    #funcoes.listarCardapio(cardapio)
    #print("\n Index:",cardapio.get("4")["prodnome"])

#Aqui carregamos os clientes
with open("clientes.json",'r',encoding="utf-8") as f:
    clientes=json.load(f)
    #funcoes.listarCardapio(cardapio)

#Aqui carregamos os pedidos
with open("pedidos.json",'r',encoding="utf-8") as f:
    pedidos=json.load(f)



def main():
    opcao=1
    while opcao!=0:
        opcao=0
        funcoes.MenuPrincipal()
        #A Aqui pega a opcao do usuário e trata se é inteiro valido
        #opcao=int(input(" Escolha a operação[0]:") or 0)
        try:
            opcao = int(input("Escolha a operação [0]: ") or 0)
        except ValueError:
            print("Entrada inválida. Digite um número. ENTER para voltar.")
            input()
            continue

        #funcoes.listarCardapio(cardapio)
        if opcao==0:
            break
        elif opcao==1:
            funcoes.listarCardapio(cardapio)
        elif opcao==2:
            funcoes.anotarPedido(pedidos,cardapio)
        elif opcao==3:
            funcoes.listarClientes(clientes)
        elif opcao==4:
            funcoes.listarVendas(pedidos,cardapio)
        else:
            print("Opção inválida. ENTER para continuar.")
            input()
            continue
        print()
        input('Tecle ENTER para voltar')

# Aqui começa o programa, aqui é uma melhor prática em Python para mais de um arquivo .py
if __name__== "__main__":
    main()
    print("\n Fim")
    #NumProduto=input("Qual produto?")
    #print("\n Index:",cardapio.get(NumProduto)["prodnome"])# Muito doido este typecast automático...


