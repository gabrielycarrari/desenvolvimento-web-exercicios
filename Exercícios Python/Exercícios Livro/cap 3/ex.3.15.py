numero = int(input("Digite um número: "))
perfeito = 0

for n in range(numero-1, 0, -1):
    if numero % n == 0:
        perfeito += n

if numero == perfeito:
    print(f"{numero} é um número perfeito.")
else:
    print(f"{numero} não é um número perfeito.")