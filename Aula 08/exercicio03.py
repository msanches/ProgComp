eleitor = 0
nEleitor = 0
soma = 0
print('Entrada:')
for i in range(10):
    idade = int(input("Digite a idade do aluno: "))
    if idade >= 16:
        eleitor = eleitor+1
    else:
        nEleitor = nEleitor+1
        soma= soma+idade
print('\nSaída')
print("A quantidade de alunos que podem votar é %d"%eleitor)
print("A média da idade dos alunos não eleitores é %.2f"%(soma/nEleitor))