# Listas e Tuplas
array: list = ['brasil', 'argentina', 'equador', 'colombia', 'chile', 'venezuela', 'peru']
arrayCPF: list = []

print(f'Show list: {array} -> Length: {len(array)}\n')
print(f'País encontrado: {array[0]}')
print(f'Países encontrados: {array[2:5]}')
print(f'Países encontrados: {array[:2]}')
print(f'Países encontrados: {array[5:]}')
print(f'Países encontrados: {array[::2]}')
print(f'Países encontrados: {array[::-1]}')  # syntax sugar

brasilFind = 'brasil' in array
print(f'Brasil foi encontrado na lista: {brasilFind}\n')

arrayCPF.append('51684935702')
arrayCPF.append('78538563009')
arrayCPF.append('64557054080')
arrayCPF.insert(1, '41120138094')

print(f'Show Cpfs: {arrayCPF}\n')
arrayCPF.remove('51684935702')
print(f'Removendo elemento a partir do valor: {arrayCPF}')
arrayCPF.pop(-1)
print(f'Removendo elemento a partir do índice: {arrayCPF}')

# Tupla: Uma vez definida não pode ser alterada
usuario: tuple = ('João', 'Gabriel', 'Ronaldo', 'Fernanda', 'Joaquina', 'Pedro')
print(f'Show tuple: {usuario}')
# unpacking
j, g, r, f, jq, p = usuario
