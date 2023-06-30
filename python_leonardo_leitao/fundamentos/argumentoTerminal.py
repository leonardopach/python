from math import pi
import sys


class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print(TerminalColor.ERRO, f"""
            E necessario informar o raio do circulo
        Sintaxe: {sys.argv[0][2:]} <raio>""", TerminalColor.NORMAL)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print(f"Area do circulo, {area}")
