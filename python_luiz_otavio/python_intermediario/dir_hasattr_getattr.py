string = "leonardo"
metodo = "capitalize"

if hasattr(string, metodo):
    print("Existe upper")
    print(getattr(string, metodo)())
print(string)
