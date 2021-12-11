fim = int(input("Digite o último número a imprimir: "))
x = 0
countMultiplos = 1
while x <= fim:
    if x%3 == 0 and countMultiplos <= 10:
        print(x)
        countMultiplos += 1
    x+=1
