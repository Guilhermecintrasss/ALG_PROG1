n = int(input("Digite um numero: "))
i = 0
numantigo = 0
ultimo = 0
primeiro = 0
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
    if(i == 1):
        ultimo = numantigo
    if(i == cont):
        primeiro = numantigo

    i = i+1
if(ultimo == primeiro):
    print("O ultimo e o primeiro digito são iguais")
else:
    print("O ultimo e o primeiro digito não são iguais")
