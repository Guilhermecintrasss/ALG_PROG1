frase = input()
i = 0
tamanho = len(frase)-1
verify = True
while(i<=tamanho):
    if(frase[i] != frase[tamanho]):
        verify = False
    i = i+1
    tamanho = tamanho-1
if(verify):
    print("SIM")
else:
    print("NAO")

