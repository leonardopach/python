dicionario = {"nome": "leonardo", "idade": 25, "Materias": ["matematica", "ingles"]}

# del dicionario["idade"]
dicionario.update({"endereco": "Rua A"})

print(dicionario)
print(dicionario["nome"])
print(dicionario.get("endereco", "Não existe"))


for chave, valor in dicionario.items():
    print(chave, valor)
