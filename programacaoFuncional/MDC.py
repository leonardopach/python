def mdc(numeros):
    def calc(divisors):
        return divisors if sum(map(lambda x: x % divisors, numeros)) == 0 \
            else calc(divisors - 1)
    return calc(min(numeros))


if __name__ == '__main__':
    print(mdc([21, 7]))
    print(mdc([125, 40]))
    print(mdc([55, 22]))
