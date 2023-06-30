nome = ["Pedro", "Ana", "Jose"]
sobrenome = ['Silva', 'Peireira', 'Golçalves']
juntos = zip(nome, sobrenome)
juntos1 = zip(nome, sobrenome)
juntos2 = zip(nome, sobrenome)
# print(juntos)
# print(list(juntos))
# print(tuple(juntos1))
# print(dict(juntos2))


def dobro(x):
    return x * 2


def quadrado(x):
    return x ** 2


if __name__ == '__main__':
    funcs = [dobro, quadrado] * 5
    for func, numero in zip(funcs, range(1, 11)):
        print(f"O {func.__name__} de {numero} é {func(numero)}")
