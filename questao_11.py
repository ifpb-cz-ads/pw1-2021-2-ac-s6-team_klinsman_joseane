#11) Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. 
# Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo 
# de juros do mês seguinte.

deposito = float(input("Informe o valor a ser depositado: "))
valorInicial = deposito
taxa = float(input("Informe a taxa de juros: "))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
depositoMensal = float(input("Informe o valor que deseja depositar: "))

for i in range(12):
    deposito = deposito + (deposito * taxa/100) + depositoMensal
    print(f"No mês de {meses[i]} o valor estava em: R${deposito:.2f}")
valorFinal = deposito - valorInicial
print(f"O lucro total em 12 meses foi de: R${valorFinal:.2f}")