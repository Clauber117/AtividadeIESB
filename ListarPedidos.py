# Uso para testes de conceitos
import json
#Aqui carregamos o cardapio.
with open("cardapio.json",'r',encoding="utf-8") as f:
    cardapio=json.load(f)
    #funcoes.listarCardapio(cardapio)
    #print("\n Index:",cardapio.get("4")["prodnome"])

#Aqui carregamos os clientes
with open("clientes.json",'r',encoding="utf-8") as f:
    clientes=json.load(f)
    #funcoes.listarCardapio(cardapio)
clientes[9]={"cpf":"99234223591","clinome":"Jeniffer Alana"}
with open('clientes.json', 'w', encoding='utf-8') as f:
    json.dump(clientes, f, ensure_ascii=False, indent=4)

#Aqui carregamos os pedidos
with open("pedidos.json",'r',encoding="utf-8") as f:
    pedidos=json.load(f)


def pegarProximoPedido(pedidos):
    # Pega todas as chaves do dicionário (ex: "1", "2", "3")
    chaves = pedidos.keys()
    numeros = []
    for chave in chaves:
        numeros.append(int(chave))
    ultimoPedido=max(numeros)
    return ultimoPedido+1

# Pegando o pedido
for chave in pedidos:
    pedido = pedidos[chave]
    print(f" Pedido: {pedido['pedido']}",f"Data: {pedido['data']}")
    print(f" CPF: {pedido['clicpf']},  Nome: {pedido['clinome']}")
    print(" Itens:")
    total = 0.0
    for prod_id in pedido["produtos"]:
        prod = cardapio.get(str(prod_id), {})
        nome = prod.get("prodnome", "Produto não encontrado")
        preco = prod.get("preco", 0.00)
        print(f" {prod_id}, {nome:<20} {preco:>6.2f}")
        total += preco
    print(f"{'\033[1;31mTotal:':>31} {total:>6.2f}\033[0m")
    print("---------------------------------------------------")

print(pegarProximoPedido(pedidos))

