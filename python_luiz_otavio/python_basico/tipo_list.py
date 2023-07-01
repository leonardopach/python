string = "ABCD"
lista = []
lista_2 = list(range(10))
lista_3 = [123, True, "Leonardo", 1.2, [123, "pedro"]]

print(type(lista), type(lista_2))
print(lista_2)
print(lista_3[4][0])
print(lista_3)
lista_3[4][1] = "Silva"
print(lista_3[4][1])

lista_3.append("Novo")
print(lista_3)
del lista_3[2]
print(lista_3)
lista_3.pop()
print(lista_3)
lista_2.clear()
print(lista_2)
lista_2.extend(lista_3)
print(lista_2)
lista_2.insert(1, "Mudou")
print(lista_2)
