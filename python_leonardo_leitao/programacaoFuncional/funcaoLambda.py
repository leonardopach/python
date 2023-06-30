numero = [1, 2, 3]

dobro = map(lambda i: i * 2, numero)
print(list(dobro))

triple = list(map(lambda x: x * 3, numero))
print(triple)

a = (1, 2, 3)
tupla = tuple(map(lambda x: x * 4, numero))
print(tupla)

compras = (
    {"quantidade": 2, "preco": 10},
    {"quantidade": 3, "preco": 20},
    {"quantidade": 5, "preco": 14},
)


def calc_preco_total(compra):
    return compra["quantidade"] * compra["preco"]


totais = tuple(
    map(
        lambda compra: compra["quantidade"] * compra["preco"], compras)
)

lambda_alternativa = tuple(map(calc_preco_total, compras))

print(f"Preços totais: {totais}")
print(f"Total geral: {sum(totais)}")
print(f"Preços totais lambda alternativa: {lambda_alternativa}")
