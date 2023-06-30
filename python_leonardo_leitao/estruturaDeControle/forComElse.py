PALAVRAS_PROIBIDAS = ["futebol", "religião", "politica"]
textos = [
    "Leonardo não gosta de futebol e politica",
    "A praia e divertida"
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Texto possui pelo menos uma palavra proibida:", palavra)
            break
    else:
        print("Texto autorizado:,", texto)
