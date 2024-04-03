import math


a = float(input("Digite a area a ser pintada \n"))
litros = a/3
qtdlatas = int(litros/18)
sobra = litros%18
qtdgaloes = math.ceil((sobra/3.6))
qtdlataspura = math.ceil(litros/18)
qtdgaloespura = math.ceil(litros/3.6)
p1 = qtdlataspura*80
p2 = qtdgaloespura*25
p3 = (qtdlatas*80) + (qtdgaloes*25)

print("Caso compre apenas latas de tinta, comprará um total de " + str(qtdlataspura) + " latas, gastando " + str(p1) + "R$ \n")

print("Caso compre apenas galoes de tinta, comprará um total " + str(qtdgaloespura) + " galoes, gastando um total de "+str(p2)+"R$\n")

print("Caso compre latas e galoes de tinta, comprará um total de " + str(qtdlatas) + " latas e "+ str(qtdgaloes) + " galões, gastando no final " +str(p3)+"R$\n")