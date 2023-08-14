def bacon_com_ovos(n):
    assert isinstance(n, int), "n deve"

    if n % 3 == 0 and n % 5 == 0:
        return "Bacon com ovos"
    return "Passar fome"
