import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'arquivo_escrever.csv'

lista_client = [
    {"nome": "Leonardo2", "idade": 25},
    {"nome": "Bruna", "idade": 30},
    {"nome": "Renata", "idade": 22},
    {"nome": "Leia", "idade": 51},
]

# Dicionario
with open(CAMINHO_CSV, 'w') as file:
    nome_colunhas = lista_client[0].keys()
    escritor = csv.DictWriter(file,
                              fieldnames=nome_colunhas)

    escritor.writeheader()

    for cliente in lista_client:
        escritor.writerow(cliente)

# por lista
# with open(CAMINHO_CSV, 'w') as file:
#     nome_colunhas = lista_client[0].keys()
#     escritor = csv.writer(file)

#     escritor.writerow(nome_colunhas)

#     for cliente in lista_client:
#         escritor.writerow(cliente.values())

with open(CAMINHO_CSV, 'r') as file:
    leitor2 = csv.DictReader(file)

    for linha in leitor2:
        print(linha)
