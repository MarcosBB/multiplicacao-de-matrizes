from Matriz import Matriz
import time
import numpy as np
import os
import ctypes
import sys
import multiprocessing

def calculaElemento(matriz1, matriz2, linha, coluna, aux_num):
    for el in range(np.shape(matriz2)[1]):
        aux_num.value += matriz1[linha][el] * matriz2[el][coluna]

def forks(matriz1, matriz2):
    print("Matriz esperada: \n", np.dot(matriz1, matriz2), "\n")
    aux_num = multiprocessing.Value('i', 0)
    resultado = np.zeros((np.shape(matriz1)[0], np.shape(matriz2)[1]), dtype=int)
    if (np.shape(matriz1)[0] != np.shape(matriz2)[1]):
        print("Não é possível multiplicar as duas matrizes")
    else:
        comeco = time.time()
        for linha in range(0,np.shape(matriz1)[0]):
            for coluna in range(0,np.shape(matriz2)[1]):
                filho = multiprocessing.Process(target=calculaElemento, args=(matriz1,matriz2,linha,coluna,aux_num))
                filho.start()
                resultado[linha][coluna] = aux_num.value
                aux_num.value = 0
        fim = time.time()
        tempo_decorrido = float((fim - comeco))
        print("Matriz Resultante: \n", resultado)
        print("\n A multiplicação levou um total de ", tempo_decorrido, " segundos.")
        return tempo_decorrido
    
def sequencial(matriz1, matriz2):
    print("Matriz esperada: \n", np.dot(matriz1,matriz2), "\n")
    aux_num = 0
    num_elementos = 0
    resultado = np.zeros((np.shape(matriz1)[0], np.shape(matriz2)[1]), dtype=int)
    if(np.shape(matriz1)[0] != np.shape(matriz2)[1]):
        print("Não é possível multiplicar as duas matrizes")
    else:
        comeco = time.time()
        for linha in range(np.shape(matriz1)[0]):
            for coluna in range(np.shape(matriz2)[1]):
                num_elementos += 1
                for el in range(np.shape(matriz2)[1]):
                    aux_num += matriz1[linha][el] * matriz2[el][coluna]
                resultado[linha][coluna] = aux_num
                aux_num = 0
        fim = time.time()
        tempo_decorrido = float((fim - comeco))
        print("Matriz Resultante: \n", resultado)
        print("\n A multiplicação levou um total de ", tempo_decorrido, " segundos.")
        return tempo_decorrido


matriz_1 = Matriz.random(100,100)
matriz_2 = Matriz.random(100,100)
print("IMPLEMENTAÇÃO SEQUENCIAL: \n")
sequencial(matriz_1, matriz_2)
print("__________________________________________________________________________\n")
print("IMPLEMENTAÇÃO COM CRIAÇÃO DE PROCESSOS: \n")
forks(matriz_1, matriz_2)
print("__________________________________________________________________________\n")