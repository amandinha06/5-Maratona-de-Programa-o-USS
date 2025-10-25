'''Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma dos fatoriasi de casa um dos valores lidos. Utilize uma variável apropriada, pois cálculo pode resultar um valor com mais de 15 digitos.

Entrada
O arquivo de entrada contém vários casos de teste. Cada caso contém dois números inteiros M (0 <= M <= 20) e N (0<= N <= 20). O fim da entrada é determinado por eof.

Saída 
Para cada cado de teste de entrada, seu programa deve imprimir uma única linha, ocntendo um núemro que é a soma de ambos os fatoriais (de M e N).

Exemplo de Entrada        Exemplo de Saída
4 4                       48
0 0                       2
0 2                       3
'''

''' Com eof: '''

import sys
import math

for linha in sys.stdin:  
    M, N = map(int, linha.split())
    soma = math.factorial(M) + math.factorial(N)
    print(soma)




'''Sem eof: '''

import math

casos = int(input("Quantos casos vai testar? "))

for _ in range(casos):
    M, N = map(int, input().split())
    soma = math.factorial(M) + math.factorial(N)
    print(soma)