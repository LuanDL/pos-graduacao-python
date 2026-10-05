def tabuada_I(n):
    i = 1
    while i <= 10:
        print(f"{n} x {i} = {n * i}")
        i += 1

def tabuada_II(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Módulo principal (main)
n = int(input("Digite um número: "))
print()
tabuada_I(n)
print()
tabuada_II(n)
print()