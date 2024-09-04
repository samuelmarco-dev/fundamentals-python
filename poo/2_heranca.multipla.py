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


class Permissions:
    def __init__(self, permissions):
        self.permissions = permissions

    def show_permissions(self):
        print(f'Permissions: {", ".join(self.permissions)}')


# Herança Múltipla
class SuperUser(User, Permissions):
    cargo = 'superuser'
    
    def __init__(self, name, age, permissions):
        User.__init__(self, name, age)  # Chama o construtor da classe User
        Permissions.__init__(self, permissions)  # Chama o construtor da classe Permissions
        self.admin = True
        
    def print_user(self):
        super().print_user()
        self.show_permissions()


# Exemplo de uso
name, idade = input('Digite seu nome: '), input('Digite sua idade: ')
permissions = input('Digite as permissões do superuser (separadas por vírgula): ').split(',')
super_user = SuperUser(name, idade, permissions)
super_user.print_user()
super_user.get_cargo()
print(super_user.__str__())
