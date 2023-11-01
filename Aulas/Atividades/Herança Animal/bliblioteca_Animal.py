from playsound import playsound



class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'O {self.nome} foi comer...')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f'O {self.nome} está miando...')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f'O {self.nome} esta latindo...')





class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def grunir(self):
        print(f'O {self.nome}  grunindo...')

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f'O {self.nome} está mugindo...')


