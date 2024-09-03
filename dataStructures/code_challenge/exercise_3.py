def contar_caracteres(string):
    chave_valor = dict()
    
    for letra in string:
        if letra in chave_valor:
            chave_valor[letra] += 1
        else:
            chave_valor[letra] = 1
            
    return chave_valor

string_user = input()
resultado = contar_caracteres(string_user)
print(resultado)
