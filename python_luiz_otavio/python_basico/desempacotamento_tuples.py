# Desempacotar
nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
nome4, *_, nome5 = ["Maria", "Helena", 1, 2, 3, "Luiz"]

print(_)
print(nome5)
print(nome1)
print(nome2)
print(nome3)
print(nome4)
print(_)

# Tuple são imutaveis

nome = ()
nomes = tuple()
nomes_tuple = "Maria", "Helena", "Luiz"
print(type(nome), type(nomes))
print(nomes_tuple)

valor = ["Maria", "Helena", 1, 2, 3, "Luiz"]

# Desempacotar com chamada de função
print(*valor)
