import os

print("a" * 80)
os.system("clear")
os.system("echo 'hello world'")
# os.system("mkdir teste")
os.system("rm -rf teste")
print(os.path.join(os.path.dirname(__file__)))
caminho = os.path.join("home/users", "teste", "desktop", "arquivo.txt")
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extesao = os.path.splitext(caminho)
print(arquivo)
print(nome_arquivo, extesao)
print(os.path.exists("/home/leonardopach/python"))

print(os.path.abspath('.'))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))

caminho = os.path.join("/home/leonardopach/python/python_luiz_otavio")
print("*" * 90)
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    for imagem in os.listdir(caminho_completo_pasta):
        print(' ', imagem)
