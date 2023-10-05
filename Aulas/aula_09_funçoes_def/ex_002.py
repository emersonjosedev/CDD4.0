from bliblioteca import  *


while True:
    entrada = input("Digite 1 para multiplicar, 2 para somar, 3 para subtrair, 4 para dividir ou qualquer outra tecla para sair:\n")
    num1 = int(input("Digite o n1"))
    num2 = int(input("Digite o n2"))
    if entrada =="1":
        multi(num1, num2)
        multi(num1, num2)
        multi(num1, num2)
    elif entrada == "2":
        somar(num1, num2)
    elif entrada == "3":
        subtrair(num1, num2)
    elif entrada == "4":
        dividir(num1, num2)
    else:
        print("Opçao invalida! tente novamente!")








