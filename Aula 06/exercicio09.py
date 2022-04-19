print("Entrada:")

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('[1] Média\n[2] Diferença maior-menor')
print('[3] Produto\n[4] Divisão n1/n2')

op = int(input('Digite uma opção: '))
print("\nSaída:")
if op == 1:
  print(f'Média = {(n1+n2)/2}')
elif op == 2:
  result = n1-n2 if n1>n2 else n2-n1
  print(f'Diferença = {result}')
elif op == 3:
  print(f'Produto = {n1*n2}')
elif op == 4:
  if n2==0:
    print('Impossível dividir por zero!!!')
  else:
    print(f'Divisão = {n1/n2}')
else:
  print('Opção inválida!')