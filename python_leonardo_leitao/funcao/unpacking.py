def soma_2(a, b):
    return a + b


def soma_3(a, b, c):
    return a + b + c


def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma_2(2, 3))
    print(soma_3(2, 4, 6))

    # packing
    print(soma_n(2))
    print(soma_n(2, 2))
    print(soma_n(2, 2, 2, 3, 4, 5))

    # unpacking
    tupla_nums = (3, 3, 3)
    print(soma_3(*tupla_nums))
    lista_nums = [3, 3, 5]
    print(soma_3(*lista_nums))
