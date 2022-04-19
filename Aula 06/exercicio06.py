n1 = float(input("Digite a primeira nota parcial: "))
n2 = float(input("Digite a segunda nota parcial: "))
media = (n1 + n2)/2

if media >= 9:
    conceito = 'A'
elif media >= 7.5:
    conceito = 'B'
elif media >= 6:
    conceito = 'C'
elif media >= 4:
    conceito = 'D'
else:
    conceito = 'E'

if conceito=='A' or conceito=='B' or conceito=='C':
    msg = 'APROVADO'
else:
    msg = 'REPROVADO'

print("Conceito: %s\nMensagem: %s"%(conceito,msg))