n = int(input("Digite a quantidade de numeros exibidos"))
a = int(input("Digite a primeira possibilidade de multiplo"))
b = int(input("Digite a segunda possibilidade de multiplo"))
i = 0
while (n!=0): 

    if(i%a == 0) or (i%b == 0):
        print(i)
        n = n-1
    i = i+1