nome = input("Digite seu nome: ").strip()
email = input("Digite seu email: ").strip()

cn = len(nome)
ce = len(email)
arroba = email.find('@')
if(cn>=1) and (ce>=1) and ("." in email[arroba:]) and ("@" in email):
        print("O email foi digitado corretamente, usuario cadastrado com sucesso")
else:
    print("Email digitado incorretamente")

        