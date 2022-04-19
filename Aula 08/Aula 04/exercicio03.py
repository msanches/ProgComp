compra = float(input("Digite o valor da compra: R$ "))
if compra > 200:
    compra = compra * 0.8
print("O valor a pagar será de: R$ %.2f"%compra)    