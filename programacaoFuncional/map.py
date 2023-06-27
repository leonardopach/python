lista_1 = [1, 2, 3]
dobro = map(lambda x: x * 2, lista_1)
print(list(dobro))

lista_2 = [
    {"nome": "João", "idade": 31},
    {"nome": "Maria", "idade": 37},
    {"nome": "José", "idade": 28},
]

so_nomes = list(map(lambda p: p["nome"], lista_2))
print(so_nomes)

so_idade = list(map(lambda p: p["idade"], lista_2))
print(so_idade)

frase = list(map(lambda p: f'{p["nome"]} tem {p["idade"]}', lista_2))
print(list(frase))
