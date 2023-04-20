from Matriz import multi_processo, sequencial, multi_processo
from utils import matriz_randomica
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    "-s",
    "--sequencial",
    action='store_const',
    const=True,
    default=False,
    help='Executa a multiplicação sequencial',
)
parser.add_argument(
    "-p",
    "--processos",
    action='store_const',
    const=True,
    default=False,
    help='Executa a multiplicação com processos',
)
parser.add_argument(
    "-t",
    "--threads",
    action='store_const',
    const=True,
    default=False,
    help='Executa a multiplicação com threads',
)

parser.add_argument(
    "-o",
    "--ordem",
    type=int,
    help="Ordem da matriz quadrada",
    default=100,
)
parser.add_argument(
    "-P",
    "--partes",
    type=int,
    help="Número de partes em que a matriz será dividida",
    default=1,
)
parser.add_argument(
    "-r",
    "--repeticoes",
    type=int,
    help="Número de repetições para executar e medir o tempo médio de execução",
    default=1,
)
args = parser.parse_args()
matriz_1 = matriz_randomica(args.ordem, args.ordem)
matriz_2 = matriz_randomica(args.ordem, args.ordem)
shape = [[0 for j in range(len(matriz_2[0]))] for i in range(len(matriz_1))]

# validação dos argumentos
if args.partes and (args.processos or args.threads):
    if args.partes > len(shape[0]):
        raise ValueError("O número de partes deve ser menor ou igual ao número de colunas da matriz")
        

multiplication_types_sum = sum([args.sequencial, args.processos, args.threads])

# Sequencial
tempos_de_execução = []
if args.sequencial or multiplication_types_sum == 0:
    print()
    print("Executando multiplicação sequencial")
    print("-----------------------------------")

    for i in range(args.repeticoes):
        comeco = time.time()
        resultado = sequencial(matriz_1, matriz_2)
        fim = time.time()

        tempos_de_execução.append(fim - comeco)
        print(f"Tempo de execução {i + 1}: {fim - comeco}")
    tempos_de_execucao = sum(tempos_de_execução) / len(tempos_de_execução)
    print(f"\033[32mMédia de tempo de execução: {tempos_de_execucao}\033[0m")


# Multiprocessos
tempos_de_execução = []
if args.processos:
    print()
    print("Executando multiplicação com processos")
    print("-----------------------------------")

    for i in range(args.repeticoes):
        comeco = time.time()
        resultado = multi_processo(matriz_1, matriz_2, args.partes)
        fim = time.time()

        tempos_de_execução.append(fim - comeco)
        print(f"Tempo de execução {i + 1}: {fim - comeco}")

    tempos_de_execucao = sum(tempos_de_execução) / len(tempos_de_execução)
    print(f"\033[32mMédia de tempo de execução: {tempos_de_execucao}\033[0m")


# Multithreads