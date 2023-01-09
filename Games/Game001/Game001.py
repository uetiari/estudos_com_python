import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
# ajustar valores entre 0 e 1
pygame.mixer.music.set_volume(0.1)
# exceto música de fundo, TDS outros sons necessitam ser .wav
soundtrack = pygame.mixer.music.load('/home/ariane/Área de Trabalho/PYGAMES/estudos_com_python/Games/Game001/BoxCat Games - CPU Talk.mp3')
# música em loop usar -1 
pygame.mixer.music.play(-1)

colider = pygame.mixer.Sound('/home/ariane/Área de Trabalho/PYGAMES/estudos_com_python/Games/Game001/smw_coin.wav')
# colider.set_volume(1)

width = 640
height = 480

x = int(width/2)
y = int(height/2)

x_blue = randint(40, 600)
y_blue = randint(50, 430)

# criando texto. Font Family, Size, Bold, Italic
font = pygame.font.SysFont('Verdana', 30, True, False)
points = 0

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Game 001 em Python by Ariane Ueti')

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    screen.fill((0, 0, 0))
    # o que será escrito na tela
    msg = f'Points: {points}'
    # texto formatado. True para antialias, não deixa serrilhado, 255 cores
    format_text = font.render(msg, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    rect_red = pygame.draw.rect(screen, (255, 0, 0), (x, y, 40, 50))

    rect_blue = pygame.draw.rect(screen, (0, 0, 255), (x_blue, y_blue, 40, 50))

    if rect_red.colliderect(rect_blue):
        x_blue = randint(40, 600)
        y_blue = randint(50, 430)
        points = points + 1
        colider.play()

    # recebe o texto que será exibido, e localização em X e Y
    screen.blit(format_text, (450, 40))

    pygame.display.update()
