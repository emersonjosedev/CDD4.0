'''Usando While escreva um algoritmo
que preencha um array A com os 10
primeiros números ímpares, iniciando por
zero
saída
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]'''

contador = 1
a = []
n_impar = 1

while contador <11:
    a.append(n_impar)
    n_impar += 2
    contador += 1

print(a)

