n = int(input("Digite a quantidade de estudantes: "))
i = 0
ap = 0
rep = 0
mt = 0
while(i<n):
    n1 = int(input("Digite a nota da p1: "))
    n2 = int(input("Digite a nota da p2: "))
    n3 = int(input("Digite a nota da p3: "))
    m = (n1+n2+n3)/3
    print("A media desse aluno é: " + str(m))
    if(m>=5):
        ap = ap + 1
    else:
        rep = rep + 1
    mt = mt + m
    i = i+1
mt = mt/n
print("A quantidade de alunos reprovados foi: " + str(rep))
print("A quantidade de alunos aprovados foi: "+str(ap))
print("A media total da turma foi: " + str(mt))
