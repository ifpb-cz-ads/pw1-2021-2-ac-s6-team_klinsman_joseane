#17) Modifique o programa anterior de forma a ler um número n. 
# Imprima os n primeiros números primos.

numero = int(input('Informe um número: '))

for i in range(2, numero+1):
    for j in range(2, i):
        if i%j == 0:
            break         
    else:
        print(i)
