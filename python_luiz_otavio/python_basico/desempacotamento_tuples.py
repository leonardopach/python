# Desempacotar
nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
nome4, *_ = ["Maria", "Helena", "Luiz"]

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
