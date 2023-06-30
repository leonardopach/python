try:
    arquivo = open("pessoas.csv")

    for registro in arquivo:
        print("Nome: {}, idade: {}".format(*registro.strip().split(",")))
except IndexError:
    pass
finally:
    arquivo.close()

if arquivo.closed:
    print("Arquivo já foi fechado!")
