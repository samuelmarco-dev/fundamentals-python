# dicionario_exemplo.py

# Exemplo de Dicionário em Python
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia",
    "notas": [7.5, 8.0, 9.2]
}

pessoa = dict(nome= "João", idade=28)

# Acessando valores no dicionário
print("Nome do aluno:", aluno["nome"])
print("Idade do aluno:", aluno["idade"])

# Modificando valores no dicionário
aluno["curso"] = "Matemática"
print("Curso atualizado:", aluno["curso"])

# Adicionando um novo par chave-valor
aluno["matricula"] = 123456
print("Dicionário após adicionar matrícula:", aluno)

# Removendo um par chave-valor
del aluno["notas"]
print("Dicionário após remover notas:", aluno)

# Iterando sobre chaves e valores
print("Iterando sobre chaves e valores do dicionário:")
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

# Verificando se uma chave existe no dicionário
if "idade" in aluno:
    print("A chave 'idade' está presente no dicionário.")
else:
    print("A chave 'idade' não está presente no dicionário.")
