num1 = int(input("Informe um número: "))
num2 = int(input("Informe um número: "))

parteInteira = 0
resto = 0

while True:
    if num1 < num2:
        resto = num1
        break
    
    num1 = num1 - num2
    parteInteira+=1

print('Divisão interira: ',parteInteira)
print('Resto da divisão: ',resto)