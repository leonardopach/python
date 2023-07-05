string = "Luiz"
print(string.upper())
print(isinstance(string, str))


class Pessoa:
    ...


p1 = Pessoa()
p1.nome = "Leonardo"
p1.sobrenome = "Pacheco"

p2 = Pessoa()
p2.nome = "Rebeca"
p2.sobrenome = "SIlva"

print(p1.nome)
print(p1.sobrenome)
print(p1)

print(p2.nome)
print(p2.sobrenome)
