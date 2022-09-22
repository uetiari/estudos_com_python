import pygame
from pygame.locals import *
# fechar a janela
from sys import exit

# inicializar o jogo
pygame.init()

# criar a tela com tuplas
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

# altera nome da janela do jogo
pygame.display.set_caption('Game 001 em Python by Ariane Ueti')

# criar loop para sempre atualizar e rodar o jogo
# todo script deve ficar dentro do loop
while True:
    # verificando se aconteceu algum evento
    for event in pygame.event.get():
        # fechar a janela quando clicar para fechar
        if event.type == pygame.QUIT:
            # jogo fecha com a função declarada acima
            pygame.quit()
            exit()
    # desenha um retângulo na tela e cor vermelha
    # na posição de x, y, largura e altura
    pygame.draw.rect(screen, (255, 0, 0), (200, 300, 40, 50))
    # desenhandum circulo na tela e cor azul
    # na posição(centro) de x, y e no raio
    pygame.draw.circle(screen, (0, 0, 255), (300, 270), 40)
    # atualiza a tela a cada rodada do For
    pygame.display.update()
