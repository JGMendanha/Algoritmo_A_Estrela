from lerMatriz import leituraMatriz
from queue import PriorityQueue

class aEstrela:
    def __init__(self, posRick, posCarl, posDaryl, posGlen, posMaggie, saida, matriz):
        self.inicio = posRick
        self.posicoes = [posCarl, posDaryl, posGlen, posMaggie, saida]
        self.matriz = matriz

    def caminho(self):
        inicial = self.inicio.strip().split(';')
        inicial = tuple(int(ini) for ini in inicial)
        with open('caminho.txt', 'w') as file: 
            for destinos in self.posicoes:
                destino = destinos.strip().split(';')
                destino = tuple(int(dest) for dest in destino)
                caminho = self.a_estrela(inicial, destino)
                for passo in caminho:
                    file.write(str(passo) + ';')
                inicial = destino 


    def a_estrela(self, inicio, destino):
        # Definir dimensões da self.matriz
        dimensao = len(self.matriz)
        
        # Inicialização dos scores
        g_score = { (i, j): float('inf') for i in range(dimensao) for j in range(dimensao) }
        f_score = { (i, j): float('inf') for i in range(dimensao) for j in range(dimensao) }
        caminho = {}
        
        # Ponto de partida e destino
        g_score[inicio] = 0
        f_score[inicio] = heuristica(inicio, destino)
        
        # Inicialização da PriorityQueue
        vizinhos = PriorityQueue()
        vizinhos.put((f_score[inicio], inicio))
        
        while not vizinhos.empty():
            _, celula_atual = vizinhos.get()
            
            # Verificar se chegamos ao destino
            if celula_atual == destino:
                caminho_final = {}
                while celula_atual in caminho:
                    caminho_final[caminho[celula_atual]] = celula_atual
                    celula_atual = caminho[celula_atual]
                caminho_final[inicio] = destino
                return caminho_final
            
            linha_atual, coluna_atual = celula_atual
            
            # Explorar vizinhos (N, S, E, W)
            for direcao in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                proxima_celula = (linha_atual + direcao[0], coluna_atual + direcao[1])
                
                if (0 <= proxima_celula[0] < dimensao and 
                    0 <= proxima_celula[1] < dimensao):
                    
                    custo_proxima_celula = self.matriz[proxima_celula[0]][proxima_celula[1]]
                    novo_g_score = int(g_score[celula_atual]) + int(custo_proxima_celula)
                    
                    if novo_g_score < g_score[proxima_celula]:
                        caminho[proxima_celula] = celula_atual
                        g_score[proxima_celula] = novo_g_score
                        f_score[proxima_celula] = novo_g_score + heuristica(proxima_celula, destino)
                        vizinhos.put((f_score[proxima_celula], proxima_celula))
        
        return None 

def heuristica(ponto_atual, ponto_destino):
        linha_atual, coluna_atual = ponto_atual
        linha_destino, coluna_destino = ponto_destino
        return abs(linha_destino - linha_atual) + abs(coluna_destino - coluna_atual)
        



           

