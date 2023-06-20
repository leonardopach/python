# print(dir(str))
nome = "Leonardo"
print(nome)
print(nome[0])

doc = """Texto multiplas \n\t...linhas"""
print(doc)

nome = "Ana Paula"
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[4:])
print(nome[0:-4])
print(nome[:3])

numeros = '1234567'
print(int(numeros[2]) + int(numeros[1]))
print(type(int(numeros[2])))
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])

frase = "Python e uma linguagem gostosinha de programar"
print('Py' in frase)
print('py' in frase.lower())
print(len(frase))

print(frase.split())
print(frase.split('i'))

a = '123'
b = ' de Oliveira 4'
print(a + b)
print(a.__add__(b))
print(str.__add__(a, b), sep='')
