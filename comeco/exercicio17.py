rendaph = float(input("Digite o quanto voce ganha por hora\n"))
horast = float(input("Digite quantas horas voce trabalha por mês\n"))

salario = float(rendaph*horast)

print("Seu salario mensal bruto é: ",salario,"\n")
print("Voce pagou ",salario*0.08," para o INCSS e ",salario*0.05," para o sindicato\n")
print("removendo os impostos seu salario mensal liquido é: ",salario*0.76,"\n")