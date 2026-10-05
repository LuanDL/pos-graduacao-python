def matriz_String(n):
    n = len(s)
    for i in range(n):
        for j in range(n):
            print(f"{s[j]}", end=" ")
        print()


def matriz_StringII(n):
    n = len(s)
    for i in range(n):
        for j in range(i+1):
            print(f"{s[j]}", end=" ")
        print()

# Módulo principal (main)
s = input("Digite uma string: ")
print()
matriz_String(s)
print()
matriz_StringII(s)