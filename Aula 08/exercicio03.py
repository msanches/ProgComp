eleitor = 0
nEleitor = 0
soma = 0
n = 10
print('Entrada:')
for i in range(n):
    idade = int(input("Digite a idade do aluno: "))
    soma += idade
    if idade >= 16:
        eleitor = eleitor+1

print('\nSaída')
print("A quantidade de alunos que podem votar é %d"%eleitor)
print("A média da idade dos alunos é %.2f"%(soma/n))