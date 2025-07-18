# Funcoes
#Ver.: 20250718.1124

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

def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def ListarCardapio():
    limparTela()
    print("CARDAPIO:")
    for id_produto, dados in cardapio.items():
        print(f"\n{id_produto}",f"{dados['prodnome']}..............",f"Preço: R$ {dados['preco']:.2f}")
        #print(f"Nome: {dados['prodnome']}")
        print(f"Ingredientes: {dados['ingredientes']}")
        #print(f"Preço: R$ {dados['preco']:.2f}")

def teste():
    print('Dentro das funções')

