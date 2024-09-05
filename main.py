from a_estrela import aEstrela
from lerMatriz import leituraMatriz

def testar_a_estrela():
    # Definição da matriz (0 = caminho livre, 1 = obstáculo)
    matriz = leituraMatriz()

    posRick = '25;15'  
    posCarl = '5;32'  
    posDaryl = '35;6' 
    posGlen = '15;25'  
    posMaggie = '41;35'
    saida = '41;21'    

    a = aEstrela(posRick, posCarl, posDaryl, posGlen, posMaggie, saida, matriz)
    a.caminho()

    with open('matrizfinal.txt', 'w') as file: 
        with open('caminho.txt', 'r') as file2:
            for i in range(42):
                for j in range(42):
                    for linha in file2:
                        caminho = linha.strip().split(';')
                    teste = str((i,j))
                    if teste in caminho:
                        file.write('**' + ';')
                    elif matriz[i][j] == 5:
                        file.write('05' + ';')
                    elif matriz[i][j] == 3:
                        file.write('03' + ';')
                    elif matriz[i][j] == 1:
                        file.write('01' + ';')
                    elif matriz[i][j] == 10:
                        file.write('10' + ';')
                    elif matriz[i][j] == 99:
                        file.write('99' + ';')
                file.write('\n')

# Executar a função de teste
testar_a_estrela()
