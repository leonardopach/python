class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print("Apagando, ", self.nome)


class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("Apagando, ", self.rua, self.numero)


cliente1 = Cliente("Maria")
cliente1.inserir_endereco("Av brasil", 85)
cliente1.inserir_endereco("Rua B", 8565)

cliente1.listar_endereco()
del cliente1
print("Programa termina aqui")
