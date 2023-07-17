import os

caminho_arquivo = "/home/leonardopach/python/"
caminho_arquivo += "modoAbertura.txt"

# Remover
# os.remove(caminho_arquivo)
os.rename(caminho_arquivo, "Nome_Alterado.txt")

# with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
#     arquivo.write("Atenção\n")
#     arquivo.write("linha 1\n")
#     arquivo.write("linha 2\n")
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())
