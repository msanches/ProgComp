a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = b*b - 4*a*c
if a == 0:
    print("Não é equação do 2º grau")
elif delta >=0:
    x1 = (-b + delta**0.5)/2*a
    x2 = (-b - delta**0.5)/2*a
    print("As raízes são:\nx1: %.1f\nx2:%.1f"%(x1,x2))
else:
    print("Não há raízes reais")