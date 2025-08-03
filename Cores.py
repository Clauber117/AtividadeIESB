# cores_ansi_completas.py

def print_campo(titulo, codigo):
    reset = "\033[0m"
    print(f"{codigo}{titulo:<25}{reset} → {repr(codigo)}")

cores = {
    "Preto":       "30",
    "Vermelho":    "31",
    "Verde":       "32",
    "Amarelo":     "33",
    "Azul":        "34",
    "Magenta":     "35",
    "Ciano":       "36",
    "Branco":      "37"
}

print("\033[1mCores normais:\033[0m")
for nome, cod in cores.items():
    print_campo(nome, f"\033[0;{cod}m")

print("\033[1mCores brilhantes:\033[0m")
for nome, cod in cores.items():
    print_campo(nome + " forte", f"\033[1;{cod}m")

print("\033[1mFundo colorido:\033[0m")
for nome, cod in cores.items():
    print_campo("Fundo " + nome, f"\033[0;{int(cod)+10}m")

print("\033[1mTexto reverso:\033[0m")
for nome, cod in cores.items():
    print_campo("Reverso " + nome, f"\033[7;{cod}m")
