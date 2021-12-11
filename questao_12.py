divida = float(input("Informe o valor da dívida: "))
juros = float(input("Informe os juros mensais: "))

valorSemJuros = divida
valorMensal = float(input("Informe o valor que deseja pagar por mês: "))
totalMeses = divida/valorMensal

juros = juros*totalMeses

divida = divida + (divida * juros/100)

print('A dívida será paga em aproximadamente', int(totalMeses), 'meses')
print(f'O valor total pago foi de R${divida:.2f}')
print(f'o total de juros pago foi de R${divida-valorSemJuros:.2f}')
