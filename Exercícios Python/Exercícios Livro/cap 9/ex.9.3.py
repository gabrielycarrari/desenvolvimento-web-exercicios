def calcularadora(op, num1, num2):
    try:
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 / num2
        else:
            raise ValueError('Operação inválida')
    except ZeroDivisionError:
        print("Erro: Divisão por zero.")
    except TypeError:
        print("Erro: Os números devem ser inteiros ou reais.")


print(calcularadora('+', 2, 3))
print(calcularadora('/', 2, 0))
print(calcularadora(',',3, 2))