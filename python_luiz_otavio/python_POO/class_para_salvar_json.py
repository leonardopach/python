class Pessoa:
    def __init__(self, nome, idade, endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.endereco = endereco


dados = {"nome": "Leonardo", "idade": 25, "endereco": 'Rua tal'}
p1 = Pessoa(**dados)
dados2 = {"nome": "Pedro", "idade": 15, "endereco": 'Rua x'}
p2 = Pessoa(**dados2)
dados3 = {"nome": "Gabriela", "idade": 23, "endereco": 'Rua y'}
p3 = Pessoa(**dados3)

db = [vars(p1), p2.__dict__, p3.__dict__]
