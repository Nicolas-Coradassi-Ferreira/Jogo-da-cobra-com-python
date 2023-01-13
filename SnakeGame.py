
import pygame
from pygame.locals import *
from Monitor import Monitor
from Snake import Snake
from Maca import Maca, PosicaoAleatoria

def Colisao(posicaoObjeto1, posicaoObjeto2):

    if posicaoObjeto1 == posicaoObjeto2:
        return True



pygame.init()

monitor = Monitor(600, 600)

acaoUsuario = ""

Relogio = pygame.time.Clock()

snake = Snake()

maca = Maca()

while acaoUsuario != "SAIR":

    Relogio.tick(30)
    monitor.PintarTela((225,225,225))

    for event in pygame.event.get():

        if event.type == QUIT:
            acaoUsuario = "SAIR"

        elif event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                acaoUsuario = "SAIR"

            elif event.key == K_w or event.key == K_UP:
                snake.direcao = "CIMA"

            elif event.key == K_a or event.key == K_LEFT:
                snake.direcao = "ESQUERDA"

            elif event.key == K_s or event.key == K_DOWN:
                snake.direcao = "BAIXO"

            elif event.key == K_d or event.key == K_RIGHT:
                snake.direcao = "DIREITA"


    #movimenta a cabeça da cobra
    if snake.direcao == "CIMA":
        snake.seguimentos[0] = (snake.seguimentos[0][0], snake.seguimentos[0][1] - 10)#definindo posição x e y da cabeça da cobra

    elif snake.direcao == "ESQUERDA":
        snake.seguimentos[0] = (snake.seguimentos[0][0] - 10, snake.seguimentos[0][1])

    elif snake.direcao == "BAIXO":
        snake.seguimentos[0] = (snake.seguimentos[0][0], snake.seguimentos[0][1] + 10)

    elif snake.direcao == "DIREITA":
        snake.seguimentos[0] = (snake.seguimentos[0][0] + 10, snake.seguimentos[0][1])


    #não deixa cobra sair da tela
    if snake.seguimentos[0][0] == 600:
        snake.seguimentos[0] = (0, snake.seguimentos[0][1])

    elif snake.seguimentos[0][0] == - 10:
        snake.seguimentos[0] = (600, snake.seguimentos[0][1])

    elif snake.seguimentos[0][1] == 600:
        snake.seguimentos[0] = (snake.seguimentos[0][0], 0)

    elif snake.seguimentos[0][1] == - 10:
        snake.seguimentos[0] = (snake.seguimentos[0][0], 600)

    #verificando se a cabeça da cobra colidiu com a maça('comeu a maça')
    if Colisao(snake.seguimentos[0], maca.posicao):
        snake.seguimentos.append(snake.seguimentos[-1])#aumenta o corpo da cobra
        maca.posicao = PosicaoAleatoria()

    snake.RenderizaSeguimentos(monitor.tela)
    maca.MostraMaca(monitor.tela)


    monitor.AtualizarTela()

pygame.quit()
