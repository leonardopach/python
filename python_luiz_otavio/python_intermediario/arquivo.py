caminho_arquivo = "/home/leonardopach/python/"
caminho_arquivo += "arquivo.txt"

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.writelines(
        ("linha 3\n", "linha 4\n"),
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print("Lendo")
    print(arquivo.readline(), end="")
    print(arquivo.readline().strip())
    print("ReadLines")
    for linha in arquivo.readlines():
        print(linha.strip())

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

caminho_arquivo = "/home/leonardopach/python/"
caminho_arquivo += "modoAbertura.txt"

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write("Atenção\n")
    arquivo.write("linha 1\n")
    arquivo.write("linha 2\n")
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())

# arquivo =  open(caminho_arquivo, 'w')

# arquivo.close()
