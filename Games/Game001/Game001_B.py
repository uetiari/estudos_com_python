import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
height = 480

# variável iniciando rect no meio da tela
x = width/2
# variável iniciando em 0 para controle do movimento rect
y = 0

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Game 001 em Python by Ariane Ueti')

# para controlar velocidade baseado no frames
clock = pygame.time.Clock()

while True:
    # usar frames por segundos
    # qnt maior frames mais rápido
    clock.tick(30)
    # para que preencha de volta com a cor preta
    # ilusão do movimento do rect
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # chamando as variáveis na tupla
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))
    # com o if ele retorna a posição 0
    # fazendo o movimento recomeçar
    if y >= height:
        y = 0
    # a cada iteração do for
    # vai mudar diretamente na variável y
    y = y + 5

    pygame.display.update()
