class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

    def get_cor(self):
        return self.cor_tinta


caneta = Caneta("Azul")
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)

print(caneta.get_cor())
