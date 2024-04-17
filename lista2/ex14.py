t1 = float(input("Digite a primeira temperatura: "))
t2 = float(input("Digite a segunda temperatura: "))
t3 = float(input("Digite a terceira temperatura: "))

if(t2<t1) and (t3>=t2): # temperatura diminuiu e aumentou ou permaneceu constante
    print("As pessoas ficaram felizes")
if(t2>t1) and (t3<=t2): # temperatura aumentou e diminuiu ou permaneceu constante
    print("As pessoas ficaram tristes")
if(t2>t1) and (t3>t2) and (t2-t1>t3-t2): #temperatura aumentou nos dois dias, mas aumentou menos do segundo para o terceiro dia
    print("As pessoas ficaram tristes")
if(t2>t1) and (t3>t2) and (t2-t1<=t3-t2): #temperatura aumentou nos dois dias, mas aumentou mais ou permaneceu constanto do segundo para o terceiro dia
    print("As pessoas ficaram felizes")
if(t2<t1) and (t3<t2) and (t2-t1>t3-t2): #temperatura diminuiu nos dois dias, mas diminuiu menos do segundo para o terceiro dia
    print("As pessoas ficaram felizes")
if(t2<t1) and (t3<t2) and (t2-t1<=t3-t2): #Temperatura diminuiu nos dois dias, mas diminuiu mais ou permaneceu constante do segundo para o terceiro dia
    print("As pessoas ficaram tristes")
if(t2 == t1):
    if(t3>t2):
        print("As pessoas ficaram felizes")
    else:
        print("As pessoas ficaram tristes")