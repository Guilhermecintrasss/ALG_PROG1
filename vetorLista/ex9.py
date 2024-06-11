numeros = input().split()
numerosSemRep = []
i = 0
numeroRepete = False
while(i<len(numeros)):
    numeros[i] = int(numeros[i])
    if(len(numerosSemRep) == 0):
        numerosSemRep.append(numeros[i])
    else:
        c = 0
        while(c<len(numerosSemRep)):
            if(numerosSemRep[c] == numeros[i]):
                numeroRepete = True
                c += len(numerosSemRep)
            c +=1
        
        if(numeroRepete == False):
            numerosSemRep.append(numeros[i])

        numeroRepete = False

    i +=1
print(numerosSemRep)
