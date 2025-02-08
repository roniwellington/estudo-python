limite = 3000.0
despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > limite:
    print("Atenção! Vc ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do orçamento.")