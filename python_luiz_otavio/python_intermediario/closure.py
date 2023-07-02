def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}"
    return saudar


s1 = criar_saudacao("bom dia")("pedro")
s2 = criar_saudacao("bom dia")
print(s1)
print(s2("Lucas"))
