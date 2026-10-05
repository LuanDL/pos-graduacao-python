def soma(a, b):
    return a + b

def sub(a,b):
    return a - b

def mult(a, b_):
    return a * b_

def divInt(a, b):
    if b == 0:
        return 0
    return a // b

def divReal(a, b):
    if b == 0:
        return 0
    return a / b

def toString(a, b):
    result = f"{a} + {b} = {soma(a, b)}\n"
    result += f"{a} - {b} = {sub(a, b)}\n"
    result += f"{a} * {b} = {mult(a, b)}\n"
    result += f"{a} // {b} = {divInt(a, b)} divisao inteira\n"
    result += f"{a} / {b} = {divReal(a, b):.2f} divisao real\n"
    return result

# módulo principal (main)
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
print()
print(toString(a, b))

