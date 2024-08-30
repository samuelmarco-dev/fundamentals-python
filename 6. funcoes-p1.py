def somar(x=0, y=0):
    print(f'Irei somar {x} com {y}')
    return x + y


def pular():
    print('\n')


numbers: list = [5, 15]
soma = somar(numbers[0], numbers[1])

print(f'O resultado da soma é: {soma:.2f}')
pular()
