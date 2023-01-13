
from pygame import Surface
from random import randint

def PosicaoAleatoria():
    posicaoX = randint(0, 600)
    posicaoY = randint(0, 600)
    return (posicaoX //10 *10, posicaoY //10 *10)

class Maca:
    def __init__(self):
        self.posicao = PosicaoAleatoria()
        self.skin = Surface((10, 10))
        self.skin.fill((255, 0, 0))

    def MostraMaca(self, janela):
        janela.blit(self.skin, self.posicao)