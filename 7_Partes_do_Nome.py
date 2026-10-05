def primeiros_Nomes(nome):
    partes = nome.split()
    n = len(partes)
    result = ""
    for i in range(n-1):
        result += partes[i] + " "

    return(result)


def sobrenome(nome):
    partes = nome.split()
    n = len(partes)
    return(partes[n-1])

# Módulo principal (main)
while True:
    nome = input("Digite o nome completo: (FIM para sair)")
    if nome.upper() == "FIM":
        break

    print()
    print(f"Primeiros nomes: {primeiros_Nomes(nome)}")
    print(f"Sobrenome: {sobrenome(nome)}")
    print()