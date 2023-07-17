import json
from class_para_salvar_json import db, Pessoa

arquivo = "salvando_json.json"

with open(arquivo, "w") as file:
    json.dump(db, file, ensure_ascii=True, indent=True)


with open(arquivo, "r") as file:
    pessoas = json.load(file)
    p1 = Pessoa(**pessoas[0])
    print(p1.nome, p1.idade)
    # for pessoa in pessoas
