'''Leia 5 valores interios. A seguir mostre quantos valores digitados foram pares, quantos valores digitiados foram impares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada:
O arquivo de entrada contém 5 valores inteiros quaisquer

Saída:
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final após cada uma.

Exemplo de entrada            exemplo de saida
-5                            3 valor(es) par(es)
0
-4                            2 valor(es) impar(es)
-3                            1 valor(es) positivo(s)
12                            3 valor(es) negativo(s)
'''

cont_1 = 0
par = 0
impar = 0
positivo = 0
negativo = 0

while cont_1 < 5:
    numero = int(input("Digite os valores: "))
    cont_1 += 1

    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')

    