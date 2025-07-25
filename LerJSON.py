#Teste de Conceito
import json

with open("cardapio.json",'r',encoding="utf-8") as f:
    cardapio=json.load(f)

with open("clientes.json",'r',encoding="utf-8") as f:
    clientes=json.load(f)

print(json.dumps(cardapio, indent=4, ensure_ascii=False))
print('---------------------------------------------------------')
print(json.dumps(clientes, indent=4, ensure_ascii=False))
#print(cardapio)

#Buscando pela chave
print()
print(cardapio["4"]["prodnome"],cardapio["4"]["ingredientes"])

