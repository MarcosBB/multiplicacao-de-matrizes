import multiprocessing
import threading
import queue
from utils import divide_linhas_por_partes, calcula_linha

def sequencial(matriz1, matriz2):
    resultado = []
    for linha in range(len(matriz1)):
        resultado.append(calcula_linha(matriz1, matriz2, linha))
    return resultado

def multi_processo(matriz1, matriz2, partes):
    def calcula_linhas(matriz1, matriz2, linhas, resultado_pipe):
        resultado = {}
        for linha in linhas:
            resultado[linha] = calcula_linha(matriz1, matriz2, linha)
        resultado_pipe.send(resultado)

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

def multi_thread(matriz1, matriz2, partes):
    def calcula_linhas(matriz1, matriz2, linhas, resultado_queue):
        resultado = {}
        for linha in linhas:
            resultado[linha] = calcula_linha(matriz1, matriz2, linha)
        resultado_queue.put(resultado)
    lista_de_linhas = divide_linhas_por_partes(len(matriz1), partes)

    resultado_queues = []
    threads = []
    for linhas in lista_de_linhas:
        resultado_queue = queue.Queue()
        resultado_queues.append(resultado_queue)
        threads.append(
            threading.Thread(
                target=calcula_linhas, 
                args=(matriz1, matriz2, linhas, resultado_queue)
            )
        )
    
    for thread in threads:
        thread.start()
    
    resultado_dict = {}
    for resultado_queue in resultado_queues:
        resultado_dict.update(resultado_queue.get())
    
    for thread in threads:
        thread.join()
    
    resultado = []
    for i in range(len(matriz1)):
        resultado.append(resultado_dict[i])
    
    return resultado