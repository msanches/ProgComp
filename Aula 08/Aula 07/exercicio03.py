salario = float(input("Digite o salário fixo: R$ "))
vendas = float(input("Digite o valor das vendas: R$ "))
comissao = vendas * 0.04
salario = salario + comissao
print("Comissão: %.2f\nSalário final: %.2f"%(comissao, salario))