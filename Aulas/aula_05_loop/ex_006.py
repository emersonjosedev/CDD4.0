acumula = 0
conta = 0

for x in range(4):
    numero = int(input("Digite"))
    if numero < 0:
        acumula = acumula +1
        print(numero)
        conta = conta +numero

positivo = 4 - acumula

print(positivo)
print(conta)













