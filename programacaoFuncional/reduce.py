from functools import reduce

pessoas = [
    {"nome": "Pedro", "idade": 11},
    {"nome": "Mariana", "idade": 18},
    {"nome": "Arthur", "idade": 26},
    {"nome": "Rebeca", "idade": 6},
    {"nome": "Thiago", "idade": 19},
    {"nome": "Gabriela", "idade": 17},
]

menor_idade = list(filter(lambda p: p["idade"] < 18, pessoas))
soma_idade = reduce(lambda idade, p: idade + p["idade"], menor_idade, 0)
print(soma_idade)
