n = int(input("Digite um numero: "))
i = 1
soma = 0
while(i<=n):
    num = int(input("Digite o "+str(i)+" numero: "))
    if(num>=0):
        soma = soma+num
    i = i+1
print(soma)