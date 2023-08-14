def somarAll(*args):
    somar = 0
    for i in args:
        somar += i
    return somar


print(somarAll(1, 2, 3, 4, 5, 6))
