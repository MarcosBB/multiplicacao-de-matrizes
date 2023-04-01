import random
class Matriz:
    @staticmethod
    def random(linhas, colunas):
        matriz = []
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                linha.append(random.randint(0,9))
            matriz.append(linha)
        return matriz
