i = 1
abaixo = 0
while(i<=7):
    t = int(input("Digite temperatura do " + str(i)+" dia: "))
    if(t<0):
        abaixo = abaixo + 1
    i = i+1
print("Foram "+str(abaixo)+" dias com temperatura abaixo de 0")
    