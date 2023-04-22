# Multiplicação de matrizes
Trata-se de um trabalho do curso de **Sistemas operacionais** da UFRN que trata do assunto de **programação paralela**. 
O objetivo é verificar as vantagens e desvantagens ta programação paralela na multiplicação de matrizes de ordens grandes.

## Rodando
### Rodando os testes de tempo de execução
Ao executar o comando a baixo è possivel medir o tempo médio de execução de multiplicação de matrizes de diferentes maneiras, incluindo implementação sequencial, usando processos ou threads
```bash
python multiplicacao_de_matrizes.py
```
Para customizar a execução você pode usar alguns parametros e definir variáveis, por exemplo:
- `-o` ou `--ordem`: define a ordem da matriz
- `-r` ou `--repeticoes`: define quantas vezes vai ser medido o tempo de execução para cada uma das implementações requeridas
- entre outras...
Para saber todos os comandos rode `python multiplicacao_de_matrizes.py --help`

#### Exemplo de comando
O comando exemplo a seguir roda as implementações sequencial e multi-processos para uma matriz de ordem 200 com 5 repetições cada e, no caso da implementação multi-processos, divide as operações entra 10 processos
```bash
python multiplicacao_de_matrizes.py --ordem 200 -P 10 --repeticoes 5 --sequencial --processos
```
saida:
```bash
Executando multiplicação sequencial
-----------------------------------
Tempo de execução 1: 1.1166918277740479
Tempo de execução 2: 1.1466114521026611
Tempo de execução 3: 1.1547222137451172
Tempo de execução 4: 1.1468758583068848
Tempo de execução 5: 1.1342251300811768
Média de tempo de execução: 1.1398252964019775

Executando multiplicação com processos
-----------------------------------
Tempo de execução 1: 0.34136390686035156
Tempo de execução 2: 0.33374881744384766
Tempo de execução 3: 0.39882850646972656
Tempo de execução 4: 0.36981964111328125
Tempo de execução 5: 0.3450462818145752
Média de tempo de execução: 0.35776143074035643
```

### Testes de unidade
Para verificar se as implementações estão funcionando da maneira correta, execute os testes rodando o comando

```bash
python -m unittest
```

## Requisitos
Para rodar esse projeto utilize o `linux` obrigatoriamente. Lembre-se também de ter o python instalado na sua máquina. Tendo tudo isso apenas rode o comando abaixo para baixar os requisitos.

```bash
pip install -r requirements.txt
```

## Autores
- [Marcos Beraldo Barros](https://github.com/MarcosBB)
- [Ezequiel Morais](https://github.com/Ezeque)
