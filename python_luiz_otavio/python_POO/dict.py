class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


dados = {"nome": "leonardo", "idade": 25}
p1 = Pessoa(**dados)

# p1.__dict__['outra'] = "coisa"
# p1.__dict__['nome'] = "Eita"

# print(p1.__dict__)
print(vars(p1))
