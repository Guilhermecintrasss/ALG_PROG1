numeros = input().split(" ")
menor = 0
i = 0
posicao = 0
a = 0
c = 0
while(i<len(numeros)):
    numeros[i] = int(numeros[i])
    i = i+1

while(c<len(numeros)):
    i = c

    while(i<len(numeros)):
        if(i == c):
            menor = numeros[i]
            posicao = i
        else:
            if(numeros[i]<menor):
                menor = numeros[i]
                posicao = i
        i = i+1

    a = numeros[c]
    numeros[c] = menor
    numeros[posicao] = a

    c = c+1

print(numeros)
    

        