import multiprocessing
from utils import divide_linhas_por_partes, calcula_linhas, calcula_linha

def sequencial(matriz1, matriz2):
    resultado = []
    for linha in range(len(matriz1)):
        resultado.append(calcula_linha(matriz1, matriz2, linha))
    return resultado

def multi_processo(matriz1, matriz2, partes):
    lista_de_linhas = divide_linhas_por_partes(len(matriz1), partes)

    resultado_pipes = []
    processos = []
    for linhas in lista_de_linhas:
        resultado_pipe, filho_pipe = multiprocessing.Pipe()
        resultado_pipes.append(resultado_pipe)
        processos.append(
            multiprocessing.Process(
                target=calcula_linhas, 
                args=(matriz1, matriz2, linhas, filho_pipe)
            )
        )
    
    for processo in processos:
        processo.start()
    
    resultado_dict = {}
    for resultado_pipe in resultado_pipes:
        resultado_dict.update(resultado_pipe.recv())
    
    for processo in processos:
        processo.join()
    
    resultado = []
    for i in range(len(matriz1)):
        resultado.append(resultado_dict[i])
    
    return resultado

def multi_thread(matriz1, matriz2, shape):
    pass