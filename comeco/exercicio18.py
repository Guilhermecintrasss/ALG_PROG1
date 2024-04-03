areap = int(input("Informe a area a ser pintada em metros quadrado \n"))

latas = int(round(((areap/3)/18)+0.49)) # round(x) arredonda x para baixo ou para cima, mas quero que ele sempre arredonde pra cima, assim somo 0.49
valort = latas*80

print("A quantidade de latas usadas serão ",latas," dando um total de ",valort,"R$ \n")

