# Funcoes
#Criacao: 20250718.1124
__versao__ = 20250727.2104

import os, json

#MenuPrincipal-----------------------------------------------------------------------------#
def MenuPrincipal():
    limparTela()
    print(" ----------------------------------------------------------------")
    print("\033[1;43m                    Coffee Shops Tia Rosa                        \033[0m")
    print(" ----------------------------------------------------------------")
    print()
    print("            1- Cardapio")
    print("            2- Anotar Pedido")
    print("            3- Listar Clientes")
    print("            4- Listar Vendas")
    print("            0- Sair")
    for i in range(6):
        print()
    print(" ----------------------------------------------------------------")

#limparTela--------------------------------------------------------------
def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

#listarCardapio-----------------------------------------------------------
def listarCardapio(cardapio):
    limparTela()
    #with open("cardapio.json",'r',encoding="utf-8") as f:
    #    cardapio=json.load(f)
    print("----------------------------------------------------------------")
    print(" \033[1;32m                  CARDAPIO:\033[0m")
    print(" ----------------------------------------------------------------")
    for id_produto, dados in cardapio.items():
        nome=dados['prodnome']
        pontinhos='.'*(30-len(nome))#
        print(f"\n {id_produto} {nome}{pontinhos} Preço:\033[1;32m R$ {dados['preco']:.2f}\033[0m")
        #print(f"\n{id_produto}",f"{dados['prodnome']}...........................",f"Preço: R$ {dados['preco']:.2f}")
        #print(f"Nome: {dados['prodnome']}")
        print(f" Ingredientes: {dados['ingredientes']}")
        #print(f"Preço: R$ {dados['preco']:.2f}")

#listarClientes--------------------------------------------------------------
def listarClientes(clientes):
    limparTela()
    #with open("cardapio.json",'r',encoding="utf-8") as f:
    #    cardapio=json.load(f)
    print(" ----------------------------------------------------------------")
    print("\033[1;32m        CADASTRO DE CLIENTES:\033[0m")
    print(" ----------------------------------------------------------------")
    for id_cliente, dados in sorted(clientes.items(),key=lambda item: item[1]['clinome']):
        print(f" {id_cliente} {dados['cpf']} {dados['clinome']}\033[0m")

#listarVendas----------------------------------------------------------------
def listarVendas(pedidos,cardapio):
    TotalDoDia=0.0;
    limparTela()
    print(" ----------------------------------------------------------------")
    print("\033[1;32m         VENDAS\033[0m")
    print(" ----------------------------------------------------------------")
    for chave in pedidos:
        pedido = pedidos[chave]
        print(f" Pedido: {pedido['pedido']}",f"Data: {pedido['data']}")
        print(f" CPF: {pedido['clicpf']},  Nome: {pedido['clinome']}")
        print(" Itens:")
        total=0.0
        for prod_id in pedido["produtos"]:
            #prod = cardapio.get(prod_id, {})
            prod=cardapio.get(str(prod_id), {})
            nome=prod.get("prodnome", "Produto não encontrado")
            preco=prod.get("preco", 0.00)
            print(f" {prod_id} , {nome:<20} {preco:>6.2f}")
            total+=preco
        print(f"{'\033[1;31mTotal:':>32} {total:>6.2f}\033[0m")
        TotalDoDia+=total
        print("---------------------------------------------------")
    print(f"{'Total do dia:':>32} {TotalDoDia:>6.2f}")


#pegarProximoPedido---------------------------------------------------------------------
def pegarProximoPedido(pedidos):
    # Pega todas as chaves do dicionário (ex: "1", "2", "3")
    chaves = pedidos.keys()
    numeros = []
    for chave in chaves:
        numeros.append(int(chave))
    ultimoPedido=max(numeros)
    return ultimoPedido+1

#anotarPedido---------------------------------------------------------------------
def anotarPedido():
    limparTela()
    print(" ----------------------------------------------------------------")
    print("\033[1;33m         ANOTAR PEDIDO:\033[0m")
    print(" ----------------------------------------------------------------")



