lista = input().split(" ")
i = 0
posicaoMenor = 0
posicaoMaior = 0
while(i<len(lista)):
    lista[i] = int(lista[i])
    i = i+1

maior = lista[0]
menor = lista[0]
somaAnt = 0
balanceada = True
removida = False
blacklist = []
i = 0
while(i < len(lista)):
        
    c = 0
    primeiraVez = True
    while(c<len(lista)):
            j = 0

            while(j<len(blacklist)):
                if(c == blacklist[j]):
                    removida = True
                j = j + 1

            if(removida != True and primeiraVez):
                primeiraVez = False
                maior = lista[c]
                menor = lista[c]
                posicaoMaior = c
                posicaoMenor = c
            if(removida != True):

                if(lista[c]>maior):
                    maior = lista[c]
                    posicaoMaior = c
                if(lista[c]<menor):
                    menor = lista[c]
                    posicaoMenor = c

            removida = False
            c = c+1
    if(i == 0):
        somaAnt = lista[posicaoMaior]+lista[posicaoMenor]

    if(lista[posicaoMaior]+lista[posicaoMenor] != somaAnt):
        balanceada = False
        somaAnt = lista[posicaoMaior]+lista[posicaoMenor]
    else:
        somaAnt = lista[posicaoMaior]+lista[posicaoMenor]

    
    print(blacklist)
    if(len(blacklist) != len(lista)):
        blacklist.append(posicaoMaior)
        blacklist.append(posicaoMenor)

    i = i+2

if(balanceada == True):
    print("A sequencia é balanceada")
else:
    print("A sequencia não é balanceada")
