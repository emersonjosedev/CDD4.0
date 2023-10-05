def multi(n1, n2):
    resposta = n1 * n2
    print(f"resposta da mutiplicaçao é {resposta}")

def somar(n1, n2):
    resposta = n1 + n2
    print(f"resposta da soma é {resposta}")

def subtrair(n1, n2):
    resposta = n1 - n2
    print(f"resposta da subitraçao é {resposta}")

def dividir(n1, n2):
    resposta = n1 / n2
    print(f"resposta da divisao é {resposta}")

def numero_sequencial():
    num = int(input("Digite um número"))
    for x in range(1, num + 1):
        for y in range(1, x + 1):
            print(x, end=(" "))
        print()

def n_sequencial_2():
    num = int(input("Digite um número"))
    for x in range(num + 1):
        for y in range(1, x + 1):
            print(y, end=(" "))
        print()

def vogais_totais(texto):
    contador = 0
    for x in texto:
        if x in "aeiou":
            contador +=1
    print(f"Total de vogais = {contador}")

def estoque(produtoo,quantidade,valor):
     calculo = quantidade * valor
     return calculo

