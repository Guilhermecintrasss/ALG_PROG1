i = 1

while(i<=7):
        num = int(input("Digite as vendas do "+str(i)+" dia da semana: "))
        if(i == 1):
            aux = num
        if(num>aux):
            aux = num
        i = i+1
print(aux)