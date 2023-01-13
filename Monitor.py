
from pygame import display
from pygame.locals import RESIZABLE

class Monitor:
    def __init__(self, COMPRIMENTO, ALTURA):
        self.tela = display.set_mode((COMPRIMENTO, ALTURA), RESIZABLE)

    def AtualizarTela(self):
        display.flip()

    def PintarTela(self, COR):
        self.tela.fill(COR)
