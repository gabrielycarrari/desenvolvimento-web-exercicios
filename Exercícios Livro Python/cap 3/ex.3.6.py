soma = 0

for n in range(1,101):
    if n % 2 != 0:
        soma += n
    
print(f"A soma dos números ímpares de 1 a 100 é {soma}.")