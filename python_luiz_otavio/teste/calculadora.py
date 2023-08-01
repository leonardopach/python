def somar(x, y):
    """Soma x e y

    >>> somar(10, 30)
    40
    """
    assert isinstance(x, (int, float)), "x precisa ser int ou float"
    assert isinstance(y, (int, float)), "y precisa ser int ou float"
    return x + y


if __name__ == "__main__":
    result = somar(2, 3)
    print(result)
    import doctest

    doctest.testmod(verbose=True)
