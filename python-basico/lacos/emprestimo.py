renda = float(input("Digite o valor da sua renda mensal: "))
parcela = float(input("Digite o valor da parcela desejada:"))

if renda > 2000 and parcela <= 0.3 * renda:
    print("Empréstimo aprovado!")
elif renda <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30%  da renda.")
    
