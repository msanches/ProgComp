altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa m/f: ")
if sexo=='m' or sexo=='M':
    ideal = (72.7*altura) - 58
else:
    ideal = (62.1*altura) - 44.7
print("O peso ideal é %.1f"%ideal)