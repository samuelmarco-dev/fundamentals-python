# lista_exemplo.py

# Exemplo de Lista em Python
frutas = ["maçã", "banana", "laranja", "uva"]

# Acessando elementos da lista
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# Modificando elementos da lista
frutas[1] = "morango"
print("Lista modificada:", frutas)

# Adicionando elementos à lista
frutas.append("abacaxi")
print("Lista após adicionar uma fruta:", frutas)

# Removendo elementos da lista
frutas.remove("laranja")
print("Lista após remover uma fruta:", frutas)

# Iterando sobre a lista
print("Iterando sobre a lista de frutas:")
for fruta in frutas:
    print(fruta)
    
for index, fruta in enumerate(frutas):
    print(f'{index}: {fruta}')

# Verificando se um item está na lista
if "uva" in frutas:
    print("Uva está na lista de frutas.")
else:
    print("Uva não está na lista de frutas.")
    
# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

# help: dir(list)