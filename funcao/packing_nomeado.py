def resultado_f1(**podium):
    for posicao, piloto in podium.items():
        print(f"{posicao} -> {piloto}")


if __name__ == '__main__':
    resultado_f1(primeiro="L. Hamilton",
                 terceiro="S. Vettel",
                 segundo="M. Verstappen",)
