import pygame
from pygame.locals import *
from sys import exit

pygame.init()

width = 640
height = 480

x = width/2
# altera pra começar com rect no meio da tela
y = height/2

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Game 001 em Python by Ariane Ueti')

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # quando player aperta a tecla
        ''' if event.type == KEYDOWN:
            # usando padrão WSAD
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            # pra subir tem que ser - por ser invertido
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20 '''
    # para mover rect com a tecla pressionada
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))

    pygame.display.update()
