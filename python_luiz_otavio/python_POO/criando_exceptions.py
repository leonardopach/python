class MeuErro(Exception):
    ...


class OutroErro(Exception):
    ...


def levantar():
    expection_ = MeuErro("A", "B", "B")
    expection_.add_note("Olha a nota 1")
    expection_.add_note("Você errou isso")
    raise expection_


try:
    levantar()
except (MeuErro, ZeroDivisionError) as erro:
    print(erro.__class__.__name__)
    print(erro)
    print()
    Exception_ = OutroErro("Vou lançar de novo")
    raise Exception_ from erro
