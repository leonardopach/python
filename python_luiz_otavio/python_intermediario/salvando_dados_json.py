import json

pessoa = {
    "nome": "Renata",
    "sobrenome": "Pacheco",
    "enderecos": [
        {"rua": "R1", "numero": 32},
        {"rua": "R2", "numero": 55},
    ],
    "altura": 1.8,
    "numeros_preferidos": (2, 4, 6, 8, 10),
    "dev": True,
    "nada": None,
}

with open("arquivo.json", "w") as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)

#  Ler JSON
with open("arquivo.json", "r", encoding="utf-8") as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(pessoa["nome"])
