produto = {"nome": "Caneta Azul", "preco": 2.5, "categoria": "Escritório"}

dc = {
    chave: valor.upper() if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}

print(dc)

lista = [
    ("a", "valor a"),
    ("b", "valor b"),
    ("c", "valor c"),
]

dc = {chave: valor for chave, valor in lista}
print(dc)

s1 = {i for i in range(100) if i % 2 == 0}
print(s1)
