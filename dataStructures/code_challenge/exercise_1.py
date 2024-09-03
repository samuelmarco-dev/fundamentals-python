def soma_tupla(tuple):
    return sum(tuple)

# Defininfo a tupla manualmente
tuple_numeros = tuple([2, 5, 6, 7, 9])
resultado = soma_tupla(tuple_numeros)
print(f'A soma dos elementos da tupla é: {resultado}')

# Utilizando a entrada via string
entrada = input()
tuple_numeros = tuple(map(int, entrada.split()))
resultado = soma_tupla(tuple_numeros)
print(f'A soma dos elementos da tupla é: {resultado}')
