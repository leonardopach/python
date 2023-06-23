class Data:
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"


d1 = Data(dia=12)
d1.mes = 3
print(d1)
d2 = Data(7, 10, ano=2023)
print(d2)
