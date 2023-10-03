repetir = "sim"
while repetir == "sim":
    n1 = int(input("Digite o numero 1 "))
    n2 = int(input("Digite o numero 2 "))
    n3 = int(input("Digite o numero 3 "))

    if n1 > n2:
        if n1 > n3:
            print("N1  e maior")
        else: print("N3 e maior")
    elif n2 > n3:
        print("n2 e maior")
    else:
        print("N3 e maior")
    repetir = input("deseja repetir?")