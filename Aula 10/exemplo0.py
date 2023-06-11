mes = ['Jan', 'Fev', 'Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']
salarios = []

for i in range(12):
    salario = float(input(f'Digite o salário de {mes[i]}: R$ '))
    salarios.append(salario)
    
#O Python possui uma função nativa dedicada à soma dos elementos de uma lista
decimo3 = sum(salarios)/12 # função sum()
um3 = decimo3 / 3

print(f'Décimo terceiro salário: R$ {decimo3:.2f}')
print(f'Um terço de férias: R$ {um3:.2f}')