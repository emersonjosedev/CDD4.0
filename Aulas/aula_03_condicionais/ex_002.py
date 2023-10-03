n1 = float(input("Escreva um número"))
n2 = float(input("Escreva um número"))
n3 = float(input("Escreva um número"))

if n1 or n2 or n3 <0 or n1 or n2 or n3 > 10:
    print("Digite uma nota valida")


soma = (n1+n2+n3) / 3

if soma >= 7:
    print("Aprovado")

else:
    if soma < 4:
        print("Reprovado")

    else:
        print("Recuperaçao")


