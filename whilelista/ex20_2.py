#Colocar em ordem crescente e ir fazendo de 2 em 2?
n = int(input())
c = 0
b = 0
while(c<n):
    a = int(input("Digite o "+str(c)+" numero: "))
    if(c != 0):
        m = 0

        if(c>=1):

            if(b>a):
                aux = a
                a = b
                b = aux

            i = b
            
            while(i>0):

                if(b!=0):
                    if(a%i == 0) and (b%i == 0):
                        m = i
                        i = i-b
                i = i-1
        else:
            m = a  
            
        b = a
    
    c = c+1

print(m)
