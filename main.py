from Matriz import matriz_randomica, multi_processo, multi_thread, sequencial
import time
import numpy as np

matriz_1 = matriz_randomica(100,100)
matriz_2 = matriz_randomica(100,100)

if (np.shape(matriz_1)[0] != np.shape(matriz_2)[1]):
    print("Não é possível multiplicar as duas matrizes")

else:
    shape = np.zeros((np.shape(matriz_1)[0], np.shape(matriz_2)[1]), dtype=int)

    print("IMPLEMENTAÇÃO SEQUENCIAL: \n")
    comeco = time.time()
    resultado = sequencial(matriz_1, matriz_2, shape)
    fim = time.time()
    print("\n A multiplicação levou um total de ", float((fim - comeco)), " segundos.")
    print("__________________________________________________________________________\n")

    print("IMPLEMENTAÇÃO COM CRIAÇÃO DE PROCESSOS: \n")
    comeco = time.time()
    resultado = multi_processo(matriz_1, matriz_2, shape)
    fim = time.time()
    print("\n A multiplicação levou um total de ", float((fim - comeco)), " segundos.")
    print("__________________________________________________________________________\n")

    print("IMPLEMENTAÇÃO COM THREADS: \n")
    comeco = time.time()
    resultado = multi_thread(matriz_1, matriz_2, shape)
    fim = time.time()
    print("\n A multiplicação levou um total de ", float((fim - comeco)), " segundos.")
    print("__________________________________________________________________________\n")