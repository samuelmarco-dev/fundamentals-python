frase = """O professor Pietro da Let's Code disse: \"Hoje a pizza é por minha conta\""""
print(frase)

google: str = 'Google'
print(f'{(google[0:3]) + (google[4:5])}')

paises: str = "brasil, argentina, equador, colombia, chile, venezuela, peru"
print(paises.split(', '))
print('\n')

header: str = '             MENU PRINCIPAL                 '
print(header.strip())
print(header.replace(" ", ""))
print('\n')

formaterErr: str = 'LiMEIra - estADo dE SãO paULo'
print(formaterErr.title())
print(formaterErr.capitalize())
print(formaterErr.upper())
print(formaterErr.lower())
print('\n')

charFind: bool = 'limeira' in formaterErr.lower()
print(f'Limeira foi encontrada na string: {charFind}')
