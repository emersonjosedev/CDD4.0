'''14. Escreva um algoritmo para ler uma
temperatura em graus Fahrenheit, calcular
e escrever o valor correspondente em graus
Celsius (baseado na fórmula abaixo):
C = ((F - 32)/9)*5
Observação: Para testar se a sua resposta
está correta saiba que 100 ⍛C = 212 '''

f = float(input("Quantos graus Fahrenheit?"))

c = ((f-32) /9) *5

print(f"{f}°f em °c é {c}°c")