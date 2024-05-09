print("Levando em consideração a fórmula: Ax² + Bx + C = 0")

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b**2 - 4*a*c
print(delta)
x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)

print(f"As possíveis soluções para x são: {x1:.2f} e {x2:.2f}.")
