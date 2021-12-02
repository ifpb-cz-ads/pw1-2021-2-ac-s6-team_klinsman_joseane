produtos = {1: 0.5,
            2: 1.0,
            3: 4.0,
            5: 7.0,
            9: 8.0}
total = 0

while True:
    opt = int(input('Digite o código de um protudo: '))
    
    if opt == 0:
        print(f'Total das compras R${total:.2f}')
        break
    
    quantidade = int(input('Informe a quantidade: '))

    if opt == 1:
        total = quantidade * 0.5
    elif(opt == 2):
        total = quantidade * 1.0
    elif(opt == 3):
        total = quantidade * 4.0
    elif(opt == 5):
        total = quantidade * 7.0
    elif(opt == 9):
        total = quantidade * 8.0
    else:
        print('Código inválido')
        
    