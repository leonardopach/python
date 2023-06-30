class Humano:
    especie = "Homo Sapiens"

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade < 0:
            raise ValueError("Idade deve ser um numero maior que zero")
        self._idade = idade

    def das_cavernas(self):
        self.especie = "homo das cavernas"
        return self

    @staticmethod
    def especies():
        adjetivos = ("Habilis", "Erectus", "Sapiens")
        return ("Australopiteco",) + tuple(f"Homo {adj}" for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Nearderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapies(Humano):
    especie = Humano.especies()[-1]


if __name__ == "__main__":
    jose = HomoSapies("Jose")
    jose.set_idade(20)
    print(f"Nome: {jose.nome} Idade: {jose.get_idade()}")
