p = float (input("Digite o quanto você aplicará por mês \n"))
i = float (input("Digite a taxa de rendimento \n"))
n = float (input("Digite por quantos meses você aplicará \n"))
va = (p*((1+i)**n) - 1)/i

print("O valor acumulado na poupaça é: " + str(va) + "\n")

