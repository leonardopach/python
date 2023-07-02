# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
print(len(pessoa))
print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)

d1 = {
    "c1": 1,
    "c2": 2,
    "l1": [0, 1, 2]
}

d2 = copy.deepcopy(d1)
d2["l1"][1] = 99999

d2["c1"] = 1000
print(d1)
print(d2)

print(pessoa.get("nome"))