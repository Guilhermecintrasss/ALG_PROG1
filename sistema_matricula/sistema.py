def borda():
    print("****************************************")

def cadastrar_aluno(nome,cpf):
    fp = open("cadastros.csv","a")
    fp.write(nome + "," + cpf + "\n")
    fp.close()

def cadastrar_disc(nome):
    fp = open("disciplinas.csv","a")
    fp.write(nome + "\n")
    fp.close()

def remover_alunos(cpf_remover):
    fp = open("cadastros.csv","r")
    linhas = fp.readlines()
    fp.close()
    dados = ""
    i = 0
    while(i<len(linhas)):
        info = linhas[i].split(",")
        nome = info[0]
        cpf_aluno = info[1]
        if(cpf_remover+"\n" != cpf_aluno):
            dados = dados + nome + "," + cpf_aluno
        i = i+1
    print(dados)
    fp = open("cadastros.csv","w")
    fp.write(dados)
    fp.close()

def remover_disc(nomedisc_remover):
    fp = open("disciplinas.csv","r")
    linhas = fp.readlines()
    fp.close()
    dados = ""
    i = 0
    while(i<len(linhas)):
        nomedisc = linhas[i]
        if(nomedisc != nomedisc_remover+"\n"):
            dados = dados + nomedisc
        i = i+1

    fp = open("disciplinas.csv","w")
    fp.write(dados)
    fp.close()
    
def editar_alunos(cpf_editar):
    fp = open("cadastros.csv","r")
    linhas = fp.readlines()
    fp.close()
    dados = ""
    i = 0
    while(i<len(linhas)):
        info = linhas[i].split(",")
        nome = info[0]
        cpf_aluno = info[1]
        if(cpf_editar + "\n" == cpf_aluno):
            print("Nome antigo: " + str(nome))
            print("Digite o novo nome: ")
            novoNome = input()
            print("Cpf antigo: " + str(cpf_aluno))
            novoCpf = input()
            dados = dados + novoNome + "," + novoCpf + "\n"
        else:
            dados = dados + nome + "," + cpf_aluno
        i = i+1
    
    print(dados)
    fp = open("cadastros.csv","w")
    fp.write(dados)
    fp.close()


def editar_disc(disc_editar):
    fp = open("disciplinas.csv","r")
    linhas = fp.readlines()
    fp.close()
    dados = ""
    i = 0
    while(i<len(linhas)):
        nome_disc = linhas[i]

        if(disc_editar + "\n" == nome_disc):
            print("Nome antigo: " + str(nome_disc))
            print("Digite o novo nome: ")
            novoNome = input()
            dados = dados + novoNome + "\n"
        else:
            dados = dados + nome_disc
        i = i+1
    
    print(dados)
    fp = open("disciplinas.csv","w")
    fp.write(dados)
    fp.close()


def relatorio_matriculas():
    print("AAAA")

def listar_alunos():
    fp = open("cadastros.csv","r")
    linhas = fp.readlines()
    fp.close()
    i = 0
    #print("Nome / CPF")
    while i < len(linhas):
        info = linhas[i].split(",")
        nome = info[0]
        cpf = info[1]
        print(str(i+1) + " - Nome: " + nome + " / Cpf: " + cpf)
        i = i+1
def listar_disc():
    fp = open("disciplinas.csv","r")
    linhas = fp.readlines()
    fp.close()
    i = 0
    while i < len(linhas):
        nome = linhas[i]
        print(str(i+1) + " - Disciplina: " + nome)
        i = i+1



borda()
print("Escolha o numero da area desejada")
print("1 - Operação com alunos")
print("2 - Operação com disciplinas")
print("3 - Relatório de matrículas")
print("4 - Sair")
borda()
op1 = int(input())
if(op1 == 1):

    borda()
    print("1 - Cadastrar um aluno")
    print("2 - Remover um aluno")
    print("3 - Editar um aluno")
    print("4 - listar alunos cadastrados")
    print("5 - Voltar")
    borda()
    op2 = int(input())

    if(op2 == 1):
        print("Digite o nome do aluno: ")
        nome = input()
        print("Digite o CPF do aluno: ")
        cpf = input()
        cadastrar_aluno(nome,cpf)

    if(op2 == 2):
        print("Digite o CPF do aluno que deseja remover: ")
        cpf = input()
        remover_alunos(cpf)

    if(op2 == 3):
        borda()
        print("Lista de alunos")
        listar_alunos()
        borda()

        print("Digite o cpf do aluno que deseja alterar: ")
        cpf = input()
        editar_alunos(cpf)

    if(op2 == 4):
        print("Nome / CPF")
        listar_alunos()

if(op1 == 2):
    borda()
    print("1 - Cadastrar uma disciplina")
    print("2 - Remover uma disciplina")
    print("3 - Editar uma disciplina")
    print("4 - listar disciplinas cadastradas")
    print("5 - Voltar")
    borda()
    op2 = int(input())
    if(op2 == 1):
        print("Digite o nome da disciplina: ")
        nome = input()
        cadastrar_disc(nome)
    if(op2 == 2):
        borda()
        print("Lista de Disciplinas")
        listar_alunos()
        borda()

        print("Digite o nome da disciplina que deseja remover: ")
        nomedisc = input()
        remover_disc(nomedisc)
    if(op2 == 4):
        print("Nome / CPF")
        listar_disc()
