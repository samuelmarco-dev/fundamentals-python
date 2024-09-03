# Solicita ao usuário um número inteiro
numero = int(input())

is_par = numero % 2 == 0
output = 'Par' if is_par else 'Ímpar'

print(output)
