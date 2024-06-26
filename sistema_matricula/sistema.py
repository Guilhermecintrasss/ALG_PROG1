def borda():
    print("****************************************")

def cadastrar_aluno(nome,cpf):
    fp = open("cadastros.csv","a")
    fp.write(nome + " " + cpf + "\n")
    fp.close()

def remover_alunos(cpf_remover):
    fp = open("cadastros.csv","r")
    linhas = fp.readlines()
    fp.close()
    dados = ""
    i = 0
    while(i<len(linhas)):
        info = linhas[i].split(" ")
        nome = info[0]
        cpf_aluno = info[1]
        if(cpf_remover != cpf_aluno):
            dados = dados + nome + " " + cpf_aluno + "\n"

    fp = open("cadastros.csv","w")
    fp.write(dados)
    fp.close()

def cadastrar_disc(nome):
    fp = open("disciplinas.csv","a")
    fp.write(nome + "\n")
    fp.close()

def remover_disc(nomedisc_remover):
    fp = open("disciplinas.csv","r")
    linhas = fp.readlines()
    fp.close()
    dados = ""
    i = 0
    while(i<len(linhas)):
        nomedisc = linhas[i]
        if(nomedisc != nomedisc_remover):
            dados = dados + nomedisc + "\n"

    fp = open("disciplinas.csv","w")
    fp.write(dados)
    fp.close()

def listar(arquivo):
    fp = open(arquivo,"r")
    linhas = fp.readlines()
    fp.close()
    i = 0
    #print("Nome / CPF")
    while i < len(linhas):
        print("1 - " + linhas[i])
        i = i+1
    



borda()
print("Escolha o numero da area desejada")
print("1 - Operação com alunos")
print("2 - Operação com disciplinas")
borda()

remover_alunos

