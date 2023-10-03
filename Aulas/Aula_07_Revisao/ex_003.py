idade = int(input("Qual sua idade?"))
mes_nascimento = int(input("Que mes você nasceu?"))
mes_atual = int(input("Qual o mes atual?"))


if mes_nascimento > mes_atual:
    ano =  2023 - idade -1
    print(f"Voce nasceu em {ano} ")

else:
    ano = 2023 - idade
    print(f"Voce nasceu em {ano}")



