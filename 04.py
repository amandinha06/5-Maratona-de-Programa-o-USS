'''Solicitaram para que você construisse um programa simples de criptografia. Este programa deve possibilitar enviar mensagens codificas sem que alguém consiga lê-las. O processo é muito simples. São feitos três passadas em todo o texto:

Na primeira passada, somente caracteres que sejam letras minusculas e mauisculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'b', letra 'y' deve virar caratere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. na terceira e ultima passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados um posição para esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira ''. 

Por exemplo, se a entrada for o "Texto #3", o primeiro processamento sobre esta entrada devera produzir "Wh{wr#3". O resultado do segundo processamento inverte os caratecres e produz "3#rw{hW". Por ultimo, com o deslocamento dos caraterees da metade em diante, o resultado final deve ser "3#rvzgV" 

Entrada:
A entrada cpntem, varios casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1<= N <= 1*10^4), indicando a quantidade de linhas que o problema deve trarar. As N linhas contem cada uma elas M (1<= M < = 1*10^3) caracteres.

Saida:
Para cada entrada, deve-se apresentar a mensagem criptografada:

exemplo de entrada            exemplo de saida
4                              3# rvzgV
Texto #3                       1FECedc
abcABC1                        ks. \n{frzx
vv.xwfxo.fd                    gi.r{hyz-xx

'''

def criptografar_linha(linha):
    primeira_passada = ''
    for char in linha:
        if char.isalpha():
            primeira_passada += chr(ord(char) + 3)
        else:
            primeira_passada += char
            
    segunda_passada = primeira_passada[::-1]
    
    metade = len(segunda_passada) // 2
    terceira_passada = ''
    for i in range(len(segunda_passada)):
        if i >= metade:
            terceira_passada += chr(ord(segunda_passada[i]) -1)
        else:
            terceira_passada += segunda_passada [i]
            
    return terceira_passada

N = int(input("Digite: "))
for _ in range(N):
    linha = input()
    print(criptografar_linha(linha))