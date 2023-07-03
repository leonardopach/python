def criar_funcao(funcao):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = funcao(*args, **kwargs)
        print(f"o Seu resultado foi {resultado}.")
        print("Ok, agora você foi decorada")
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    print(f"{inverte_string.__name__}")
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        print("Precisa ser uma string")


invertida = inverte_string("Leonardo")
print(invertida)
