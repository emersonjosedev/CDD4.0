'''Ler valor n e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive).Considere '''
n = int(input("Digite um Número"))

for x in range(1,n + 1, 1):
    print(x, end=" ")