# conjunto_exemplo.py

# Exemplo de Conjunto em Python
numeros = {1, 2, 3, 4, 5}
num_alter = set([1, 2, 3, 4, 5])

# Acessando um elemento
num_alter = list(numeros)
print(num_alter[0])

# Adicionando elementos ao conjunto
numeros.add(6)
print("Conjunto após adicionar um número:", numeros)

# Removendo elementos do conjunto
numeros.remove(3)
print("Conjunto após remover um número:", numeros)

# Verificando se um item está no conjunto
if 2 in numeros:
    print("O número 2 está no conjunto.")
else:
    print("O número 2 não está no conjunto.")

# Iterando sobre o conjunto
print("Iterando sobre o conjunto de números:")
for numero in numeros:
    print(numero)

# Operações de conjuntos
pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7, 9}

# União
print("União dos conjuntos:", numeros.union(pares))

# Interseção
print("Interseção dos conjuntos:", numeros.intersection(pares))

# Diferença
print("Diferença entre os conjuntos:", numeros.difference(pares))

# Diferença simétrica
print("Diferença simétrica entre os conjuntos:", numeros.symmetric_difference(pares))
