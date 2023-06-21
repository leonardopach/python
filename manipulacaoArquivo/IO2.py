arquivo = open("pessoas.csv")
for registro in arquivo:
    print("Nome: {} idade: {}".format(*registro.strip().split(",")), end="")
arquivo.close()
