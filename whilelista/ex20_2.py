def mdc(n1,n2):
    resto = 1
    while(resto!=0):
        resto = n1%n2
        n1 = n2
        n2 = resto
    return n1

num = int(input())
i = 0
a = 0
b = 0
while(i<num):
    if(i==0):
        a = int(input())
        m = a
    else:
        b = int(input())
        m = mdc(a,b)
        a = m
    i = i+1

print(m)
    


    