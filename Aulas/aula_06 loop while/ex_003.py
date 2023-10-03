valor1 = int(input("DIGITE VALOR 1\n"))
valor2 = int(input("DIGITE VALOR 2\n"))
parar = 1

while valor2 == 0:

    valor2 = int(input("0 e invalido cara! novamente"))
    parar += 1
    if parar == 5:
        print("Número de tentativas esgotadas")
        break
else:
    divisao = valor1 / valor2
    print(f"O resultado da divisão é : {divisao}")







