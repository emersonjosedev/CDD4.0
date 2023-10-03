from random import randint

numero = int(input("Escolha um nuemro entre 1 e 10\n"))
aleatorio = randint(1,10)
print(f"o numero sorteado foi {aleatorio}")

if numero == aleatorio:
    print("Voce acertou")


else:
    print("Voce errou")