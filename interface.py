import pygame
import sys
from lerMatriz import leituraMatriz

def animacao_final(matriz, posicoes_finais, vetPosicoes):
    custo_atual = 0
    pygame.init()

    dimensao_celula = 20
    linhas = len(matriz)
    colunas = len(matriz[0])
    largura_janela = colunas * dimensao_celula
    altura_janela = linhas * dimensao_celula

    custos = calculoCustosFinais(vetPosicoes)

    tela = pygame.display.set_mode((largura_janela, altura_janela))
    pygame.display.set_caption("Matriz Colorida com Animação")

    fonte = pygame.font.SysFont(None, 36)
    cor_texto = (0, 0, 0)

    desenhar_matriz(linhas, colunas, tela, dimensao_celula, matriz)

    pygame.display.flip()

    indice_custo = 0

    for pos in posicoes_finais:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        linha, coluna = pos

        pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(coluna * dimensao_celula, linha * dimensao_celula, dimensao_celula, dimensao_celula))

        if indice_custo < len(custos):
            custo_atual = custo_atual + custos[indice_custo]
            texto = fonte.render(f'Custo atual = {custo_atual}', True, cor_texto)
            tela.blit(texto, (10, 10))
            indice_custo += 1

        pygame.display.flip()

        pygame.time.delay(200)

        tela.fill((255, 255, 255))
        desenhar_matriz(linhas, colunas, tela, dimensao_celula, matriz)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def desenhar_matriz(linhas, colunas, tela, dimensao_celula, matriz):
    for i in range(linhas):
        for j in range(colunas):
            valor = matriz[i][j]
            cor = valor_para_cor(valor)
            pygame.draw.rect(tela, cor, pygame.Rect(j * dimensao_celula, i * dimensao_celula, dimensao_celula, dimensao_celula))

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

def desenhar_label(tela, fonte, cor_texto, informacao):
    texto = fonte.render(informacao, True, cor_texto)
    tela.blit(texto, (10, 10)) 

def caminho_final():
    caminho_final = []
    with open('caminho.txt', 'r') as file:
        for linha in file:
            linha = linha.strip().split(';')
            linha = linha[::-1]
            for i in range(len(linha) - 1):
                tupla = eval(linha[i + 1])
                caminho_final.append(tupla)
    return caminho_final

def calculoCustosFinais(vetPos):
    matriz = leituraMatriz()
    custos = []
    i = 0
    with open('caminho.txt', 'r') as file:
        with open('custos.txt', 'a') as file:
            for linha in file:
                linha = linha.strip().split(';')
                linha = linha[::-1]
                linha = linha[1:]
                for j in range(len(linha)):
                    tuplaObjetivo = tuple(int(item) for item in vetPos[i].split(';'))
                    tuplaAtual = tuple(int(item) for item in linha[j].strip('()').split(','))
                    linha_atual, coluna = tuplaAtual
                    custoTuplaAtual = int(matriz[linha_atual][coluna])
                    heuristica_valor = heuristica(tuplaAtual, tuplaObjetivo)
                    total = custoTuplaAtual + heuristica_valor
                    custos.append(total)
                i += 1
    return custos


def heuristica(ponto_atual, ponto_destino):
    linha_atual, coluna_atual = ponto_atual
    linha_destino, coluna_destino = ponto_destino
    return abs(linha_destino - linha_atual) + abs(coluna_destino - coluna_atual)

