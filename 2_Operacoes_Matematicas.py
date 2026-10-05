from math import sqrt

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def quadrado(n):
    return n * 4

def cubo(n):
    return n ** 3

def raiz_quadrada(n):
    if n < 0:
        return 0
    return sqrt(n)

def toString(n):
    result = f"O dobro de {n} é {dobro(n)}\n"
    result += f"O triplo de {n} é {triplo(n)}\n"
    result += f"O quadrado de {n} é {quadrado(n)}\n"
    result += f"O cubo de {n} é {cubo(n)}\n"
    result += f"A raiz quadrada de {n} é {raiz_quadrada(n):.4f}\n"
    return result

# módulo principal (main)
n = int(input("Digite um número: "))
print()
print(toString(n))