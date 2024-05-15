def quebra(n):
    nstr = str(n)
    i = 0
    num = ""
    while(i<len(nstr)):
        if(i == 0):
            pn = nstr[i]
        elif(i == len(nstr) - 1):
            un = nstr[i]
        else:
            num = num+nstr[i]
        i = i+1
    return pn,un,num


n = int(input())
p,u,num = quebra(n)
print(p)
print(u)
print(num)
