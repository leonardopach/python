print(sum([1, 2, 3]))
# Fibonacci com lista


def fibonacci2(limite):
    resultado = [0, 1]
    for _ in range(2, limite):
        resultado.append(sum(resultado[-2:]))
    return resultado


if __name__ == "__main__":
    for fib in fibonacci2(20):
        print(f"{fib}", end=",")
