from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input("Digite um valor: "))

print(f"Numero secreto {numero_secreto} foi encontrado")
