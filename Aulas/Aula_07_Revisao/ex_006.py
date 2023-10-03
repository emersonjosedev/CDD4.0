refazer = "sim"
while refazer == "sim":
    base = int(input("base?"))
    while base == 0 :
        base = int(input("base?"))
    altura = int(input("Altura"))
    while altura == 0 :
        altura = int(input("Altura"))
    a = (base * altura) /2
    print(a)
    refazer = input("Quer refazer?")








