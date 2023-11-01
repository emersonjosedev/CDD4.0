class Pessoa:
    def __init__(self, nome, idade, peso, comida, comendo=False, falando = False, dormindo = False):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comida = comida
        self.comendo = comendo
        self.falando = falando
        self.domindo = dormindo

    def falar(self):

        if self.falando == False:
            print(f"{self.nome} está falando")
            self.falando = True
        else:
            print(f"{self.nome} já está falando")
    def parar_falar(self):
        if self. falando == True:
            self.falando = False
            print(f"{self.nome} parou de falar")
        else:
            pass
    def comer(self):

        if self.comendo == True:
            print(f"{self.nome} ja esta comendo")
        else:
            self.comendo = True
            print(f"{self.nome} esta comendo {self.comida}")
    def parar_comer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} parou de comer")
        else:
            pass

    def dormir(self):
        if self.domindo == False:
            print(f"{self.nome} esta dormindo")
            self.domindo = True
        else:
            print(f"{self.nome} já esta dormindo")

    def acordar (self):
        if self.domindo == True:
            self.domindo = False
            print(f"{self.nome} Acordou")
        else:
            pass

