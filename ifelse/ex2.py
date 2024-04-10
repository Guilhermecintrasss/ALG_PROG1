d = int(input("Digite o dia que voce nasceu: "))
m = int(input("Digite o mes que voce nasceu: "))
a = int(input("Digite o ano que voce nasceu: "))
da = int(input("Digite o dia atual: "))
ma = int(input("Digite o mes atual: "))
aa = int(input("Digite o ano atual: "))

idade = aa - a

if(m>ma):
    idade = idade - 1
elif(d>da):
    idade = idade-1

print(idade)