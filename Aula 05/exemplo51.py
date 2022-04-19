#Exemplo utilizando match-case
valor = float(input('Digite o valor da compra R$ '))
parcelas = int(input('Digite a qtde de parcelas (2-4-6-8): '))

match parcelas:
    case 2:
        valor = valor*1.03
    case 4:
        valor = valor*1.07
    case 6:
        valor = valor*1.09
    case 8:
        valor = valor*1.12
    case _:
        valor = 0
    
if valor == 0:
    print('Número de parcelas inválido!')
else:
    print('Valor de cada parcela: R$ %.2f' %(valor/parcelas))

