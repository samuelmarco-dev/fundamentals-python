class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular       # Atributo público
        self._saldo = saldo_inicial  # Atributo protegido
        self.__password = '1234'     # Atributo privado
        
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self._saldo += valor
        else:
            print("Saldo inválido!")
            
    @saldo.deleter
    def saldo(self):
        print("Saldo zerado!")
        self._saldo = 0


# Exemplo de uso
conta = ContaBancaria("João", 1000)
print(conta.saldo)

conta.saldo = 250
print(conta.saldo)

del conta.saldo
print(conta.saldo)
