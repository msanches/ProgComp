npar = 0
nimpar = 0
menor = 100
while True:
    num = float(input("Digite um número real: "))
    if num%2==0:
        npar = npar+1
    else:
        nimpar = nimpar+1
    resp = input("Deseja continuar s/n? ")
    if num > menor:
        menor = menor
    else:
        menor = num
    if resp =='n' or resp =='N': break

print("Foram digitados:\n%d par(es) e\n%d ímpar(es)" %(npar,nimpar))
print("O menor número digitado foi", menor)