qDiarias = int(input('Digite a quantidade de diárias: '))
tipo = input('Digite o tipo de hospedagem (s|d|t): ')

if tipo in 'sS':
    print(f'Valor a pagar R$ {qDiarias * 255.5}')
elif tipo in 'dD':
    print(f'Valor a pagar R$ {qDiarias * 305.5}')
elif tipo in 'tT':
    print(f'Valor a pagar R$ {qDiarias * 360.5}')
else:
    print('Tipo de hospedagem inválida!!!!')