import random

def matriz_randomica(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(0,9))
        matriz.append(linha)
    return matriz

def divide_linhas_por_partes(quantidade_de_linhas, partes):
    linhas_por_parte = quantidade_de_linhas // partes
    linhas = []
    for i in range(partes):
        linhas.append([j for j in range(i * linhas_por_parte, (i + 1) * linhas_por_parte)])
    
    if quantidade_de_linhas % partes != 0:        
        ultima_linha = linhas[-1][-1]
        for linha in linhas:
            ultima_linha += 1
            if (ultima_linha < quantidade_de_linhas):
                linha.append(ultima_linha)
            else:
                break    
    return linhas

def calcula_elemento(matriz1, matriz2, linha, coluna):
    resultado = 0
    for i in range(len(matriz2[1])):
        resultado += matriz1[linha][i] * matriz2[i][coluna]
    return resultado

def calcula_linha(matriz1, matriz2, linha):
    resultado = []
    for coluna in range(len(matriz2[0])):
        resultado.append(calcula_elemento(matriz1, matriz2, linha, coluna))
    return resultado