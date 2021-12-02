deposito = float(input("Informe o valor a ser depositado: "))
valorInicial = deposito
taxa = float(input("Informe a taxa de juros: "))
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']


for i in range(12):
    deposito = deposito + (deposito * taxa/100)
    print(f"No mês de {meses[i]} o valor estava em: R${deposito:.2f}")
valorFinal = deposito - valorInicial
print(f"O lucro total em 12 meses foi de: R${valorFinal:.2f}")
    