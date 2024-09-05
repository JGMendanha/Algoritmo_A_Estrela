def leituraMatriz():
    j = 0
    matriz = [['0' for _ in range(42)] for _ in range(42)]
    with open('matriz.txt', 'r') as file:
        for linha in file:
            valor = linha.strip().split(';')
            for i in range(0,41):
                matriz[j][i] = int(valor[i])
            j += 1
    return matriz

def leituraMatrizPersonalizada():
    j = 0
    matriz = [['0' for _ in range(42)] for _ in range(42)]
    with open('matriz_editavel.txt', 'r') as file:
        for linha in file:
            valor = linha.strip().split(';')
            for i in range(0,41):
                matriz[j][i] = int(valor[i])
            j += 1
    return matriz
