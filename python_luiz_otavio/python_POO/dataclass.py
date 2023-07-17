from dataclasses import asdict, astuple, dataclass, field


@dataclass
class Pessoa:
    nome: str = field(default="Missing", repr=False)
    sobrenome: str = "not sent"
    idade: int = 100
    endereco: list[str] = field(default_factory=list)

    @property
    def nome_completo(self):
        return f"{self.nome} {self.sobrenome}"

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.spli()
        self.nome = nome
        self.sobrenome = " ".join(sobrenome)


if __name__ == "__main__":
    p1 = Pessoa()
    print(p1)
    print(asdict(p1).values())
    print(asdict(p1).keys())
    print(asdict(p1).items())
    print(astuple(p1)[0])
