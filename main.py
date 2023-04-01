from Matriz import Matriz
import time
import numpy as np

#   IMPLEMENTAÇÃO SEQUENCIAL DO PROBLEMA
def sequencial(matriz1, matriz2):
    comeco = time.time()
    print("Matriz esperada: \n", np.dot(matriz1,matriz2), "\n")
    aux_num = 0
    resultado = np.zeros((np.shape(matriz1)[0], np.shape(matriz2)[1]), dtype=int)
    if(np.shape(matriz1)[0] != np.shape(matriz2)[1]):
        print("Não é possível multiplicar as duas matrizes")
    else:
        for linha in range(np.shape(matriz1)[0]):
            for coluna in range(np.shape(matriz2)[1]):
                for el in range(np.shape(matriz2)[1]):
                    aux_num += matriz1[linha][el] * matriz2[el][coluna]
                resultado[linha][coluna] = aux_num
                aux_num = 0
        fim = time.time()
        tempo_decorrido = float((fim - comeco) *1000)
        print("Matriz Resultante: \n", resultado)
        print("\n A multiplicação levou um total de ", tempo_decorrido, " milissegundos.")
        return tempo_decorrido



matriz_1 = Matriz.random(3,3)
matriz_2 = Matriz.random(3,3)
sequencial(matriz_1, matriz_2)