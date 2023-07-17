import os
from itertools import count

caminho = os.path.join("/home/leonardopach/python/python_luiz_otavio")
counter = count()
for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, "Pasta atual", root)

    for dir_ in dirs:
        print(" ", the_counter, "Dir", root)

    for file_ in files:
        print("  ", the_counter, "File", file_)
