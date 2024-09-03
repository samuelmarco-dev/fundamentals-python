salario = 1500

def salario_bonus(bonus):
    global salario
    
    salario += bonus
    return salario

def say_hello():
    print('Hello, World!')
    
def say_hello_user(user = ''):
    if not user:
        say_hello()
    
    else:
        print(f'Hello, {user}!')

say_hello_user()
say_hello_user('João da Silva')

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(retorna_antecessor_e_sucessor(10))

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    
'''
    Função apenas por posição
        def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
            ...
        def criar_carro(*args):
            modelo, ano, placa, marca, motor, combustivel = args
            ...
    
    Função apenas por nome
        def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
            ...
        def criar_carro(**kwargs):
            modelo = kwargs.get('modelo'), 
            ano = kwargs.get('ano'), 
            ...
'''

# Argumentos posicionais
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Argumentos via *args
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# Argumentos via **kwargs
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
