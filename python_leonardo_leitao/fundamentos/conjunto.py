a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(type(a))
print(a)
a = set('python3')
print(a)
print('3' in a, 4 not in a)

# operações
c1 = {1, 2, 3}
c2 = {2, 3}

print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)
print(c2 <= c1)  # subconjunto
print(c1 >= c2)  # superconjunto

print(c1 - c2)
