def quebra(n):
    nstr = str(n)
    i = 0
    num = ""
    if(len(nstr) == 1):
        pn = n
        un = n
    else:    
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
num = n
verify = True
while(num != ""):
    pn,un,num = quebra(num)
    if(pn != un):
        verify = False
if(verify):
    print("É palindromo")
else:
    print("Não é palindromo")
    
