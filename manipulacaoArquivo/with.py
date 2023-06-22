with open("pessoas.csv") as arquivo:
    for registro in arquivo:
        print("Nome: {}, idade: {}".format(*registro.strip().split(",")))

if arquivo.closed:
    print("Arquivo já foi fechado!")
