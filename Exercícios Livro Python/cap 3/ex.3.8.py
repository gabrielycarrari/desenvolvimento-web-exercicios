numero = int(input("Digite um número: "))
fatorial = 1

for n in range(numero, 0, -1):
    fatorial *= n

print(f"{numero}! = {fatorial}")