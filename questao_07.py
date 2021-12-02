#7) Escreva um programa que leia dois números. Imprima o resultado da multiplicação
# do primeiro pelo segundo. Utilize apenas os operadores de soma e subtração para 
# calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois 
# números como somas sucessivas de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

cont = 1
soma = 0
while cont<=num2:
    soma = soma + num1
    cont = cont + 1
print("%d x %d = %d" %(num1, num2, soma))