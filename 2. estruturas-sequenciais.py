# Prever montante que o usuário pode economizar dado seu salário mensal
salario = float(input('Informe seu salário: R$ '))
confirm = input('Confirme seu salario com "sim": ')

while confirm != 'sim':
    salario = float(input('Informe seu salário: R$ '))
    confirm = input('Confirme seu salario com "sim": ')

gastoMensal = float(input('Informe seu gasto mensal médio: R$ '))
confirm2 = input('Confirme seu salario com "sim": ')

while confirm2 != 'sim':
    gastoMensal = float(input('Informe seu gasto mensal médio: R$ '))
    confirm2 = input('Confirme seu salario com "sim": ')

print(f'Valor que pode ser economizado anualmente: {(salario*12) - (gastoMensal*12)}')
