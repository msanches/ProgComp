carneirinho = 0
print('Entrada:')
while True:
    resp = input("Já dormi s/n? ")
    if resp=='s' or resp=='S':
       break
    else:
        carneirinho = carneirinho+1
print('\nSaída:')
print("Você contou %d carneirinhos!"%carneirinho)