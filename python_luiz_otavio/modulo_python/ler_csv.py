import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / "arquivo.csv"


with open(CAMINHO_CSV, "r") as file:
    leitor2 = csv.DictReader(file)

    for linha in leitor2:
        print(linha)

print("*" * 90)

# with open(CAMINHO_CSV, 'r') as file:
#     leitor = csv.reader(file)

#     for linha in leitor:
#         print(linha)
