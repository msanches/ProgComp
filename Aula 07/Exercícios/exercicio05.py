masc = 0
fem = 0
cm = 0
cf = 0
while True:
    sexo = input("Digite o sexo da pessoa (F/M): ")
    altura = float(input("Digite a altura da pessoa em m: "))
    if sexo=='f' or sexo=='F':
        fem = fem+altura
        cf = cf+1
    else:
        masc = masc+altura
        cm = cm+1
    resp = input("Deseja continuar s/n?")
    if resp=='n' or resp=='N': break
print("A altura média dos homens é %.1fm " %(masc/cm))
print("A altura média das mulheres é %.1f m" %(fem/cf))