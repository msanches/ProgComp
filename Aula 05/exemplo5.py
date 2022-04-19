peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite a sua altura em m: '))

imc = peso / altura**2

if imc < 20:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso normal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obeso.')
else:
    print('Obeso mórbido.')