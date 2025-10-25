'''Se a palavra tiver 10 ou mais caracteres → é palavrão

Caso contrário → palavrinha

A entrada vai até acabar (EOF), então usamos try/except ou for simples.'''

palavra = input()
cont = 0

for letra in palavra:
    cont += 1 

if cont >= 10:
    print("palavrao")
else:
    print("palavrinha")