class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def print_interna(self):
        return f"Olá {self.nome} {self.sobrenome}"


p1 = Pessoa("Leonardo", "Pacheco")
print(p1.print_interna())
