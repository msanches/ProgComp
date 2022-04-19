soma = 0
maior = 0
n = ''
h = 0
print('Entrada:')
for i in range(10):
    nome = input('Digite o nome do aluno: ')
    altura = float(input(f'Digite a altura do aluno {nome} em cm: '))
    soma += altura
    if altura > maior:
        maior = altura
        n = nome
        h = altura
media = soma/10
print('\nSaída:')
print(f'Aluno mais alto: {n} com {h} cm de altura')
print(f'Média das alturas da turma: {media} cm')