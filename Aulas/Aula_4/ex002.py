h = int(input("Digite a hora"))
m = int(input("Digite a hora"))
h2 = int(input("Digite a hora"))
m2 = int(input("Digite a hora"))
tempo = 0

if h > 12:
    h -= 12


if h2 > 12:


    h2 -= 12


total_min = m + m2

if total_min > 60:
    total_min -= 60
    tempo = +1


total_hora = h + h2 + tempo

if total_hora > 12:
    total_hora -= 12


print(f"Sao {total_hora}:{total_min}")



