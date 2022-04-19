algoritmo exemplo4
	inicio
		real num, media, soma
		inteiro contador
		caracter resp
		contador = 0
		soma = 0
		resp = 's'
		
		enquanto(resp =='s' ou resp =='S'){
			escreva("Digite digite um número:")
			leia(num)
			soma = soma + num
			contador = contador + 1
			escreva("Deseja continuar (S/N)?")
			leia(resp)
		}
		media = soma/contador
		escreva("A média dos números digitados é:" + media
	fim
	