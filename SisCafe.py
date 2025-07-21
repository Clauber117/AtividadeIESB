#Lógica Algoritmos e Programação de Computadores
#Prof.   : Francisco Lima
#Id Al   : 2586101058
#aluno   : Clauber Araújo Lima
#Turma   : ADADS3A
#Criacao : 20250716.1334
__versao__ = 20250720.1142

import os, curses, json
import funcoes


#Aqui carregamos o cardapio.
with open("cardapio.json",'r',encoding="utf-8") as f:
    cardapio=json.load(f)
    #funcoes.listarCardapio(cardapio)

def main():
    while True:
        opcao=0
        funcoes.MenuPrincipal()
        opcao=int(input("Escolha a operação[1]:") or 1)
        #funcoes.listarCardapio(cardapio)
        if opcao==0:
            break
        elif opcao==1:
            funcoes.listarCardapio(cardapio)
        print()
        input('Tecle ENTER para voltar')




if __name__== "__main__":
    main()
    print("\n Fim")
