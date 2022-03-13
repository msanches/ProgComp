import math
sombra = float(input("Digite o comprimento da sombra em m: "))
angulo = math.radians(float(input("Digite o ângulo em graus: ")))
altura = math.tan(angulo) * sombra

print("A altura do prédio é de %.2f m" % (altura))

