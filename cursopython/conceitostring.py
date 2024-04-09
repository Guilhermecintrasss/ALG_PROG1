#       posicões
#       -9 -8 -7 -6 -5 -4 -3 -2 -1
#       012345678
nome = "Guilherme"

print("Quantia de letras no nome " + str(len(nome))) #Conta a quantia de caracteres
print("Ultimo caractere do nome: " + nome[-1])
print("Apenas as letras do L pra frente: " + nome[3:]) #O ":" faz com que sejam lidas todos os elementos daquela posição pra frente
print("Apenas as letras atras do L " + nome[:3])
print("Apenas as letras atras da penultima letra  " + nome[:-2]) # da penultima letra pra tras
print("O nome inteiro : " + nome[:])
print("O nome do L ao E" + nome[3:6]) #Pega da posição 3 até antes da posição 6

mesa = ["banana","Pera"]
fruta = "Pera"

if(fruta in mesa): #Checa pra ver se um elemento esta presente em um vetor(Um texto contido em outro)
    print("A fruta esta na mesa")

nomefeio = "viniCius"

print("O seu nome com apenas a primeira letra mauiscula é: " + nomefeio.capitalize())
print("O seu nome com todas as letras minusculas é: " + nomefeio.casefold())
print("O seu nome com todas as leras maiusculas é: " + nomefeio.upper())
print("A letra i aparece no nome "+ str(nomefeio.count('i'))+ " vezes")
print(nomefeio.endswith("ius")) # Vai retornar true, já que o nome termina em ius
print(nomefeio.find('u'))  # Encontra a posição do elemento no vetor
print(nomefeio.isalnum()) #Verifica se o nomefeio é feito apenas de letras e numeros, "#,?,[],~" levam o resultado a ser falso, mas nesse caso nao tem então é verdadeiro
print(nomefeio.isnumeric()) # Verifica se todos são numeros
print("O nome substituindo todos os i, por 1: " + nomefeio.replace('i','1'))
print('''Textos com 3 aspas
      podem ser escritos em mais de 1
      linha''')
splitnes = (''' faturamento = 25
        meu nome é heitor
      aula de programacao''').splitlines()
print(splitnes[0],splitnes[1],splitnes[2]) #Separa em vetores por linhas
print("Vinicius começa com vini?: " + str(nomefeio.startswith('vini'))) #Checa com se começa com essas caracteres
nomefeioerrado = "   vinicius   "
print("Nome com imperfeições: " + nomefeioerrado)
print("nome sem espaços indesejados: " + nomefeioerrado.strip()) #Retira espaços

