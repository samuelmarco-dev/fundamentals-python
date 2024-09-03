# tupla_exemplo.py

# Exemplo de Tupla em Python
cores = ("vermelho", "verde", "azul", "amarelo")

# Acessando elementos da tupla
print("Primeira cor:", cores[0])
print("Última cor:", cores[-1])

# Tentando modificar a tupla (causará erro)
# cores[1] = "roxo"  # Isso resultará em um TypeError, pois tuplas são imutáveis

# Desempacotamento de tupla
cor1, cor2, cor3, cor4 = cores
print("Cores desempacotadas:", cor1, cor2, cor3, cor4)

# Iterando sobre a tupla
print("Iterando sobre a tupla de cores:")
for cor in cores:
    print(cor)

# Verificando se um item está na tupla
if "verde" in cores:
    print("Verde está na tupla de cores.")
else:
    print("Verde não está na tupla de cores.")

# Filtrar tupla
numeros = (1, 30, 21, 2, 9, 65, 34)
pares = tuple(numero for numero in numeros if numero % 2 == 0)
print(pares)

# help: dir(tuple)