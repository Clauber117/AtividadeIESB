#Teste de Conceito
import json

with open("cardapio.json",'r',encoding="utf-8") as f:
    cardapio=json.load(f)

print(json.dumps(cardapio, indent=4, ensure_ascii=False))
#print(cardapio)


#Buscando pela chav
print()
print(cardapio["4"]["prodnome"],cardapio["4"]["ingredientes"])

