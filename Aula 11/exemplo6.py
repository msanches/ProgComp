import os
limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplica = lambda a, b: a * b
divide = lambda a, b: a / b

while True:
    limpar()
    print('Calculadora lambda')
    print('[1] Soma\n[2] Subtração\n[3] Divisão\n[4] Multiplicação\n[0] Sair')
    op = int(input('Digite uma opção: '))
    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))
    if op == 0: break
    elif op == 1: print(soma(a,b))
    elif op == 2: print(subtracao(a,b) )
    elif op == 3: print(multiplica(a,b))
    elif op == 4: print(divide(a,b))
    else: print('Opção inválida!!')
    input('Pressione uma tecla para continuar...')