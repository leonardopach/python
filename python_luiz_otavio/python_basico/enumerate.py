nome = ["Maria", "Helena", "Luiz"]

lista_enumerada = enumerate(nome)
print([valor for valor in lista_enumerada])

for indice, nome in enumerate(nome):
    print(indice, nome)
