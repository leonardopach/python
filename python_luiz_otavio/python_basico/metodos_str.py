frase = " Olha só que, coisa interessante  "
lista_palavras = frase.split(', ')

lista_frase_fixed = []
for i, frase in enumerate(lista_palavras):
    lista_frase_fixed.append(lista_palavras[i].strip())

print(lista_palavras)
print(lista_frase_fixed)
frase_unidas = ', '.join(lista_frase_fixed)
print(frase_unidas)
