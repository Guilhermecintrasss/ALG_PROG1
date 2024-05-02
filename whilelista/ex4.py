n = int(input("Digite um numero para elevar o 2: "))
i = 0
res = ""
while(i<n):
    num = 2**i
    res = res + str(num) + " "
    i = i+1
print(res) #Tem um espaço inutil no final :'(