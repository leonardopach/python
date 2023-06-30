for x in range(1, 11):
    print(f"x = {x}")

for j in range(10):
    print(f"j = {j}")

for y in range(1, 11, 2):
    print(f"y = {y}")

for x in range(10):
    for y in range(10):
        print(f"{x} * {y} = {x * y}")

palavra = "leonardo"
for letra in palavra:
    print(letra, end=",")

aprovados = ["Leonardo", "Bianca", "Bianca", "Pedro"]
for nome in aprovados:
    print(nome)
