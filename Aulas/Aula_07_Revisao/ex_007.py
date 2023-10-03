n = int(input('Quantos Números voce quer tirar a media?'))
soma = 0
for x in range(n):
    nota = float(input("Qual a nota?"))
    soma = nota + soma

media = soma / n
print(media)