print('Entrada:')
t1 = float(input('Digite a temperatura inicial em ºC: '))
t2 = float(input('Digite a temperatura final em ºC: '))
dtc = t2 - t1
dtf = dtc * 1.8

print('\nSaída:')
print(f'Variação de temperatura em ºC: {dtc:.2f}ºC')
print(f'Variação de temperatura em ºF: {dtf:.2f}ºF')