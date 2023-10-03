senha = "cdd123"
d_senha = input("Digite a senha")
contador = 1

while d_senha != senha:
    contador = contador+  1
    d_senha = input("Digite a senha novamente")

    if contador >= 3 and senha != d_senha:
        print("Tentivas esgotadas")
        break

else:
    print("Bem vindo ")

