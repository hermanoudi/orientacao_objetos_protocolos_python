# encapsulamento
# capacidade de esconder a implementação interna e expor apenas o que for conveniente.
# # Convenção de nomes

class Conta:
    _tipo_de_conta = "corrente" # protegido / protected (Somente pode ser usando dentro da classe)
    __id_interno = 456789 # Privado

    def __init__(self, cliente):
        self.cliente = cliente
        self._saldo = 0

    def consultar(self): # getter
        if self._saldo < 0:
            print("AVISO: Você está devendo...")
        return self._saldo

    def depositar(self, value):
        self._saldo += value

    def sacar(self, value):
        if self._saldo < value:
            print("AVISO: Saldo insuficiente")
        self._saldo -= value

conta = Conta("Hermano")
conta.depositar(100)
conta.depositar(50)
conta.sacar(80)
print(conta.consultar()) # code smell

print(dir(conta))
