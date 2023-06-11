#Método com retorno e parametro
def areaTriangulo(base,altura):
	area = base*altura/2
	return area
	
#principal
base = float(input("Digite o valor da base"))
altura = float(input("Digite o valor da altura"))
area = areaTriangulo(base,altura)
print("Área = ", area)
print("Área = ", areaTriangulo(22,55))

