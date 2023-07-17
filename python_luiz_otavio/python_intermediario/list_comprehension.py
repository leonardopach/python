print(list(range(10)))
print(list(valor for valor in range(10) if valor % 2 == 0))

lista = [numero * 2 for numero in range(10)]
print(lista)

#  Com mais de 1 for
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x, y))

print(lista)

lista = [(x, y) for x in range(3) for y in range(3)]
print(lista)
