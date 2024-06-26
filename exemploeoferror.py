n1 = int(input())

continua = True
mensagem = ""

while continua:
    mensagem = mensagem + str(n1) + " ; "
    try:
        n1 = int(input())
    except EOFError:
        continua = False

#Lê as informações de input de um outro arquivo, e nao do teclado