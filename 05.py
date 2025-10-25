'''Em um país, imaginário denomidado Lisard, todos os habitantes ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benefico da populção, sem qualuqer desvio. A moeda deste paés é o Rombus, cojo simbolo é o R$.
Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar de imposto de renda, segundo a tabela abaixo.

Renda                      Imposto de renda
de 0.00 a R$2000.0             insento
de R$2000.01 até R$3000.0       8%
de R$3000.01 até R$4500.0       18%
acima de R$4500.0               28%

Lembre que, se o salario for R$3002.0, a taxa que incide é de 8% apenas sobre R$1000.0, pois a faixa de salario que fica de R$0.0 até R$2000.0 é insenta de Imposto de renda. No exemplo fornecido (abaixo), a taxa é 8% sobre R$1000.0 + 18% sobre R$2.0, o que resulta em R$80.36 no total. O valor deve ser impresso com duas casas decimais.

Entrada
A entrada contém apenas um valor de ponto fluente, com duas casas decimais.

Saida
Imprima o texto 'R$' seguindo de um espaço e do valor total devido de imposto de renda, com duas casas após o ponto. Se o valor de entrada for menor ou igual a 2000, deverá ser impressa a mensagem 'Insento'

Exemplos de Entrada                Exemplos de Saida
3002.00                            R$ 80.36
1701.12                            Insento
4520.00                            R$ 355.60
'''

salario = float(input("Digite seu salário: "))

imposto = 0.0

if salario <= 2000:
    print("Insento")
elif salario <=3000:
    imposto = (salario - 2000) * 0.08
    print(f"R$ {imposto:.2f}")
elif salario <=4500:
    imposto = (1000.0 * 0.08) + (salario - 3000.00) * 0.18
    print(f"R$ {imposto:.2f}")
else:
    imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + (salario - 4500) * 0.28
    print(f"R$ {imposto:.2f}")
