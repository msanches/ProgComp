qDiarias = int(input('Digite a quantidade de diárias: '))
tipo = input('Digite o tipo de hospedagem (s|d|t): ')

if tipo == 's' or tipo == 'S':
    print(f'Valor a pagar R$ {qDiarias * 255.5}')
elif tipo == 'd' or tipo == 'D':
    print(f'Valor a pagar R$ {qDiarias * 305.5}')
elif tipo == 't' or tipo == 'T':
    print(f'Valor a pagar R$ {qDiarias * 360.5}')
else:
    print('Tipo de hospedagem inválida!!!!')