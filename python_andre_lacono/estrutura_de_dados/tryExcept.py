try:
    letras = ["a", "b", "c"]
    print(letras[3])
except IndexError as e:
    print(e)

try:
    valor = int(input("Digite um valor: "))
    print(valor)
except ValueError as e:
    print(e)
else:
    print("valor correto")
finally:
    print("final")
print("Continua...")
