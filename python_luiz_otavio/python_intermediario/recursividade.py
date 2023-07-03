def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)


# Exemplo de uso:
numero = 5
fatorial = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {fatorial}")
