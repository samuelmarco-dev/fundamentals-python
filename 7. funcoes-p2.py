def calcular_media(array):
    soma = 0
    for index in range(len(array)):
        soma += array[index]
    return soma / len(array)


def soma_var(*args):  # nos retorna uma tupla
    print(args, type(args))


def print_info(**kwargs):  # nos retorna um dicionário
    print(kwargs, type(kwargs))


numbers: list = [1, 5, 8, 9, 5, 4, 7, 5, 6]
media = calcular_media(numbers)

print(f'A soma de {numbers} resulta em uma média de: {media:.3f}')

soma_var(1, 2, 4, 8, 9)
print_info(nome='Pietro', sobrenome='Ribeiro')
