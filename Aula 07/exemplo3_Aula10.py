#Exemplo 3 - while contado
cont = 1 #contador
while cont<=10:
	n1=float(input("Digite a primeira nota"))
	n2=float(input("Digite a segunda nota"))
	print("Aluno:", cont, " - Média: ", (n1+n2)/2)
	cont = cont + 1
