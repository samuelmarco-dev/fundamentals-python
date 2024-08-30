# Estrutura de repetição com loop For
nomesPessoas: list = []
nomesPaises: list = ['São Paulo', 'Paris', 'Rio de Janeiro', 'Miami', 'Berlim']
cidade: dict = {
    'nome': 'São Paulo',
    'estado': 'SP',
    'pais': 'Brasil',
    'pop': '12.3mi'
}

for x in nomesPaises:
    print(f'Cidade iterada: {x}')
print('\n')

for key in cidade:
    print(f'{key}: {cidade[key]}')
print('\n')

for index in range(5):
    entrada: str = input('Informe o do aluno: ')
    nomesPessoas.append(entrada)
print('\n')

for i in range(len(nomesPessoas)):
    print(f'Nome do aluno: {nomesPessoas[i]}')
print('\n')

# adiciona pares ao dicionário: hashTable
pares: dict = {}
arr_pares = []

for key in range(0, 51, 2):
    pares[key] = key
    arr_pares.append(key)

print(f'Show dict: {pares}')
print(f'Show Array: {arr_pares}')
