'''
    string (str)
    numbers (int, float, complex)
    sequence (list, tuple, range)
    map (dict)
    colection (set, fronzenset)
    boolean (bool)
    binary (bytes, bytearray, memoryview)
'''

import math;

str = 'python'
int = 10
float = math.sqrt(250)
complex = 1j

# List: Uma sequência mutável de elementos.
frutas = ['banana', 'maça', 'uva']

# Tuple: Uma sequência imutável de elementos.
cores = ('amarelo', 'azul', 'verde')

# Dict: Um mapeamento de chave-valor.
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia"
}

# Set: Uma coleção não ordenada de elementos únicos.
vogais = {"a", "e", "i", "o", "u"}

# Frozenset: Um set imutável.
consoantes = frozenset({"b", "c", "d", "f", "g"})

# Bytes: Uma sequência imutável de valores de byte (0-255).
dados = b"telemetria"
print(dados)

# Bytearray: Uma sequência mutável de valores de byte (0-255).
dados_mut = bytearray(dados)
dados_mut[0] = 88 
print(dados_mut)