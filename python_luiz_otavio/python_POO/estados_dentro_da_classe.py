class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f"{self.nome} Já está filmando...")
            return
        print(f"{self.nome} está filmando")
        self.filmando = True

    def parar_filmar(self):
        if self.filmando is not True:
            print(f"{self.nome} parou de filmar...")
            return
        print(f"{self.nome} não está filmando")
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar filmando...")
            return
        print(f"{self.nome} Está filmando")


c1 = Camera("Canon")
c2 = Camera("Sony")
c1.filmar()
c1.filmar()
print(c1.filmando)
c1.parar_filmar()
c1.parar_filmar()
print(f"{c1.filmando=}")
c1.fotografar()
print(c2.filmando)
