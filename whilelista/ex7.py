n = int(input("Digite um numero: "))
i = 1
somap = 0
somai = 0
while(i<=n):
    num = int(input("Digite o "+str(i)+" numero: "))
    if(num%2==0):
        somap = somap+num
    else:
        somai = somai+num

    i = i+1
print("A soma dos pares é: " + str(somap))
print("A soma dos impares é: " + str(somai))