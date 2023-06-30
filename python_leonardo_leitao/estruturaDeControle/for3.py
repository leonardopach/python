from random import randint


def sortear_dado():
    dado = randint(1, 6)
    return dado


for dado in range(1, 7):
    if dado % 2 == 1:
        continue

    if sortear_dado() == dado:
        print("ACERTOU", dado)
        break
else:
    print("Não Acertou o numero")
