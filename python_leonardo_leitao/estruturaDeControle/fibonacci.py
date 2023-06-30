def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f"{penultimo}, {ultimo}", end=",")
    while ultimo < limite:
        proximo = penultimo + ultimo
        print(proximo, end=",")
        penultimo = ultimo
        ultimo = proximo


# Fibonacci com lista
def fibonacci2(limite):
    resultado = [0, 1]
    while resultado[-1] < limite:
        resultado.append(resultado[-2] + resultado[-1])
    return resultado


if __name__ == "__main__":
    fibonacci(20000)
    for fib in fibonacci2(20):
        print(f"{fib}")
