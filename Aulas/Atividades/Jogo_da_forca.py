'''Lembre-se do jogo da forca
Detalhe, desenhando a forca
----------
|.         |
|.         @
|.        /|\
|.         /\
|.'''

palavra = "elefante"
sequencia = input("Digite a sequência de caracteres: ")


letras = []

if sequencia in palavra:
    for i in range(len(sequencia)):
        letra = input(f"Digite a letra {i + 1}: ")
        if letra in sequencia:
            letras.append(letra)
print(letras)









