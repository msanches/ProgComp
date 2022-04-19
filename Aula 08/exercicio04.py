print('Entrada:')
conta = input('Digite o número da conta com 4 algarismos: ')
soma = 0
for d in conta:
    soma += int(d)
digito = soma%10
print('\nSaída:')
print(f'Número da conta completo: 00{conta}-{digito}')