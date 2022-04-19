placa = int(input('Digite os quatro digitos da placa do veículo: '))
final = placa%10

match final:
    case 1 | 2:
        print("O veículo não pode circular às segundas-feiras")
    case 3 | 4:
        print("O veículo não pode circular às terças-feiras")
    case 5 | 6:
        print("O veículo não pode circular às quartas-feiras")
    case 7 | 8:
        print("O veículo não pode circular às quintas-feiras")
    case 9 | 0:
        print("O veículo não pode circular às sextas-feiras")
    case _:
        print("Placa inválida")

        