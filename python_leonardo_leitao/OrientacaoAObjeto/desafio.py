class Carro:
    def __init__(self, velocidade_maxima):
        self.velocidade_maxima = velocidade_maxima
        self.velocidade_atual = 0

    def acelerar(self, delta):
        if self.velocidade_atual >= self.velocidade_maxima:
            self.velocidade_atual = self.velocidade_maxima
        else:
            self.velocidade_atual += delta
        return self.velocidade_atual

    def frear(self, delta):
        nova_velocidade = self.velocidade_atual - delta
        if nova_velocidade >= 0:
            self.velocidade_atual = nova_velocidade
        else:
            self.velocidade_atual = 0
        return self.velocidade_atual


c1 = Carro(180)

for _ in range(25):
    print(c1.acelerar(8))

for _ in range(10):
    print(c1.frear(25))
