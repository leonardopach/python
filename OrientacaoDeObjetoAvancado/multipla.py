class Animal:
    @property
    def capacidade(self):
        return ("dormir", "comer", "beber")


class Homem(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ("Amar", "Falar", "estudar")


class Aranha(Animal):
    @property
    def capacidade(self):
        return super().capacidade + ("fazer teia", "andar pelas paredes")


class HomeAranha(Homem, Aranha):
    @property
    def capacidade(self):
        return super().capacidade + \
            ("Bater em bandidos", "Atirar teias entre os predios")


if __name__ == "__main__":
    john = Homem()
    print(f"Aranha : {john.capacidade}")

    aranha = Aranha()
    print(f"Aranha : {aranha.capacidade}")

    peter = HomeAranha()
    print(f"Peter Parker : {peter.capacidade}")
