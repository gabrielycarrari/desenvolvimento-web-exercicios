numero = int(input("Digite um número: "))
fibonacci = []

for n in range(0,numero,1):
    if n == 0 or n == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[n-1] + fibonacci[n-2])

print(fibonacci)