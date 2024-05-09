cpf = input("Digite o cpf (apenas os números): ")

if len(cpf) == 11 and cpf.isdigit():
    print("CPF válido.")
else:
    print("CPF inválido.")