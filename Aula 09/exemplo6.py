num = input('Digite um número: ').upper()
base = int(input('Digite a base [2] [8] [16]'))

n = len(num)-1
decimal = 0
digitos = '0123456789ABCDEF'

for d in num:
    decimal += digitos.find(d)*base**n
    n = n-1

print(f'O número na base {base} é igual ao decimal {decimal}')