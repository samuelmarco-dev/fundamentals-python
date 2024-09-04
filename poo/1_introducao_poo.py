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
        print(f'{self.__class__.__name__}: {self.name} foi destruido da memória') 

name, idade = input('Digite seu nome: '), input('Digite sua idade: ')
user = User(name, idade)
user.print_user()
user.get_cargo()
print(user.__str__())

del user
