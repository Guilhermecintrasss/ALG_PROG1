def cpf_existe(cpf):
    fp = open("cadastros.csv","r")
    linhas = fp.readlines()
    fp.close()
    i = 0
    existe = False
    while(i<len(linhas)):
        info = linhas[i].split(",")
        cpf_aluno = info[0]

        if (cpf_aluno == cpf):
            existe = True
        i = i+1
    return existe

def disc_existe(disc):
    fp = open("disciplinas.csv","r")
    linhas = fp.readlines()
    fp.close()
    i = 0
    existe = False
    while(i<len(linhas)):
        info = linhas[i].split(",")
        nome = info[0].split("\n")
        nome = nome[0]
        if (nome == disc):
            existe = True
        i = i+1
    return existe
def ja_matriculado(cpf,nome_disc):
    fp = open("disciplinas.csv","r")
    linhas_disc = fp.readlines()
    i = 0
    existe = False
    while(i<len(linhas_disc)):
        info = linhas_disc[i].split(",")
        nomeAtual = info[0].split("\n")
        nomeAtual = nomeAtual[0]
        if(nomeAtual == nome_disc):
            j = 1
            while(j<len(info)):
                cpfAtual = info[j]
                if(cpf == cpfAtual):
                    existe = True
                j = j+1
        i = i+1
    return existe

def borda():
    print("****************************************")

def cadastrar_aluno(nome,cpf):
    existe = cpf_existe(cpf)
    if(existe == True):
        print("Porfavor, digite um CPF não existente")
    elif(len(cpf) != 14):
        print("Porfavor, digite um cpf valido")
    else:
        fp = open("cadastros.csv","a")
        fp.write(cpf + "," + nome + "\n")
        fp.close()

def cadastrar_disc(nome):
    existe = disc_existe(nome)
    if(existe == True):
        print("Porfavor, digite uma disciplina não existente")
    else:
        fp = open("disciplinas.csv","a")
        fp.write(nome + "\n")
        fp.close()

def remover_alunos(cpf_remover):
    fp = open("cadastros.csv","r")
    linhas = fp.readlines()
    removeu = False
    fp.close()
    dados = ""
    i = 0
    while(i<len(linhas)):
        info = linhas[i].split(",")
        nome = info[1]
        cpf_aluno = info[0]
        if(cpf_remover != cpf_aluno):
            dados = dados + cpf_aluno + "," + nome
        else:
            removeu = True
        i = i+1
    if(removeu == False):
        print("Não foi encontrado nenhum aluno com este CPF")
    else:
        fp = open("cadastros.csv","w")
        fp.write(dados)
        fp.close()
        fp = open("disciplinas.csv","r")
        linhas_disc = fp.readlines()
        fp.close()
        i = 0
        dados_disc = ""
        while(i<len(linhas_disc)):
            tudoSemN = linhas_disc[i].split("\n")
            info = tudoSemN[0].split(",")
            j = 1
            dados_disc = dados_disc + info[0]
            while(j<len(info)):
                cpf_aluno = info[j]
                if(cpf_aluno != cpf_remover):
                    dados_disc =  dados_disc + "," + cpf_aluno
                j = j+1

            dados_disc = dados_disc + "\n"

            i = i+1
        fp = open("disciplinas.csv","w")
        fp.write(dados_disc)
        fp.close()


def remover_disc(nomedisc_remover):
    fp = open("disciplinas.csv","r")
    linhas = fp.readlines()
    fp.close()
    removeu = False
    dados = ""
    i = 0
    while(i<len(linhas)):
        info = linhas[i].split(",")
        nomedisc = info[0].split("\n")
        nomedisc = nomedisc[0]
        if(nomedisc != nomedisc_remover):
            dados = dados + linhas[i]
        else:
            removeu = True
        i = i+1
    if(removeu == False):
        print("Não foi encontrado nenhuma disciplina com este nome")
    else:
        fp = open("disciplinas.csv","w")
        fp.write(dados)
        fp.close()
    
def editar_alunos(cpf_editar):
    existe = cpf_existe(cpf_editar)
    if(existe == True):
        fp = open("cadastros.csv","r")
        linhas = fp.readlines()
        fp.close()
        dados = ""
        novoCpf = ""
        i = 0
        while(i<len(linhas)):
            info = linhas[i].split(",")
            nome = info[1]
            cpf_aluno = info[0]
            if(cpf_editar == cpf_aluno):
                print("Nome antigo: " + str(nome))
                print("Digite o novo nome: ")
                novoNome = input()
                print("Cpf antigo: " + str(cpf_aluno))
                novoCpf = input()
                dados = dados + novoCpf + "," + novoNome + "\n"
            else:
                dados = dados + cpf_aluno + "," + nome
            i = i+1
    
        print(dados)
        fp = open("cadastros.csv","w")
        fp.write(dados)
        fp.close()
        fp = open("disciplinas.csv","r")
        linhas_disc = fp.readlines()
        fp.close()
        i = 0
        dados_disc = ""
        while(i<len(linhas_disc)):
            tudoSemN = linhas_disc[i].split("\n")
            info = tudoSemN[0].split(",")
            j = 1
            dados_disc = dados_disc + info[0]
            while(j<len(info)):
                cpf_aluno = info[j]
                if(cpf_aluno == cpf_editar):
                    dados_disc =  dados_disc + "," + novoCpf
                else:
                    dados_disc =  dados_disc + "," + cpf_aluno 
                j = j+1

            dados_disc = dados_disc + "\n"

            i = i+1
            fp = open("disciplinas.csv","w")
            fp.write(dados_disc)
            fp.close()
    else:
        print("CPF incorreto")


