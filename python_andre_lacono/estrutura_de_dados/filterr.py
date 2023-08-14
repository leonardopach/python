lista1 = [1, 2, 3, 4, 5, 6, 7, 8]


filterr = filter(lambda x: x % 2 == 0, lista1)


print(list(filterr))
