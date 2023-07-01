numeros = range(0, 10, 2)
print(numeros)

for numero in numeros:
    print(numero)

texto = 'leonardo'.__iter__()
print(next(texto))

iterator = iter(texto)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

lista = [1, 2, 3, 4, 5]

for x in lista:
    print(x, end="")
