class Foo:
    def __init__(self):
        self.publico = "isso e publico"
        self._protected = "isso e protegido"
        self.__private = "isso e private"

    def metodo_publico(self):
        self._metodo_protected()
        self.__metodo_private()
        print(self.__private)
        return "metodo_publico"

    def _metodo_protected(self):
        print("_metodo_protected")
        return "metodo_protected"

    def __metodo_private(self):
        print("__metodo_private")
        return "__metodo_private"


f = Foo()
print(f.publico)
print(f.metodo_publico())
# print(f._protected)
# print(f._metodo_protected())
