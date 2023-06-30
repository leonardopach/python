dicionario = {"nome": "Leonardo", "idade": 25,
              "Cursos": ['inglês', 'Português']}

print(dicionario["Cursos"][0])
print(dicionario["nome"])
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
print(dicionario.get('idade'))

pessoa = {"nome": "Leonardo", "idade": 25,
          "Cursos": ['react', 'python']}

pessoa['idade'] = 44
pessoa['Cursos'].append("Angular")
print(pessoa["idade"])
print(pessoa["Cursos"])
pessoa.pop("idade")
print(pessoa)
pessoa.update({"idade": 25, "Sexo": "M"})
print(pessoa)
del pessoa["Cursos"][0]
print(pessoa)
pessoa.clear()
print(pessoa)
