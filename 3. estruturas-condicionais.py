precoApp: float = float(input('Informe o valor da corrida em seu app favorito: R$'))
valorPassagem: float = float(input('Informe o valor da passagem de ônibus: R$'))

if precoApp <= 30.00 and precoApp <= valorPassagem*5:
    print(f'Legal! Estou disposto a pagar R${precoApp} pela corrida')
elif precoApp <= valorPassagem*6:
    print(f'Hmm! O preço está dinâmico, aguarde 3min para verificar se o preço da corrida iŕa diminuir')
else:
    print(f'Não estou disposto a pagar R${precoApp} pela corrida! Vou de ônibus...')
