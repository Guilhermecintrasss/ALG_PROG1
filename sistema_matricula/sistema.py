def borda():
    print("****************************************")

def cadastrar_aluno(nome,cpf):
    fp = open("cadastros.csv","a")
    fp.write(nome + " " + cpf + "\n")
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
        info = linhas[i].split(" ")
        nome = info[0]
        cpf_aluno = info[1]
        if(cpf_remover != cpf_aluno):
            dados = dados + nome + " " + cpf_aluno + "\n"

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
        if(nomedisc != nomedisc_remover):
            dados = dados + nomedisc + "\n"

    fp = open("disciplinas.csv","w")
    fp.write(dados)
    fp.close()
def editar_alunos():
    print("AAAA")
def editar_disc():
    print("AAAA")


def relatorio_matriculas():
    fp = open("disciplinas.csv","r")
    linhasdisc = fp.readlines()
    fp.close()

    fp = open("cadastros.csv","r")
    linhascad = fp.readlines()
    fp.close()
    i = 0
    contador = 1
    while i < len(linhasdisc):
        j = 0
        print("Disciplina: " + linhasdisc[i])

        while j <len(linhascad):
            info = linhascad[j].split(" ")
            nome = info[0]
            cpf = info[1]

def listar(arquivo):
    fp = open(arquivo,"r")
    linhas = fp.readlines()
    fp.close()
    i = 0
    #print("Nome / CPF")
    while i < len(linhas):
        print(str(i+1) + " - " + linhas[i])
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
    if(op2 == 4):
        print("Nome / CPF")
        listar("cadastros.csv")

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
        print("Digite o nome da disciplina que deseja remover: ")
        cpf = input()
        remover_disc(cpf)
    if(op2 == 4):
        print("Nome / CPF")
        listar("disciplinas.csv")
