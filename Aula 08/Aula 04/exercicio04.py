luz = float(input("Digite o valor da conta de luz: R$ "))
agua = float(input("Digite o valor da conta de água: R$ "))
telefone = float(input("Digite o valor da conta de telefone: R$ "))
salario = float(input("Digite o seu salário: R$ "))

contas = luz + agua + telefone
if salario > contas:
    salario = salario - contas
    print("Restou R$ %.2f do seu salário!" %salario)
else:
    print("Salário insuficiente!!!")