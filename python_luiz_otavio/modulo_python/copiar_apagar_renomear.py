import os
import shutil

# mover/Renomear -> shutil.move

HOME = os.path.expanduser('~')
PYTHON = os.path.join(HOME, 'python')
PASTA_ORIGINAL = os.path.join(PYTHON, "copiar_arquivo")
NOVA_PASTA = os.path.join(PYTHON, "nova_pasta")


os.makedirs(NOVA_PASTA, exist_ok=True)


for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)

        shutil.copy(caminho_arquivo, caminho_novo_arquivo)
