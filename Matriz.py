import random
import numpy as np
import multiprocessing

def matriz_randomica(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(0,9))
        matriz.append(linha)
    return matriz

def calcula_elemento(matriz1, matriz2, linha, coluna, aux_num, shape):
    for el in range(len(shape[1])):
        aux_num.value += matriz1[linha][el] * matriz2[el][coluna]
    
def sequencial(matriz1, matriz2, shape):
    resultado = shape.copy()
    for linha in range(len(shape[0])):
        for coluna in range(len(shape[1])):
            aux_num = 0
            for el in range(len(shape[1])):
                aux_num += matriz1[linha][el] * matriz2[el][coluna]
            resultado[linha][coluna] = aux_num
    return resultado

def multi_processo(matriz1, matriz2, shape):
    aux_num = multiprocessing.Value('i', 0)    
    resultado = shape.copy()
    for linha in range(len(shape[0])):
        for coluna in range(len(shape[1])):
            filho = multiprocessing.Process(
                target=calcula_elemento, 
                args=(matriz1, matriz2, linha, coluna, aux_num, shape),
            )
            filho.start()
            resultado[linha][coluna] = aux_num.value
            aux_num.value = 0
    return resultado

def multi_thread(matriz1, matriz2, shape):
    pass