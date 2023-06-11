#método com retorno e com parametros
def somaValores(a,b):
	return (a+b)

#principal
v1 = float(input("Digite o primeiro valor"))
v2 = float(input("Digite o segundo valor"))
resul = somaValores(v1,v2) #chama a função
print("Soma = ", resul)
print("Soma = ", somaValores(8.5,7.8))

