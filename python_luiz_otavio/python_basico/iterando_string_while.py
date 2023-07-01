frase = "O python é uma linguagem de programação "\
    "multiparadigma. "\
    "Python foi criado por Guido van Rossum"

frase_lower = frase.lower()

print(frase_lower.count("python"))

i = 0

while i < len(frase_lower):
    letra_atual = frase_lower[i]
    quantas_vezes_letra_apareceu = frase_lower.count(letra_atual)

    print(f"{letra_atual} - {quantas_vezes_letra_apareceu}")
    i += 1
