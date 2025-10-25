'''A entrada possui duas linhas:

Um inteiro N (1 ≤ N ≤ 40), representando a pressão desejada.

Um inteiro M (1 ≤ M ≤ 40), representando a pressão medida pela bomba.

Saída

Seu programa deve imprimir um único valor inteiro:
N - M, que é a diferença entre a pressão desejada e a pressão lida.

Exemplos
Entrada	Saída
30
18	      12
27
27	      0
27
30	     -3'''

N = int(input())
M = int(input())

X = N - M

print(X)