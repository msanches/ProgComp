media = float(input('Digite a média do aluno: '))
freq = float(input('Digite o percentual de frequência: '))

if freq < 75:
    print('Reprovado por faltas!')
elif media < 6:
    print('Reprovado por nota!!!')
else:
    print('Aprvado')