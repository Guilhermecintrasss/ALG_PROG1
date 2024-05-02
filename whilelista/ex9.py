n = int(input("Digite um numero: "))
i = 1
pos = 0
npos = 0
while(i<=n):
    num = int(input("Digite o "+str(i)+" numero: "))
    if(num>0):
        pos = pos+1
    else:
        npos = npos+1
    i = i+1
print("Numeros positivos: " + str(pos))
print("Numeros não positivos: "+str(npos))