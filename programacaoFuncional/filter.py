numero = [x for x in range(1, 11)]
print(numero)

pessoas = [
    {"nome": "Pedro", "idade": 11},
    {"nome": "Mariana", "idade": 18},
    {"nome": "Arthur", "idade": 26},
    {"nome": "Rebeca", "idade": 6},
    {"nome": "Thiago", "idade": 19},
    {"nome": "Gabriela", "idade": 17},
]

menor_idade = list(filter(lambda p: p["idade"] < 18, pessoas))
maior_idade = list(filter(lambda p: p["idade"] > 18, pessoas))
maior_char = list(filter(lambda p: len(p["nome"]) > 6, pessoas))
print(menor_idade)
print(maior_idade)
print(maior_char)
