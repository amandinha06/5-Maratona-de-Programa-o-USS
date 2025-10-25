'''Rosy é uma professora de Ensino Médio que foi convidada para dar aulas na Inglaterra. Apesar de falar inglês, ela ficou nervosa com a mudança, mas aceitou o desafio. Na primeira prova aplicada aos alunos, Rosy utilizou o sistema de notas numéricas de 0 a 100, como faz no Brasil. Porém, na Inglaterra, o sistema usado é com conceitos de A a E, então ela precisou converter as notas.
Depois de conversar com outros professores, Rosy recebeu a seguinte tabela para converter as notas numéricas:

Nota	Conceito
0	       E
1 a 35	   D
36 a 60	   C
61 a 85	   B
86 a 100   A

Como ela já tem muitas provas para corrigir, pediu sua ajuda para automatizar a conversão.

Entrada:
A entrada contém um único número inteiro N (0 ≤ N ≤ 100), representando a nota numérica do aluno.

Saída:
Você deve imprimir um único caractere: A, B, C, D ou E, correspondente ao conceito da nota.

Exemplos
Entrada	Saída
35	D
86	A
0	E'''

nota = int(input())

if nota == 0:
    print("E")
elif 1<= nota <=35:
    print("D")
elif 36<= nota <= 60:
    print("C")
elif 31 <= nota <= 85:
    print("B")
elif 86 <= nota <= 100:
    print("A")
else:
    print("Nota inválida!")