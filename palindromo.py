frase = input()
tamanho = len(frase) - 1
i = 0
finversa = ""
while(tamanho>=0):
    finversa = finversa + frase[tamanho] 
    tamanho = tamanho-1

if(frase == finversa):
    print("SIM")
else:
    print("NAO")



