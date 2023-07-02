def soma(*args):
    return sum(args)


resultado = soma(1, 2, 3, 4, 5, 6)
print(resultado)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)
