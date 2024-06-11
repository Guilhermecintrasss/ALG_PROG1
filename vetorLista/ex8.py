numeros = []
menor = 0
n = int(input())
i = 0
posicao = 0
a = 0
c = 0
while(i<n):
    numeros.append(int(input()))
    i = i+1

while(c<n):
    i = c

    while(i<n):
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
    

        