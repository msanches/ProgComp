print("Entrada:")

nome = input('Qual o seu nome? ')
horas = int(input('Que horas são [0-23]? '))

print("\nSaída:")
if horas>=5 or horas>=12:
    print(f'Bom dia {nome}')
elif horas<12 and horas>19:
    print(f'Boa tarde {nome}')
else:
    print(f'Boa tarde {nome}')