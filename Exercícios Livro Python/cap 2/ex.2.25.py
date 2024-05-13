a = float(input("Digite o número a: "))
b = float(input("Digite o número b: "))
op = input("Digite a operação (+, -, *, /): ")

match op:
    case '+':
        print(f"{a} + {b} = {a + b}")
    case '-':
        print(f"{a} - {b} = {a - b}")
    case '*':
        print(f"{a} * {b} = {a * b}")
    case '/':
        print(f"{a} / {b} = {a / b}")
    case _:
        print("Operação inválida.")
