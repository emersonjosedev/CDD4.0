"""20. Escreva um algoritmo que receba do
usuário 10 números, guarde num array e
mostre:
1. todos os números ímpares;
2. todos os números pares;
3. todos os números positivos;
4. todos os números negativos;
5. todos os zeros que aparecem no array"""

a = []
for x in range(10):
    a.append((int(input("Digite 10 numeros inteiros"))))
n_impares = []
n_pares = []
n_positivos = []
n_negativos = []
n_zeros = []

for a in a:
    if a % 2 != 0:
        n_impares.append(a)
    else:
        n_pares.append(a)

    if a > 0:
        n_positivos.append(a)
    elif a < 0:
        n_negativos.append(a)
    else:
        n_zeros.append(a)

print(f"n° impares = {n_impares}\n n° pares = {n_pares}\n n°positivos = {n_positivos}\n"
      f" n° negativos = {n_negativos}\n n° zeros = {n_zeros}")
