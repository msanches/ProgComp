algoritmo inverso
	inicio
		inteiro num, d1, d2, d3, inverso
		escreva("Digite um número com três dígitos:")
		leia(num)
		d1 = num div 100
		d2 = num % 100 div 10
		d3 = num % 10
		inverso = d3 * 100 + d2 * 10 + d3
		escreva("O inverso do número digitado é: ", inverso)
	fim
	