def editar_disc(disc_editar):
    fp = open("disciplinas.csv","r")
    linhas = fp.readlines()
    fp.close()
    dados = ""
    i = 0
    while(i<len(linhas)):
        tudoSemN = linhas[i].split("n")
        info = tudoSemN[0].split(",")
        nome_disc = info[0]
        
        if(disc_editar == nome_disc):
            print("Nome antigo: " + str(nome_disc))
            print("Digite o novo nome: ")
            novoNome = input()
            dados = dados + novoNome
        else:
            dados = dados + nome_disc
        j = 1
        while(j < len(info)):
            dados = dados + "," + info[j]
            j = j+1
        dados = dados
        i = i+1

    print(dados)
    fp = open("disciplinas.csv","w")
    fp.write(dados)
    fp.close()

def listar_alunos():
    fp = open("cadastros.csv","r")
    linhas = fp.readlines()
    fp.close()
    i = 0
    #print("Nome / CPF")
    while i < len(linhas):
        info = linhas[i].split(",")
        nome = info[1]
        cpf = info[0]
        print(str(i+1) + " - Cpf: " + cpf + " / Nome: " + nome)
        i = i+1
def listar_disc():
    fp = open("disciplinas.csv","r")
    linhas = fp.readlines()
    fp.close()
    i = 0
    while i < len(linhas):
        info = linhas[i].split(",")
        nome = info[0].split("\n")
        nome = nome[0]
        print(str(i+1) + " - Disciplina: " + nome)
        i = i+1

def matricular_aluno(cpf_aluno,nome_disc):
            fp = open("disciplinas.csv","r")
            linhas_disc = fp.readlines()
            fp.close()
            dados = ""
            i = 0
        
            while(i<len(linhas_disc)):
                info = linhas_disc[i].split(",") #com o \n
                nomedisc = info[0].split("\n")
                nomedisc = nomedisc[0]

                tudocomn = linhas_disc[i].split("\n")
                if(nome_disc == nomedisc):
                    tudo = tudocomn[0] #Tirei o \n
                    dados = dados + tudo + "," + cpf_aluno + "\n"
                else:
                    dados = dados + tudocomn[0] + "\n"
                i = i+1
            print(dados)
            fp = open("disciplinas.csv","w")
            fp.write(dados)
            fp.close()

def relatorio_matriculas():
    fp = open("cadastros.csv","r")
    linhas_alunos = fp.readlines()
    fp.close()

    fp = open("disciplinas.csv","r")
    linhas_disc = fp.readlines()
    fp.close()
    i = 0
    nomes_relatorio = []
    while(i<len(linhas_disc)):
        tudoSemN = linhas_disc[i].split("\n")
        info = tudoSemN[0].split(",")
        j = 1

        while(j<len(info)):
            cpf_disc = info[j]
            c = 0

            while(c<len(linhas_alunos)):
                info_aluno = linhas_alunos[c].split(",")
                cpf_aluno = info_aluno[0]
                nome_aluno = info_aluno[1]
                nome_aluno = nome_aluno.split("\n")
                nome_aluno = nome_aluno[0]
                if(cpf_disc == cpf_aluno):
                        
                        nome_no_cpf = nome_aluno

                c = c+1
            nomes_relatorio.append(nome_no_cpf)
            j = j+1

        print("Disciplina: " + info[0])
        print("Quantidade de matriculas: " + str(len(nomes_relatorio)))
        print("Alunos matriculados:")
        c2 = 0
        while(c2<len(nomes_relatorio)):
            print(str(c2+1) + "- " + str(nomes_relatorio[c2]))
            c2 = c2+1
        borda()
        nomes_relatorio = []
        i = i+1

continua = True
while continua:

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
        print("4 - Cadastrar um aluno em uma disciplina")
        print("5 - Listar alunos cadastrados")
        print("6 - Voltar")
        borda()
        op2 = int(input())

        if(op2 == 1):
            print("Digite o nome do aluno: ")
            nome = input()
            print("Digite o CPF do aluno: ")
            cpf = input()
            cadastrar_aluno(nome,cpf)

        if(op2 == 2):
            borda()
            print("Lista de alunos")
            listar_alunos()
            borda()
        
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
            borda()
            print("Lista de alunos")
            listar_alunos()
            borda()

            print("Digite o CPF do aluno que se matriculará:")
            cpf = input()
            existe = cpf_existe(cpf)
            if(existe):
                borda()
                print("Lista de Disciplinas")
                listar_disc()
                borda()

                print("Digite o nome da disciplina a qual ele se matriculará")
                disc = input()
                matriculado = ja_matriculado(cpf,disc)
                disciplina_existe = disc_existe(disc)
                if(disciplina_existe):
                    if(not matriculado):
                        matricular_aluno(cpf,disc)
                    else:
                        print("Aluno já matriculado")
                else:
                    print("Disciplina incorreta")
            else:
                print("CPF invalido")

        if(op2 == 5):
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
            listar_disc()
            borda()

            print("Digite o nome da disciplina que deseja remover: ")
            nomedisc = input()
            remover_disc(nomedisc)

        if(op2 == 3):
            borda()
            print("Lista de Disciplinas")
            listar_disc()
            borda()

            print("Digite o nome da disciplina que deseja alterar: ")
            nomedisc = input()
            editar_disc(nomedisc)

        if(op2 == 4):
            print("Nome / CPF")
            listar_disc()
    if(op1 == 3):
        relatorio_matriculas()

    if(op1 == 4):
        continua = False
        print("Até logo!")
        