def elementos_comuns(list_one, list_two):
    list_one = list(map(int, list_one))
    list_two = list(map(int, list_two))
    
    print(list_one, list_two)
    
    conjunto_list_one = set(list_one)
    conjunto_list_two = set(list_two)
    
    return list(conjunto_list_one.intersection(conjunto_list_two))

# Leitura dos dados de cada lista
entrada_list_one = input().split()
entrada_list_two = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in entrada_list_one) and all(item.isdigit() for item in entrada_list_two):
    comuns = elementos_comuns(entrada_list_one, entrada_list_two)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
