from abc import ABCMeta


class Humano(metaclass=ABCMeta):
    especie = "Homo Sapiens"

    def __init__(self, nome):
        self.nome = nome
        self._idade = None

    @property
    def inteligente(self):
        pass

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
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

    @property
    def inteligente(self):
        return False


class HomoSapies(Humano):
    especie = Humano.especies()[-1]

    @property
    def inteligente(self):
        return True


if __name__ == "__main__":

    try:
        anonimo = Humano("John Doe")
        print(anonimo.inteligente)
    except TypeError:
        print("Propriedade abstrata")

    jose = HomoSapies("José")
    print("{} de classe {}, inteligente {}".format(
        jose.nome, jose.__class__.__name__, jose.inteligente))
    gronk = Nearderthal("Gronk")
    print("{} de classe {}, inteligente {}".format(
        gronk.nome, gronk.__class__.__name__, gronk.inteligente))
