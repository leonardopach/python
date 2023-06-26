class Humano:
    especie = "Homo Sapiens"

    def __init__(self, nome):
        self.nome = nome

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
    jose = HomoSapies("José")
    grokn = Nearderthal("Grokn")
    print(
        f'Evolução (a partir de classe):{", ".join(HomoSapies.especies())}')
    print(
        f'Evolução (a partir de instancia):{", ".join(jose.especies())}')
    print(
        f'Homo Sapiens evoluido? {HomoSapies.is_evoluido()}')
    print(
        f'Homo Nearderthal evoluido? {Nearderthal.is_evoluido()}')
    print(f"José evoluido? {jose.is_evoluido()}")
    print(f"Grokn evoluido? {grokn.is_evoluido()}")
