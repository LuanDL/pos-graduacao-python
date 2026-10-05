def linha(tipo="*", tamanho=10):
    result = ""
    for i in range(tamanho):
        result += tipo
    return result


# Módulo principal (main)
print(linha())
print(linha("X", 10))
print(linha(tipo= '-'))
print(linha(tamanho= 20))
print(linha(tipo='ABC', tam=5))