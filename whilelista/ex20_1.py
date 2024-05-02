a = int(input())
b = int(input())
m = 0
if(b>a):
    aux = a
    a = b
    b = aux
i = b

while(i>0):
    if(a%i == 0) and (b%i == 0):
        m = i
        i = i-b

    i = i-1
print(m)
