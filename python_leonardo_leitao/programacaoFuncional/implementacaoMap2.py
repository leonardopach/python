def mapear(funcao, lista):
    return (funcao(elemento) for elemento in lista)


if __name__ == '__main__':
    print(list(mapear(lambda x: x ** 2, [1, 2, 3])))
    valor = {f'teste: {valor}': valor for valor in range(10)}
    print(dict(valor))
