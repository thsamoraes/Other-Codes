import math

print("Vamos resolver uma expressão quadrática, ou seja, do tipo ax² + bx + c = 0.")

a = float(input("Digite o valor de a "))
b = float(input("Digite o valor de b "))
c = float(input("Digite o valor de c "))

d = b**2 - 4*a*c

if d < 0:
    print("Sua equação não possui raízes reais.")
else:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
    if d==0:
        print("Sua equação possui duas raízes reais iguais: x =1",x1)
    else:
        print("Sua equação possui duas raízes reais: x =",x1," e x =",x2)
