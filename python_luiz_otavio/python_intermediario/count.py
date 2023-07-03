from itertools import count

# Count iterators infinito
c1 = count(10, 8)
r1 = range(10)

for i in c1:
    if i >= 100:
        break
    print(i)

for i in r1:
    print(i)
