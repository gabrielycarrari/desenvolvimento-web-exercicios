import re

cpf = input("Digite um CPF: ")

formato_cpf = r'[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}'
formato_cpf2 = r'\d{3}.\d{3}.\d{3}-\d{2}'

if re.fullmatch(formato_cpf2, cpf):
    print(f"CPF {cpf} está no formato correto.")
else:
    print(f"CPF {cpf} não está no formato correto.")