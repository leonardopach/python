from dataclasses import asdict, astuple, dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.spli()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


if __name__ == '__main__':
    p1 = Pessoa("Leonardo", "Pacheco")
    p2 = Pessoa("Leonardo", "23")
    print(p1 == p2)
    print(p1)
    print(asdict(p1).values())
    print(asdict(p1).keys())
    print(asdict(p1).items())
    print(astuple(p1)[0])
