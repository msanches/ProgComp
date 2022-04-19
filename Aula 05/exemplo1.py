# Cálculo da média - Operador ternário
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

media = (n1+n2)/2
resultado = 'Aprovado' if media >=6 else 'Reprovado'
print(f'Você foi {resultado}, com media {media}')