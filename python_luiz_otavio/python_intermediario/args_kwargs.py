a, b = 1, 2
print(a, b)

pessoa = {
    'nome': 'aline',
    'sobrenome': 'Souza',
}

(a1, a2) = pessoa.items()
print(a1, a2)

dados_pessoas = {
    'idade': 15,
    'altura': 1.8
}

pessoas_completa = {**pessoa, **dados_pessoas}

print(pessoas_completa)
