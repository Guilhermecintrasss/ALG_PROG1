n = input("Digite um numero: ")
i = 0
numantigo = 0
verify = 0
while(i<len(n)):
    if(i>0):
        if(numantigo == n[i]):
            verify = 1

    numantigo = n[i]
    i = i+1
if(verify == 1):
    print("Existem 2 numeros consecutivos iguais neste numero")
else:
    print("Nao existem 2 numeros consecutivos iguais nesse numero")
