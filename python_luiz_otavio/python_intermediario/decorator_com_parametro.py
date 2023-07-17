def decoradora(func):
    print("Decoradora 1")

    def aninhada(*args, **kwargs):
        print("Aninhada")
        res = func(*args, **kwargs)
        return res

    return aninhada


@decoradora
def soma(x, y):
    return x + y


multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
print(multiplica(10, 5))
