def saudacao(msg, nome):
    return f"{msg}, {nome}"


def executa(funcao, *args):
    return funcao(*args)


saudacao_2 = saudacao

v = executa(saudacao_2, "hello 2", "leonardo")

print(v)
