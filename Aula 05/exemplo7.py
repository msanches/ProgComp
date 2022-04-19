placa = int(input('Digite os quatro dígitos da placa do veículo: '))

final = placa % 10

if final == 1 or final == 2:
    print('O veículo não pode circular às segundas-feiras')
elif final == 3 or final == 4:
    print('O veículo não pode circular às terças-feiras')
elif final == 5 or final == 6:
    print('O veículo não pode circular às quartas-feiras')
elif final == 7 or final == 8:
    print('O veículo não pode circular às quintas-feiras')
else:
    print('O veículo não pode circular às sextas-feiras')