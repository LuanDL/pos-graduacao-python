def sinal_I(n):
    if n < 0:
        return "<<< Negativo >>>"

    if n == 0:
        return "<<< Neutro >>>"

    if n > 0:
        return "<<< Positivo >>>"

def sinal_II(n):
    if n < 0:
        return "<<< Negativo >>>"
    else:
        if n == 0:
            return "<<< Neutro >>>"
        else:
            return "<<< Positivo >>>"

def sinal_III(n):
    if n < 0:
        return "<<< Negativo >>>"
    elif n == 0:
        return "<<< Neutro >>>"
    else:
        return "<<< Positivo >>>"

# Módulo principal (main)
tam = int(input("Digite o tamanho da entrada: "))

for i in range(tam):
    print()
    n = int(input(f"Digite o {i + 1}º número: "))
    print(sinal_I(n))
    print(sinal_II(n))
    print(sinal_III(n))