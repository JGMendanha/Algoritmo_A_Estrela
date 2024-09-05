import pygame
import sys

def exibir_matriz_com_label(matriz, informacao):
    pygame.init()

    dimensao_celula = 20
    linhas = len(matriz)
    colunas = len(matriz[0])
    largura_janela = colunas * dimensao_celula
    altura_janela = linhas * dimensao_celula

    tela = pygame.display.set_mode((largura_janela, altura_janela))
    pygame.display.set_caption("Matriz com Label")

    fonte = pygame.font.SysFont(None, 36)  # Cria uma fonte
    cor_texto = (255, 255, 255)  # Cor do texto (branco)

    def valor_para_cor(valor):
        if valor == 1:
            return (64, 64, 64)
        elif valor == 3:
            return (205, 133, 63)
        elif valor == 5:
            return (144, 238, 144)
        elif valor == 10:
            return (192, 192, 192)
        elif valor == 99:
            return (0, 0, 139)
        else:
            return (255, 255, 255)

    def desenhar_matriz():
        for i in range(linhas):
            for j in range(colunas):
                valor = matriz[i][j]
                cor = valor_para_cor(valor)
                pygame.draw.rect(tela, cor, pygame.Rect(j * dimensao_celula, i * dimensao_celula, dimensao_celula, dimensao_celula))

    def desenhar_label():
        texto = fonte.render(informacao, True, cor_texto)
        tela.blit(texto, (largura_janela - texto.get_width() - 10, 10))  # Posiciona o texto no canto superior direito

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill((0, 0, 0))  # Limpa a tela com a cor preta
        desenhar_matriz()
        desenhar_label()
        pygame.display.flip()

import random
matriz_exemplo = [[random.choice([1, 3, 5, 10, 99]) for _ in range(42)] for _ in range(42)]

informacao = "Informação no canto superior direito"
exibir_matriz_com_label(matriz_exemplo, informacao)
