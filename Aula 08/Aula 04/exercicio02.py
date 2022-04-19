turno = input("Digite o seu turno de trabalho D/N: ")
qhoras = int(input("Digite a quantidade de horas trabalhadas: "))
if turno == 'n' or turno == 'N':
    salario = qhoras * 45
else:
    salario = qhoras * 37.5
print("O seu salário será de: R$ %.2f" %salario)