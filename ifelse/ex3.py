n1 = int(input("Digite um valor: ")) 
n2 = int(input("Digite outro valor: "))
n3 = int(input("Digite ouro valor: "))
n4 =  int(input("Digite ouro valor: "))

if(n1>n2) and (n1>n3) and (n1>n4):
    a = n1
    n1 = n4
    n4 = n1

    if(n2> n1):
        a = n1
        n1 = n2
        n2 = a
    if(n3 > n2):
        a = n2
        n2 = n3
        n3 = a
    if(n2> n1):
        a = n1
        n1 = n2
        n2 = a
    if(n3 > n1):
        a = n1
        n1 = n3
        n3 = a
if(n2>n1) and (n2>n3) and (n2>n4):
    a = n2
    n2 = n4
    n4 = a
    if(n2> n1):
        a = n1
        n1 = n2
        n2 = a
    if(n3 > n2):
        a = n2
        n2 = n3
        n3 = a
    if(n2> n1):
        a = n1
        n1 = n2
        n2 = a
    if(n3 > n1):
        a = n1
        n1 = n3
        n3 = a
if(n3>n1) and (n3>n2) and (n3>n4):
    a = n3
    n3 = n4
    n4 = a
    if(n2> n1):
        a = n1
        n1 = n2
        n2 = a
    if(n3 > n2):
        a = n2
        n2 = n3
        n3 = a
    if(n2> n1):
        a = n1
        n1 = n2
        n2 = a
    if(n3 > n1):
        a = n1
        n1 = n3
        n3 = a
if(n4>n1)and(n4>n2)and(n4>n3):
    a = n4
    n4 = n1
    n1 = a
    if(n2> n1):
        a = n1
        n1 = n2
        n2 = a
    if(n3 > n2):
        a = n2
        n2 = n3
        n3 = a
    if(n2> n1):
        a = n1
        n1 = n2
        n2 = a
    if(n3 > n1):
        a = n1
        n1 = n3
        n3 = a

print("A ordem é: " + str(n1) + str(n2) + str(n3) + str(n4))




