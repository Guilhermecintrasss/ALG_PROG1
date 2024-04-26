n = input("Digite um numero: ")
i = 0
numantigo = 0
f = len(n)
while(i<f):
    if(i==0):
        ni = n[i]
    if(i == (f-1)):
        nf = n[i]

    i = i+1

if(ni == nf):
    print("o primeiro e o ultimo numero são iguais")
else:
    print("o primeiro e o ultimo numero não são iguais")
