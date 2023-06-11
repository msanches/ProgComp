num = []

while True:
  n = int(input('Digite um número inteiro: '))
  if n==0:
    break
  num.append(n)

media = sum(num)/ len(num)
print(f'{media:.2f}')
print(num)

