lista = []
print(len(lista))
print(lista.append(1))
print(lista.append(5))
print(lista)
print(len(lista))

nova_lista = [1, 5, "Ana", "Bia"]
print(nova_lista)
nova_lista.remove(1)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

lista = [1, 5, "Rebeca", "Guilherme", 3.1415]
print(lista.index("Rebeca"))
print(lista[2])
print(lista[-1])
print(1 in lista)
print("Rebeca" in lista)
print("PEdro" not in lista)

lista = ["Ana", "Lia", "Rebeca", "Guilherme", "Pedro"]
print(lista[1:3])
print(lista[::2])
print(lista[::])
print(lista[:])
print(lista[::-1])
del lista[::2]
print(lista)
