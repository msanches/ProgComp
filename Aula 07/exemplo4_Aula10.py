#Exemplo 4 - While com laço condicional
soma = 0 #Acumulador
qtde = 0   #Contador
resp = "s"
while resp == "s" or resp == "S":
	n1 = int(input("Digite um número"))
	soma = soma + n1
	qtde = qtde + 1
	#atualização da variável de controle
	resp = input("Deseja continuar?(s/n)")
print("Média = ", soma/qtde)
