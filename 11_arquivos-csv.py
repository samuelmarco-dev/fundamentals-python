# CVS: comma separated values - valores separados por vírgula
import csv

# leitura de código .csv
with open('./covid.csv', 'r', encoding='utf-8') as covid_brasil:
    leitor = csv.reader(covid_brasil)
    next(leitor)
    for linha in leitor:
        if float(linha[2]) >= 1:
            print(linha)

# mesmo código de forma nativa
with open('./covid.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha)

# escrevendo arquivos .csv
with open('./users.csv', 'w', encoding='utf-8', newline='') as data_users:
    escritor = csv.writer(data_users)
    escritor.writerow(['nome', 'sobrenome', 'e-mail', 'gênero'])
    escritor.writerow(['pietro', 'roberto', 'pietro@email.com', 'masculino'])

with open('./users.csv', 'r', encoding='utf-8') as data_read:
    leitor = csv.reader(data_read)
    for linha in leitor:
        print(linha)
