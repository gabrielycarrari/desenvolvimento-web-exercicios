palavra = input("Digite uma palavra: ")
invertido = palavra[::-1]

if palavra == invertido:
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")
