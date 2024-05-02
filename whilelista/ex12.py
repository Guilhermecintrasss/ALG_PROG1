n = int(input("Digite o numero de estudantes: "))
i = 1
while(i<=n):
    nota = int(input("Digite a nota do estudante "+str(i)+": "))
    if(i == 1):
        nma = nota
        nme = nota
    if(nma<nota):
        nma = nota
    if(nme>nota):
        nme = nota
    i = i+1
print("A nota maxima foi: "+ str(nma))
print("A nota minima foi: "+str(nme))