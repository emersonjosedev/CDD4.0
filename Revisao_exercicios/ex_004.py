'''4. Crie um algoritmo que receba 3
números e informe qual o maior entre
eles.'''

n1 = int(input("Digite o N1 "))
n2 = int(input("Digite o N2 "))
n3 = int(input("Digite o N3 "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior numero")

elif n2 > n3:
    print(f"{n2} é o maior numero")

else:
    print(f"{n3} é o maior numero")