s1 = set("leonardo")
print(s1, type(s1))
s2 = {"Luiz", 1, 2, 3}
print(s2, type(s2))

s1 = set()  # vazio
s1 = {"Luiz", 1, 2, 3}  # com dados

s1 = {1, 2, 3, 4, 3, 3, 3, 2, 1, 4}
print(s1)
print(4 in s1)
for numero in s1:
    print(numero, end=", ")
print("\nPulando linha")
l1 = [1, 2, 3, 4, 3, 2, 1, 4, 2]
s1 = set(l1)
l2 = list(s1)
print(l2)

s1 = set()
s1.add("Leonardo")
print(s1)
s1.update(("Ola mundo", 1, 2, 3, 4))
print(s1)
s1.discard("Leonardo")
print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1.union(s2)
print(s3)
s3 = s1.intersection(s2)
print(s3)
s3 = s1.difference(s2)
print(s3)
s3 = s1 ^ s2
print(s3)
