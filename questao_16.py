numero = int(input('Informe um número: '))
count = 0

for i in range(2, numero):
    if numero%i == 0:
        count += 1
            
if count == 0:
    print('Primo!')
else:
    print('Não é primo!')