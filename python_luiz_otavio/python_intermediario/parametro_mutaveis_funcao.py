def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes("Leonardo")
adiciona_clientes("Joana", cliente1)
adiciona_clientes("Fernando", cliente1)
print(cliente1)

cliente2 = adiciona_clientes("heletro")
adiciona_clientes("Mariano", cliente2)
print(cliente2)
