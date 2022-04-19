h = float(input("Digite a altura do tronco da pirâmide em cm: "))
bMenor = float(input("Digite o valor da base menor em cm: "))
bMaior = float(input("Digite o valor da base maior em cm: "))

aMaior = bMaior**2
aMenor = bMenor**2

volume = h/3*(aMaior + aMenor + (aMaior*aMenor)**0.5)
print("O volume da pirâmide é %.2f cm³" %(volume))