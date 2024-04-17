i = int(input())
while(i>0):
    h,m = input().split()
    h = int(h)
    m = int(m)
    mt = 1440 - ((h*60) + m)
    print(mt)
    i= i-1