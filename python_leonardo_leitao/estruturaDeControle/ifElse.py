
def nota_conceito(notas):
    if notas >= 10.0:
        return "Nota Invalida"
    elif notas >= 9.1:
        return "A-"
    elif notas >= 8.1:
        return "B"
    elif notas >= 7.1:
        return "B-"
    elif notas >= 6.1:
        return "C"
    elif notas >= 5.1:
        return "C-"
    elif notas >= 4.1:
        return "D"
    elif notas >= 3.1:
        return "D-"
    elif notas >= 2.1:
        return "E"
    elif notas >= 1.1:
        return "E-"
    elif notas >= 0:
        return "E-"
    else:
        return "Nota Invalida"


if __name__ == "__main__":
    notas = float(input("Qual a nota do Aluno: "))
    conceito = nota_conceito(notas)
    print(conceito)
