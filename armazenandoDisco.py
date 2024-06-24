def escreve_no_arquivo(nomes,datas,quantidades):

    fp = open("gasolinas.csv","w") #Devolve um ponteiro do arquivo no disco
    #w, Permite escrever no arquivo, substituindo qualquer informação antes
    #r, Permite ler as linhas do arquivo
    #a, Escreve no final do arquivo, nao substui linhas

    i = 0
    tamanho = len(nomes)
    while i < tamanho:
        fp.write(str(nomes[i]) + ",")
        try: #Tente fazer isso
            fp.write(str(datas[i]) + ",")
        except IndexError:# Exeto quando dar o "IndexError", que seria erro de acessar posição invalida
            fp.write("-,")
        try:
            fp.write(str(quantidades[i]) + "\n")
        except IndexError:
            fp.write("-\n")
        i += 1
    fp.close() # Torna o ponteiro invalido
    fp = open("gasolinas.csv","r") 
    linhas = fp.readlines() # Cria um vetor com os dados que armazenou no disco
    #linhas[0] == "Pedro,01/01/24,12.3"
    #linhas[1] == "Samuel,02/02/24,34.6"
    #...
    i = 0
    while(i<len(linhas)):
        print("Cliente" + str(i)+":")
        print("\t" + linhas[i])
        i+=1
    

    fp.close() # Torna o ponteiro invalido

nomes = ["Pedro","Samuel","Julio"]
datas = ["01/01/24","02/02/24"]
quantidades = [12.3,34.6]
escreve_no_arquivo(nomes,datas,quantidades)



