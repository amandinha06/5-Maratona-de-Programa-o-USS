'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento de um fabrica, e informe-o o expresso no formato horas:minutos:segundos
Entrada:
O arquivo de entrada comtém um valor inteiro N
Saida:
Imprima o tempo lido no arquivo de entrada(segundo), ocnvertido para horas:minutos:segundos, conforme exemplo fornecido.
Exemplos de entrada                Exemplos de saida
556                                0:9:16
1                                  0:0:1
140153                             38:55:53
'''

N = int(input("Digite o valor em segundos: "))

hora = N // 3600
N = N % 3600
minuto = N // 60
segundo = N % 60

    
print(f"{hora:.0f}:{minuto:.0f}:{segundo:.0f}")