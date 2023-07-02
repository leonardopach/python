dicionario = {
    "nome": "Leonardo",
    "Idade": 25,
    "altura": 1.84,
    "enderecos": [
        {"rua": "tall", "numero": 13},
        {"rua": "tall", "numero": 321},
    ],
}

pessoa = {}

print(type(dicionario))
print(dicionario["nome"])
print(dicionario["enderecos"][0])

pessoa["nome"] = "leonardo"
print(pessoa.get("nome"))
