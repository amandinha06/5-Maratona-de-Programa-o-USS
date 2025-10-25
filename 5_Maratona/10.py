'''
Entrada:
A entrada contém vários casos de teste. A primeira linha de um caso contém um único inteiro N indicando o número de vezes jogadas (1<= N <= 1000. A lina seguintre contém N interiros Ri, separados por um espaço, descrevendo a lista de resultados. Se Ri = 0 então Maria venceu o iésimo jogo, se Ri = 1 então João venceu o iésimo jogo (1 <= i <= N). O fim da entrada é indicado por N = 0

Saída:
PAra cada caso de teste na entrada, seu programa deverá escrever um alinha contendo a sentença "Mary won X times and John won Y times", onde 0 <= X e 0 <= Y

Exemplo de entrada             Exemplo de saida
5                              Mary won 3 times and John won 2 times.
0 0 1 0 1                      Mary won 5 times and John won 1 times.
6
0 0 0 0 0 1
0
'''

while True:
    N = int(input())
    if N == 0:
        break
    resultados = list(map(int, input().split()))
    mary = 0
    john = 0

    for r in resultados:
        if r == 0:
            mary += 1
        elif r == 1:
            john += 1

    print(f"Mary won {mary} times and John won {john} times.")
