texto = "Aqui tem um pedaço da historia"
print(f"Em algum momento da Historia, {texto}")


# > - Esquerda
# < - Direira
# ^ - Centro

variavel = "ABC"

print(f"{variavel}")
print(f"{variavel: >10}")
print(f"{variavel: <10}")
print(f"{variavel: ^10}")
print(f"{1000.716234123:,.1f}")
print(f"{-1000.716234123:,.1f}")
print(f"{1000.716234123:+,.1f}")
print(f"{1000.716234123:0=+10,.1f}")
print("O hexadecimal de %d é %08X"% (1500, 1500))