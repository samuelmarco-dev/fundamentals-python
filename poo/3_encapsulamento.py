class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular       # Atributo público
        self._saldo = saldo_inicial  # Atributo protegido
        self.__password = '1234'     # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Depósito inválido!")

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saque inválido ou saldo insuficiente!")

    def consultar_saldo(self):
        return self._saldo

    # Método privado para uso interno
    def __aplicar_taxa(self, taxa):
        self._saldo -= self._saldo * taxa
        print(f"Taxa de {taxa * 100}% aplicada ao saldo.")

    def aplicar_taxa_de_manutencao(self):
        self.__aplicar_taxa(0.01)  # Exemplo de taxa de 1%
        
    def showPassword(self, password):
        if password == self.__password:
            print(self.__password)
        else:
            print('Senha inválida')


# Exemplo de uso
conta = ContaBancaria("João", 1000)
conta.depositar(200)
print(f"Saldo atual: R$ {conta.consultar_saldo():.2f}")

conta.sacar(150)  
print(f"Saldo atual: R$ {conta.consultar_saldo():.2f}") 

# Acessando um método privado indiretamente
conta.aplicar_taxa_de_manutencao()
print(f"Saldo após taxa de manutenção: R$ {conta.consultar_saldo():.2f}")

''' 
    Tentar acessar diretamente um atributo protegido ou método privado 
    não é uma boa prática, mas pode ser feito
    
    Por exemplo: print(conta._saldo) # Acesso a um atributo protegido
    conta.__aplicar_taxa(0.02)       # Erro, já que o método é privado.
'''
