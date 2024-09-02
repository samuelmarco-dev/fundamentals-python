cumprimento: str = 'Olá, '
nome: str = input('Informe seu nome: ')

print(cumprimento + nome)
print(nome * 3)
print(f'{cumprimento}{nome}. Seja bem-vindo\n')

price: float = 6.549
print(f'O preço do diesel hoje está em: R${price:.2f}')
print(f'O preço do diesel hoje está em: R${round(price, 2)}')
