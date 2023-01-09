import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

width = 640
height = 480

x = width/2
y = height/2

# define variáveis do rect_blue
# randint escolhe valor aleatório entre dois parâmetros
# valores já desconsiderando valores do rect
x_blue = randint(40, 600)
y_blue = randint(50, 430)

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

    # caso segurando a tecla
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    rect_red = pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))

    # adiciona rect azul
    rect_blue = pygame.draw.rect(screen, (0, 0, 255), (x_blue, y_blue, 40, 50))

    # verificando se rect_red encosta(colliderect, colisão) no rect_blue
    # td vez que colidir, rect_blue muda de posição aleatoriamente
    if rect_red.colliderect(rect_blue):
        x_blue = randint(40, 600)
        y_blue = randint(50, 430)

    pygame.display.update()
