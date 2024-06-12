dic = {} # Um vetor que usa strings como posição

#-1 , -1 , 3 , 2
numeros = input().split(" ")

i = 0
while i < len(numeros):
    atual = numeros[i]
    dic[atual] = 0
    i = i+1

#dic['-1'] = 0
#dic['-1'] = 0 --> apenas sobreescreve, a posição ja existe
#dic['3'] = 0
#dic['2'] = 0
i = 0
while(i<len(numeros)):
    atual = numeros[i]
    dic[atual] += 1 # dic[-1] +=1, dic[-1] +=1, dic[3] += 1, dic[2] += 1
    i +=1

#dic['-1'] = 2
#dic['3'] = 1
#dic['2'] = 1

chaves = list(dic.keys()) # Retorna todas chaves do dicionario (as "posições" que existem nele) --> -1, 3 , 2
#chaves -> ['-1' , '3' , '2'] (Transformado em lista)
i = 0
while(i<len(chaves)):
    print("O numero "+ str(chaves[i])+ " aparece "+ str(dic[chaves[i]])+" vezes")
    i+=1