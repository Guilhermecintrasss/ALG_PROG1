n = int(input("Digite um numero inteiro: "))
i=0
soma = 0
while(n>i):
    n1 = int(input("Digite o " + str(i+1) +" numero: "))
    if(n1 > 0):
        soma = soma+n1
    i = i+1
print(soma)
    