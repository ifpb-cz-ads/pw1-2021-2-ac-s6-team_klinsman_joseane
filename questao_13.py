#13) Escreva um programa que leia números inteiros do teclado. 
# O programa deve ler os números até que o usuário digite 0 (zero). 
# No final da execução, exiba a quantidade de números digitados, 
# assim como a soma e a média aritmética.

cont = 0
soma = 0
while True:
    num = int(input("Informe um número inteiro ou digite 0 para encerrar: "))
    if(num == 0): 
        break
    cont += 1
    soma = soma + num
print("Foi informado %d números" %cont)
print("A soma dos números informados é %d" %soma)
print("A média dos números informados é %d" %(soma/cont))