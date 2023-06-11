medias = []
nomes = []

x = int(input('Digite a quantidade de alunos: '))
for i in range(x):
  nome = input('Digite o nome do aluno: ')
  n1 = float(input(f'Qual a 1ª nota do {nome}? '))
  n2 = float(input(f'Qual a 2ª nota do {nome}? '))
  media = (n1+n2) / 2
  medias.append(media)
  nomes.append(nome)

print(10*'-')
n = input('Digite o nome do aluno que deseja exibir: ')
if n in nomes:
    i = nomes.index(n)
    result = 'APROVADO' if medias[i] >= 6.0 else 'REPROVADO'
    print(f'O aluno {nomes[i]} foi {result} com média {medias[i]:.2f}')
else:
  print('Aluno não encontrado!')