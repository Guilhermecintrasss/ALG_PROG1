i=1
tempextra = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
tempresp = 0
alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
qtdcorreta = 0
while(i!=0): 

    n= int(input())
    i = n
    if(i != 0): 

        while(n>0):
            c = 0
            let,min,resp = input().split()
            min = int(min)
            va = len(alfa) - 1
            while(va>=c): # Como eu consigo percorrer o alfabeto sem necessariamente ir para a proxima letra quando ele errar

                if(let == alfa[c]):
                    if(resp == "correct"):

                        tempresp = tempextra[c] + min + tempresp
                        qtdcorreta = qtdcorreta+1

                    elif(resp == "incorrect"):

                        tempextra[c] = tempextra[c] + 20

                c = c+1


            n = n-1
        print(str(qtdcorreta) + " " + str(tempresp))
        qtdcorreta = int(qtdcorreta)
        tempresp = int(tempresp)
        qtdcorreta = 0
        tempresp = 0
        tempextra = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
