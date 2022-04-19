print('Entrada:')
tamanho = int(input('Digite o tamanho o arquivo em MB: '))
velocidade = int(input('Digite a velocidade do link de internet (Mbps: '))

segundos =  tamanho/velocidade
minutos = segundos//60
segundos = segundos%60
print('\nSaída:')
print(f'Tempo aproximado para download: {minutos} minutos e {segundos} segundos.')
