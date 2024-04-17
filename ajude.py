i=1
c = 0
tempexra = 0
alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while(i!=0):

    n= int(input())
    i = n
    if(i != 0):

        while(n>0):

            let,min,resp = input("Digite a letra, o minuto e a resposta: ").split()

            while(len(alfa)>=c): # Como eu consigo percorrer o alfabeto sem necessariamente ir para a proxima letra quando ele errar

                if(let == alfa[c]):
                    if(resp == "correct"):
                        tempresp = tempextra[c] + min
                    elif(resp == "incorrect"):
                        tempextra = tempextra[c] + 20
            c = c+1


            n = n-1

