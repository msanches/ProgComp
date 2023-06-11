# Exemplo de cálculo do IMC em Python
# utilizando duas funções

def calculaIMC(peso, altura):
    res = peso / altura**2
    return(res)

def despedida():
    print("Obrigado por usar este programa!")
    print("Até logo!")
 
peso = float(input("Digite o peso da pessoa, em Kg: "))
altura = float(input("Digite a estatura da pessoa, em m: "))
print("O IMC é ", calculaIMC(peso,altura), " Kg/m²")
despedida()


