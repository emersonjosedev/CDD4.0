h_inico = int(input("Que horas começou?"))
h_fim = int(input("Que horas terminou?"))


if h_fim >= h_inico:
    hora = h_fim - h_inico

else:
   hora = 24 - h_inico + h_fim

print(hora)


