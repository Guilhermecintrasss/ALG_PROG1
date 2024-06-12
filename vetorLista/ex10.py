numeros = input().split(" ")
i = 0
numerosRepetidos = []
jaExiste = False
while(i<len(numeros)):
    numeros[i] = int(numeros[i])
    i += 1

i = 0
while(i<len(numeros)):
    j = i+1
    while(j<len(numeros)):
        if(numeros[i] == numeros[j]):
            c = 0
            while(c<len(numerosRepetidos)):
                if(numeros[i] == numerosRepetidos[c]):
                    jaExiste = True
                    c = c+len(numerosRepetidos)
                c+=1
            if(jaExiste == False):
                numerosRepetidos.append(numeros[i])
            jaExiste = False
            
        j+=1
    i +=1
print(numerosRepetidos)



            
