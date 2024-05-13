numeros = []

maior = segundo_maior = float('-inf') 
menor = segundo_menor = float('inf')

for n in range(10):
    numeros.append(float(input("Digite um número: ")))

for n in numeros:
    if n > maior:
        segundo_maior = maior
        maior = n
    elif n < maior and n > segundo_maior:
        segundo_maior = n
    
    if n < menor:
        segundo_menor = menor
        menor = n
    elif n > menor and n < segundo_menor:
        segundo_menor = n

print(f"O segundo maior número é {segundo_maior}")
print(f"O segundo menor número é {segundo_menor}")