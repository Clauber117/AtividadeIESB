#Versionar
#Adaptado da internet

import re
from datetime import datetime
import sys

def atualizarVersao(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        # Data atual no formato desejado
        agora = datetime.now()
        nova_versao = agora.strftime('%Y%m%d.%H%M')
        nova_linha = f'__versao__ = {nova_versao}'

        # Regex para localizar linha de versão
        padrao = r'__versao__\s*=\s*\d{8}\.\d{4}'
        if not re.search(padrao, conteudo):
            print("⚠️  Linha de versão não encontrada no formato esperado.")
            return

        # Substitui a linha com a nova versão
        conteudo_novo = re.sub(padrao, nova_linha, conteudo)

        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo_novo)

        print(f"Versão atualizada para: {nova_versao}")

    except FileNotFoundError:
        print(f"❌ Arquivo '{arquivo}' não encontrado.")
    except Exception as e:
        print(f"❌ Erro: {e}")

# Execução via linha de comando
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python versionar.py arquivo.py")
    else:
        atualizarVersao(sys.argv[1])
