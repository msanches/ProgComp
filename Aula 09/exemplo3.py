decimal = int(input('Digite um número decimal: '))
print('[2] binário\n[8] Octal\n[16] Hexadecimal')
base = int(input('Escolha uma base para conversão: '))

num_conv = ''
digitos = '0123456789ABCDEF'
while decimal > 0:
    num_conv = str(digitos[decimal % base]) + num_conv
    decimal = decimal // base

print(f'O número convertido para a base {base} é igual a {num_conv}')