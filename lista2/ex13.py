l1 = float(input("Digite um lado: "))
l2 = float(input("Digite um lado: "))
l3 = float(input("Digite um lado: "))

if(l2>l1):
    a = l1
    l1 = l2
    l2 = a
if(l3 > l1):
    a = l1
    l1 = l3
    l3 = a
if(l3>l2):
    a = l2
    l2 = l3
    l3 = a

if(l1>l2 + l3):
    print("Nao forma triangulo")
if(l1**2 == l2**2 + l3**2):
    print("Triangulo retângulo")
if(l1**2 > l2**2 + l3**2):
    print("Triangulo obtusangulo")
if(l1**2 < l2**2 + l3**2):
    print("Triangulo acutângulo")
if(l1 == l2) and (l1 == l3) and (l2 == l3):
    print("Triangulo equilatero")
elif(l1 == l2) or (l1 == l3) or (l2 == l3):
    print("Triangulo isosceles")