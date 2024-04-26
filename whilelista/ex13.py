n = int(input("Digite um numero inteiro: "))
i = 0
verify = 0
numantigo = 0
while(n>i):
    n1 = int(input("Digite o "+str(i+1)+" numero: "))
    if(numantigo>n1):
        verify = 1

    numantigo = n1
    i = i+1
if(verify == 1):
    print("A sequencia nao esta em ordem crescente")
else:
    print("A sequencia esta em ordem crescente")