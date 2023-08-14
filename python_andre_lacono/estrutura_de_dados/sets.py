lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

num1 = set(lista1)
num2 = set(lista2)

print(num1)
print(num2)

print(num1 | num2)  # Union
print(num1 - num2)  # Difference
print(num1 ^ num2)  # Symmetric Difference

sets = {1, 2, 3, 4, 5, 6}
sets.add(10)
sets.remove(1)
sets.update({7, 8, 9})
sets.discard(9)

print(sets)
