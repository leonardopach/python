import os
import shutil

# mover/Renomear -> shutil.move

HOME = os.path.expanduser('~')
PYTHON = os.path.join(HOME, 'python')
PASTA_ORIGINAL = os.path.join(PYTHON, "copiar_arquivo")
NOVA_PASTA = os.path.join(PYTHON, "nova_pasta")


shutil.rmtree(NOVA_PASTA)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA, NOVA_PASTA + ' Eita')
