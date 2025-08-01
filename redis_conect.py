#Teste de conceito
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

# Pegando todas as chaves do tipo usuario:*
for key in r.scan_iter("usuario:*"):
    dados = r.hgetall(key)
    print(f"{key.decode()}:")
    for campo, valor in dados.items():
        print(f"  {campo.decode()}: {valor.decode()}")
