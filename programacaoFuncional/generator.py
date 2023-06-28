def cores_arco_tris():
    yield "Vermelho"
    yield "Laranja"
    yield "Amarelo"
    yield "Verde"
    yield "Azul"
    yield "Indigo"
    yield "Violeta"


if __name__ == "__main__":
    gerator = cores_arco_tris()
    print(type(gerator))
    for x in gerator:
        print(x)
