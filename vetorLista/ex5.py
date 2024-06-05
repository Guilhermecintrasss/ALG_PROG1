n = int(input())
roleta = [0] * 37
i = 0
res = ""

while(i<n):
    numero = int(input())
    if(numero>=0 and numero<=36):
        roleta[numero] += 1
        i = i+1
    else:
        print("Valor invalido! Digite um valor entre 0 e 36.")




i=0
while(i<=36):
    if(i != 36):
        res = res + str(roleta[i]) + " "
    else:
        res = res + str(roleta[i])
    
    i += 1

print(res)