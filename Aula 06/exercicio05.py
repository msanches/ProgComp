import math
area = float(input("Digite a área a ser pintada (em m²): "))
qlitros = area/3
qlatas = math.ceil(qlitros/18)
valor = qlatas * 80
print("Você precisará comprar %d latas" %qlatas)
print("O valor total a pagar será de R$ %.2f" %valor)