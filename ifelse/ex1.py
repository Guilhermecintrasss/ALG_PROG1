n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))
n3 = int(input("Digite sua terceira nota: "))
ml = int(input("Digite sua media nas listas: "))

media = (n1 + n2*2 + n3*3 + ml*2)/7

if(media>=9):
    print("Conceito A")

if(media>=7.5) and (media<9):
    print("Conceito B")

if(media>=6) and (media<7.5):
    print("Conceito C")

if(media>=4) and (media<6):
    print("Conceito D")

if(media<4):
    print("Conceito E")