class Pessoa:
    ano = 2023

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("hey")

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls("Anônima", idade)


p1 = Pessoa("João", 24)
p2 = Pessoa.criar_com_50_anos("Higor")
p3 = Pessoa.criar_sem_nome(24)
print(Pessoa.ano)
Pessoa.metodo_de_classe()
print(p2.nome, p2.idade)
print(p3.idade, p3.nome)
