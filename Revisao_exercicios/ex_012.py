'''12. Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores'''

eleitores = int(input("Quantos eleitores? "))
v_brancos= int(input("Quantos votos em branco? "))
nulos = int(input("Quantos nulos? "))
validos = int(input("Quantos validos? "))

r_vbrancos = (v_brancos / eleitores) * 100
r_nulos = (nulos / eleitores) * 100
r_validos = (validos / eleitores) * 100



print(f"{r_vbrancos}% brancos, {r_validos}% validos e {r_nulos}% nulos")




