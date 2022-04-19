valor = float(input('Digite o valor da compra R$ '))
parcelas = int(input('Digite a quantidade de parcelas (2-4-6-8) '))

if parcelas == 2:
    valor = valor * 1.03
elif parcelas == 4:
    valor = valor * 1.07
elif parcelas == 6:
    valor = valor * 1.09
elif parcelas == 8:
    valor = valor * 1.12
else:
    valor = 0

if valor == 0:
    print('O número de parcelas é inválido!!!')
else:
    print(f'O valor de cada parcela é: R$ {valor/parcelas}')