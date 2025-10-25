'''Entrada: A entrada é composta por vários casos de teste. Cada caso de teste consiste de uma única linha, quem contém três interiso A, B e C (A,B,C só podem ser 0 ou 1), indicando respectivamente os valores escolhidos por Alice, Bento e Clara. O final da entrada é determinado por EOF (End of Line)
Saída: Para cada caso de teste, seu programa deve produzir uma única linha, contendo um único caractere. Se o cencedor é Alice o caractere deve ser A, se o vencedor for Bento o caractere deve ser B, se o vencedor é Clara deve ser C.'''


A, B, C = map(int, input().split())
if A != B and A != C:
    print("A")
elif B != A and B != C:
    print("B")
elif C != A and C != B:
    print("C")
else:
    print("*")
    