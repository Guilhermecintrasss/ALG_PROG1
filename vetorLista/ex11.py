lista = input().split(" ")
i = 0
posicaoMenor = 0
posicaoMaior = 0
blacklistposicao = []
while(i<len(lista)):
    lista[i] = int(lista[i])

maior = lista[0]
menor = lista[0]
i = 0
while(i < len(lista)):
        
    c = 1
    while(i<len(lista)):
        if(lista[i]>maior):
            maior = lista[i]
            posicaoMaior = i
        if(lista[i]<menor):
            menor = lista[i]
            posicaoMenor = i
    blacklistposicao.append(posicaoMaior)
    blacklistposicao.append(posicaoMenor)


