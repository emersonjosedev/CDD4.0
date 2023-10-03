'''15. Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente'''

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

if n1 < n2:
    print(f"{n1}, {n2}")

else:
    print(f"{n2}, {n1}")