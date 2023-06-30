PALAVRAS_PROIBIDAS = {"futebol", "religião", "política"}
textos = [
    "Leonardo não gosta de futebol e religião",
    "A praia é divertida"
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print("Texto possui palavras proibidas:", intersecao)
    else:
        print("Texto possui palavras:", texto)
