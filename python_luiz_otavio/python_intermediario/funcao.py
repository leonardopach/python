# def teste (parametros):
#
# teste(argumento)
def imprimir(texto):
    print(f"{texto}")


def somar(x, y, z=None) -> None:
    if z is not None:
        return x + y + z
    else:
        return x + y


def saudacao(nome="ola sem nome"):
    print(nome)


valor = "Hello world"
imprimir(valor)
print(somar(2, 10))
print(somar(y=2, x=5))
saudacao("Leonardo")
saudacao()
