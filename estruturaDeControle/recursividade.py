def imprimir(maximo, atual):
    if atual < maximo:
        print(atual, end=",")
        imprimir(maximo, atual + 1)


def fibonacci(quantidade, sequencia=(0, 1)):
    if len(sequencia) == quantidade:
        return sequencia
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))


imprimir(5, 1)

if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=",")
