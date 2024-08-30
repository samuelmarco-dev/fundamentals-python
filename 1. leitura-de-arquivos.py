arquivo = open('./dom_casmurro.txt', 'r')  # or open('./dom_casmurro.txt', 'r', encoding='utf-8')
dom_casmurro = arquivo.read()
print(f'Informações do arquivo:\n {dom_casmurro}')
arquivo.close()

linhas_dom_casmurro = arquivo.readline()
print('Linhas do arquivo: \n')
while linhas_dom_casmurro != '':
    print(linhas_dom_casmurro, end='')
    linhas_dom_casmurro = arquivo.readline()
arquivo.close()

for linha in arquivo:
    print(linha, end='')
arquivo.close()

# fechar leitura automaticamente
with open('./dom_casmurro.txt', 'r') as livro_dom_casmurro:
    content = livro_dom_casmurro.read()
    print(content)
