intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

print('Entrada:')
while True:
    num = int(input('Digite um número positivo (-1 para sair): '))
    if num < 0:
        break
    elif num <= 25:
        intervalo1 += 1
    elif num <= 50:
        intervalo2 += 1
    elif num <= 75:
        intervalo3 += 1
    else:
        intervalo4 += 1

print('\nSaída:')
print(f'[0-25]: {intervalo1} números')
print(f'[25-50]: {intervalo2} números')
print(f'[50-75]: {intervalo3} números')
print(f'[75-100]: {intervalo4} números')