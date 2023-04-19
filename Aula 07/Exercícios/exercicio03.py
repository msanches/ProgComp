valor = int(input("Digite um número inteiro: "))
s = 0
for n in range(1,valor+1):
    s = s + 1/n
print("A soma é: ", s)