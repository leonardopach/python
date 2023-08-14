from datetime import datetime


class Funcionarios:
    def __init__(self, idade, nome, ano_nascimento) -> None:
        self.idade = idade
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def calcular_idade(self):
        ano = self.ano_nascimento.split("/")
        ano_pessoa = datetime.today().year - int(ano[len(ano) - 1])
        return ano_pessoa

    def __str__(self):
        return f"olá {self.nome}, e tenho {self.idade}"

    def somar(self, x, y):
        return x + y


if __name__ == "__main__":
    ps1 = Funcionarios(25, "leonardo", "17/02/1998")
    print(ps1.calcular_idade())
    print(ps1)
    print(ps1.nome)
