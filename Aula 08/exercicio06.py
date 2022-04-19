print('Entrada:')
hora = float(input('Digite o valor da hora aula: R$ '))
cargaH = int(input('Digite a carga horária semanal: '))
print('\nSaída:')
salario = hora*cargaH*4.5
salario = salario + salario*1/6
print(f'Salário final: R$ {salario:.2f}')