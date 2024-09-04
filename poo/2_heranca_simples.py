class User:
    cargo = 'user'
    
    def __init__(self, name, age):
        self.name = name
        self.idade = age
        self.admin = False
        
    def print_user(self):
        print(f'User: {self.name}, {self.idade}')   
        
    def get_cargo(cls):
        print(cls.cargo)
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def __del__(self):
        print(f'{self.__class__.__name__}: {self.name} foi destruído da memória')


# Herança Simples
class Admin(User):
    cargo = 'admin'
    
    def __init__(self, name, age, privileges):
        super().__init__(name, age)  # Chama o construtor da classe base
        self.admin = True
        self.privileges = privileges

    def print_user(self):
        super().print_user()
        print(f'Privileges: {self.privileges}')
        

# Exemplo de uso
name, idade = input('Digite seu nome: '), input('Digite sua idade: ')
privileges = input('Digite os privilégios do admin: ')
admin = Admin(name, idade, privileges)
admin.print_user()
admin.get_cargo()
print(admin.__str__())
