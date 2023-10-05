p_p1 = 0
p_p2 = 0
for x in range(3):
    p1 = input("pedra, papel ou tesoura?")
    p2 = input("pedra, papel ou tesoura?")

    if p1 == "pedra" and p2 == "tesoura" or p1 == "tesoura" and p2 == "papel" or p1 == "papel" and p2 == "pedra":
        p_p1 += 1
        print(f" 1°Jogador  +{p_p1} pontos")

    elif p2 == "pedra" and p1 == "tesoura" or p2 == "tesoura" and p1 == "papel" or p2 == "papel" and p1 == "pedra":
        p_p2 += 1
        print(f" 2°Jogador  +{p_p2} pontos")

    else:
        print("Empatou")

if p_p1 > p_p2:
    print("Jogador 1 venceu")

elif p_p2 > p_p1:
    print("jogador 2 venceu")

else:
    print("empate")















