# Dicionários- Estrutura de dados, coleção associativa desordenada
dadosCidades: dict = {'nomes': ['São Paulo', 'Rio de Janeiro'], 'populacao': [12.18, 8.78], 'pais': 'Brasil'}
dadosCidadesCopy = dadosCidades.copy()
dadosCidadesCopy.update({
    'updateAt': 'now'
})

if dadosCidades.get('prefeito'):
    print(f'O dicionário possui a chave prefeito: {dadosCidades["prefeito"]}')
else:
    print('O dicionário não possui a chave prefeito')

print(f'\nShow dict: {dadosCidades}')
print(f'Show dict copy: {dadosCidadesCopy}')

print(f'\nLista de chaves dict: {dadosCidades.keys()}')
print(f'Lista de chaves dict: {dadosCidades.values()}')
print(f'Lista de chaves dict: {dadosCidades.items()}')
