import math
print('Entrada:')
turmas = int(input('Digite a quantidade de turmas: '))
soma = 0

for i in range(turmas):
    qte = int(input(f'Digite a quantidade de alunos da {i+1}ª turma: '))
    soma +=qte
media = math.ceil(soma/turmas)
print('\nSaída:')
print(f'As turmas têm em média {media} alunos.')