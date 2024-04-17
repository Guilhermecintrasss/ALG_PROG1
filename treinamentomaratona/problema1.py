i = int(input())

qtd = input().split()

for i in qtd:
    i = int(i)
    if(i/14>1) and (i%14<=6) and (i%14>=1):
        print("YES")
    else:
        print("NO")