from a_estrela import aEstrela
from lerMatriz import leituraMatriz
import interface  as it

def configuracao_padrao():
    
    matriz = leituraMatriz()

    posRick = '21;13'  
    posCarl = '5;32'  
    posDaryl = '35;35' 
    posGlen = '32;8'  
    posMaggie = '13;31'
    saida = '41;21'    

    a = aEstrela(posRick, posCarl, posDaryl, posGlen, posMaggie, saida, matriz)
    a.caminho()
    caminho = it.caminho_final()
    vetPosicoes = [posCarl, posDaryl, posGlen, posMaggie, saida]
    it.animacao_final(matriz,  caminho, vetPosicoes)

def configuracao_personalizada():

    matriz = leituraMatriz()

    posRick = input('DIGITE A POSIÇÃO INICIAL DE RICK SEPARANDO POR PONTO E VIRGULA (EXEMPLO: 1;1): ')  
    posCarl = input('DIGITE A POSIÇÃO DE CARL SEPARANDO POR PONTO E VIRGULA (EXEMPLO: 1;1): ')  
    posDaryl = input('DIGITE A POSIÇÃO DE DARYL SEPARANDO POR PONTO E VIRGULA (EXEMPLO: 1;1): ') 
    posGlen = input('DIGITE A POSIÇÃO DE GLEN SEPARANDO POR PONTO E VIRGULA (EXEMPLO: 1;1): ')  
    posMaggie = input('DIGITE A POSIÇÃO DE MAGGIE SEPARANDO POR PONTO E VIRGULA (EXEMPLO: 1;1): ')
    saida = input('DIGITE A POSIÇÃO DE SAÍDA SEPARANDO POR PONTO E VIRGULA (EXEMPLO: 1;1): ')

    a = aEstrela(posRick, posCarl, posDaryl, posGlen, posMaggie, saida, matriz)
    a.caminho()

    caminho = it.caminho_final()

    vetPosicoes = [posCarl, posDaryl, posGlen, posMaggie, saida]
    it.animacao_final(matriz, caminho, vetPosicoes)


print("BEM VINDO AO TESTE DO ALGORITMO A*\nSELECIONE QUAL CONFIGURAÇÃO DESEJA FAZER:")
escolha = int(input('SELECIONE 1 PARA USAR A CONFIGURAÇÃO PADRÃO OU 2 PARA SUA PRÓPRIA CONFIGURAÇÃO: '))

if escolha == 1:
    configuracao_padrao()
else: 
    configuracao_personalizada()

