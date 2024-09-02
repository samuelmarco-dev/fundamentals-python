def verificador_ano_bissexto():
    ano = int(input())

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:
    divisivel_por_quatro = ano % 4 == 0
    divisivel_por_cem = ano % 100 == 0
    divivel_por_quatrocentos = ano % 400 == 0
    
    if (divisivel_por_quatro and not divisivel_por_cem) or divivel_por_quatrocentos:
        print('SIM')
    else:
        print('NÃO')

verificador_ano_bissexto()