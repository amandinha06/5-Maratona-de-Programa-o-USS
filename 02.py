'''Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variavel X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linho após o resultado, caso contrario, você receberá 'presentaion error'. 
Entrada:
A entrada contém 2 valores inteiros.
Saída:
Imprima a mensagem "X = " (letra X maiuscula)seguindo pelo valor da variavel X e prlo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade. conforme o exemplo abaixo. 
Exemplos de entrada        Exemplos de saida
10                             X = 19
9        

-10                            X = -6
4

15                             X = 8
-7
'''

A = int(input("Digite um número: "))
B = int(input("Digite um número: "))

X = A + B
print(f'X = {X}')