nome = input("Digite o nome do produto: ")
valor = float(input("Digite o valor de compra do produto R$ "))

if valor < 10:
    lucro = 70
elif valor < 30:
    lucro = 50
elif valor < 50:
    lucro = 40
else:
    lucro = 30
venda = valor + (valor *lucro/100)
print("O valor de venda de %s é R$ %.2f" %(nome, venda))