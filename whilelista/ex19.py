n = int(input("Digite um numero natural: "))
i = 0
t = 0
while(i<n):
    t = (i+1)/(n-i) + t
    i = i+1
print(t)