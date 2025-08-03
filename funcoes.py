# Funcoes
#Criacao: 20250718.1124
__versao__ = 20250802.1118

import os, json
from datetime import date


#MenuPrincipal-----------------------------------------------------------------------------#
def MenuPrincipal():
    limparTela()
    data=date.today().strftime("%d/%m/%Y")
    print(" ----------------------------------------------------------------")
    print(f"\033[1;43m                    Coffee Shops Tia Rosa              {data}\033[0m")
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
        pontinhos='.'*(30-len(nome))# aqui pra colocar os pontos para alinhar a listagem na e fazilitar a leitura
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
        print(f" {int(id_cliente):02} {dados['cpf']} {dados['clinome']}\033[0m")

#listarVendas----------------------------------------------------------------
def listarVendas(pedidos,cardapio):
    TotalDoDia=0.0;
    limparTela()
    print(" ----------------------------------------------------------------")
    print("\033[1;32m         VENDAS\033[0m")
    print(" ----------------------------------------------------------------")
    for chave in pedidos:
        pedido=pedidos[chave]
        print(f" Pedido: {pedido['pedido']}",f"Data: {pedido['data']}")
        print(f" CPF: {pedido['clicpf']},  Nome: {pedido['clinome']}")
        print(" Itens:")
        total=0.0
        for prod_id in pedido["produtos"]:
            #prod=cardapio.get(prod_id, {})
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
    chaves=pedidos.keys()
    numeros=[]
    for chave in chaves:
        numeros.append(int(chave))
    ultimoPedido=max(numeros)
    return ultimoPedido+1

#pegarProximoPedido---------------------------------------------------------------------
def pegarDescItem(cardapio, numItem):
    item=cardapio.get(str(numItem))
    if item:
        nome = item.get("prodnome", "Descrição não encontrada")
        preco = item.get("preco", 0.00)
        return nome, preco
    else:
        return "Item não encontrado", 0.00

#anotarPedido---------------------------------------------------------------------
def anotarPedido(pedidos, cardapio):
    limparTela()
    numProximoPedido = pegarProximoPedido(pedidos)
    numItem = 0
    ItensPedido = []
    totalPedido = 0.0

    print(" ----------------------------------------------------------------")
    print("\033[1;33m         ANOTAR PEDIDO:\033[0m")
    print(" ----------------------------------------------------------------")
    print(" Pedido:\033[1;32m", numProximoPedido, "\033[0m")
    print(" ----------------------------------------------------------------")

    while True:
        numItem = input("Item: ")
        if numItem == "" or numItem == "99":
            break
        descItem, precoItem = pegarDescItem(cardapio, numItem)
        print(f"\033[1A\033[10C← {descItem} - R$ {precoItem:.2f}")
        totalPedido += float(precoItem)
        ItensPedido.append(int(numItem))  # tyepcast para se colocar outra coisa não dê erro no programa

    print(" Total Pedido: \033[1;31m", f"R$ {totalPedido:.2f}", "\033[0m")

    NomeCliente = input("\033[1;34m Nome do Cliente:\033[0m ")
    CPFCliente  = input("\033[1;34m CPF  do Cliente:\033[0m ")

    # novo pedido
    novoPedido = {
        "pedido": numProximoPedido,
        "data": date.today().strftime("%Y%m%d"),
        "clicpf": CPFCliente,
        "clinome": NomeCliente,
        "produtos": ItensPedido
    }

    # Inserir no json de pedidos
    pedidos[str(numProximoPedido)] = novoPedido

    # Gravar no arquivo pedidos.json
    with open("pedidos.json", "w", encoding="utf-8") as f:
        json.dump(pedidos, f, indent=4, ensure_ascii=False)

    print("\n\033[1;32mPedido registrado com sucesso!\033[0m")
    #input("Tecle ENTER para voltar.")









