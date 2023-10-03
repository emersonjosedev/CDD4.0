voltar = "sim"
while voltar == "sim":
    n1 = float(input("Digite sua nota "))
    n2 = float(input("Digite sua nota "))

    media = (n1 + n2) / 2

    if media >= 4 and media < 7:
        print(f"Recuperação com media {media}")
    elif media >= 7:
        print(f"aprovado com media {media}")
    else:
        print(f"Reprovado com media {media}")

    voltar = input("Quer refazer?")





