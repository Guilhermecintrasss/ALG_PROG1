n = int(input("Digite um numero: "))
i = 0
numantigo = 0
verify = 0
cont = 0
a = n
while(i==0): #Busco saber quantos digitos tem no numero e jogo no count
    if(a == 0):
        i = 1
    else:
        a = int(a/10) 
        cont = cont+1
a = n 
while(i<=cont): #Comparo os digitos
    numantigo = a%10 
    a = int(a/10) 
    if(a!=0):

        if(numantigo == a%10): 
            verify = 1

    i = i+1
if(verify==1):
    print("Existem numeros consecutivos nesse numero")
else:
    print("Não existem numeros consecutivos nesse numero")
