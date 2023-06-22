import sys
generator = (i ** 2 for i in range(10) if i % 2 == 0)
dobrosPares = [i * 2 for i in range(10) if i % 2 == 0]

dicionario = {f'Item {i}': i * 2 for i in range(10) if i % 2 == 0}
print(dicionario)
for i in generator:
    print(i)

print(f"Generator: {sys.getsizeof(generator)}kbs")
print(f"comprehension: {sys.getsizeof(dobrosPares)}kbs")
