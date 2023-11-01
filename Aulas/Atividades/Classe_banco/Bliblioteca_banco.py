class Conta:
    def __init__(self, numero,saldo, nome, tipo, status, limite ):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = status
        self.limite = limite

    def depositar(self,vr_deposito = False):
        if self.status == True:
            self.vr_deposito = vr_deposito
            self.saldo = self.vr_deposito + self.saldo
            return self.saldo
        else:
            pass




    def sacar(self,sacar):

        if self.status == True:
            self.sacar = sacar
            if self.sacar > self.saldo:
                print(f"Saque invalido! seu saldo é {self.saldo}$")
            else:
                self.saldo -= self.sacar
                print(self.saldo)
        else:
            pass







    def ativar_conta(self):
        if self.saldo <= 0:
            self.status = False

            print("Conta desativada")
        else:
            print("Conta ativada")






    def verificar_saldo(self):
        if self.status == True:
            print(f"Saldo {self.saldo}$")
        else:
            pass





