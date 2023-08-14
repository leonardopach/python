def somar(x):
    func2 = lambda x: x + 10
    return func2(x) * 10


print(somar(2))

somar2 = lambda x, y: x + y
print(somar2(2, 15))
