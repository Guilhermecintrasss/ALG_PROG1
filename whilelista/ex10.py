n = int(input("Digite um numero: "))
i = 1
somap = 0
somai = 0
while(i<=n):
    num = int(input("Digite o "+str(i)+" numero: "))
    if(num%2==0):
        somap = somap+1
    else:
        somai = somai+1

    i = i+1
print("A quantia de pares é: " + str(somap))
print("A quantia de impares é: " + str(somai))