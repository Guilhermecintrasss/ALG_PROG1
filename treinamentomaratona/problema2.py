d = int(input())
a,l,p = input().split()
a = int(a)
l = int(l)
p = int(p)

if(a>=d) and (l>=d) and (p>=d):
    print("S")
else:
    print("N")