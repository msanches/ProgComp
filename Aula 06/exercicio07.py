print('Coordenadas de um ponto P(x, y)')
x = float(input('Digite a coordenada x: '))
y = float(input('Digite a coordenada y: '))

if x>0 and y>0:
    quad = 1
elif x<0 and y>0:
    quad = 2
elif x<0 and y<0:
    quad = 3
else:
    quad = 4
print(f'O ponto ({x}, {y}) pertence ao {quad}º quadrante')