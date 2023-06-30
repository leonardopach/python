from decimal import Decimal, getcontext
print()

a = 5
b = 2.5
print(a / b)
print(a + b)
print(a * b)
print(type(a))
print(type(b))
print(type(a - b))

print(b.is_integer())
print(5.0.is_integer())
print(int.__add__(2, 3))
print((-3.6).__abs__())
print(1.1 + 2.2)
getcontext().prec = 10
print(Decimal(1) / Decimal(7))
print(dir())
