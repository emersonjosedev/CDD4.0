'''8. Faça um código que receba 4
números e realize a soma deles e a
média entre eles. e mostre os
resultados'''

soma = 0
for x in range(4):
    numero = float(input("Digite um numero "))
    soma = soma + numero

media = soma/ 4

print(f"Sua média é {media}")