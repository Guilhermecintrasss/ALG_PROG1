def mdc(n1,n2):
    resto = 1
    while(resto!=0):
        resto = n1%n2
        n1 = n2
        n2 = resto
    return n1

n1 = int(input())
n2 = int(input())

print(mdc(n1,n2))