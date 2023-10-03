'''11. Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias.'''

i_ano = int(input("Sua idade em anos? "))
i_mes = int(input("e quanros  meses ?"))
i_dia = int(input("E quantos dias?"))

calculo = (i_ano * 365) + (i_mes * 30) + i_dia

print(f"Você tem {calculo} dias.")