n = int(input("Digite o numero de senquencias: "))
num = 1
soma = 0
res = ""
while(0<n):

    while(num != 0):
        num = int(input("Digite numeros da sequencia(0 termina): "))
        if(num%2 == 0):
            soma = soma+num
    res = res + str(soma) + " "
    soma = 0
    num = 1
    n=n-1
print(res)