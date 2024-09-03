# Conversão de Tipos em Python

# Conversão de inteiro para string
numero_inteiro = 123
numero_string = str(numero_inteiro)
print(f"Convertendo inteiro para string: {numero_string} (tipo: {type(numero_string)})")

# Conversão de string para inteiro
string_numero = "456"
numero_inteiro_convertido = int(string_numero)
print(f"Convertendo string para inteiro: {numero_inteiro_convertido} (tipo: {type(numero_inteiro_convertido)})")

# Conversão de float para inteiro (perde a parte decimal)
numero_float = 78.9
numero_inteiro_de_float = int(numero_float)
print(f"Convertendo float para inteiro: {numero_inteiro_de_float} (tipo: {type(numero_inteiro_de_float)})")

# Conversão de inteiro para float
numero_inteiro_para_float = float(numero_inteiro)
print(f"Convertendo inteiro para float: {numero_inteiro_para_float} (tipo: {type(numero_inteiro_para_float)})")

# Conversão de string para float
string_para_float = "12.34"
numero_float_convertido = float(string_para_float)
print(f"Convertendo string para float: {numero_float_convertido} (tipo: {type(numero_float_convertido)})")

# Conversão de lista para conjunto (elimina duplicatas)
lista_numeros = [1, 2, 3, 1, 2]
conjunto_numeros = set(lista_numeros)
print(f"Convertendo lista para conjunto: {conjunto_numeros} (tipo: {type(conjunto_numeros)})")

# Conversão de conjunto para lista
conjunto_para_lista = list(conjunto_numeros)
print(f"Convertendo conjunto para lista: {conjunto_para_lista} (tipo: {type(conjunto_para_lista)})")

# Conversão de dicionário para lista de chaves
dicionario = {"a": 1, "b": 2, "c": 3}
lista_chaves = list(dicionario.keys())
print(f"Convertendo dicionário para lista de chaves: {lista_chaves} (tipo: {type(lista_chaves)})")

# Conversão de lista para string (concatenando elementos)
lista_palavras = ["Python", "é", "legal"]
string_concatenada = " ".join(lista_palavras)
print(f"Convertendo lista para string: '{string_concatenada}' (tipo: {type(string_concatenada)})")
