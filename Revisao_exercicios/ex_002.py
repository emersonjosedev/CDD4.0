'''2. Crie um código que leia um número
diferente de zero e diga se este número
é positivo ou negativo'''

numero = int(input("Digite um numero "))

if numero == 0:
    print("0 Nao é valido tente novamente!")

elif numero > 0:
    print("Numero Positivo")

else:
    print("Número negativo")