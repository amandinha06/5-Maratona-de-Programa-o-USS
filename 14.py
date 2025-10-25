'''Todos os anos acontece a Grande Corrida na cidade de Mlogônia. Cada carro participa da corrida e completa um certo número de voltas. O tempo de cada volta é anotado, e o carro vencedor é aquele que termina a corrida com o menor tempo total.

Você deve escrever um programa que receba:
N → o número de carros (3 ≤ N ≤ 100)
M → o número de voltas (1 ≤ M ≤ 100)
Depois disso, serão fornecidos N conjuntos de linhas, onde cada conjunto contém M valores inteiros, representando o tempo gasto pelo carro em cada volta.

Seu programa deve somar os tempos de cada carro e determinar:
O carro com o menor tempo total → 1º colocado
O carro com o segundo menor tempo total → 2º colocado
O carro com o terceiro menor tempo total → 3º colocado

Não haverá empates.
A numeração dos carros é a ordem de entrada:
O primeiro conjunto é o Carro 1, o segundo é o Carro 2, e assim por diante.

Saída
Imprimir três linhas, contendo os números dos carros:
<carro vencedor>
<segundo colocado>
<terceiro colocado>'''

N, M = map(int, input().split())

tempos = []

for i in range(1, N + 1):
    valores = list(map(int, input().split()))
    total = sum(valores)
    tempos.append((total, i))

tempos.sort()

print(tempos[0][1])
print(tempos[1][1])
print(tempos[2][1])
