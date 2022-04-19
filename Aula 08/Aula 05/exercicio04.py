n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
op = int(input("Digite a operação:\n1-Soma\n2-Subtração\n3-Multiplicaçao\n4-Divisão"))

if op == 1:
    result = n1 + n2
elif op == 2:
    result = n1 - n2
elif op == 3:
    result = n1 * n2
else:
    result = n1 / n2

print("Resultado: ", result)