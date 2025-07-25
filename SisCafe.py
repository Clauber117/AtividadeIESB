#Lógica Algoritmos e Programação de Computadores
#Prof.  : Francisco Lima
#Id Al  : 2586101058
#aluno  : Clauber Araújo Lima
#Turma  : EADADS3A
#Criacao: 20250716.1334
__versao__ = 20250725.1021

import os, curses, json
import funcoes


#Aqui carregamos o cardapio.
with open("cardapio.json",'r',encoding="utf-8") as f:
    cardapio=json.load(f)
    #funcoes.listarCardapio(cardapio)

#Aqui carregamos os clientes
with open("clientes.json",'r',encoding="utf-8") as f:
    clientes=json.load(f)
    #funcoes.listarCardapio(cardapio)

def main():
    opcao=1
    while opcao!=0:
        opcao=0
        funcoes.MenuPrincipal()
        opcao=int(input(" Escolha a operação[0]:") or 0)
        #funcoes.listarCardapio(cardapio)
        if opcao==0:
            break
        elif opcao==1:
            funcoes.listarCardapio(cardapio)
        elif opcao==3:
            funcoes.listarClientes(clientes)
        print()
        input('Tecle ENTER para voltar')


if __name__== "__main__":
    main()
    print("\n Fim")
