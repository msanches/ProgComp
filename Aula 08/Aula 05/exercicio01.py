idade = int(input("Digite a sua idade: "))
if idade < 16:
    classe = "não-eleitor"
elif idade >=18 and idade <= 65:
    classe = "eleitor obrigatório"
else:
    classe = "eleitor facultativo"
print("Sua classe eleitoral é:", classe)