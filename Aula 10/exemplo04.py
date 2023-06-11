notas = []
soma = 0
n = int(input('Entre com o número de notas: '))
for i in	range(n):
  nota = float(input(f'Entre com a {i+1}ª nota: '))
  notas.append(nota)
  soma+=nota
print(notas)

soma = 0
media = soma/n
print(f'{media:.2f}')