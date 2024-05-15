def comprimento(n):
    nstr = str(n)
    split = nstr.split(" ")
    return len(split)

def ciclo(n):
    i = 1
    res = str(n)
    while(n != 1):
        if(n % 2 == 0):
            n = int(n/2)
        else:
            n = int(n*3+1)
        res = res + " " + str(n)
        i = i+1
    return res

k = int(input())
i = 0
while(i < k):
    n = int(input())
    print(ciclo(n))
    print(comprimento(ciclo(n)))