'''5. Crie um algoritmo que leia um
número e diga se ele é par ou ímpar'''

numero = int(input("Digite um número para saber se e par ou ímpar"))
resultado = numero % 2

if resultado == 0:
    print("Número par")
else:
    print("Número ímpar")


