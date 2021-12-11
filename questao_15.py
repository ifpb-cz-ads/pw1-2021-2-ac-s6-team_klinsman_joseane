#15) Escreva um programa que exiba uma lista de opções (menu): 
# adição, subtração, divisão, multiplicação e sair. Imprima a 
# tabuada da operação escolhida. Repita até que a opção "saída" seja escolhida.

while(True):
    menu = input("""Qual operação deseja escolher: 
             + para somar
             - para subtrair
             x para multiplicar
             / para dividir
             ou digite qualquer letra para sair: """)
    if(menu == "+"):
        for tabuada in range(1, 11):
            for numero in range(1, 11):
                print("%d + %d = %d" %(tabuada, numero, tabuada + numero))
    elif(menu == "-"):
        for tabuada in range(1, 11):
            for numero in range(1, 11):
                print("%d - %d = %d" %(tabuada, numero, tabuada - numero))
    elif(menu == "x"):
        for tabuada in range(1, 11):
            for numero in range(1, 11):
                print("%d x %d = %d" %(tabuada, numero, tabuada * numero))
    elif(menu == "/"):
        for tabuada in range(1, 11):
            for numero in range(1, 11):
                print("%d / %d = %d" %(tabuada, numero, tabuada / numero))
    else:
        print("Programa encerrado!")
    
