# Estruturas de repetição com While
count = 0

while count < 10:
    print(f'Valor do contador: {count}')
    count += 1  # count++
    if count == 1:
        continue
    if count == 8:
        break

print(f'Fim da repetição do bloco while, valor do contador: {count}')
