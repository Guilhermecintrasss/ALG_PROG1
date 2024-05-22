Gc_casa = 0
Gc_esc = 0
n = int(input())
i = 0
totalesc = 0
totalcasa = 0
while(i<n):
    ida,volta = input().split()

    if(ida == "chuva"):
        if(Gc_casa !=0):
            Gc_casa = Gc_casa - 1
            Gc_esc = Gc_esc + 1
        else:
            Gc_esc = Gc_esc + 1
            totalcasa = totalcasa+1
    if(volta == "chuva"):
        if(Gc_esc !=0):
            Gc_esc = Gc_esc - 1
            Gc_casa = Gc_casa + 1
        else:
            Gc_casa = Gc_casa + 1
            totalesc = totalesc+1
    i = i+1

print(str(totalcasa) + " " + str(totalesc))