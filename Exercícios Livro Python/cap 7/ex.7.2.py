arquivo = input("Digite o nome do arquivo: ")

with open(arquivo, "r") as file:
    linhas = file.readlines()

print(f"O arquivo {arquivo} tem {len(linhas)} linhas.")