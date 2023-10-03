nome = input("Qual seu nome?\n")

idade = int(input("Qual sua idade?\n"))

salario = float(input("Qual o seu salario?\n"))

aumento_1 = float(input("Qual seu aumento?"))

aumento2 = aumento_1 / 100 * salario

aumento_final = salario + aumento2

quantos_filhos = int(input("Quantos boneco te meteram?"))

abono = 150 * quantos_filhos

ferias = (aumento_final / 3)  + aumento_final

desconto_inss = (aumento_final / 100 *8)
desconto_ir = (aumento_final / 100 *15)

renda_total = (ferias -desconto_ir - desconto_inss) + abono

print(f"Hola {nome} sua idade é {idade} \nseu salario é {salario} seu salario final  é {aumento_final}\n voce tem {quantos_filhos} seu "
      f"abono e de {abono}\n seu abono de ferias é {ferias}\n sua renda total é {renda_total}")

