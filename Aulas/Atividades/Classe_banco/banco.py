from Bliblioteca_banco import *
banco = Conta("002",0,"Emerson", "Corrente",True,0)

banco.depositar(29)
banco.depositar(3)

banco.sacar(100)
banco.verificar_saldo()
banco.ativar_conta()
'''Crie uma classe que tenha os atributos, número da
conta, saldo, status da conta( se ela está ativa ou
não), nome do cliente, tipo da conta. e que possibilite
ao cliente, depositar, sacar, verificar saldo e
possibilidade de ativar a conta ou desativar a conta.
para desativar uma conta, é necessário que o saldo
este zerado.

conta bancária
atributos:
*número
*saldo
*nome
*tipo
*status
*limite
métodos
*depositar
*sacar
*ativarconta
*verificarsald
'''


