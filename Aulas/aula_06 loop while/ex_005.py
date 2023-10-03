refazer = "s"
while refazer == "s":

        nota_av1 = float(input("Qual a nota av1"))
        while nota_av1 < 0 or nota_av1 > 10:
            nota_av1 = float(input("Valor invalido tente novamente entre 0 e 10 \n "))
        nota_av2 = float(input("Qual a nota av2"))

        while nota_av2 < 0 or nota_av2 > 10:
            nota_av2 = float(input("Valor invalido tente novamente entre 0 e 10 \n"))

        media = (nota_av2 + nota_av1) / 2

        print(f"Sua media é {media}")

        refazer = input("Quer refazer?")

        while refazer == "sim":
            break

