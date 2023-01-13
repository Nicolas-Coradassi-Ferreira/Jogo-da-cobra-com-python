
from pygame import Surface

class Snake:
    def __init__(self):
        self.seguimentos = [(300, 50), (300, 40), (300, 30), (300, 20), (300, 10)]
        self.skin = Surface((10,10))
        self.skin.fill((0, 255, 0))
        self.direcao = "BAIXO"

    def RenderizaSeguimentos(self, janela):

        for posicao in self.seguimentos:
            janela.blit(self.skin, posicao)

        for seguimento in range(-1, -(len(self.seguimentos)), -1):
            self.seguimentos[seguimento] = (self.seguimentos[seguimento - 1][0], self.seguimentos[seguimento - 1][1])

