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
    # atualiza a tela a cada rodada do For
    pygame.display.update()