time1 = input("Digite o nome do seu time")
gol1 = int(input(f"Quantos gols o {time1} marcou?"))

time2 = input("Digite o nome do seu time")
gol2 = int(input(f"Quantos gols o {time2} marcou?"))

if gol1 == gol2:
    print("Empate")

else:
    if gol1 > gol2:
        print(f"O {time1} venceu")
    else:
        print(f"O {time2} venceu")


