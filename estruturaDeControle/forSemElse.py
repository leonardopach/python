PALAVRAS_PROIBIDAS = ["futebol", "religião", "politica"]
textos = [
    "Leonardo não gosta de futebel e politica",
    "A praia e divertida"
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print("Texto possui pelo menos uma palavra proibida:", palavra)
            found = True
            break

    if not found:
        print("Texto autorizado:,", texto)
