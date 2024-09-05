from lerMatriz import leituraMatriz
from queue import PriorityQueue

class aEstrela:
    def __init__(self, posRick, posCarl, posDaryl, posGlen, posMaggie, saida, matriz):
        self.inicio = posRick
        self.posicoes = [posCarl, posDaryl, posGlen, posMaggie, saida]
        self.matriz = matriz
        self.custo_total = 0
        self.custo_local = []

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
                    file.write('\n')
                    inicial = destino 
                with open('custo_total.txt', 'w') as file:
                    file.write('CUSTO TOTAL: ' + str(self.custo_total))


    def a_estrela(self, inicio, destino):
        dimensao = len(self.matriz)
        
        custo_heuristico = { (i, j): float('inf') for i in range(dimensao) for j in range(dimensao) }
        custo_acumulado = { (i, j): float('inf') for i in range(dimensao) for j in range(dimensao) }
        caminho = {}
        
        custo_heuristico[inicio] = 0
        custo_acumulado[inicio] = heuristica(inicio, destino)
        
        vizinhos = PriorityQueue()
        vizinhos.put((custo_acumulado[inicio], inicio))
        
        with open("custo_caminho.txt", "a") as file:
            while not vizinhos.empty():
                custo_local, celula_atual = vizinhos.get()
                if celula_atual == destino:
                    caminho_final = {}
                    while celula_atual in caminho:
                        caminho_final[caminho[celula_atual]] = celula_atual
                        celula_atual = caminho[celula_atual]
                    caminho_final[celula_atual] = destino
                    self.custo_total = self.custo_total + custo_acumulado[proxima_celula]
                    return caminho_final
                
                linha_atual, coluna_atual = celula_atual
                
                for direcao in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    proxima_celula = (linha_atual + direcao[0], coluna_atual + direcao[1])
                    
                    if (0 <= proxima_celula[0] < dimensao and 0 <= proxima_celula[1] < dimensao):
                        custo_proxima_celula = self.matriz[proxima_celula[0]][proxima_celula[1]]
                        novo_custo_heuristico = int(custo_heuristico[celula_atual]) + int(custo_proxima_celula)
                        
                        if novo_custo_heuristico < custo_heuristico[proxima_celula]:
                            caminho[proxima_celula] = celula_atual
                            custo_heuristico[proxima_celula] = novo_custo_heuristico
                            custo_acumulado[proxima_celula] = novo_custo_heuristico + heuristica(proxima_celula, destino)
                            
                            vizinhos.put((custo_acumulado[proxima_celula], proxima_celula))               
        return None

def heuristica(ponto_atual, ponto_destino):
    linha_atual, coluna_atual = ponto_atual
    linha_destino, coluna_destino = ponto_destino
    return abs(linha_destino - linha_atual) + abs(coluna_destino - coluna_atual)
        



           

