data = input("Digite uma data no formato: ")

if len(data) != 10 or data[2] != '/' or data[5] != '/':
    print("Data inválida.")
    exit()

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

# Alternativa 1
# if dia < 1 or dia > 31 or mes < 1 or mes > 12 or ano < 1 or ano > 9999:
#     print("Data inválida.")
# else:
#     print(f"{data} é uma data válida.")

# Alternativa 2
if dia > 0 and dia < 32:
    if mes > 0 and mes < 13:
        if ano > 0 and ano < 10000:
            print(f"{data} é uma data válida.")


    