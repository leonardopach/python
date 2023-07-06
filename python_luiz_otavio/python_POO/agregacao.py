class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produto(self, *produtos):
        self._produtos.extend(produtos)

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)
p3, p4 = Produto('Caderno', 1.20), Produto('Relógio', 20)
carrinho.inserir_produto(p1, p2, p3, p4)
carrinho.listar_produtos()
