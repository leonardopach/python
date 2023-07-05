class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome
        variavel = "valor"
        print(variavel)

    def comendo(self, alimento):
        return f"{self.nome} Está comendo {alimento}"

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)


leao = Animal(nome="Leão")
print(leao.nome)
print(leao.executar("Zebra"))
