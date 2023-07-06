class MinhaString(str):
    def upper(self):
        print("Chamando upper")
        retorno = super(MinhaString, self).upper()
        return retorno

    def capitalize(self):
        print("Chamando capitalize")
        retorno = super(MinhaString, self).capitalize()
        return retorno


string = MinhaString("leonardo")
print(string.upper())
print(string.capitalize())


class A:
    atributo_a = "valor A"

    def metodo(self):
        print("A")


class B(A):
    atributo_b = "valor B"

    def metodo(self):
        super().metodo()
        print("B")


class C(B):
    atributo_c = "valor C"

    def metodo(self):
        super().metodo()
        print("C")


atributo = C()

print(atributo.atributo_a)
print(atributo.atributo_b)
print(atributo.atributo_c)
atributo.metodo()
print(C.mro())
