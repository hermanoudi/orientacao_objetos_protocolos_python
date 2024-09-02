# encapsulamento
# capacidade de esconder a implementação interna e expor apenas o que for conveniente.
# # Propriedades

class Conta:
    _tipo_de_conta = "corrente" # protegido / protected (Somente pode ser usando dentro da classe)
    __id_interno = 456789 # Privado

    def __init__(self, cliente):
        self.cliente = cliente
        self.__saldo = 0
    
    @property # getter
    def saldo(self):
        return self.__saldo
    

    @saldo.setter
    def saldo(self, value):
        self.__saldo += value

    
    @saldo.deleter
    def saldo(self):
        self.__saldo = 0



conta = Conta("Hermano")
print(conta.cliente)
conta.saldo = 200
print(conta.saldo)

conta.saldo = -50
print(conta.saldo)

del conta.saldo
print(conta.saldo)
