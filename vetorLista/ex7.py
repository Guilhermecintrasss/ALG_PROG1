numeros = input().split(" ")
i = 0
while(i<len(numeros)):
    numeros[i] = int(numeros[i])
    i = i + 1
menor = 0
i = 0

while(i<len(numeros)):
    if(i == 0):
        menor = numeros[i]
    else:
        if(numeros[i]<menor):
            menor = numeros[i]
    i = i+1


print(menor)
    

        