import csv

with open("pessoas.csv") as entrada:
    for pessoas in csv.reader(entrada):
        print("Nome: {}, idade: {}".format(*pessoas))
