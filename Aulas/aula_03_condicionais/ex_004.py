combustivel = input("Gasolina ou e-tanol")
litros = float(input("quantos litros?"))


if combustivel == "g":
    gasolina = 5.80
    print(f"Voce ira pagar {gasolina * litros}")

else:
    etanol = 4.90
    print(f"Voce ira pagar {etanol * litros}")

