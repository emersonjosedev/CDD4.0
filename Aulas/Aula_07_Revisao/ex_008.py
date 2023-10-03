'''entrada = input("Digite 1 para saber antecessor ou 2 para sucessor  ou 3 para sair \n")
while entrada != "3":
    if entrada == "1":
        d_antecessor = int(input("Digite o para saber antecessor"))
        antecessor = d_antecessor- 1
        print(antecessor)
        entrada = input("Digite 1 para saber antecessor ou 2 para sucessor  ou 3 para sair \n")
    elif entrada == "2":
        d_sucessor = int(input("Digite para saber o sucessor"))
        sucessor = d_sucessor + 1
        print(sucessor)
        entrada = input("Digite 1 para saber antecessor ou 2 para sucessor  ou 3 para sair \n")
    else:
        break'''

#----------------------------RESPOSTA PROFESSOR-------------------------------

while True:
    entrada = input("Digite 1 para saber antecessor ou 2 para sucessor  ou 3 para sair \n")
    num = int(input("Digite o numero"))

    if entrada == "1":
        print(num - 1)

    elif entrada == "2":
        print(num +1)

    else:
        break











