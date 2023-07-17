import sys

letras = ["eu", "sou", "um", "futuro", "programador"]
iterator = iter(letras)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

generator = (n for n in range(1000))
lista = [n for n in range(1000)]
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


def generator(numero=0, maximo=10):
    while True:
        yield numero
        numero += 1
        if numero > maximo:
            return


gen = generator()
for n in gen:
    print(n)
