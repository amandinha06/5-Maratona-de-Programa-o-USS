'''Dada uma expressão qualquer com parênteses, indique se a quantidade de parênteses está correta ou não, sem levar em conta o restante da expressão. Por exemplo:

a + (b*c)-2-a         está correto
(a+b * (2-c) -2+a)*2  está correto

enquanto:

(a+b-(2+c)           está incorreto
2*(3-a))             está incorreto
)3+b*(2-c)(          está incorreto

ou seja, todo parênteses que fecha deve ter um outro parênteses que abre correspondente e não pode haver parêntes que fecha sem um previo parenteses que abre e a quantidade total de parenteses que abre e fecha dev ser igual.

Entrada 
Como entrada, haverá N expressões (1<= N <= 10000), cada uma delas com até 1000 caracteres.

Saída
O arquivo de sáida deverá ter a quantidade de linhas correspondente ao arquivo de entrada, cada uma delas contendo as palavras correct ou incorrect de acordo com as regras fornecidas acima. 

Exemplo de Entrada                    exemplo de saída
a+(b+c)-2-a                           correct
(a+b*(2-c)-2+a)*2                     correct
(a*b-(2+c)                            incorrect
2+(3-a))                              incorrect
)3+b*(2-c)(                           incorrect
'''

N = int(input("Digite o número de expressões: "))

for _ in range(N):
    expressao = input().strip()
    cont = 0
    valido = True
    
    for char in expressao:
        if char == '(':
            cont +=1
        elif char == ')':
            if cont > 0:
                cont -= 1
            else:
                valido = False
                break
        
    if cont != 0:
        valido = False
        
    print("correct" if valido else "incorrect")
    
    
'''Modo de fazer usando pilhas:'''

N = int(input("Digite o número de expressões: "))
for _ in range (N):
   expressao = input().strip()
   pilha = []
   valido = True
   
   for char in expressao:
       if char == '(' :
           pilha.append('(')
       elif char == ')':
           if pilha:
               pilha.pop()
           else:
               valido = False
               break
if pilha:
    valido = False

print("correct" if valido else "incorrect")