import csv

header = ['nome', 'sobrenome']
dados = []
opt = int(input('Oque você deseja fazer?\n1- Cadastro\n0- Sair\n'))

while opt != 0:
    nome = input('Informe seu nome: ')
    sobrenome = input('Informe seu sobrenome: ')
    dados.append([nome, sobrenome])
    opt = int(input('O que você deseja fazer?\n1- Cadastro\n0- Sair\n'))
print(f'Dados informados pelo usuário: {dados}')

with open('./data.csv', 'w', encoding='utf-8', newline='') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(header)
    escritor.writerows(dados)
    #all = [header, dados] -> escritor.writerows(all)

with open('./data.csv', 'r', encoding='utf-8') as data:
    leitor = csv.reader(data, delimiter=',')
    for linha in leitor:
        print(linha)
