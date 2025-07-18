#Teste de Conceito
import json

cardapio={
    1: {"prodnome": "Cafe Expresso",
        "ingredientes": "cafe moído agua quente",
        "preco": 5.50},
    2: {"prodnome": "Cafe Cappuccino",
        "ingredientes": "cafe expresso, leite vaporizado, espuma de leite, canela",
        "preco": 8.90},
    3: {"prodnome": "Cafe com Leite",
        "ingredientes": "cafe expresso, leite vaporizado",
        "preco": 9.50},
    4: {"prodnome": "Cafe Mocha",
        "ingredientes": "cafe expresso, leite, chocolate, chantilly",
        "preco": 12.00},
    5: {"prodnome": "Cha Verde",
        "ingredientes": "folhas de cha verde, água quente, mel (opcional)",
        "preco": 7.00},
    7: {"prodnome": "Toddy",
        "ingredientes": "Toddy e leite",
        "preco": 4.00},
    8: {"prodnome": "Nescau",
        "ingredientes": "Nescau e leite",
        "preco": 4.00},
    9: {"prodnome": "Pao de Queijo",
        "ingredientes": "Pao de Queijo",
        "preco": 3.50},
   10: {"prodnome": "Coxinha",
        "ingredientes": "Coxinha",
        "preco": 4.50}
}

# Grava em arquivo JSON
with open('cardapio.json', 'w', encoding='utf-8') as f:
    json.dump(cardapio, f, ensure_ascii=False, indent=4)
